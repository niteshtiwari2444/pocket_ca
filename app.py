import os
import streamlit as st
import pandas as pd
import plotly.express as px

import data_utils as du
from assistant import ask_pocket_ca, generate_report_narrative, get_model
from theme import LEDGER_CSS, apply_ledger_chart_theme, kpi_card_html

st.set_page_config(page_title="Pocket C.A.", page_icon="💰", layout="wide")
st.markdown(LEDGER_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Sidebar: API key + data upload
# ---------------------------------------------------------------------------
st.sidebar.markdown(
    "<div style='font-family:Inter,sans-serif; font-size:1.35rem; font-weight:800; color:#171523;'>💰 Pocket C.A.</div>",
    unsafe_allow_html=True,
)
st.sidebar.caption("Your pocket accounting assistant")


def _get_secret(name):
    try:
        return st.secrets[name]
    except Exception:
        return None


api_key = os.environ.get("GEMINI_API_KEY") or _get_secret("GEMINI_API_KEY") or st.sidebar.text_input(
    "Gemini API key",
    type="password",
    help="Free — get one at https://aistudio.google.com/apikey (no credit card needed).",
)
if not api_key:
    st.sidebar.caption("👉 Get a free key: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)")

st.sidebar.divider()
st.sidebar.subheader("Your data")
uploaded = st.sidebar.file_uploader("Upload transactions (CSV/XLSX)", type=["csv", "xlsx", "xls"])
use_sample = st.sidebar.button("Use sample data instead", use_container_width=True)

if "df" not in st.session_state:
    st.session_state.df = None
if "messages" not in st.session_state:
    st.session_state.messages = []

if uploaded is not None:
    try:
        st.session_state.df = du.load_transactions(uploaded)
        st.sidebar.success(f"Loaded {len(st.session_state.df)} transactions.")
    except Exception as e:
        st.sidebar.error(str(e))

if use_sample:
    st.session_state.df = du.load_sample_data()
    st.sidebar.success(f"Loaded {len(st.session_state.df)} sample transactions.")

if st.session_state.df is not None:
    with st.sidebar.expander("Preview data"):
        st.dataframe(st.session_state.df.head(10), use_container_width=True, hide_index=True)

st.sidebar.divider()
st.sidebar.caption(
    "⚠️ Pocket C.A. gives general educational guidance only. "
    "It is not a substitute for a licensed accountant or financial advisor."
)

# ---------------------------------------------------------------------------
# Main area: tabs
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="pca-header">
      <div>
        <div class="pca-greeting">Welcome back 👋</div>
        <div class="pca-title">Pocket C.A.</div>
        <div class="pca-tagline">Your AI accounting assistant — every answer grounded in your real, computed numbers.</div>
      </div>
      <div class="pca-avatar">💰</div>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_chat, tab_reports = st.tabs(["💬  Chat", "📊  Reports"])

# ---------------------------------------------------------------------------
# Chat tab
# ---------------------------------------------------------------------------
with tab_chat:
    if st.session_state.df is None:
        st.markdown(
            '<div class="pca-note">Upload your transactions in the sidebar '
            '(or click <b>Use sample data</b>) to get personalized answers.</div>',
            unsafe_allow_html=True,
        )
        st.write("")

    for msg in st.session_state.messages:
        avatar = "🧾" if msg["role"] == "user" else "🪙"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    example_cols = st.columns(3)
    example_qs = [
        "What did I spend the most on last month?",
        "Am I saving enough each month?",
        "Show me all my food delivery orders",
    ]
    for col, q in zip(example_cols, example_qs):
        if col.button(q, use_container_width=True):
            st.session_state["_pending_prompt"] = q

    user_prompt = st.chat_input("Ask about your spending, savings, or general accounting...")
    pending = st.session_state.pop("_pending_prompt", None)
    final_prompt = user_prompt or pending

    if final_prompt:
        if not api_key:
            st.error("Please enter your free Gemini API key in the sidebar first.")
        else:
            st.session_state.messages.append({"role": "user", "content": final_prompt})
            with st.chat_message("user", avatar="🧾"):
                st.markdown(final_prompt)

            with st.chat_message("assistant", avatar="🪙"):
                with st.spinner("Thinking..."):
                    try:
                        model = get_model(api_key)
                        reply = ask_pocket_ca(model, st.session_state.messages, st.session_state.df)
                    except Exception as e:
                        reply = f"Something went wrong calling the AI model: {e}"
                    st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# ---------------------------------------------------------------------------
# Reports tab
# ---------------------------------------------------------------------------
with tab_reports:
    df = st.session_state.df
    if df is None:
        st.markdown(
            '<div class="pca-note">Upload your transactions (or use sample data) '
            'in the sidebar to generate a report.</div>',
            unsafe_allow_html=True,
        )
    else:
        months = sorted(df["month"].unique())
        selected_month = st.selectbox("Period", options=["All time"] + months, index=0)
        month_filter = None if selected_month == "All time" else selected_month

        summary = du.compute_summary(df, month=month_filter)
        trend = du.compute_trend(df).to_dict(orient="records")
        merch = du.top_merchants(df, n=6)

        savings_rate = summary.get("savings_rate_pct")
        trend_class = "positive" if (savings_rate is not None and savings_rate >= 0) else "negative"
        trend_text = f"↑ {savings_rate}% savings rate" if savings_rate is not None else None

        st.markdown(
            f"""
            <div class="pca-kpi-row">
              {kpi_card_html("💵", "rgba(79,70,229,0.10)", "Total Income", f"${summary['total_income']:,.2f}")}
              {kpi_card_html("💳", "rgba(220,38,38,0.10)", "Total Expenses", f"${summary['total_expenses']:,.2f}")}
              {kpi_card_html("🏦", "rgba(139,92,246,0.15)", "Net Savings", f"${summary['net_savings']:,.2f}", trend_text, trend_class)}
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="pca-section-title">Spending by category</div>', unsafe_allow_html=True)
            cat_df = pd.DataFrame(summary["top_categories"])
            if not cat_df.empty:
                fig = px.pie(cat_df, names="category", values="amount", hole=0.62)
                apply_ledger_chart_theme(fig)
                st.markdown('<div class="pca-chart-card">', unsafe_allow_html=True)
                st.plotly_chart(fig, use_container_width=True, theme=None)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.caption("No expense data for this period.")

        with col_b:
            st.markdown('<div class="pca-section-title">Monthly trend</div>', unsafe_allow_html=True)
            trend_df = pd.DataFrame(trend)
            if not trend_df.empty:
                fig2 = px.line(
                    trend_df, x="month", y=["income", "expenses", "net"],
                    markers=True, line_shape="spline",
                )
                apply_ledger_chart_theme(fig2)
                st.markdown('<div class="pca-chart-card">', unsafe_allow_html=True)
                st.plotly_chart(fig2, use_container_width=True, theme=None)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.caption("Not enough data for a trend.")

        st.markdown('<div class="pca-section-title">Top merchants</div>', unsafe_allow_html=True)
        merch_df = pd.DataFrame(merch).sort_values("total")
        if not merch_df.empty:
            fig3 = px.bar(merch_df, x="total", y="merchant", orientation="h")
            apply_ledger_chart_theme(fig3)
            fig3.update_traces(marker_color="#4F46E5")
            st.markdown('<div class="pca-chart-card">', unsafe_allow_html=True)
            st.plotly_chart(fig3, use_container_width=True, theme=None)
            st.markdown('</div>', unsafe_allow_html=True)

        st.divider()
        st.markdown('<div class="pca-section-title">AI-generated summary</div>', unsafe_allow_html=True)
        if st.button("Generate narrative report", type="primary"):
            if not api_key:
                st.error("Please enter your free Gemini API key in the sidebar first.")
            else:
                with st.spinner("Writing your report..."):
                    try:
                        model = get_model(api_key)
                        narrative = generate_report_narrative(model, summary, trend, merch)
                        st.session_state["_narrative"] = narrative
                    except Exception as e:
                        st.error(f"Couldn't generate the report: {e}")

        if st.session_state.get("_narrative"):
            st.markdown(st.session_state["_narrative"])
            report_text = (
                f"# Pocket C.A. Financial Report — {selected_month}\n\n"
                f"{st.session_state['_narrative']}\n\n"
                f"## Numbers\n"
                f"- Total income: ${summary['total_income']:,.2f}\n"
                f"- Total expenses: ${summary['total_expenses']:,.2f}\n"
                f"- Net savings: ${summary['net_savings']:,.2f}\n"
            )
            st.download_button(
                "⬇ Download report as Markdown",
                data=report_text,
                file_name=f"pocket_ca_report_{selected_month}.md",
                mime="text/markdown",
            )

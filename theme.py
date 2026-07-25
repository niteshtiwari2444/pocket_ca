"""
theme.py
Visual identity for Pocket C.A. — clean, minimal fintech-SaaS look
(Stripe/Linear/Mercury inspired) instead of default Streamlit gray boxes.

Note on scope: this is a Streamlit app, not React. Streamlit doesn't support
Framer Motion or component libraries like Lucide React, and it doesn't expose
a way to build a true collapsible "drawer" sidebar or live theme toggle
without extra plumbing. What IS fully achievable — and implemented here —
is the visual language: color system, spacing, soft-shadow cards, rounded
corners, hover/lift micro-animations via CSS, and matching chart styling.
"""

LEDGER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --bg: #F8F7F2;
  --card: #FFFFFF;
  --text-primary: #1A1A1A;
  --text-secondary: #6B7280;
  --forest: #0F4C3A;
  --emerald: #1E7A5A;
  --gold: #D4A017;
  --success: #16A34A;
  --danger: #DC2626;
  --border-soft: rgba(15,76,58,0.08);
  --shadow-sm: 0 1px 2px rgba(15,23,20,0.04);
  --shadow-md: 0 4px 16px rgba(15,23,20,0.07);
  --shadow-lg: 0 10px 28px rgba(15,23,20,0.10);
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.stApp {
  background-color: var(--bg);
}

/* ---------- Typography ---------- */
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  color: var(--text-primary);
}
h1, h2, h3 {
  font-family: 'Inter', sans-serif !important;
  color: var(--text-primary) !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em;
}

/* ---------- Sidebar: light, minimal, soft shadow instead of hard border ---------- */
[data-testid="stSidebar"] {
  background-color: var(--card);
  box-shadow: 2px 0 12px rgba(15,23,20,0.05);
  border-right: none;
}
[data-testid="stSidebar"] * {
  color: var(--text-primary) !important;
}
[data-testid="stSidebar"] hr {
  border-color: var(--border-soft) !important;
  margin: 1.2rem 0;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
  background-color: var(--bg);
  border: 1.5px dashed rgba(15,76,58,0.25);
  border-radius: 14px;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"]:hover {
  border-color: var(--gold);
  background-color: #FBF9F2;
}

/* ---------- Compact header card ---------- */
.pca-header {
  background: var(--card);
  border-radius: 18px;
  box-shadow: var(--shadow-md);
  padding: 1.6rem 2rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: fadeInUp 0.4s ease-out;
}
.pca-greeting {
  font-size: 0.85rem;
  color: var(--text-secondary);
  font-weight: 500;
  margin-bottom: 0.2rem;
}
.pca-title {
  font-size: 1.9rem;
  font-weight: 800;
  color: var(--text-primary);
  letter-spacing: -0.02em;
  margin: 0;
}
.pca-tagline {
  font-size: 0.92rem;
  color: var(--text-secondary);
  margin-top: 0.3rem;
}
.pca-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--forest), var(--emerald));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  box-shadow: var(--shadow-sm);
  flex-shrink: 0;
}

/* ---------- KPI cards (custom, replaces st.metric for full control) ---------- */
.pca-kpi-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1.6rem;
}
.pca-kpi-card {
  background: var(--card);
  border-radius: 18px;
  box-shadow: var(--shadow-sm);
  padding: 1.4rem 1.5rem;
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  animation: fadeInUp 0.45s ease-out;
}
.pca-kpi-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}
.pca-kpi-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  margin-bottom: 0.7rem;
}
.pca-kpi-label {
  font-size: 0.78rem;
  color: var(--text-secondary);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 0.3rem;
}
.pca-kpi-value {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--text-primary);
  letter-spacing: -0.01em;
}
.pca-kpi-trend {
  display: inline-block;
  font-size: 0.76rem;
  font-weight: 600;
  padding: 0.15rem 0.55rem;
  border-radius: 999px;
  margin-top: 0.5rem;
}
.pca-kpi-trend.positive { background: rgba(22,163,74,0.1); color: var(--success); }
.pca-kpi-trend.negative { background: rgba(220,38,38,0.1); color: var(--danger); }
.pca-kpi-trend.neutral  { background: rgba(107,114,128,0.1); color: var(--text-secondary); }

/* ---------- Buttons ---------- */
.stButton button,
.stButton button p,
.stButton button span {
  font-family: 'Inter', sans-serif !important;
  font-weight: 600 !important;
}
.stButton button {
  background: var(--card) !important;
  color: var(--forest) !important;
  border: 1px solid var(--border-soft) !important;
  border-radius: 12px !important;
  box-shadow: var(--shadow-sm);
  padding: 0.5rem 1rem !important;
  transition: transform 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease !important;
}
.stButton button p, .stButton button span { color: var(--forest) !important; }
.stButton button:hover,
.stButton button:focus {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
  background: #FBFAF6 !important;
  border-color: rgba(15,76,58,0.18) !important;
}
.stButton button:active { transform: translateY(0); }
.stButton button[kind="primary"],
.stButton button[kind="primary"] p,
.stButton button[kind="primary"] span {
  color: #ffffff !important;
}
.stButton button[kind="primary"] {
  background: var(--forest) !important;
  border: none !important;
}
.stButton button[kind="primary"]:hover {
  background: var(--emerald) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab"] {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--text-secondary);
  transition: color 0.15s ease;
}
.stTabs [aria-selected="true"] {
  color: var(--forest) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
  background-color: var(--forest) !important;
  transition: all 0.25s ease;
}

/* ---------- Chat ---------- */
[data-testid="stChatMessage"] {
  border-radius: 16px;
  border: none;
  background: var(--card);
  box-shadow: var(--shadow-sm);
  animation: fadeInUp 0.25s ease-out;
}
[data-testid="stChatInput"] {
  border-radius: 14px;
}
[data-testid="stChatInput"] textarea {
  font-family: 'Inter', sans-serif;
}

/* ---------- Section titles ---------- */
.pca-section-title {
  font-family: 'Inter', sans-serif;
  color: var(--text-primary);
  font-size: 1.1rem;
  font-weight: 700;
  margin: 1.2rem 0 0.8rem 0;
}

/* ---------- Empty-state / info callout ---------- */
.pca-note {
  background: var(--card);
  border-radius: 14px;
  box-shadow: var(--shadow-sm);
  border-left: 3px solid var(--gold);
  padding: 0.9rem 1.2rem;
  font-size: 0.92rem;
  color: var(--text-secondary);
  animation: fadeIn 0.3s ease-out;
}

/* ---------- Chart card wrapper ---------- */
.pca-chart-card {
  background: var(--card);
  border-radius: 18px;
  box-shadow: var(--shadow-sm);
  padding: 1rem 1.2rem 0.4rem 1.2rem;
  margin-bottom: 1.2rem;
  transition: box-shadow 0.2s ease;
}
.pca-chart-card:hover {
  box-shadow: var(--shadow-md);
}

/* ---------- Misc widget polish ---------- */
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
  border-radius: 10px !important;
  box-shadow: var(--shadow-sm);
  border-color: var(--border-soft) !important;
}
</style>
"""

# Shared Plotly styling so charts match the new palette instead of default
# Plotly colors.
PLOTLY_COLORWAY = ["#0F4C3A", "#D4A017", "#1E7A5A", "#DC2626", "#6B7280", "#93C5AD"]


def apply_ledger_chart_theme(fig):
    """
    Apply the Pocket C.A. palette/fonts to a Plotly figure. Sets colors
    explicitly on every text element because Streamlit's built-in Plotly
    theme overlay otherwise overrides unset properties.
    IMPORTANT: pass theme=None to st.plotly_chart() when using this, or
    Streamlit will re-apply its own theme on top and wash the colors out.
    """
    ink = "#1A1A1A"
    muted = "#6B7280"
    fig.update_layout(
        colorway=PLOTLY_COLORWAY,
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(family="Inter, sans-serif", color=ink, size=13),
        title=dict(font=dict(color=ink)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=muted, size=12)),
        margin=dict(t=25, b=20, l=10, r=10),
    )
    fig.update_xaxes(
        gridcolor="rgba(15,23,20,0.06)",
        zerolinecolor="rgba(15,23,20,0.12)",
        tickfont=dict(color=muted),
        title=dict(font=dict(color=muted)),
        linecolor="rgba(15,23,20,0.12)",
    )
    fig.update_yaxes(
        gridcolor="rgba(15,23,20,0.06)",
        zerolinecolor="rgba(15,23,20,0.12)",
        tickfont=dict(color=muted),
        title=dict(font=dict(color=muted)),
        linecolor="rgba(15,23,20,0.12)",
    )
    fig.update_traces(textfont_color="#ffffff", selector=dict(type="pie"))
    return fig


def kpi_card_html(icon: str, icon_bg: str, label: str, value: str, trend_text: str = None, trend_class: str = "neutral") -> str:
    """Build one custom KPI card as HTML (used instead of st.metric for full styling control)."""
    trend_html = f'<div class="pca-kpi-trend {trend_class}">{trend_text}</div>' if trend_text else ""
    return f"""
    <div class="pca-kpi-card">
      <div class="pca-kpi-icon" style="background:{icon_bg};">{icon}</div>
      <div class="pca-kpi-label">{label}</div>
      <div class="pca-kpi-value">{value}</div>
      {trend_html}
    </div>
    """

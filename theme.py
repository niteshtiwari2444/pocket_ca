"""
theme.py
Visual identity for Pocket C.A. — professional, corporate fintech look
(think Bloomberg Terminal meets a modern private-bank portal, rather than
a playful consumer app). Muted navy/slate palette, restrained shadows,
sharper corners, no gradients or emoji-forward chrome.

Note on scope: this is a Streamlit app, not React. Streamlit doesn't support
Framer Motion or component libraries like Lucide React, and it doesn't expose
a way to build a true collapsible "drawer" sidebar or live theme toggle
without extra plumbing. What IS fully achievable — and implemented here —
is the visual language: color system, spacing, flat cards with hairline
borders, restrained micro-animations via CSS, and matching chart styling.
"""

LEDGER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap');

:root {
  --bg: #F1F3F6;
  --card: #FFFFFF;
  --text-primary: #1B2430;
  --text-secondary: #5C6773;
  --primary: #1F3A5F;
  --primary-hover: #16283F;
  --accent: #3E6B8C;
  --success: #1B7A43;
  --danger: #A02B2B;
  --border-soft: rgba(27,36,48,0.10);
  --shadow-sm: 0 1px 2px rgba(27,36,48,0.06);
  --shadow-md: 0 2px 8px rgba(27,36,48,0.08);
  --shadow-lg: 0 6px 18px rgba(27,36,48,0.10);
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(6px); }
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
  font-family: 'Source Sans 3', sans-serif;
  color: var(--text-primary);
}
h1, h2, h3 {
  font-family: 'Source Sans 3', sans-serif !important;
  color: var(--text-primary) !important;
  font-weight: 700 !important;
  letter-spacing: -0.01em;
}

/* ---------- Sidebar: flat, hairline border instead of soft glow ---------- */
[data-testid="stSidebar"] {
  background-color: var(--card);
  border-right: 1px solid var(--border-soft);
  box-shadow: none;
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
  border: 1.5px dashed rgba(27,36,48,0.25);
  border-radius: 6px;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"]:hover {
  border-color: var(--accent);
  background-color: #EDF1F5;
}

/* ---------- Header bar: flat card, no gradient avatar ---------- */
.pca-header {
  background: var(--card);
  border: 1px solid var(--border-soft);
  border-radius: 8px;
  box-shadow: var(--shadow-sm);
  padding: 1.4rem 1.8rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: fadeInUp 0.35s ease-out;
}
.pca-greeting {
  font-size: 0.8rem;
  color: var(--text-secondary);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 0.25rem;
}
.pca-title {
  font-size: 1.7rem;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.01em;
  margin: 0;
}
.pca-tagline {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-top: 0.3rem;
}
.pca-avatar {
  width: 44px;
  height: 44px;
  border-radius: 6px;
  background: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: #ffffff;
  flex-shrink: 0;
}

/* ---------- KPI cards: flat, hairline border, no lift-on-hover theatrics ---------- */
.pca-kpi-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1.6rem;
}
.pca-kpi-card {
  background: var(--card);
  border: 1px solid var(--border-soft);
  border-radius: 8px;
  box-shadow: var(--shadow-sm);
  padding: 1.3rem 1.4rem;
  transition: box-shadow 0.15s ease, border-color 0.15s ease;
  animation: fadeInUp 0.35s ease-out;
}
.pca-kpi-card:hover {
  box-shadow: var(--shadow-md);
  border-color: rgba(27,36,48,0.18);
}
.pca-kpi-icon {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  margin-bottom: 0.7rem;
}
.pca-kpi-label {
  font-size: 0.74rem;
  color: var(--text-secondary);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.3rem;
}
.pca-kpi-value {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 1.55rem;
  font-weight: 500;
  color: var(--text-primary);
  letter-spacing: -0.01em;
}
.pca-kpi-trend {
  display: inline-block;
  font-size: 0.74rem;
  font-weight: 600;
  padding: 0.12rem 0.5rem;
  border-radius: 4px;
  margin-top: 0.5rem;
}
.pca-kpi-trend.positive { background: rgba(27,122,67,0.10); color: var(--success); }
.pca-kpi-trend.negative { background: rgba(160,43,43,0.10); color: var(--danger); }
.pca-kpi-trend.neutral  { background: rgba(92,103,115,0.10); color: var(--text-secondary); }

/* ---------- Buttons: squared-off, no lift animation ---------- */
.stButton button,
.stButton button p,
.stButton button span {
  font-family: 'Source Sans 3', sans-serif !important;
  font-weight: 600 !important;
}
.stButton button {
  background: var(--card) !important;
  color: var(--primary) !important;
  border: 1px solid var(--border-soft) !important;
  border-radius: 6px !important;
  box-shadow: none;
  padding: 0.5rem 1rem !important;
  transition: background-color 0.15s ease, border-color 0.15s ease !important;
}
.stButton button p, .stButton button span { color: var(--primary) !important; }
.stButton button:hover,
.stButton button:focus {
  background: #EDF1F5 !important;
  border-color: rgba(27,36,48,0.22) !important;
}
.stButton button[kind="primary"],
.stButton button[kind="primary"] p,
.stButton button[kind="primary"] span {
  color: #ffffff !important;
}
.stButton button[kind="primary"] {
  background: var(--primary) !important;
  border: none !important;
}
.stButton button[kind="primary"]:hover {
  background: var(--primary-hover) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab"] {
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--text-secondary);
  transition: color 0.15s ease;
}
.stTabs [aria-selected="true"] {
  color: var(--primary) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
  background-color: var(--primary) !important;
  transition: all 0.2s ease;
}

/* ---------- Chat ---------- */
[data-testid="stChatMessage"] {
  border-radius: 8px;
  border: 1px solid var(--border-soft);
  background: var(--card);
  box-shadow: none;
  animation: fadeIn 0.2s ease-out;
}
[data-testid="stChatInput"] {
  border-radius: 6px;
}
[data-testid="stChatInput"] textarea {
  font-family: 'Source Sans 3', sans-serif;
}

/* ---------- Section titles ---------- */
.pca-section-title {
  font-family: 'Source Sans 3', sans-serif;
  color: var(--text-primary);
  font-size: 1.05rem;
  font-weight: 700;
  margin: 1.2rem 0 0.8rem 0;
  border-bottom: 1px solid var(--border-soft);
  padding-bottom: 0.4rem;
}

/* ---------- Empty-state / info callout ---------- */
.pca-note {
  background: var(--card);
  border: 1px solid var(--border-soft);
  border-radius: 6px;
  border-left: 3px solid var(--accent);
  padding: 0.9rem 1.2rem;
  font-size: 0.92rem;
  color: var(--text-secondary);
  animation: fadeIn 0.25s ease-out;
}

/* ---------- Chart card wrapper ---------- */
.pca-chart-card {
  background: var(--card);
  border: 1px solid var(--border-soft);
  border-radius: 8px;
  padding: 1rem 1.2rem 0.4rem 1.2rem;
  margin-bottom: 1.2rem;
  box-shadow: var(--shadow-sm);
}

/* ---------- Misc widget polish ---------- */
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
  border-radius: 6px !important;
  box-shadow: none;
  border-color: var(--border-soft) !important;
}
</style>
"""

# Shared Plotly styling so charts match the new palette instead of default
# Plotly colors — muted navy/slate/steel instead of bright indigo/violet.
PLOTLY_COLORWAY = ["#1F3A5F", "#3E6B8C", "#7C93A8", "#A02B2B", "#1B7A43", "#B8C2CC"]


def apply_ledger_chart_theme(fig):
    """
    Apply the Pocket C.A. palette/fonts to a Plotly figure. Sets colors
    explicitly on every text element because Streamlit's built-in Plotly
    theme overlay otherwise overrides unset properties.
    IMPORTANT: pass theme=None to st.plotly_chart() when using this, or
    Streamlit will re-apply its own theme on top and wash the colors out.
    """
    ink = "#1B2430"
    muted = "#5C6773"
    fig.update_layout(
        colorway=PLOTLY_COLORWAY,
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(family="Source Sans 3, sans-serif", color=ink, size=13),
        title=dict(font=dict(color=ink)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=muted, size=12)),
        margin=dict(t=25, b=20, l=10, r=10),
    )
    fig.update_xaxes(
        gridcolor="rgba(27,36,48,0.06)",
        zerolinecolor="rgba(27,36,48,0.12)",
        tickfont=dict(color=muted),
        title=dict(font=dict(color=muted)),
        linecolor="rgba(27,36,48,0.12)",
    )
    fig.update_yaxes(
        gridcolor="rgba(27,36,48,0.06)",
        zerolinecolor="rgba(27,36,48,0.12)",
        tickfont=dict(color=muted),
        title=dict(font=dict(color=muted)),
        linecolor="rgba(27,36,48,0.12)",
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

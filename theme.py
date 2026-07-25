"""
theme.py
Visual identity for Pocket C.A. — a "general ledger" look: deep forest
green + parchment/cream cards + gold hairline accents + serif headings
and monospace figures. Modeled after a physical accounting ledger /
private-bank statement rather than a generic SaaS dashboard.

Important: every color below is FORCED with !important so the app looks
identical whether the person has Streamlit's own theme set to "Light" or
"Dark" in Settings. We don't inherit Streamlit's background/text colors
at all — the ledger palette (forest green header/sidebar, cream cards,
dark-green ink text, gold accents) is applied unconditionally, so nothing
goes low-contrast or invisible when the user's system/Streamlit theme
flips.

Note on scope: this is a Streamlit app, not React. Streamlit doesn't support
Framer Motion or component libraries like Lucide React, and it doesn't expose
a way to build a true collapsible "drawer" sidebar or live theme toggle
without extra plumbing. What IS fully achievable — and implemented here —
is the visual language: color system, spacing, hairline-bordered cards,
restrained micro-animations via CSS, and matching chart styling.
"""

LEDGER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Source+Sans+3:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap');

:root {
  --ink: #16241D;
  --ink-soft: #3E4A3F;
  --forest: #0F3D2E;
  --forest-deep: #0A2E22;
  --forest-hover: #0C3226;
  --cream: #F5EFDC;
  --page-bg: #FBF8EF;
  --gold: #C9A227;
  --gold-soft: rgba(201,162,39,0.35);
  --gold-wash: rgba(201,162,39,0.10);
  --success: #1F7A4D;
  --danger: #A6392E;
  --shadow-sm: 0 1px 2px rgba(15,61,46,0.08);
  --shadow-md: 0 3px 10px rgba(15,61,46,0.12);
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* ---------- Force the ledger palette regardless of Streamlit's own
   light/dark theme setting ---------- */
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
  background-color: var(--page-bg) !important;
  color: var(--ink) !important;
}
[data-testid="stHeader"] {
  background-color: transparent !important;
}

/* ---------- Typography ---------- */
html, body, [class*="css"], p, span, div, label {
  font-family: 'Source Sans 3', sans-serif;
  color: var(--ink);
}
h1, h2, h3 {
  font-family: 'Playfair Display', serif !important;
  color: var(--forest) !important;
  font-weight: 700 !important;
  letter-spacing: -0.01em;
}

/* ---------- Sidebar: deep forest green, cream text, gold hairlines ---------- */
[data-testid="stSidebar"] {
  background-color: var(--forest) !important;
  border-right: 1px solid var(--gold-soft);
}
[data-testid="stSidebar"] * {
  color: var(--cream) !important;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
  font-family: 'Playfair Display', serif !important;
  color: var(--cream) !important;
}
[data-testid="stSidebar"] hr {
  border-color: var(--gold-soft) !important;
  margin: 1.2rem 0;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
  background-color: var(--forest-hover) !important;
  border: 1.5px dashed var(--gold-soft) !important;
  border-radius: 6px;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"]:hover {
  border-color: var(--gold) !important;
  background-color: var(--forest-deep) !important;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button {
  background-color: var(--cream) !important;
  color: var(--forest) !important;
  border: none !important;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button * {
  color: var(--forest) !important;
}
[data-testid="stSidebar"] [data-testid="stTextInput"] input {
  background-color: var(--forest-hover) !important;
  color: var(--cream) !important;
  border: 1px solid var(--gold-soft) !important;
  border-radius: 6px !important;
}
[data-testid="stSidebar"] [data-testid="stAlert"] {
  background-color: var(--forest-hover) !important;
  border: 1px solid var(--gold-soft) !important;
  border-radius: 6px;
}
[data-testid="stSidebar"] [data-testid="stExpander"] {
  background-color: var(--forest-hover) !important;
  border: 1px solid var(--gold-soft) !important;
  border-radius: 6px;
}

/* ---------- Header banner: forest green with gold eyebrow + serif title ---------- */
.pca-header {
  background: linear-gradient(155deg, var(--forest) 0%, var(--forest-deep) 100%);
  border-radius: 10px;
  box-shadow: var(--shadow-md);
  padding: 1.9rem 2.2rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: fadeInUp 0.35s ease-out;
}
.pca-eyebrow {
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  margin-bottom: 0.6rem;
}
.pca-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.3rem;
  font-weight: 800;
  color: var(--cream);
  letter-spacing: -0.01em;
  margin: 0;
}
.pca-tagline {
  font-size: 0.92rem;
  color: rgba(245,239,220,0.78);
  margin-top: 0.5rem;
  max-width: 46ch;
}
.pca-greeting {
  /* kept for backward compatibility with older markup */
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  margin-bottom: 0.6rem;
}
.pca-avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: transparent;
  border: 1.5px solid var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  flex-shrink: 0;
}

/* ---------- KPI cards: parchment with gold hairline border ---------- */
.pca-kpi-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1.6rem;
}
.pca-kpi-card {
  background: var(--cream);
  border: 1px solid var(--gold-soft);
  border-radius: 8px;
  box-shadow: var(--shadow-sm);
  padding: 1.3rem 1.5rem;
  transition: box-shadow 0.18s ease, border-color 0.18s ease;
  animation: fadeInUp 0.35s ease-out;
}
.pca-kpi-card:hover {
  box-shadow: var(--shadow-md);
  border-color: var(--gold);
}
.pca-kpi-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  margin-bottom: 0.7rem;
}
.pca-kpi-label {
  font-size: 0.74rem;
  color: var(--ink-soft);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.35rem;
}
.pca-kpi-value {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--forest);
  letter-spacing: -0.01em;
}
.pca-kpi-trend {
  display: inline-block;
  font-size: 0.74rem;
  font-weight: 600;
  padding: 0.15rem 0.55rem;
  border-radius: 999px;
  margin-top: 0.55rem;
}
.pca-kpi-trend.positive { background: rgba(31,122,77,0.12); color: var(--success); }
.pca-kpi-trend.negative { background: rgba(166,57,46,0.12); color: var(--danger); }
.pca-kpi-trend.neutral  { background: rgba(62,74,63,0.10); color: var(--ink-soft); }

/* ---------- Buttons ---------- */
.stButton button,
.stButton button p,
.stButton button span {
  font-family: 'Source Sans 3', sans-serif !important;
  font-weight: 600 !important;
}
.stButton button {
  background: var(--cream) !important;
  color: var(--forest) !important;
  border: 1px solid var(--gold-soft) !important;
  border-radius: 6px !important;
  box-shadow: var(--shadow-sm);
  padding: 0.5rem 1rem !important;
  transition: background-color 0.15s ease, border-color 0.15s ease !important;
}
.stButton button p, .stButton button span { color: var(--forest) !important; }
.stButton button:hover,
.stButton button:focus {
  background: var(--gold-wash) !important;
  border-color: var(--gold) !important;
}
.stButton button[kind="primary"],
.stButton button[kind="primary"] p,
.stButton button[kind="primary"] span {
  color: var(--cream) !important;
}
.stButton button[kind="primary"] {
  background: var(--forest) !important;
  border: 1px solid var(--gold) !important;
}
.stButton button[kind="primary"]:hover {
  background: var(--forest-hover) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab"] {
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 600;
  font-size: 0.92rem;
  color: var(--ink-soft) !important;
  transition: color 0.15s ease;
}
.stTabs [data-baseweb="tab"] p { color: inherit !important; }
.stTabs [aria-selected="true"] {
  color: var(--forest) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
  background-color: var(--gold) !important;
  transition: all 0.2s ease;
}
.stTabs [data-baseweb="tab-border"] {
  background-color: var(--gold-wash) !important;
}

/* ---------- Chat ---------- */
[data-testid="stChatMessage"] {
  border-radius: 10px;
  border: 1px solid var(--gold-soft);
  background: var(--cream) !important;
  box-shadow: var(--shadow-sm);
  animation: fadeIn 0.2s ease-out;
}
[data-testid="stChatMessage"] * {
  color: var(--ink) !important;
}
[data-testid="stChatInput"] {
  border-radius: 8px;
  background: var(--cream) !important;
  border: 1px solid var(--gold-soft) !important;
}
[data-testid="stChatInput"] textarea {
  font-family: 'Source Sans 3', sans-serif;
  color: var(--ink) !important;
}

/* ---------- Section titles ---------- */
.pca-section-title {
  font-family: 'Playfair Display', serif;
  color: var(--forest);
  font-size: 1.25rem;
  font-weight: 700;
  margin: 1.2rem 0 0.8rem 0;
  border-bottom: 2px solid var(--gold);
  padding-bottom: 0.4rem;
  display: inline-block;
}

/* ---------- Empty-state / info callout ---------- */
.pca-note {
  background: var(--cream) !important;
  border: 1px solid var(--gold-soft);
  border-radius: 6px;
  border-left: 3px solid var(--gold);
  padding: 0.9rem 1.2rem;
  font-size: 0.92rem;
  color: var(--ink-soft) !important;
  animation: fadeIn 0.25s ease-out;
}

/* ---------- Chart card wrapper ---------- */
.pca-chart-card {
  background: var(--cream) !important;
  border: 1px solid var(--gold-soft);
  border-radius: 8px;
  padding: 1rem 1.2rem 0.4rem 1.2rem;
  margin-bottom: 1.2rem;
  box-shadow: var(--shadow-sm);
}

/* ---------- Misc widget polish ---------- */
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
  background-color: var(--cream) !important;
  border-radius: 6px !important;
  box-shadow: var(--shadow-sm);
  border-color: var(--gold-soft) !important;
  color: var(--ink) !important;
}
[data-testid="stSelectbox"] div[data-baseweb="select"] * {
  color: var(--ink) !important;
}
[data-baseweb="popover"] li, [data-baseweb="menu"] li {
  background-color: var(--cream) !important;
  color: var(--ink) !important;
}
[data-testid="stDataFrame"] {
  border: 1px solid var(--gold-soft);
  border-radius: 6px;
}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
  color: var(--ink);
}
[data-testid="stCaptionContainer"], .stCaption, small {
  color: var(--ink-soft) !important;
}
</style>
"""

# Shared Plotly styling so charts match the ledger palette — deep forest,
# gold, and muted olive/rust instead of default Plotly colors.
PLOTLY_COLORWAY = ["#0F3D2E", "#C9A227", "#5E7C6B", "#A6392E", "#8C9A6E", "#D8C48A"]


def apply_ledger_chart_theme(fig):
    """
    Apply the Pocket C.A. ledger palette/fonts to a Plotly figure. Sets
    colors explicitly on every text element because Streamlit's built-in
    Plotly theme overlay otherwise overrides unset properties, and because
    charts must stay legible whether Streamlit's own theme is set to Light
    or Dark.
    IMPORTANT: pass theme=None to st.plotly_chart() when using this, or
    Streamlit will re-apply its own theme on top and wash the colors out.
    """
    ink = "#16241D"
    muted = "#3E4A3F"
    cream = "#F5EFDC"
    fig.update_layout(
        colorway=PLOTLY_COLORWAY,
        paper_bgcolor=cream,
        plot_bgcolor=cream,
        font=dict(family="Source Sans 3, sans-serif", color=ink, size=13),
        title=dict(font=dict(family="Playfair Display, serif", color=ink)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=muted, size=12)),
        margin=dict(t=25, b=20, l=10, r=10),
    )
    fig.update_xaxes(
        gridcolor="rgba(15,61,46,0.10)",
        zerolinecolor="rgba(15,61,46,0.18)",
        tickfont=dict(color=muted),
        title=dict(font=dict(color=muted)),
        linecolor="rgba(15,61,46,0.18)",
    )
    fig.update_yaxes(
        gridcolor="rgba(15,61,46,0.10)",
        zerolinecolor="rgba(15,61,46,0.18)",
        tickfont=dict(color=muted),
        title=dict(font=dict(color=muted)),
        linecolor="rgba(15,61,46,0.18)",
    )
    fig.update_traces(textfont_color="#F5EFDC", selector=dict(type="pie"))
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

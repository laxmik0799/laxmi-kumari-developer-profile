"""
Laxmi Kumari: developer profile as a Streamlit web app.

Run locally:   pip install -r requirements.txt && streamlit run app.py
Content lives in profile_data.py; this file is only presentation.
"""

from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

from profile_data import (
    CAREER_GOALS,
    EXPERIENCE,
    INTERESTS,
    LINKS,
    PROFILE,
    PROJECTS,
    SIDE_PROJECTS,
    SKILLS,
    STATS_CARDS,
)

ROOT = Path(__file__).parent

st.set_page_config(
    page_title=f"{PROFILE['name']} · Software Developer",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={"About": f"{PROFILE['name']}: developer profile · {LINKS['repo']}"},
)


# ───────────────────────── helpers ─────────────────────────
@st.cache_data
def b64(path: str) -> str:
    """Base64-encode a repo file so it can be inlined in HTML (works for PNG and SVG)."""
    return base64.b64encode((ROOT / path).read_bytes()).decode()


def img_tag(path: str, alt: str, style: str = "width:100%") -> str:
    mime = "image/svg+xml" if path.endswith(".svg") else "image/png"
    return f'<img src="data:{mime};base64,{b64(path)}" alt="{alt}" style="{style}" />'


def chips(items: list[str], highlight: set[str] | None = None) -> str:
    highlight = highlight or set()
    return "".join(f'<span class="chip{" on" if i in highlight else ""}">{i}</span>' for i in items)


def section(index: str, eyebrow: str, title: str, anchor: str) -> None:
    st.markdown(f'<p class="eyebrow"><span>{index}</span> ── {eyebrow}</p>', unsafe_allow_html=True)
    st.header(title, anchor=anchor, divider=False)


def divider() -> None:
    st.markdown(img_tag("assets/images/divider.png", "", "width:100%;margin:2.2rem 0 1rem"), unsafe_allow_html=True)


# ───────────────────────── styles ─────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap');

:root { --violet:#8b5cf6; --blue:#4f7cff; --cyan:#22d3ee; --ink:#0b1024; --muted:#94a3b8; }
html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; }
[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(900px 500px at 85% -5%, rgba(139,92,246,.18), transparent 60%),
    radial-gradient(700px 500px at -10% 40%, rgba(34,211,238,.07), transparent 60%),
    #05060f;
}
[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
.block-container { max-width: 1180px; padding-top: 2.2rem; padding-bottom: 4rem; }

h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; letter-spacing: -.01em; }
h2 { font-size: 2.1rem !important; font-weight: 700 !important; color: #fff !important; padding-top: .2rem !important; }

.eyebrow { font-family: 'JetBrains Mono', monospace; font-size: .78rem; letter-spacing: .25em; text-transform: uppercase;
           color: var(--cyan); margin-bottom: -.6rem; }
.eyebrow span { color: #a78bfa; }

.card { background: rgba(255,255,255,.035); border: 1px solid rgba(255,255,255,.09); border-radius: 18px; padding: 1.3rem 1.4rem;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.05); transition: transform .35s ease, border-color .35s ease, box-shadow .35s ease; height: 100%; }
.card:hover { transform: translateY(-3px); border-color: rgba(139,92,246,.55); box-shadow: 0 18px 40px -22px rgba(139,92,246,.8); }
.card .k { font-family: 'JetBrains Mono', monospace; font-size: .72rem; letter-spacing: .18em; text-transform: uppercase; color: #64748b; }
.card .v { font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 1.08rem; color: #fff; margin-top: .35rem; }
.card p { color: #cbd5e1; margin: .4rem 0 0; font-size: .95rem; }

.chip { display: inline-block; margin: 0 .4rem .5rem 0; padding: .32rem .8rem; border-radius: 999px; font-family: 'JetBrains Mono', monospace;
        font-size: .82rem; color: #cbd5e1; border: 1px solid rgba(255,255,255,.12); background: rgba(255,255,255,.04); transition: all .25s ease; }
.chip:hover { border-color: rgba(34,211,238,.6); color: #fff; }
.chip.on { color: #fff; border-color: var(--cyan); background: rgba(34,211,238,.14); box-shadow: 0 0 18px -6px var(--cyan); }

.goal { display: flex; gap: 1rem; align-items: baseline; padding: .7rem 0; border-bottom: 1px solid rgba(255,255,255,.06); color: #e2e8f0; }
.goal b { font-family: 'JetBrains Mono', monospace; color: #a78bfa; font-weight: 500; }

.badge { display:inline-flex; align-items:center; gap:.45rem; padding:.25rem .7rem; border-radius:999px; font-size:.78rem;
         border:1px solid rgba(52,211,153,.35); color:#6ee7b7; background:rgba(52,211,153,.08); font-family:'JetBrains Mono',monospace; }
.badge i { width:7px; height:7px; border-radius:50%; background:#34d399; display:inline-block; }

.note { font-size: .8rem; color: #64748b; font-family: 'JetBrains Mono', monospace; letter-spacing: .04em; }

[data-testid="stSidebar"] { background: #070a18; border-right: 1px solid rgba(255,255,255,.06); }
[data-testid="stSidebar"] a.nav { display:block; padding:.42rem .2rem; color:#cbd5e1; text-decoration:none; font-size:.95rem; border-radius:8px; }
[data-testid="stSidebar"] a.nav:hover { color:#fff; background: rgba(255,255,255,.05); padding-left:.6rem; transition: all .2s ease; }

[data-testid="stTabs"] button p { font-family: 'Space Grotesk', sans-serif; font-size: 1rem; }
img { border-radius: 14px; }
</style>
""",
    unsafe_allow_html=True,
)

# ───────────────────────── sidebar ─────────────────────────
NAV = [
    ("about", "Introduction"),
    ("skills", "Technical Skills"),
    ("experience", "Experience"),
    ("projects", "Featured Projects"),
    ("interests", "Interests & Goals"),
    ("activity", "GitHub Activity"),
    ("connect", "Connect"),
]
with st.sidebar:
    st.markdown(
        f"""<p style="font-family:'Space Grotesk';font-weight:700;letter-spacing:.2em;font-size:1.05rem;color:#fff;margin:0">
        {PROFILE['brand'].split('.')[0]}<span style="color:#22d3ee">.{PROFILE['brand'].split('.')[1]}</span></p>
        <p class="note" style="margin-top:.2rem">{PROFILE['tagline']}</p>""",
        unsafe_allow_html=True,
    )
    st.markdown("".join(f'<a class="nav" href="#{a}" target="_self">{t}</a>' for a, t in NAV), unsafe_allow_html=True)
    st.divider()
    st.link_button("GitHub profile", LINKS["github"], icon=":material/code:", use_container_width=True)
    if LINKS["linkedin"]:
        st.link_button("LinkedIn", LINKS["linkedin"], icon=":material/work:", use_container_width=True)
    st.link_button("Source of this app", LINKS["repo"], icon=":material/folder_open:", use_container_width=True)

# ───────────────────────── hero ─────────────────────────
st.markdown(img_tag("assets/images/developer-banner.png", f"{PROFILE['name']}: {' / '.join(PROFILE['titles'])}"), unsafe_allow_html=True)
st.markdown(
    f'<div style="margin:1rem 0 0;display:flex;gap:.6rem;flex-wrap:wrap;align-items:center">'
    f'<span class="badge"><i></i>{PROFILE["role"]} · {PROFILE["organisation"]}</span>'
    f'<span class="chip" style="margin:0">IIT (BHU) Varanasi</span></div>',
    unsafe_allow_html=True,
)

# ───────────────────────── about ─────────────────────────
divider()
section("01", "Introduction", "Who I am", "about")
left, right = st.columns([1.35, 1], gap="large")
with left:
    for para in PROFILE["intro"]:
        st.markdown(para)
    st.code(
        f"role        → {PROFILE['role']} @ {PROFILE['organisation']}\n"
        "education   → B.Tech · IIT (BHU) Varanasi\n"
        "focus       → Backend · Full-Stack · System Design · AI",
        language="text",
    )
with right:
    st.markdown(img_tag("assets/images/developer-illustration.png", "Illustration: technologies orbiting the LK monogram"), unsafe_allow_html=True)

cols = st.columns(4)
for col, (k, v) in zip(
    cols,
    [
        ("Role", PROFILE["role"]),
        ("Organisation", PROFILE["organisation"]),
        ("Education", "IIT (BHU) Varanasi"),
        ("Focus", "Backend · Full-Stack · AI"),
    ],
):
    col.markdown(f'<div class="card"><div class="k">{k}</div><div class="v">{v}</div></div>', unsafe_allow_html=True)

# ───────────────────────── skills ─────────────────────────
divider()
section("02", "Technical Skills", "From the interface to the data layer", "skills")
st.markdown(img_tag("assets/images/tech-stack.png", "Technology stack graphic"), unsafe_allow_html=True)
st.write("")

f1, f2 = st.columns([2, 1])
with f1:
    chosen = st.pills("Show categories", list(SKILLS), selection_mode="multi", default=list(SKILLS), key="skill_cats")
with f2:
    query = st.text_input("Find a technology", placeholder="e.g. Spring, React, SQL", key="skill_q").strip().lower()

matches = {s for items in SKILLS.values() for s in items if query and query in s.lower()}
shown = [c for c in SKILLS if c in (chosen or [])]
if query and not matches:
    st.caption(f"No technology matches “{query}”.")
grid = st.columns(3)
for i, cat in enumerate(shown):
    items = SKILLS[cat]
    if query and not (set(items) & matches):
        continue
    grid[i % 3].markdown(
        f'<div class="card" style="margin-bottom:1rem"><div class="v" style="margin:0 0 .8rem">{cat}</div>{chips(items, matches)}</div>',
        unsafe_allow_html=True,
    )
if not shown:
    st.info("Select at least one category to see technologies.")

# ───────────────────────── experience ─────────────────────────
divider()
section("03", "Professional Experience", "Where I build", "experience")
for job in EXPERIENCE:
    with st.container(border=True):
        a, b = st.columns([4, 1])
        a.subheader(f"💼 {job['title']} · {job['org']}", anchor=False)
        b.markdown(f'<div style="text-align:right;padding-top:.6rem"><span class="badge"><i></i>{job["status"]}</span></div>', unsafe_allow_html=True)
        st.markdown(job["summary"])
        for p in job["points"]:
            st.markdown(f"- {p}")

# ───────────────────────── projects ─────────────────────────
divider()
section("04", "Featured Projects", "Projects that solve real problems", "projects")
choice = st.segmented_control("Project", list(PROJECTS), default=list(PROJECTS)[0], key="project", label_visibility="collapsed")
proj = PROJECTS[choice or list(PROJECTS)[0]]
name = choice or list(PROJECTS)[0]

st.markdown(f"### {proj['icon']} {name}")
st.markdown(f"**{proj['tagline']}** &nbsp; <span class='chip'>{proj['category']}</span>", unsafe_allow_html=True)
st.markdown(img_tag(proj["image"], f"{name} illustrative graphic"), unsafe_allow_html=True)

t_over, t_arch, t_feat, t_flow, t_mine = st.tabs(["Overview", "Architecture", "Features", "Workflow", "My contributions"])
with t_over:
    c1, c2 = st.columns(2, gap="large")
    c1.markdown("##### Problem")
    c1.markdown(proj["problem"])
    c2.markdown("##### Objective")
    c2.markdown(proj["objective"])
    st.markdown("##### Technology")
    st.markdown(chips(proj["stack"]), unsafe_allow_html=True)
with t_arch:
    st.markdown(img_tag(proj["diagram"], f"{name} architecture diagram"), unsafe_allow_html=True)
with t_feat:
    fc = st.columns(4)
    for i, (k, v) in enumerate(proj["features"].items()):
        fc[i % 4].markdown(f'<div class="card" style="margin-bottom:1rem"><div class="v" style="margin:0">{k}</div><p>{v}</p></div>', unsafe_allow_html=True)
with t_flow:
    st.graphviz_chart(proj["workflow"], use_container_width=True)
with t_mine:
    for c in proj["contributions"]:
        st.markdown(f"- {c}")
    st.caption("Built in a professional setting. Described at a high level, with no proprietary code, data or internal details.")

st.link_button(f"Read the full {name} case study on GitHub", f"{LINKS['repo']}/blob/main/{proj['doc']}", icon=":material/description:")

for sp in SIDE_PROJECTS:
    st.markdown(
        f'<div class="card" style="margin-top:1.4rem"><div class="k">Also building</div>'
        f'<div class="v">🪐 {sp["name"]}</div><p>{sp["summary"]}</p>'
        f'<p style="margin-top:.8rem"><a href="{sp["live"]}" target="_blank">Live demo ↗</a> &nbsp;·&nbsp; '
        f'<a href="{sp["code"]}" target="_blank">Code ↗</a></p></div>',
        unsafe_allow_html=True,
    )

# ───────────────────────── interests & goals ─────────────────────────
divider()
section("05", "Interests & Goals", "What drives me", "interests")
ic = st.columns(len(INTERESTS))
for col, (emoji, title, desc) in zip(ic, INTERESTS):
    col.markdown(f'<div class="card"><div style="font-size:1.6rem">{emoji}</div><div class="v">{title}</div><p>{desc}</p></div>', unsafe_allow_html=True)

st.write("")
st.markdown("#### Career goals")
g1, g2 = st.columns(2, gap="large")
for i, goal in enumerate(CAREER_GOALS):
    (g1 if i < 4 else g2).markdown(f'<div class="goal"><b>{i + 1:02d}</b>{goal}</div>', unsafe_allow_html=True)

# ───────────────────────── activity ─────────────────────────
divider()
section("06", "GitHub Activity", "Building in public", "activity")
available = [(p, a) for p, a in STATS_CARDS if (ROOT / p).exists()]
if available:
    st.markdown(img_tag(available[0][0], available[0][1]), unsafe_allow_html=True)
    rest = st.columns(max(1, len(available) - 1))
    for col, (p, a) in zip(rest, available[1:]):
        col.markdown(img_tag(p, a), unsafe_allow_html=True)
    st.caption("Generated daily by a GitHub Action in the profile repository.")
else:
    st.caption("Stats cards appear here after the repository's GitHub Action runs.")

# ───────────────────────── connect ─────────────────────────
divider()
section("07", "Connect", "Let's build something meaningful", "connect")
st.markdown("Open to conversations about backend engineering, full-stack products and AI-driven applications.")
cc = st.columns(3)
cc[0].link_button("GitHub · laxmik0799", LINKS["github"], icon=":material/code:", use_container_width=True)
if LINKS["linkedin"]:
    cc[1].link_button("LinkedIn", LINKS["linkedin"], icon=":material/work:", use_container_width=True)
if LINKS["email"]:
    cc[2].link_button("Email", f"mailto:{LINKS['email']}", icon=":material/mail:", use_container_width=True)

st.markdown(
    f'<p class="note" style="text-align:center;margin-top:3rem">© {PROFILE["name"]} · {PROFILE["brand"]} · '
    "Graphics are original illustrations</p>",
    unsafe_allow_html=True,
)


# =====================================================
# GHANA LEFT-BACK DEBATE
# Baba Rahman vs Derrick Köhn
# =====================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="🇬🇭 Ghana Left-Back Debate",
    layout="wide"
)

# ---------------------------------------------------
# BANNER
# ---------------------------------------------------
banner = Image.open("players.jpg")

st.image(
    banner,
    use_container_width=True
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🇬🇭 Baba Rahman vs Derrick Köhn")
st.subheader("Who Should Start at Left-Back for the Black Stars?")

st.markdown("""
This dashboard compares the 2025/26 league performances of
Baba Rahman and Derrick Köhn across:

- Attacking Output
- Creativity
- Possession
- Defensive Performance
- Discipline
- Overall Readiness
""")

# =====================================================
# DATA
# =====================================================

df = pd.DataFrame({

    "Player": ["Baba Rahman", "Derrick Köhn"],

    "Matches": [25, 29],
    "Minutes": [1920, 1899],
    "90s": [21.3, 21.1],

    "Goals": [2, 1],
    "Assists": [2, 2],
    "xG": [1.43, 2.15],
    "xA": [1.87, 3.78],

    "Shots": [14, 28],

    "Pass Accuracy": [78.8, 76.3],

    "Chances Created": [13, 25],
    "Big Chances Created": [4, 5],

    "Successful Crosses": [9, 31],
    "Cross Accuracy": [19.1, 27.0],

    "Successful Dribbles": [5, 11],
    "Dribble Success": [31.2, 42.3],

    "Duels Won": [78, 67],
    "Duel Win %": [51.3, 44.1],

    "Aerial Duels Won": [23, 6],
    "Aerial Win %": [53.5, 50.0],

    "Touches": [1508, 1138],
    "Touches Box": [38, 33],

    "Dispossessed": [8, 23],
    "Fouls Won": [21, 16],

    "Defensive Contributions": [114, 87],
    "Tackles": [29, 34],
    "Interceptions": [19, 8],
    "Recoveries": [69, 88],
    "Clearances": [61, 40],
    "Dribbled Past": [11, 9],

    "Clean Sheets": [9, 3],

    "Goals Conceded": [18, 32],
    "xGA": [22.0, 29.9],

    "Yellow Cards": [3, 5],
    "Red Cards": [0, 1]
})

# =====================================================
# KPI SECTION
# =====================================================

st.header("📊 Player Overview")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🇬🇭 Baba Rahman")

    st.metric("Minutes", "1,920")
    st.metric("Goals", "2")
    st.metric("Assists", "2")
    st.metric("Clean Sheets", "9")

with col2:
    st.subheader("🇬🇭 Derrick Köhn")

    st.metric("Minutes", "1,899")
    st.metric("Goals", "1")
    st.metric("Assists", "2")
    st.metric("Clean Sheets", "3")

# =====================================================
# RAW DATA
# =====================================================

st.header("📋 Comparison Dataset")

st.dataframe(df, use_container_width=True)

# =====================================================
# ATTACKING OUTPUT
# =====================================================

st.header("⚽ Attacking Output")

attack_df = pd.DataFrame({
    "Metric": [
        "Goals",
        "Assists",
        "xG",
        "xA",
        "Chances Created"
    ],
    "Baba Rahman": [
        2,
        2,
        1.43,
        1.87,
        13
    ],
    "Derrick Köhn": [
        1,
        2,
        2.15,
        3.78,
        25
    ]
})

fig = px.bar(
    attack_df,
    x="Metric",
    y=["Baba Rahman", "Derrick Köhn"],
    barmode="group"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# POSSESSION
# =====================================================

st.header("🎯 Possession & Ball Security")

possession_df = pd.DataFrame({
    "Metric": [
        "Pass Accuracy",
        "Duel Win %",
        "Aerial Win %",
        "Touches Box"
    ],
    "Baba Rahman": [
        78.8,
        51.3,
        53.5,
        38
    ],
    "Derrick Köhn": [
        76.3,
        44.1,
        50.0,
        33
    ]
})

fig = px.bar(
    possession_df,
    x="Metric",
    y=["Baba Rahman", "Derrick Köhn"],
    barmode="group"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# DEFENSIVE COMPARISON
# =====================================================

st.header("🛡️ Defensive Performance")

def_df = pd.DataFrame({
    "Metric": [
        "Tackles",
        "Interceptions",
        "Recoveries",
        "Clearances"
    ],
    "Baba Rahman": [
        29,
        19,
        69,
        61
    ],
    "Derrick Köhn": [
        34,
        8,
        88,
        40
    ]
})

fig = px.bar(
    def_df,
    x="Metric",
    y=["Baba Rahman", "Derrick Köhn"],
    barmode="group"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# DISCIPLINE
# =====================================================

st.header("🟨 Discipline")

discipline_df = pd.DataFrame({
    "Metric": [
        "Yellow Cards",
        "Red Cards"
    ],
    "Baba Rahman": [
        3,
        0
    ],
    "Derrick Köhn": [
        5,
        1
    ]
})

fig = px.bar(
    discipline_df,
    x="Metric",
    y=["Baba Rahman", "Derrick Köhn"],
    barmode="group"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# RADAR CHART
# =====================================================

st.header("📡 Player Profile Radar")

radar = pd.DataFrame({
    "Metric": [
        "Attack",
        "Creativity",
        "Defense",
        "Possession",
        "Discipline"
    ],

    "Baba": [
        54.319685,
        46.465020,
        100.000000,
        100.000000,
        100.000000
    ],

    "Kohn": [
        100.000000,
        100.000000,
        96.410884,
        92.810458,
        64.705882
    ]
})

fig = go.Figure()

fig.add_trace(
    go.Scatterpolar(
        r=radar["Baba"],
        theta=radar["Metric"],
        fill="toself",
        name="Baba Rahman"
    )
)

fig.add_trace(
    go.Scatterpolar(
        r=radar["Kohn"],
        theta=radar["Metric"],
        fill="toself",
        name="Derrick Köhn"
    )
)

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0,100]
        )
    ),
    showlegend=True
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# READINESS INDEX
# =====================================================

st.header("🏆 Left-Back Readiness Index")

readiness = pd.DataFrame({
    "Player": [
        "Baba Rahman",
        "Derrick Köhn"
    ],
    "Score": [
        86.3,
        93.4
    ]
})

fig = px.bar(
    readiness,
    x="Player",
    y="Score",
    text="Score",
    title="🇬🇭 Left-Back Readiness Index"
)

fig.update_traces(
    texttemplate="%{text:.1f}",
    textposition="outside"
)

fig.update_layout(
    yaxis_title="Readiness Score",
    xaxis_title="Player"
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
### Analyst Verdict

The data reveals two contrasting left-back profiles.

Derrick Köhn scores highest in the readiness model due to:

• Superior attacking output
• Greater creativity
• Higher xA
• More chances created
• Stronger crossing threat

Baba Rahman remains the stronger defensive option due to:

• Better defensive balance
• Better possession security
• Better discipline
• More aerial dominance

Final Readiness Index:

🥇 Derrick Köhn — 93.4

🥈 Baba Rahman — 86.3

Conclusion:
Köhn profiles as the more attack-oriented modern full-back,
while Baba offers greater defensive stability and reliability.
""")

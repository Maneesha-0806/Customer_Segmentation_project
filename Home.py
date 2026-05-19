import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0F1117;
}

/* Main spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #1A1D24, #111318);
    border: 1px solid #2A2D35;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #A0A0A0;
    font-size: 18px;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: white;
    font-size: 40px;
    font-weight: bold;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "outputs/clustered_customers.csv"
    )

filtered_df = load_data()
# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("📊 Analytics Hub")

st.sidebar.markdown("""
### Customer Intelligence Platform

Analyze:
- Customer Segmentation
- RFM Analytics
- Customer Personas
- Revenue Trends
- CLV
- Business Insights
""")
# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("🔍 Filter Dashboard")

# --------------------------------
# PERSONA FILTER
# --------------------------------

selected_persona = st.sidebar.multiselect(
    "Select Persona",

    options=filtered_df['Persona'].unique(),

    default=filtered_df['Persona'].unique()
)

# --------------------------------
# COUNTRY FILTER
# --------------------------------

selected_country = st.sidebar.multiselect(
    "Select Country",

    options=sorted(
        filtered_df['Country'].unique()
    ),

    default=sorted(
        filtered_df['Country'].unique()
    )
)

# --------------------------------
# REVENUE FILTER
# --------------------------------

min_revenue = int(
    filtered_df['Monetary'].min()
)

max_revenue = int(
    filtered_df['Monetary'].max()
)

selected_revenue = st.sidebar.slider(
    "Revenue Range",

    min_value=min_revenue,

    max_value=max_revenue,

    value=(
        min_revenue,
        max_revenue
    )
)
# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------

filtered_df = filtered_df[

    (filtered_df['Persona'].isin(selected_persona))

    &

    (filtered_df['Country'].isin(selected_country))

    &

    (
        filtered_df['Monetary']
        .between(
            selected_revenue[0],
            selected_revenue[1]
        )
    )

]
st.sidebar.markdown("### 📌 Active Filters")

st.sidebar.write(
    f"Customers Selected: {len(filtered_df)}"
)
if st.sidebar.button("Reset Filters"):

    st.rerun()
# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("📊 Customer Analytics Dashboard")

st.markdown("""
Analyze customer behavior, purchasing patterns,
and business performance using Machine Learning
and RFM Analysis.
""")

st.divider()

# ---------------------------------------------------
# KPI VALUES
# ---------------------------------------------------

total_customers = len(filtered_df)

total_revenue = round(
    filtered_df['Monetary'].sum(), 2
)

avg_frequency = round(
    filtered_df['Frequency'].mean(), 2
)

avg_clv = round(
    filtered_df['CLV'].mean(), 2
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Customers",
        value=f"{total_customers:,}"
    )

with col2:
    st.metric(
        label="Revenue",
        value=f"${total_revenue:,.0f}"
    )

with col3:
    st.metric(
        label="Avg Frequency",
        value=avg_frequency
    )

with col4:
    st.metric(
        label="Avg CLV",
        value=f"${avg_clv:,.0f}"
    )# ---------------------------------------------------
# KEY HIGHLIGHTS + PIE CHART
# ---------------------------------------------------

col5, col6 = st.columns([1,1])

with col5:

    st.markdown("""
    <div class="section-card">

    <h2 style="color:#00ADB5;">
    📈 Key Highlights
    </h2>

    <ul style="
        font-size:18px;
        line-height:2;
    ">

    <li>VIP customers generate highest revenue.</li>

    <li>Frequent buyers have higher CLV.</li>

    <li>Some customer segments indicate churn risk.</li>

    <li>Customer personas improve marketing targeting.</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)

with col6:

    persona_counts = (
        filtered_df['Persona']
        .value_counts()
    )

    fig = px.pie(
        values=persona_counts.values,
        names=persona_counts.index,
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F1117",
        plot_bgcolor="#0F1117",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# RFM DISTRIBUTIONS
# ---------------------------------------------------

st.subheader("📈 RFM Analysis")

col7, col8, col9 = st.columns(3)

with col7:

    fig1 = px.histogram(
        filtered_df,
        x='Recency',
        template='plotly_dark',
        title='Recency Distribution'
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col8:

    fig2 = px.histogram(
        filtered_df,
        x='Frequency',
        template='plotly_dark',
        title='Frequency Distribution'
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with col9:

    fig3 = px.histogram(
        filtered_df,
        x='Monetary',
        template='plotly_dark',
        title='Monetary Distribution'
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# CUSTOMER SEGMENTATION
# ---------------------------------------------------

st.subheader("👥 Customer Segmentation")

fig4 = px.scatter(
    filtered_df,
    x='Frequency',
    y='Monetary',
    color='Persona',
    size='Recency',
    hover_data=['CLV'],
    template='plotly_dark'
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ---------------------------------------------------
# 3D VISUALIZATION
# ---------------------------------------------------

st.subheader("🌍 3D Customer Segmentation")

fig5 = px.scatter_3d(
    filtered_df,
    x='Recency',
    y='Frequency',
    z='Monetary',
    color='Persona',
    template='plotly_dark'
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# ELBOW METHOD
# ---------------------------------------------------

st.subheader("📉 Elbow Method")

features = filtered_df[
    ['Recency','Frequency','Monetary']
]

scaler = StandardScaler()

scaled = scaler.fit_transform(
    features
)

wcss = []

for i in range(1,11):

    km = KMeans(
        n_clusters=i,
        random_state=42
    )

    km.fit(scaled)

    wcss.append(km.inertia_)

fig6 = px.line(
    x=range(1,11),
    y=wcss,
    markers=True,
    template='plotly_dark'
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.success("""
Optimal clustering appears around K=4.
""")

st.divider()

# ---------------------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------------------

st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10,5))

sns.heatmap(
    filtered_df[
        ['Recency','Frequency','Monetary','CLV']
    ].corr(),
    annot=True,
    cmap='viridis',
    ax=ax
)

st.pyplot(fig)

st.divider()

# ---------------------------------------------------
# TOP CUSTOMERS
# ---------------------------------------------------

st.subheader("🏆 Top Customers")

top_customers = filtered_df.sort_values(
    by='Monetary',
    ascending=False
).head(10)

st.dataframe(
    top_customers,
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.subheader("💡 Business Insights")

best_cluster = (
    filtered_df.groupby('Cluster')['Monetary']
    .mean()
    .idxmax()
)

st.success(f"""
Cluster {best_cluster}
generates the highest revenue.
""")

churn_risk = filtered_df[
    filtered_df['Recency']
    > filtered_df['Recency'].mean()
]

st.warning(f"""
{len(churn_risk)} customers
are at risk of churn.
""")

vip_revenue = filtered_df[
    filtered_df['Persona']
    == 'VIP Customers'
]['Monetary'].sum()

st.info(f"""
VIP customers contribute
${vip_revenue:,.0f}
in revenue.
""")

st.markdown("""
### Recommendations

- Focus on retaining VIP customers.
- Re-engage inactive customers using discounts.
- Improve loyalty programs for frequent buyers.
- Personalize campaigns based on personas.
""")

st.divider()

# ---------------------------------------------------
# DOWNLOAD REPORT
# ---------------------------------------------------

st.subheader("⬇ Download Report")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Customer Segments",
    data=csv,
    file_name='customer_segments.csv',
    mime='text/csv'
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    color:#888888;
    padding:20px;
">
Customer Analytics Dashboard • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
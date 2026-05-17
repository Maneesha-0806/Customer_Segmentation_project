import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# --------------------------------
# LOAD DATA
# --------------------------------

df = pd.read_excel(
    "data/online_retail.xlsx"
)

# --------------------------------
# CLEAN DATA
# --------------------------------

df.dropna(inplace=True)

df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]

# --------------------------------
# TOTAL PRICE
# --------------------------------

df['TotalPrice'] = (
    df['Quantity'] * df['UnitPrice']
)

# --------------------------------
# DATE CONVERSION
# --------------------------------

df['InvoiceDate'] = pd.to_datetime(
    df['InvoiceDate']
)

# --------------------------------
# CREATE RFM FEATURES
# --------------------------------

snapshot_date = (
    df['InvoiceDate'].max()
    + pd.Timedelta(days=1)
)

rfm = df.groupby('CustomerID').agg({

    'InvoiceDate': lambda x:
        (snapshot_date - x.max()).days,

    'InvoiceNo': 'nunique',

    'TotalPrice': 'sum',

    'Country': 'first'

})

rfm.columns = [
    'Recency',
    'Frequency',
    'Monetary',
    'Country'
]

# --------------------------------
# CUSTOMER LIFETIME VALUE
# --------------------------------

rfm['CLV'] = (
    rfm['Frequency'] *
    rfm['Monetary']
)

# --------------------------------
# SCALE FEATURES
# --------------------------------

features = [
    'Recency',
    'Frequency',
    'Monetary'
]

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(
    rfm[features]
)

# --------------------------------
# K-MEANS CLUSTERING
# --------------------------------

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

rfm['Cluster'] = (
    kmeans.fit_predict(rfm_scaled)
)

# --------------------------------
# PERSONA LABELS
# --------------------------------

persona_map = {

    0: "VIP Customers",

    1: "Loyal Customers",

    2: "At Risk Customers",

    3: "New Customers"
}

rfm['Persona'] = (
    rfm['Cluster']
    .map(persona_map)
)

# --------------------------------
# SILHOUETTE SCORE
# --------------------------------

score = silhouette_score(
    rfm_scaled,
    rfm['Cluster']
)

print(f"Silhouette Score: {score}")

# --------------------------------
# SAVE OUTPUT
# --------------------------------

rfm.to_csv(
    "outputs/clustered_customers.csv"
)

print("RFM Analysis Complete!")
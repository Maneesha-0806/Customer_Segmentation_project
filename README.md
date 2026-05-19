# Customer Analytics Dashboard using Machine Learning

An interactive Customer Analytics Dashboard built using Python, Streamlit, and Machine Learning to analyze customer behavior, perform segmentation, generate business insights, and visualize customer trends.

---

# Live Demo

🌐 Live App:  
[:contentReference[oaicite:0]{index=0}](https://customersegmentationproject-aprfymr8vv7almjgfbeqsq.streamlit.app/)

---

# Project Overview

This project focuses on customer segmentation and analytics using RFM Analysis and K-Means Clustering. The dashboard provides interactive visualizations, AI-powered insights, churn analysis, Customer Lifetime Value (CLV) analysis, and dynamic filtering capabilities.

The system helps businesses:
- Understand customer purchasing behavior
- Identify high-value customers
- Detect churn risk
- Optimize marketing strategies
- Improve customer retention

---

# Features

## Customer Analytics
- RFM Analysis (Recency, Frequency, Monetary)
- Customer Lifetime Value (CLV)
- Customer Segmentation
- Churn Risk Identification

## AI-Powered Insights
- Automated business recommendations
- AI-generated customer insights
- Revenue optimization suggestions
- Marketing strategy recommendations

## Interactive Dashboard
- KPI cards
- Interactive Plotly charts
- 3D segmentation visualization
- Correlation heatmap
- Dynamic filtering
- Downloadable reports

## UI Features
- Dark theme dashboard
- Responsive layout
- Interactive sidebar filters
- Professional analytics interface

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Dashboard development |
| Pandas | Data analysis |
| NumPy | Numerical computations |
| Scikit-learn | Machine Learning |
| Plotly | Interactive visualizations |
| Matplotlib | Plotting |
| Seaborn | Statistical visualization |
| Groq API | AI-powered insights |
| GitHub | Version control |
| Streamlit Cloud | Deployment |

---

# Project Structure

```bash
Customer_Segmentation_project/
│
├── .streamlit/
│   ├── config.toml
│
├── data/
│   ├── Online_Retail.xlsx
│
├── outputs/
│   ├── clustered_customers.csv
│
├── Home.py
├── rfm_analysis.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

# Dataset

Dataset Used:
- Online Retail Dataset from Kaggle

Dataset contains:
- Customer IDs
- Invoice details
- Product information
- Purchase quantity
- Revenue information
- Customer country

Additional engineered features:
- Recency
- Frequency
- Monetary Value
- CLV
- Customer Persona
- Cluster Labels

---

# Machine Learning Workflow

## Data Preprocessing
- Missing value handling
- Invalid transaction removal
- Feature engineering
- Revenue calculation

## RFM Analysis
- Recency calculation
- Frequency calculation
- Monetary analysis

## Customer Segmentation
- Data scaling
- K-Means clustering
- Persona assignment

## AI Insights
- Business recommendations
- Churn analysis
- Marketing insights

---

# Dashboard Features

## KPI Metrics
- Total Customers
- Total Revenue
- Average Frequency
- Average CLV

## Interactive Visualizations
- Persona Distribution
- Revenue Analysis
- Customer Segmentation
- 3D Cluster Visualization
- Correlation Heatmap
- Elbow Method Analysis

## Dynamic Filters
- Persona Filter
- Country Filter
- Revenue Filter

---

# AI Insights Module

The dashboard integrates Groq API to generate intelligent business recommendations based on customer analytics data.

Example insights:
- Customer retention strategies
- Revenue optimization ideas
- Churn mitigation recommendations
- Personalized marketing suggestions

---

# 📦 Requirements

```text
streamlit
pandas
numpy
plotly
matplotlib
seaborn
scikit-learn
openpyxl
groq
```

---

# Key Business Insights

- VIP customers contribute the highest revenue
- Loyal customers show high purchase frequency
- At-risk customers require re-engagement campaigns
- Personalized marketing improves customer retention
- AI-generated insights support business decision-making

---

# Future Enhancements

- Predictive churn modeling
- Recommendation systems
- SQL database integration
- Real-time analytics
- Authentication system
- Mobile-responsive dashboard
- PDF report generation
- Natural language query support

---

# Deployment

The application is deployed using:
- GitHub
- Streamlit Community Cloud

---

# Author

**Maneesha C A**

GitHub:  
[:contentReference[oaicite:1]{index=1}](https://github.com/Maneesha-0806/Customer_Segmentation_project)

---

# License

This project is developed for educational and portfolio purposes.

---

# Acknowledgements

- Kaggle
- Streamlit
- Scikit-learn
- Plotly
- Groq API
- Open-source Python community

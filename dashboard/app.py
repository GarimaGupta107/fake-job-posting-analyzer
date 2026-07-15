import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Fake Job Posting Analyzer",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Fake Job Posting Analyzer")
st.markdown("""
This dashboard analyzes genuine and fraudulent job postings using
**Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Streamlit**.
""")

df=pd.read_csv("fake_job_postings_cleaned.csv")

# ---------------- Sidebar ----------------
st.sidebar.header("Filters")

industry = st.sidebar.selectbox(
    "Select Industry",
    ["All"] + sorted(df["industry"].dropna().unique().tolist())
)

employment = st.sidebar.selectbox(
    "Employment Type",
    ["All"] + sorted(df["employment_type"].dropna().unique().tolist())
)

education = st.sidebar.selectbox(
    "Required Education",
    ["All"] + sorted(df["required_education"].dropna().unique().tolist())
)

experience = st.sidebar.selectbox(
    "Required Experience",
    ["All"] + sorted(df["required_experience"].dropna().unique().tolist())
)

filtered_df = df.copy()

if industry != "All":
    filtered_df = filtered_df[filtered_df["industry"] == industry]

if employment != "All":
    filtered_df = filtered_df[filtered_df["employment_type"] == employment]

if education != "All":
    filtered_df = filtered_df[
        filtered_df["required_education"] == education
    ]

if experience != "All":
    filtered_df = filtered_df[
        filtered_df["required_experience"] == experience
    ]

st.subheader("Filtered Dataset")

st.dataframe(filtered_df)


# ---------------- KPI Calculations ----------------

total_jobs = len(filtered_df)

genuine_jobs = len(filtered_df[filtered_df["fraudulent"] == 0])

fake_jobs = len(filtered_df[filtered_df["fraudulent"] == 1])

fraud_rate = (fake_jobs / total_jobs * 100) if total_jobs > 0 else 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📄 Total Jobs", total_jobs)

with col2:
    st.metric("✅ Genuine Jobs", genuine_jobs)

with col3:
    st.metric("❌ Fake Jobs", fake_jobs)

with col4:
    st.metric("📈 Fraud Rate", f"{fraud_rate:.2f}%")


st.subheader("📊 Fraud Distribution Analysis")
fraud_count = (
    filtered_df["fraudulent"]
    .value_counts()
    .reset_index()
)

fraud_count.columns = ["Job Type", "Count"]

fraud_count["Job Type"] = fraud_count["Job Type"].replace({
    0: "Genuine",
    1: "Fake"
})

col1, col2 = st.columns(2)
with col1:

    fig = px.pie(
        fraud_count,
        names="Job Type",
        values="Count",
        title="Genuine vs Fake Jobs",
        hole=0.4
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        fraud_count,
        x="Job Type",
        y="Count",
        color="Job Type",
        title="Number of Genuine and Fake Jobs",
        text="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

employment_data = (
    filtered_df
    .groupby(["employment_type", "fraudulent"])
    .size()
    .reset_index(name="Count")
)

employment_data["fraudulent"] = employment_data["fraudulent"].replace({
    0: "Genuine",
    1: "Fake"
})

st.subheader("💼 Employment Type Analysis")

fig = px.bar(
    employment_data,
    x="employment_type",
    y="Count",
    color="fraudulent",
    barmode="group",
    title="Employment Type vs Genuine/Fake Jobs"
)

st.plotly_chart(fig, use_container_width=True)

industry_fraud = (
    filtered_df
    .groupby("industry")["fraudulent"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

industry_fraud.columns = ["Industry", "Fraud Rate (%)"]

st.subheader("🏭 Top 10 Industries by Fraud Rate")

fig = px.bar(
    industry_fraud,
    x="Industry",
    y="Fraud Rate (%)",
    color="Fraud Rate (%)",
    text="Fraud Rate (%)",
    title="Top 10 Industries with Highest Fraud Rate"
)

fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(fig, use_container_width=True)

industry_jobs = (
    filtered_df["industry"]
    .value_counts()
    .head(10)
    .reset_index()
)

industry_jobs.columns = ["Industry", "Jobs"]

fig = px.bar(
    industry_jobs,
    x="Industry",
    y="Jobs",
    color="Jobs",
    text="Jobs",
    title="Top 10 Industries by Number of Jobs"
)

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(fig, use_container_width=True)

location_jobs = (
    filtered_df["location"]
    .value_counts()
    .head(10)
    .reset_index()
)

location_jobs.columns = ["Location", "Jobs"]

st.subheader("📍 Top 10 Job Locations")

fig = px.bar(
    location_jobs,
    x="Location",
    y="Jobs",
    color="Jobs",
    text="Jobs",
    title="Top 10 Locations by Job Count"
)

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(fig, use_container_width=True)

fake_locations = (
    filtered_df[filtered_df["fraudulent"] == 1]["location"]
    .value_counts()
    .head(10)
    .reset_index()
)

fake_locations.columns = ["Location", "Fake Jobs"]


fig = px.bar(
    fake_locations,
    x="Location",
    y="Fake Jobs",
    color="Fake Jobs",
    text="Fake Jobs",
    title="Top 10 Locations with Fake Job Postings"
)

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(fig, use_container_width=True)

logo_data = (
    filtered_df
    .groupby(["has_company_logo", "fraudulent"])
    .size()
    .reset_index(name="Count")
)

logo_data["has_company_logo"] = logo_data["has_company_logo"].replace({
    0: "No Logo",
    1: "Logo Available"
})

logo_data["fraudulent"] = logo_data["fraudulent"].replace({
    0: "Genuine",
    1: "Fake"
})

st.subheader("🏢 Company Logo Analysis")

fig = px.bar(
    logo_data,
    x="has_company_logo",
    y="Count",
    color="fraudulent",
    barmode="group",
    text="Count",
    title="Company Logo vs Fraudulent Jobs"
)

st.plotly_chart(fig, use_container_width=True)

filtered_df["company_profile_missing"] = (
    filtered_df["company_profile"].isnull()
).astype(int)

profile_data = (
    filtered_df
    .groupby(["company_profile_missing", "fraudulent"])
    .size()
    .reset_index(name="Count")
)

profile_data["company_profile_missing"] = profile_data["company_profile_missing"].replace({
    0: "Profile Available",
    1: "Profile Missing"
})

profile_data["fraudulent"] = profile_data["fraudulent"].replace({
    0: "Genuine",
    1: "Fake"
})

st.subheader("📄 Company Profile Analysis")

fig = px.bar(
    profile_data,
    x="company_profile_missing",
    y="Count",
    color="fraudulent",
    barmode="group",
    text="Count",
    title="Company Profile Availability vs Fraud"
)

st.plotly_chart(fig, use_container_width=True)

experience_data = (
    filtered_df
    .groupby(["required_experience", "fraudulent"])
    .size()
    .reset_index(name="Count")
)

experience_data["fraudulent"] = experience_data["fraudulent"].replace({
    0: "Genuine",
    1: "Fake"
})

st.subheader("💼 Experience Requirement Analysis")

fig = px.bar(
    experience_data,
    x="required_experience",
    y="Count",
    color="fraudulent",
    barmode="group",
    text="Count",
    title="Experience Requirement vs Fraud"
)

fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)


education_data = (
    filtered_df
    .groupby(["required_education", "fraudulent"])
    .size()
    .reset_index(name="Count")
)

education_data["fraudulent"] = education_data["fraudulent"].replace({
    0: "Genuine",
    1: "Fake"
})

st.subheader("🎓 Education Requirement Analysis")

fig = px.bar(
    education_data,
    x="required_education",
    y="Count",
    color="fraudulent",
    barmode="group",
    text="Count",
    title="Education Requirement vs Fraud"
)

fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)

salary_df = filtered_df[filtered_df["salary_range"].notna()].copy()

salary_df[["min_salary", "max_salary"]] = (
    salary_df["salary_range"]
    .str.split("-", expand=True)
)

salary_df["min_salary"] = pd.to_numeric(
    salary_df["min_salary"],
    errors="coerce"
)

salary_df["max_salary"] = pd.to_numeric(
    salary_df["max_salary"],
    errors="coerce"
)

salary_df["avg_salary"] = (
    salary_df["min_salary"] +
    salary_df["max_salary"]
) / 2

st.subheader("💰 Salary Distribution")

fig = px.histogram(
    salary_df,
    x="avg_salary",
    nbins=30,
    title="Average Salary Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.box(
    salary_df,
    x="fraudulent",
    y="avg_salary",
    color="fraudulent",
    title="Average Salary vs Fraud"
)

fig.update_xaxes(
    tickvals=[0,1],
    ticktext=["Genuine","Fake"]
)

st.plotly_chart(fig, use_container_width=True)

remote_data = (
    filtered_df
    .groupby(["telecommuting","fraudulent"])
    .size()
    .reset_index(name="Count")
)

remote_data["telecommuting"] = remote_data["telecommuting"].replace({
    0:"Non Remote",
    1:"Remote"
})

remote_data["fraudulent"] = remote_data["fraudulent"].replace({
    0:"Genuine",
    1:"Fake"
})

st.subheader("🌐 Remote Job Analysis")

fig = px.bar(
    remote_data,
    x="telecommuting",
    y="Count",
    color="fraudulent",
    barmode="group",
    text="Count",
    title="Remote vs Fraudulent Jobs"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("🔥 Correlation Heatmap")

corr = filtered_df[
    [
        "telecommuting",
        "has_company_logo",
        "has_questions",
        "fraudulent"
    ]
].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Matrix"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📌 Key Insights")

st.markdown("""
- Genuine job postings are much more common than fraudulent postings.
- Jobs without company logos are more likely to be fraudulent.
- Missing company profiles are frequently associated with fake jobs.
- Certain industries have a higher fraud rate than others.
- Remote jobs should be verified carefully before applying.
- Salary analysis is based only on available salary information.
""")

st.subheader("📥 Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_fake_jobs.csv",
    mime="text/csv"
)
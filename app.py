import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Page title
st.title("🎓 Student Success Prediction App")

# Sidebar for user input
st.sidebar.header("Enter Student Details:")

study_commitment = st.sidebar.selectbox("Study Commitment", ("Low", "High"))
famsupport_score = st.sidebar.slider("Family Support Score (0 = Low, 1 = High)", 0, 1, 0)
risk_factor = st.sidebar.slider("Risk Factor (0 = Low Risk, 1 = High Risk)", 0.0, 1.0, 0.5)
social_activity = st.sidebar.slider("Social Activity (0 = Low, 1 = High)", 0, 1, 0)

# Convert user input to DataFrame
user_input = pd.DataFrame({
    "study_commitment": [1 if study_commitment == "High" else 0],
    "famsupport_score": [famsupport_score],
    "risk_factor": [risk_factor],
    "social_activity": [social_activity]
})

# Dummy data for clustering
# (in real app, use your cleaned dataset here)
data = pd.DataFrame({
    "study_commitment": np.random.randint(0, 2, 100),
    "famsupport_score": np.random.randint(0, 2, 100),
    "risk_factor": np.random.rand(100),
    "social_activity": np.random.randint(0, 2, 100)
})

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)

# Predict the cluster for user input
cluster = kmeans.predict(user_input)[0]

# Display the prediction
st.subheader("🎯 Prediction Result:")
if cluster == 0:
    st.success("This student might need moderate support to succeed! ✨")
elif cluster == 1:
    st.warning("This student might be at higher risk. Consider interventions! 🚨")
else:
    st.info("This student is on a good track! Keep encouraging them! 🌟")

# Show user input
st.subheader("📝 Student Details:")
st.write(user_input)
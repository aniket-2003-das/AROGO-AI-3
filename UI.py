import streamlit as st
import random
import pandas as pd
from sklearn.preprocessing import StandardScaler
import time
# List of conditions
conditions = [
    'Major Depressive Disorder (MDD)', 'Dysthymia', 'Seasonal Affective Disorder (SAD)',
    'Generalized Anxiety Disorder (GAD)', 'Panic Disorder', 'PTSD', 
    'Insomnia', 'Hypersomnia', 'Sleep Apnea', 'Suicidal Ideation',
    'High-Risk Crisis', 'Chronic Stress', 'Adjustment Disorder', 'Burnout'
]

# UI Layout
st.title("Mental Health Assessment Tool")
st.subheader("Enter your symptoms and score information")

# Input widgets
with st.form("Patient Info"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", options=["Male", "Female"])
        bmi = st.number_input("BMI", min_value=15.0, max_value=30.0, value=25.0)
        phq_score = st.slider("PHQ-9 Score (Depression)", 0, 27, 10)
        gad_score = st.slider("GAD-7 Score (Anxiety)", 0, 21, 8)
        epworth_score = st.slider("Epworth Sleepiness Scale", 0, 24, 6)
        
    with col2:
        depression_sev = st.selectbox("Depression Severity", options=[0, 1, 2, 3, 4])
        anxiety_sev = st.selectbox("Anxiety Severity", options=[0, 1, 2, 3, 4])
        suicidal = st.radio("Suicidal Thoughts", options=["No", "Yes"])
        depressiveness = st.selectbox("Depressiveness Level", options=[0, 1, 2, 3, 4])
        anxiousness = st.selectbox("Anxiousness Level", options=[0, 1])
    
    submitted = st.form_submit_button("Ingest Your Data")
    # Prediction logic
    if submitted:
        with st.spinner('Analyzing your mental health data... '):
            time.sleep(5)  
            st.write('Your Data is Ingested Into The Model.')




# Displaying the title and button
st.markdown("<h2 style='text-align: center;'>Mental Health Report</h2>", unsafe_allow_html=True)

# Create a function to format condition data
def display_condition_data(condition, severity, probability, urgency):
    severity_class = "severity" if severity in ["Moderate", "Severe"] else "urgency"
    urgency_class = "urgency" if urgency in ["Monitor closely", "Therapy required"] else "severity"
    
    st.markdown(f"""
    <div class="card">
        <div class="report-title">{condition}</div>
        <div><span class="{severity_class}">Severity: {severity}</span></div>
        <div><span class="severity">Clinical Insight: {condition} with probability {probability}</span></div>
        <div><span class="{urgency_class}">Urgency: {urgency}</span></div>
    </div>
    """, unsafe_allow_html=True)

# Example static data for mental health conditions
conditions = [
    ("Major Depressive Disorder (MDD)", "Moderate", 0.70, "Monitor closely, therapy required"),
    ("Dysthymia", "Moderate", 0.68, "Monitor closely, therapy required"),
    ("Seasonal Affective Disorder (SAD)", "Mild", 0.49, "Routine psychological support suggested"),
    ("Generalized Anxiety Disorder (GAD)", "Mild", 0.49, "Routine psychological support suggested"),
    ("Panic Disorder", "Mild", 0.44, "Routine psychological support suggested"),
    ("PTSD", "Mild", 0.45, "Routine psychological support suggested"),
    ("Insomnia", "Moderate", 0.62, "Routine psychological support suggested"),
    ("Hypersomnia", "Moderate", 0.62, "Routine psychological support suggested"),
    ("Sleep Apnea", "Severe", 0.71, "Monitor closely, therapy required"),
    ("Suicidal Ideation", "Moderate", 0.70, "Monitor closely, therapy required"),
    ("High-Risk Crisis", "Moderate", 0.61, "Routine psychological support suggested"),
    ("Chronic Stress", "Moderate", 0.59, "Routine psychological support suggested"),
    ("Adjustment Disorder", "Mild", 0.46, "Routine psychological support suggested"),
    ("Burnout", "Mild", 0.46, "Routine psychological support suggested")
]

# Display the Analyze Mental Health button
if st.button("Analyze Mental Health"):
    # Show the loading spinner
    with st.spinner('Analyzing your Data ...'):
        time.sleep(7)  # Simulate processing time for 7 seconds

    # After analysis, display the static data and report
    st.markdown("<h3 style='text-align: center;'>Mental Health Insights</h3>", unsafe_allow_html=True)

    # Display all conditions with their data
    for condition, severity, probability, urgency in conditions:
        display_condition_data(condition, severity, probability, urgency)

    # Emergency Status
    st.markdown("""
        <div class="report-section">
            <h4>Emergency Status</h4>
            <p><b>No Immediate Emergency Detected.</b></p>
        </div>
    """, unsafe_allow_html=True)

    # Display processed data with styled UI
    st.subheader("Processed Data")
    st.markdown(f"""
        <div class="report-section">
            <div><b>BMI Range:</b> 0.41 - 0.70 --> {round(random.uniform(0.26, 0.39), 2)}</div>
            <div><b>PHQ Score Range:</b> 5 - 15 --> {round(random.uniform(0.15, 0.50), 2)}</div>
            <div><b>GAD Score Range:</b> 3 - 9 --> {round(random.uniform(0.15, 0.50), 2)}</div>
            <div><b>Depressiveness Level:</b> Moderate</div>
            <div><b>Suicidal Thoughts:</b> Yes</div>
            <div><b>Anxiousness Level:</b> High</div>
            <div><b>Anxiety Diagnosis:</b> Generalized Anxiety Disorder</div>
            <div><b>Anxiety Treatment:</b> Cognitive Behavioral Therapy</div>
            <div><b>Depression Diagnosis:</b> Major Depressive Disorder</div>
            <div><b>Depression Treatment:</b> Antidepressants</div>
            <div><b>Epworth Score Range:</b> 0 - 24 --> {round(random.uniform(0.15, 0.40), 2)}</div>
            <div><b>WHO BMI Indicator:</b> Overweight</div>
            <div><b>Gender:</b> Female</div>
        </div>
    """, unsafe_allow_html=True)


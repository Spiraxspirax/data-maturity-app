# app.py

import streamlit as st
from questions import domains
from scoring import score_responses, maturity_level
from dashboard import create_radar

st.set_page_config(page_title="Data Maturity Assessment", layout="wide")
st.title("📊 Data Maturity Assessment Tool")
st.markdown("Evaluate your organization’s data maturity across key capabilities.")

responses = {}
with st.form("assessment_form"):
    for domain, questions in domains.items():
        st.subheader(f"📘 {domain}")
        domain_responses = []
        for q in questions:
            rating = st.slider(q, 1, 5, step=1)
            domain_responses.append(rating)
        responses[domain] = domain_responses
    submitted = st.form_submit_button("Submit Assessment")

if submitted:
    scores = score_responses(responses)
    st.success("Assessment submitted! View your results below.")
    st.write("### 📈 Domain Scores")
    for domain, score in scores.items():
        st.write(f"**{domain}**: {score} – *{maturity_level(score)}*")

    st.plotly_chart(create_radar(scores), use_container_width=True)


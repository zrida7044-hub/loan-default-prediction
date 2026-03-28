import streamlit as st
import numpy as np

st.title("Loan Default Prediction App")

st.write("Enter applicant details below:")

income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.selectbox("Credit History (1=Good, 0=Bad)", [0, 1])

if st.button("Predict Loan Status"):
    if credit_history == 1 and income > 5000:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")

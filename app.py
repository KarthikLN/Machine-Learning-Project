import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
model = joblib.load("fraud_model.pkl")    #Trained model
# App Title
st.title("Bank Fraud Detection App")

st.write("Enter transaction details below:")

# User Inputs
step = st.number_input("Step", min_value=0)

type_transaction = st.selectbox(
    "Transaction Type",
    ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
)

amount = st.number_input("Amount", min_value=0.0)

oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0)

oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0)

original_transaction_count = st.number_input(
    "Original Transaction Count",
    min_value=0
)

destination_transaction_count = st.number_input(
    "Destination Transaction Count",
    min_value=0
)

destination_average_amount = st.number_input(
    "Destination Average Amount",
    min_value=0.0
)

destination_total_amount = st.number_input(
    "Destination Total Amount",
    min_value=0.0
)

# Encode transaction type
type_mapping = {
    
    
    "DEBIT":0 ,
     "TRANSFER": 1,
     "CASH_OUT": 2,
     "CASH_IN": 3,
     "PAYMENT": 4
   
}

type_encoded = type_mapping[type_transaction]

# Create DataFrame
new_data = pd.DataFrame({
    'step': [step],
    'type': [type_encoded],
    'amount': [amount],
    'oldbalanceOrg': [oldbalanceOrg],
    'newbalanceOrig': [newbalanceOrig],
    'oldbalanceDest': [oldbalanceDest],
    'newbalanceDest': [newbalanceDest],
    'original_transaction_count': [original_transaction_count],
    'destination_transaction_count': [destination_transaction_count],
    'destination_average_amount': [destination_average_amount],
    'destination_total_amount': [destination_total_amount]
})

# Prediction
if st.button("Predict Fraud"):

    prediction = model.predict(new_data)[0]

    if prediction == 1:
        st.error("Fraudulent Transaction Detected")
    else:
        st.success("Legitimate Transaction")




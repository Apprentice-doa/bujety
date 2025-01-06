# Import Libraries
import datetime
import pandas as pd
import streamlit as st
from data_processing import data_input


expense_options = ['Food', 'Giving', 'Transportation', 'Airtime', 'Data', 'Self-care', 'Treats']

# Title
st.title('Expense Tracker')
# Fuction to input the data through streamlit text_area feature
def row_input():
    expense = st.selectbox('Enter the name of the expense:', expense_options)
    amount = st.text_area('Enter the amount of the expense:', key='amount_input')
    date = st.date_input('Enter the date of the expense:',datetime.date.today())

    # st.write(f"Expense: {expense}, Amount: {amount}, Date: {date}")
    return expense, amount, date


# Instantiate the row_input function
inputs = row_input()
if st.button('Submit Expense'):
    if inputs[0] and inputs[1] and inputs[2]:  # Ensure all inputs are filled
        final_output = data_input(inputs[0], inputs[1], inputs[2])
        final_output_expense = final_output.add_expense()
        updated_sheet = pd.read_csv('data.csv')
        st.write("Expense added successfully!")
        st.write(updated_sheet)
    else:
        st.warning("Please fill out all fields before submitting.")

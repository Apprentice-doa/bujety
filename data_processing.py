# Import Libraries
import pandas as pd
import streamlit as st
import csv

# Create a csv file to store the data
def create_csv():
    # Create a dictionary of key and values
    data = {'Name of Expenses' : [], 'Amount' : [], 'Date': []
            }
    # Create a dataframe of the dictionary
    df = pd.DataFrame(data)
    # Convert the dataframe to a csv file
    df.to_csv('data.csv', index = False)

sheet = pd.read_csv('data.csv')


class data_input:
    def __init__(self, expense, amount, date):
        self.expense = expense
        self.amount = amount
        self.date = date

    def add_expense(self):
        expense_data = {
            'Name of Expenses': self.expense,
            'Amount': self.amount,
            'Date': self.date
        }
        sheet.loc[len(sheet)] = expense_data

        # Save the updated DataFrame back to the data.csv file
        sheet.to_csv('data.csv', index=False)
        #or
        # with open('data.csv', mode='a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerow([self.expense, self.amount, self.date])




import openai
import pandas as pd
import streamlit as st

# Function to load data and initialize
def load_and_initialize_data():
    # Load the articles from CSV files
    yomiuri_df = pd.read_csv('Articles_yomiuri.csv', encoding='utf-8-sig')
    jungang_df = pd.read_csv('Articles_jungang.csv', encoding='utf-8-sig')

    # Combine both DataFrames
    combined_df = pd.concat([yomiuri_df, jungang_df], ignore_index=True)

    return combined_df
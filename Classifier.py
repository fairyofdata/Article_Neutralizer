import openai
import pandas as pd
import streamlit as st

# Function to classify titles using OpenAI API (updated for ChatCompletion)
def classify_titles_with_general_labels(titles):
    # Combine all titles into a single prompt to avoid splitting into chunks
    message_content = "The following are news article titles related to Japan-Korea relations. Please classify each title into an appropriate general topic, such as Economy, Politics, Culture, Sports, Diplomacy, or Other. The goal is to classify articles into broad categories that best reflect the overall theme or context of each article, ensuring that each category has at least one Korean and one Japanese article where possible. If a category cannot have both, reassign those articles to 'Other'. Be flexible and comprehensive in classification; for example, North Korea's nuclear threat and Japan-Korea military cooperation can both be classified as Security & Diplomacy:\n"
    for idx, title in enumerate(titles):
        message_content += f"{idx + 1}. {title}\n"
    message_content += (
        "\nProvide a classification label (e.g., Security & Diplomacy, Culture & History, Social & Economy, Other) for each title in the format:\n"
        "1. [Label]\n"
        "2. [Label]\n"
        "..."
    )

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest model
        messages=[
            {"role": "system", "content": "You are an expert in analyzing Japan-Korea relations and providing general classifications for topics."},
            {"role": "user", "content": message_content}
        ],
        max_tokens=3000,  # Allow more tokens for larger responses
        temperature=0.3  # Lower temperature for more consistent responses
    )

    # Extract the classifications from the response
    classifications = response["choices"][0]["message"]["content"].strip()
    classification_lines = classifications.split("\n")
    labels = []
    for line in classification_lines:
        parts = line.split(". ")
        if len(parts) == 2:
            labels.append(parts[1])
        else:
            labels.append("Unknown")
    return labels
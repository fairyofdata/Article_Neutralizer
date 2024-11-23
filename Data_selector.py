import openai
import pandas as pd
import streamlit as st

# Function to select the most relevant Korean-Japanese article pair using OpenAI API
def select_korean_japanese_pair(titles):
    # Combine selected titles into a prompt for finding the most relevant pair
    message_content = "The following are news article titles that have been classified under the general topic. Please select one Korean article and one Japanese article that discuss the same specific event or individual. The goal is to identify the most relevant pair that deals with the same subject in detail.\n\n"
    for idx, title in enumerate(titles):
        message_content += f"{idx + 1}. {title}\n"
    message_content += (
        "\nSelect one Korean article and one Japanese article that discuss the same specific topic. Provide the result strictly in the format:\n"
        "Korean: [Index]\nJapanese: [Index]\n"
        "Ensure that you only use this format without adding any extra information."
    )

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest model
        messages=[
            {"role": "system", "content": "You are an expert in analyzing Japan-Korea relations and identifying the most relevant articles on similar topics."},
            {"role": "user", "content": message_content}
        ],
        max_tokens=2000,  # Allow more tokens for detailed responses
        temperature=0.3  # Lower temperature for more consistent responses
    )

    # Extract the selected pair from the response
    selection = response["choices"][0]["message"]["content"].strip()
    st.write("Response from OpenAI:", selection)  # Log the response for debugging purposes
    korean_idx = japanese_idx = None
    try:
        # Split the response by lines and search for Korean and Japanese indices
        lines = selection.split("\n")
        for line in lines:
            if "Korean:" in line:
                korean_idx = int(line.split(":")[1].strip()) - 1
            elif "Japanese:" in line:
                japanese_idx = int(line.split(":")[1].strip()) - 1
    except (ValueError, IndexError) as e:
        st.error(f"Error parsing the selected indices: {e}")
        st.write("Response from OpenAI:", selection)
        return None, None

    # Return the indices if they were successfully parsed
    if korean_idx is None or japanese_idx is None:
        st.error("Failed to select a Korean-Japanese article pair. Please try selecting a different label.")
        return None, None

    return korean_idx, japanese_idx

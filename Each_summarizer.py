import openai
import pandas as pd
import streamlit as st

# Function to summarize an article using OpenAI API
def summarize_article(article_content, language):
    # Limit the content length to avoid token limit issues
    truncated_content = article_content[:2000]  # Limit the article to 2000 characters to manage token limits

    # Create prompt for summarization
    message_content = (
        f"The following is a news article in {language}. Please provide a summary that captures the key points in 6-7 sentences in English.\n\n"
        f"Article:\n{truncated_content}\n\n"
        "Summary:"
    )

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert news editor who summarizes articles effectively."},
            {"role": "user", "content": message_content}
        ],
        max_tokens=300,  # Reduce max_tokens to avoid overflow
        temperature=0.5
    )

    # Extract the summary from the response
    summary = response["choices"][0]["message"]["content"].strip()
    return summary
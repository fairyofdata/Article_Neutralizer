import openai
import pandas as pd
import streamlit as st

# Function to generate a neutral article from selected Korean and Japanese articles using OpenAI API
def generate_neutral_article(korean_summary, japanese_summary):
    # Combine the summaries into a prompt for generating a neutral article
    message_content = (
        "The following are summaries of two news articles, one in Korean and one in Japanese, both discussing the same relevant event or topic. "
        "Please generate a neutral news article that details the key points from both summaries while providing a balanced perspective. "
        "Ensure that all key points from both the Korean and Japanese summaries are included. Highlight similarities and differences explicitly where relevant. "
        "Also, include comparisons between the reporting styles of the two articles, such as 'Jung-ang Daily (Korean) reported (key point of Jung-ang Daily's article), while Yomiuri Shimbun (Japanese) reported (key point of Yomiuri Shimbun's article)'.\n\n"
        "Korean Summary:\n"
        f"{korean_summary}\n\n"
        "Japanese Summary:\n"
        f"{japanese_summary}\n\n"
        "Please provide the result in two versions: one in Korean and one in Japanese."
    )

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest model
        messages=[
            {"role": "system", "content": "You are an expert journalist skilled in creating balanced and neutral news articles from multiple sources."},
            {"role": "user", "content": message_content}
        ],
        max_tokens=1500,  # Reduce max_tokens to fit both versions without exceeding token limits
        temperature=0.5
    )

    # Extract the generated neutral articles from the response
    generated_articles = response["choices"][0]["message"]["content"].strip()
    return generated_articles

import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os
from Both_loader import load_and_initialize_data
from Classifier import classify_titles_with_general_labels
from Data_selector import select_korean_japanese_pair
from Each_summarizer import summarize_article
from Final_Neutralizer import generate_neutral_article

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Main workflow for Streamlit app
def main():
    st.title("Korean-Japanese Article Analysis and Neutral Article Generation")

    # Load and initialize data
    if "combined_df" not in st.session_state:
        st.session_state.combined_df = load_and_initialize_data()

    combined_df = st.session_state.combined_df

    # Display available articles
    if st.checkbox("Show loaded articles"):
        st.dataframe(combined_df[['title', 'content']])

    # Extract titles for classification
    titles = combined_df['title'].tolist()

    # Classify titles into categories
    if st.button("Classify Article Titles"):
        average_token_per_title = 43
        estimated_tokens = len(titles) * average_token_per_title + 500  # Adding extra tokens for prompt and response
        if estimated_tokens <= 4096:
            labels = classify_titles_with_general_labels(titles)
            st.session_state.combined_df['label'] = labels
            st.session_state.combined_df.to_csv('combined_articles_with_labels.csv', index=False, encoding='utf-8-sig')
            st.success("Data with labels saved to 'combined_articles_with_labels.csv'")
            st.dataframe(st.session_state.combined_df[['title', 'label']])
        else:
            st.error(f"Estimated tokens ({estimated_tokens}) exceed the 4096 token limit for OpenAI API.")

    # Ensure 'label' column exists before proceeding
    if 'label' not in st.session_state.combined_df.columns:
        st.warning("Please classify the article titles first before proceeding.")
        return

    # Select a category to refine further
    unique_labels = st.session_state.combined_df['label'].unique()
    selected_label = st.selectbox("Please select a label to refine further:", unique_labels)

    # Filter articles based on the selected label
    filtered_df = st.session_state.combined_df[st.session_state.combined_df['label'] == selected_label]
    filtered_titles = filtered_df['title'].tolist()

    # Select the most relevant Korean-Japanese article pair
    if st.button("Select Korean-Japanese Article Pair"):
        korean_idx, japanese_idx = select_korean_japanese_pair(filtered_titles)
        if korean_idx is not None and japanese_idx is not None:
            selected_articles = filtered_df.iloc[[korean_idx, japanese_idx]]
            korean_article_content = selected_articles.iloc[0]['content']
            japanese_article_content = selected_articles.iloc[1]['content']
            st.write("Selected Korean and Japanese articles for neutral article generation:")
            st.dataframe(selected_articles[['title', 'content']])

            # Summarize both articles
            korean_summary = summarize_article(korean_article_content, "Korean")
            japanese_summary = summarize_article(japanese_article_content, "Japanese")

            st.write("\nSummarized Korean Article:")
            st.write(korean_summary)
            st.write("\nSummarized Japanese Article:")
            st.write(japanese_summary)

            # Generate a neutral article from the summaries
            neutral_article = generate_neutral_article(korean_summary, japanese_summary)
            st.write("\nGenerated Neutral Articles (Korean and Japanese Versions):")
            st.write(neutral_article)

            # Verification to check if key points from both summaries are included
            if korean_summary.split()[0] in neutral_article and japanese_summary.split()[0] in neutral_article:
                st.success("Key points from both summaries are included in the neutral article.")
            else:
                st.warning("It seems that key points from one of the summaries may be missing in the generated article.")

            filtered_df.to_csv('filtered_articles_with_detailed_labels.csv', index=False, encoding='utf-8-sig')
            st.success("Data with refined labels saved to 'filtered_articles_with_detailed_labels.csv'")
        else:
            st.error("Article pair selection failed. Please retry with a different category.")

if __name__ == "__main__":
    main()

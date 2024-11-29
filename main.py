import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os
from Article_Jungang import scrape_jungang_articles
from Article_Yomiuri import scrape_yomiuri_articles
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
    st.title("🌏 **Korean-Japanese Article Analysis and Neutral Article Generation** 🌏")
    st.markdown(
        """
        **Welcome!**  
        This app allows you to:  
        1️⃣ Scrape articles from **Jungang** and **Yomiuri**  
        2️⃣ Classify and analyze article titles  
        3️⃣ Generate **neutral summaries** for better understanding of both perspectives.
        """
    )

    st.divider()  # Visually separate sections

    # Section 1: Article Scraping
    st.header("📥 **Step 1: Article Scraping**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📰 Scrape **Yomiuri** Articles"):
            scrape_yomiuri_articles()
            st.success("Yomiuri articles scraped successfully!")
    with col2:
        if st.button("📰 Scrape **Jungang** Articles"):
            scrape_jungang_articles()
            st.success("Jungang articles scraped successfully!")

    st.divider()

    # Section 2: Data Loading and Display
    st.header("📂 **Step 2: Load and View Articles**")
    if "combined_df" not in st.session_state:
        st.session_state.combined_df = load_and_initialize_data()

    combined_df = st.session_state.combined_df

    if st.checkbox("👀 Show Loaded Articles"):
        st.markdown("### **Loaded Articles**")
        st.dataframe(combined_df[['title', 'content']])

    st.divider()

    # Section 3: Title Classification
    st.header("🏷️ **Step 3: Classify Article Titles**")
    titles = combined_df['title'].tolist()

    if st.button("🧩 Classify Titles"):
        average_token_per_title = 43
        estimated_tokens = len(titles) * average_token_per_title + 500
        if estimated_tokens <= 4096:
            labels = classify_titles_with_general_labels(titles)
            st.session_state.combined_df['label'] = labels
            st.session_state.combined_df.to_csv('combined_articles_with_labels.csv', index=False, encoding='utf-8-sig')
            st.success("🎉 Classification complete! Data saved to 'combined_articles_with_labels.csv'.")
            st.dataframe(st.session_state.combined_df[['title', 'label']])
        else:
            st.error(f"🚨 Token limit exceeded! Estimated tokens: {estimated_tokens} > 4096.")

    st.divider()

    # Section 4: Label Selection and Pair Refinement
    st.header("🔍 **Step 4: Refine Articles by Labels**")
    if 'label' not in st.session_state.combined_df.columns:
        st.warning("⚠️ Please classify article titles first!")
        return

    unique_labels = st.session_state.combined_df['label'].unique()
    selected_label = st.selectbox("🗂️ Select a label to refine:", unique_labels)

    filtered_df = st.session_state.combined_df[st.session_state.combined_df['label'] == selected_label]
    filtered_titles = filtered_df['title'].tolist()

    if st.button("🔗 Select Korean-Japanese Article Pair"):
        korean_idx, japanese_idx = select_korean_japanese_pair(filtered_titles)
        if korean_idx is not None and japanese_idx is not None:
            selected_articles = filtered_df.iloc[[korean_idx, japanese_idx]]
            korean_article_content = selected_articles.iloc[0]['content']
            japanese_article_content = selected_articles.iloc[1]['content']
            st.markdown("### **Selected Articles**")
            st.dataframe(selected_articles[['title', 'content']])

            # Summarize articles
            st.markdown("### 📝 **Summarized Articles**")
            korean_summary = summarize_article(korean_article_content, "Korean")
            japanese_summary = summarize_article(japanese_article_content, "Japanese")

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("🇰🇷 Korean Summary")
                st.write(korean_summary)
            with col2:
                st.subheader("🇯🇵 Japanese Summary")
                st.write(japanese_summary)

            # Generate neutral article
            st.markdown("### 🌐 **Generated Neutral Article**")
            neutral_article = generate_neutral_article(korean_summary, japanese_summary)
            st.write(neutral_article)

            # Key Point Verification
            if korean_summary.split()[0] in neutral_article and japanese_summary.split()[0] in neutral_article:
                st.success("✅ Key points from both summaries are included.")
            else:
                st.warning("⚠️ Some key points might be missing from the neutral article.")

            filtered_df.to_csv('filtered_articles_with_detailed_labels.csv', index=False, encoding='utf-8-sig')
            st.success("📄 Refined data saved to 'filtered_articles_with_detailed_labels.csv'.")
        else:
            st.error("❌ Article pair selection failed. Try another label.")

if __name__ == "__main__":
    main()

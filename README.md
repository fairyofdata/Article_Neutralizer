**🌐 Available README Versions:**  
[🇰🇷 한국어 (Korean)](https://github.com/fairyofdata/LLM_NAKOJA/blob/master/README_KR.md) | [🇯🇵 日本語 (Japanese)](https://github.com/fairyofdata/LLM_NAKOJA/blob/master/README_JP.md)  

# LLM-Based Korea-Japan Relations Neutral Article Generator 📰🤝🤖

> **[경요세계(瓊瑤世界)](https://www.seoul.co.kr/news/editOpinion/world-stories/2024/07/12/20240712035005): 'Two Jade Orbs Reflecting Each Other'**  
‐ Inscription on the two-story bell tower left by astronomer [Park An-Gi](https://encykorea.aks.ac.kr/Article/E0020900) in Shizuoka’s Seikenji Temple, 1643  
> **[성신교린(誠信交隣)](https://www.donga.com/news/People/article/all/20210416/106434451/1): 'Exchange with Sincerity and Trust'**  
‐ Written by [Amenomori Hōshū](https://busan.grandculture.net/Contents?local=busan&dataType=01&contents_id=GC04203537) in the book「Kyoryo Seisei」 at Busan Choryang Japanese dormitory, 1728  

---

## **Project Objective**

This project aims to provide a neutral perspective on Korea-Japan relations by crawling and analyzing news articles from both countries. Users can intuitively experience all steps—crawling, classification, summarization, and neutral article generation—via a Streamlit-based interface.  

---

## 📖 **Project Overview**

- Crawl news articles with specific keywords which means Korea-Japan relations ("한일" in Korean, "日韓" in Japanese) from **[Joongang Ilbo](https://www.joongang.co.kr/)** and **[Yomiuri Shimbun](https://www.yomiuri.co.jp/)**.
- Expand coverage to include **Joongang, Kyunghyang, Asahi, and Yomiuri**, incorporating political biases from both sides to ensure comprehensive neutrality.
- Cluster crawled articles by topic and generate neutral articles reflecting multifaceted perspectives using OpenAI API.  
- The service is built on Streamlit, allowing users to experience each step directly.  
- **[Preview](https://github.com/fairyofdata/Article_Neutralizer/blob/master/NAKOJA_Preview.png)** the entire process if executing it yourself is cumbersome.  

---

## **Key Features**

- **Article Crawling**: Gather article lists and full content from Korean and Japanese media based on specific keywords.  
- **Data Classification**: Cluster articles by topics for categorization.  
- **Summarization**: Summarize the core content of selected articles.  
- **Neutral Article Generation**: Generate articles with neutral perspectives based on the summaries.  

---

## 🛠️ **Tech Stack**

- **Crawling**: Selenium, BeautifulSoup, Pandas  
- **Text Processing & Clustering**: OpenAI API, HuggingFace  
- **Neutral Article Generation**: OpenAI API (GPT model)  
- **Interface**: Streamlit  
- **Language**: Python 3.8+  

---

## 🚀 **Installation & Execution**

1. **Clone the Project**
   ```bash
   git clone https://github.com/fairyofdata/LLM_NAKOJA
   cd LLM_NAKOJA
   ```

2. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**
   ```bash
   streamlit run main.py
   ```

   Access the app locally at http://localhost:8501 to explore the features.  

---

## 🖥️ **Feature Usage Guide**  
⚠️ *Note: Prompt optimization is in progress.*  

### 1. **Start Crawling**  
   - Click **"Collect Joongang Articles"** or **"Collect Yomiuri Articles"** to gather news articles.  
   - Articles matching keywords which means Korea-Japan relations ("한일" in Korean, "日韓" in Japanese) are collected.  
   - The article count updates in real-time during the process.  
   - Once crawling completes, the article list is displayed.  

### 2. **Classify Data**  
   - Click the **"Classify Headlines"** button to group articles by category.  
   - Categorized articles appear in table format for user review.  

### 3. **Select Articles for Analysis**  
   - Choose a category and click **"Select Korea-Japan Article Pair"** to find articles addressing similar topics.  

### 4. **Generate Neutral Article**  
   - Click the **"Generate Neutral Article"** button to create a neutral article based on selected articles.  
   - The generated article reflects diverse perspectives to provide balanced insights into bilateral issues.  

---

## 📂 **Architecture Explanation**

- **Crawling Module**: Collects article lists and links from news websites using Selenium and BeautifulSoup, then retrieves full text by accessing individual links.  
- **Classification Module**: Uses OpenAI API to analyze article titles and categorize them by topic.  
- **Summarization & Neutral Article Generation Module**: Summarizes selected articles and generates neutral articles through the OpenAI API.  
- **User Interface (UI)**: Built with Streamlit, providing buttons and visual results for each feature.  

---

## 📈 **Performance & Quality Testing**

- Tested across various topics to verify classification and neutral article generation.  
- Accuracy and quality improvements will be driven by user feedback.  

---

## 🔍 **Potential Improvements & Future Features**

- **Multilingual Support**: Expand to handle languages beyond Korean and Japanese.  
- **Real-Time Updates**: Automatically fetch and update articles at regular intervals.  
- **Enhanced AI Models**: Improve summarization and understanding accuracy by integrating advanced NLP models.  

---

## 💡 **Significance & Business Applications**

This project aims to reconstruct biased news reports between Korea and Japan into neutral perspectives, fostering mutual understanding. It serves as a practical showcase of data science and NLP techniques applied to real-world text processing and generation challenges.  

**Business Use Cases**:  
- **Insights from Data Analysis**: Companies can analyze public sentiment on bilateral issues to guide strategy.  
- **Efficiency Through Automation**: Automate the labor-intensive process of article collection, classification, and summarization.  
- **Agility in Market Response**: Use real-time data to quickly adapt to shifting public and market trends.  

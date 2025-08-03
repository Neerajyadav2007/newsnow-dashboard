import streamlit as st
import requests
from bs4 import BeautifulSoup

# Page config
st.set_page_config(page_title="🗞️ NewsNow - Live News Headlines", layout="wide")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>🗞️ NewsNow</h1>
    <h4 style='text-align: center; color: gray;'>Your Real-Time News Dashboard</h4>
    <hr>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📌 Select News Category")
news_sources = {
    "India": "https://www.ndtv.com/india",
    "World": "https://www.ndtv.com/world-news",
    "Technology": "https://www.ndtv.com/technology",
    "Sports": "https://www.ndtv.com/sports"
}
category = st.sidebar.radio("Choose", list(news_sources.keys()))
url = news_sources[category]

# Show button
if st.button("🔍 Show Headlines"):
    def fetch_headlines(url):
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")
        headlines = soup.find_all("h2", class_="newsHdng")
        data = []
        for tag in headlines[:8]:
            headline = tag.text.strip()
            link = tag.find("a")["href"]
            data.append((headline, link))
        return data

    # Display after clicking
    st.subheader(f"📰 Top Headlines in {category}")
    cols = st.columns(2)
    headlines = fetch_headlines(url)
    for i, (title, link) in enumerate(headlines):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
                <div style='padding:10px; background-color:#f0f8ff; border-radius:8px; margin-bottom:15px;'>
                    <b>🗞️ {title}</b><br>
                    <a href='{link}' target='_blank'>Read more</a>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <br><hr>
    <p style='text-align:center; color:gray;'>🔧 Built with ❤️ by <b>Neeraj Ramesh Yadav</b></p>
""", unsafe_allow_html=True)
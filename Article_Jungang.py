from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
from urllib.parse import urljoin


def scrape_articles(browser, base_url, savefile='./Articles_jungang.csv'):
    '''
    중앙일보 검색 결과 페이지에서 모든 기사를 순회하며 데이터를 수집하고 CSV 파일로 저장하는 함수

    Parameters:
        browser: Selenium webdriver 인스턴스
        base_url: 검색 결과 첫 페이지의 URL
        savefile: 수집 결과를 저장할 CSV 파일 경로와 파일명
    '''
    all_articles = []
    consecutive_failures = 0
    max_failures = 5
    max_articles = 25  # 최대 수집 기사 수

    # 페이지로 이동
    browser.get(base_url)
    time.sleep(2)  # 페이지가 로드될 시간을 대기

    # BeautifulSoup으로 페이지 파싱
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 페이지에서 기사 목록을 탐색
    articles_elements = soup.select('#container > section > div > section > ul > li > div > h2 > a')

    for idx, article in enumerate(articles_elements):
        if len(all_articles) >= max_articles:
            print(f"Maximum article limit of {max_articles} reached. Stopping the scraping process.")
            break

        try:
            # 사진 기사 여부 확인
            if article.text.strip().startswith('[사진]'):
                print(f"Skipping photo article at index {idx + 1}")
                continue

            # 기사 제목과 링크 추출
            title = article.text.strip()
            article_url = urljoin(base_url, article['href'])

            # 기사 내용 수집을 위해 해당 기사 링크로 이동
            browser.get(article_url)
            time.sleep(2)  # 페이지가 로드될 시간을 대기

            # 페이지를 가장 하단까지 스크롤
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 스크롤 후 대기

            # BeautifulSoup으로 기사 페이지 파싱
            article_soup = BeautifulSoup(browser.page_source, 'html.parser')

            # 기사 제목 수집
            title_content_element = article_soup.select('#container > section > article > header > h1')
            title_content = title_content_element[0].text.strip() if title_content_element else 'No Title Content'

            # 발행일 수집
            date_element = article_soup.select('#container > section > article > header > div.datetime > div > p:nth-child(2)')
            date = date_element[0].text.strip() if date_element else 'No Date'

            # 여러 문단으로 이루어진 기사 내용 수집 (더 일반적인 CSS 선택자 사용)
            content_elements = article_soup.select('div#article_body p')
            if not content_elements:
                content_elements = article_soup.select('div.p-main-contents p')
            content = [element.text.strip() for element in content_elements if element.text.strip()]
            content = "\n".join(content) if content else 'No Content'

            # 수집 시점 추가
            collection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 기사 정보를 하나의 딕셔너리로 저장
            all_articles.append({
                'title': title,
                'url': article_url,
                'date': date,
                'title_content': title_content,
                'content': content,
                'collection_time': collection_time
            })

            # 기사 수집 성공 시 연속 실패 횟수 초기화
            consecutive_failures = 0

            # 상위 페이지로 돌아가기
            browser.back()
            time.sleep(2)

        except Exception as e:
            print(f"Error occurred while processing article at index {idx + 1}: {e}")
            consecutive_failures += 1
            if consecutive_failures >= max_failures:
                print("Maximum consecutive failures reached. Stopping the scraping process.")
                break
            continue

    # 수집 결과를 CSV 파일로 저장
    df = pd.DataFrame(all_articles)
    df.to_csv(savefile, index=False, encoding='utf-8-sig')
    print(f"Data saved to {savefile}")


# 실행 예시
browser = webdriver.Chrome()
base_url = 'https://www.joongang.co.kr/search/news?keyword=%ED%95%9C%EC%9D%BC&startDate=&endDate=&searchin=%ED%95%9C%EC%9D%BC&accurateWord=&stopword=&sourceCode=1%2C3&sfield=all&serviceCode=10%2C11%2C12%2C13%2C15%2C14%2C35%2C18'
# 검색 결과 페이지에서 기사 크롤링 실행
scrape_articles(browser, base_url, savefile='./Articles_jungang.csv')
# 브라우저 종료
browser.quit()

# LLM 기반 한일관계 중립기사 자동생성기📰🤝🤖

> **[경요세계(瓊瑤世界)](https://www.seoul.co.kr/news/editOpinion/world-stories/2024/07/12/20240712035005) : '두 옥구슬이 서로를 비추다'** </br>‐ 1643년 천문학자 [박안기(朴安期)](https://encykorea.aks.ac.kr/Article/E0020900)가 시즈오카현 청견사에 남긴 2층 종루 현판의 문장</br>
> **[성신교린(誠信交隣](https://www.donga.com/news/People/article/all/20210416/106434451/1)[)](https://www.tokyo-np.co.jp/article/324411) : '성실과 진심으로써 교류하다'** </br>‐ 1728년 [아메노모리 호슈(雨森芳洲)](https://busan.grandculture.net/Contents?local=busan&dataType=01&contents_id=GC04203537)가 부산 초량왜관에서 집필한 「교린제성」의 문장

**프로젝트 수행 목적**  
이 프로젝트는 한일관계를 다룬 양국의 뉴스 기사를 크롤링하여 특정 한일관계 이슈에 대한 중립적인 시각을 제공하는 것을 목표로 합니다. Streamlit기반 사용자 인터페이스(UI)를 통해 기사 크롤링, 분류, 요약 및 중립 기사 생성의 모든 프로세스를 직관적으로 수행할 수 있습니다.

## 📖 프로젝트 개요

* 한국 언론(**[중앙일보](https://www.joongang.co.kr/)**)와 일본 언론(**[요미우리신문](https://www.yomiuri.co.jp/)**)에서 기사를 키워드(각각 '한일', '日韓')로 기사를 크롤링합니다.
* 현재는 2개사 뿐이나, 추후 **중앙-경향-아사히-요미우리** 4개사로 양국 각 내부적 좌우 정치성향까지 망라하는 중립성을 갖추도록 확장 예정
* 크롤링한 기사들을 동일 주제끼리 군집화하고, OpenAI API를 활용해 다각적인 시각을 반영한 중립 기사를 생성합니다.
* 이 서비스는 사용자가 직접 각 단계를 체험할 수 있도록 Streamlit으로 구축되었습니다. 
* **직접 실행이 번거로우신 분은 전체 프로세스를 [미리보기](https://github.com/fairyofdata/Article_Neutralizer/blob/master/NAKOJA_Preview.png)하실 수 있습니다.**

### 주요 기능
- **기사 크롤링**: 한국 및 일본 언론사에서 특정 키워드로 기사 목록을 수집하고, 개별 기사 본문까지 크롤링합니다.
- **데이터 분류**: 수집된 기사를 주제별로 그룹화하여 카테고리화합니다.
- **요약**: 각 카테고리에서 선택된 기사의 핵심 내용을 요약합니다.
- **중립 기사 생성**: 요약된 내용을 바탕으로 중립적인 시각의 기사를 생성하여 사용자에게 제공합니다.

## 🛠️ 기술 스택

- **크롤링**: Selenium, BeautifulSoup, Pandas
- **텍스트 처리 및 군집화**: OpenAI API, HuggingFace
- **중립 기사 생성**: OpenAI API (GPT 모델)
- **인터페이스**: Streamlit
- **언어**: Python 3.8+

## 🚀 설치 및 실행 방법

1. **프로젝트 클론**
   ```bash
   git clone https://https://github.com/fairyofdata/Article_Neutralizer
   cd Article_Neutralizer
   ```

2. **필수 라이브러리 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **Streamlit 앱 실행**
   ```bash
   streamlit run main.py
   ```

   로컬 서버에서 앱이 실행되며, http://localhost:8501 에서 접속하여 프로젝트의 주요 기능을 체험할 수 있습니다.
   

## 🖥️ 기능별 사용 방법
⚠️Alert: 프롬프트 최적화 중입니다.

### 1. **크롤링 시작**
   - 기사를 수집하려면 **Jungang 기사 수집** 또는 **Yomiuri 기사 수집** 버튼을 누릅니다.
   - 각 언론사로부터 키워드(각각 '한일', '日韓')에 맞는 기사가 수집됩니다.
   - 크롤링이 진행되면서 수집된 기사 건수가 실시간으로 업데이트됩니다.
   - 크롤링이 완료되면 기사 목록이 화면에 표시됩니다.

### 2. **데이터 분류**
   - **기사 제목 분류** 버튼을 클릭하여 수집된 기사들을 카테고리별로 분류합니다.
   - 분류된 기사는 테이블 형식으로 화면에 표시되며, 사용자는 이를 검토할 수 있습니다.

### 3. **분석을 위한 기사 선택**
   - 특정 카테고리를 선택하고 **한일 기사 쌍 선택** 버튼을 클릭하여 양국에서 같은 주제를 다루는 기사 쌍을 선택합니다.

### 4. **중립 기사 생성**
   - **중립 기사 생성 버튼**을 클릭하여 선택된 기사들을 바탕으로 중립적인 시각의 기사를 생성합니다.
   - 생성된 기사는 다각적인 이해를 반영하여 양국 간의 이슈에 대해 객관적인 정보를 제공합니다.

## 📂 아키텍처 설명

- **크롤링 모듈**: Selenium과 BeautifulSoup을 사용하여 각 언론사의 웹페이지에서 특정 키워드에 맞는 기사 목록과 링크를 수집합니다. 이후 개별 링크로 접근하여 기사 본문을 크롤링합니다.
- **데이터 분류 모듈**: OpenAI API를 사용하여 각 기사의 제목을 분석하고 주제별로 카테고리화합니다.
- **요약 및 중립 기사 생성 모듈**: OpenAI API를 통해 선택된 기사들의 요약문을 생성하고, 이를 바탕으로 중립적인 시각의 기사를 자동으로 작성합니다.
- **사용자 인터페이스 (UI)**: Streamlit을 사용하여 각 기능에 접근할 수 있는 버튼과 결과를 시각적으로 표시합니다.

## 📈 성능 및 품질 테스트

- 다양한 주제로 크롤링하여 분류 및 중립 기사 생성 결과를 검토했습니다.
- 카테고리화 및 중립 기사 생성의 정확성은 사용자의 피드백을 통해 지속적으로 개선할 계획입니다.

## 🔍 개선 가능성 및 차후 확장 기능

- **다국어 지원 개선**: 한국어와 일본어 외 다른 언어의 기사까지 처리할 수 있도록 확장 가능.
- **실시간 업데이트 기능**: 특정 시간 간격마다 기사를 자동으로 업데이트하여 최신 기사를 제공하는 기능 추가.
- **AI 모델 고도화**: 현재 사용 중인 GPT 모델 외에 다른 NLP 모델을 사용하여 문서 이해 및 요약 정확도를 높이는 방향으로 개선 가능.

## 💡 프로젝트의 의의 및 비즈니스적 활용

이 프로젝트는 한국과 일본 간의 편향된 언론 보도를 중립적인 시각으로 재구성하여 양국 간의 이해를 증진시키는 것을 목표로 합니다. 다양한 언어와 문화를 다루는 텍스트 데이터 처리, 분류 및 생성 AI 모델의 활용을 통해 실제 데이터 과학과 NLP 기술을 포트폴리오에 효과적으로 녹여내는 사례로 활용될 수 있습니다.

**비즈니스적 활용 유용성**:
- **데이터 분석을 통한 인사이트 도출**: 회사는 한국과 일본 간의 뉴스 보도를 분석함으로써 변화하는 사회적 분위기와 각 이슈에 대한 대중의 반응을 이해하고, 이를 바탕으로 새로운 전략 방향을 수립할 수 있습니다.
- **업무 자동화로 효율성 증대**: 이 프로젝트는 기사 수집과 분류, 요약 및 중립 기사 생성의 모든 단계를 자동화하여 기존에 많은 인적 자원과 시간이 필요했던 작업을 효과적으로 간소화합니다. 이를 통해 회사는 리소스를 절감하고, 보다 높은 가치를 창출하는 업무에 집중할 수 있게 됩니다.
- **시장 대응 능력 강화**: 실시간으로 업데이트되는 데이터와 분석 결과를 통해 회사는 빠르게 변화하는 시장 상황에 민첩하게 대응할 수 있는 능력을 갖출 수 있습니다.
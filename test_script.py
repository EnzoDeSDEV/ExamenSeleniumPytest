import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def chrome_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(options=chrome_options)
    yield chrome
    chrome.quit()

def test_article_extraction(chrome_browser):
    chrome_browser.get("https://www.lemonde.fr/")

    # Accepter les cookies
    accept_cookies(chrome_browser)

    article_section = WebDriverWait(chrome_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[3]/section[1]/section[5]'))
    )
    articles = article_section.find_elements(By.CLASS_NAME, 'article--river')

    assert articles, "Aucun article trouvé"

    for article in articles:
        title_element = WebDriverWait(article, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.article__title'))
        )
        title = title_element.text.strip()

        url_element = article.find_element(By.CSS_SELECTOR, 'a')
        url = url_element.get_attribute('href')

        assert title, "Le titre de l'article est vide"
        assert url, "L'URL de l'article est vide"

def accept_cookies(driver):
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/footer/button'))
        )
        cookie_button.click()
    except Exception as e:
        print("Impossible d'accepter les cookies:", str(e))

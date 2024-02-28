from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://www.lemonde.fr/")

# Récupérer l'élément contenant tous les articles en utilisant XPath
article_section = chrome.find_element(By.XPATH, '/html/body/main/div[3]/section[1]/section[5]')

# Récupérer les éléments correspondant à chaque article à l'intérieur de l'élément contenant tous les articles
articles = article_section.find_elements(By.CLASS_NAME, 'article--river')

for article in articles:
    # Récupérer le titre de l'article
    title_element = article.find_element(By.CSS_SELECTOR, 'a h3.article__title')
    title = title_element.text.strip()
    
    # Récupérer l'URL de l'article
    url_element = article.find_element(By.CSS_SELECTOR, 'a')
    url = url_element.get_attribute('href')
    
    # Afficher le titre et l'URL de l'article
    print("Titre:", title)
    print("URL:", url)
    print()

chrome.quit()
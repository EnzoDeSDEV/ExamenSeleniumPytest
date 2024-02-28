from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver):
    try:
        # Attendre que le bouton d'acceptation des cookies soit visible
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/footer/button'))
        )
        # Cliquer sur le bouton d'acceptation des cookies
        cookie_button.click()
    except Exception as e:
        print("Impossible d'accepter les cookies:", str(e))

def get_article_info():
    chrome_options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get("https://www.lemonde.fr/")

    # Accepter les cookies
    accept_cookies(chrome)

    # Attendre que l'élément contenant tous les articles soit visible
    article_section = WebDriverWait(chrome, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[3]/section[1]/section[5]'))
    )

    # Récupérer les éléments correspondant à chaque article à l'intérieur de l'élément contenant tous les articles
    articles = article_section.find_elements(By.CLASS_NAME, 'article--river')
    
    article_info_list = []
    for article in articles:
        # Attendre que le titre de l'article soit visible
        title_element = WebDriverWait(article, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.article__title'))
        )
        title = title_element.text.strip()

        # Récupérer l'URL de l'article
        url_element = article.find_element(By.CSS_SELECTOR, 'a')
        url = url_element.get_attribute('href')

        # Ajouter les informations de l'article à la liste
        article_info_list.append({'Titre': title, 'URL': url})

    chrome.quit()
    return article_info_list

# Appel de la méthode et récupération des informations
articles_info = get_article_info()

# Affichage des informations récupérées
for article_info in articles_info:
    print("Titre:", article_info['Titre'])
    print("URL:", article_info['URL'])
    print()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_2():
    # Настройка драйвера браузера
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Переход на сайт sbis.ru и переход в раздел "Контакты"
        driver.get("https://sbis.ru/")
        contacts_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/contacts"]')))
        contacts_link.click()
    
        # Проверка, что определен наш регион и наличия списка партнеров
        region_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]'))).text
        assert "Республика Башкортостан" in region_text, "Регион определен неверно."
        partners_list_before = driver.find_elements(By.CSS_SELECTOR, '[itemprop="name"]')
        assert partners_list_before!=[], "Список партнеров отсутствует"

        # Изменение региона на Камчатский край
        change_region_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]')))
        change_region_button.click()
    
        kamchatka_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="sbis_ru-Region-Panel__list-l"] :nth-child(43)')))
        kamchatka_option.click()
    
        # Проверка, что подставился выбранный регион
        new_region_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="s-Grid-col s-Grid-col--xm12"] [class="sbis_ru-Region-Chooser__text sbis_ru-link"]'))).text
        assert "Камчатский край" in new_region_text, "Не удалось изменить регион на Камчатский край."

        # Проверка, что список партнеров изменился
        partners_list_after = driver.find_elements(By.CSS_SELECTOR, '[itemprop="name"]')
        assert partners_list_before != partners_list_after, "Список партнеров не изменился после смены региона."
    
        # Проверка, что URL содержит информацию о регионе
        current_url = driver.current_url
        assert "kamchatskij-kraj" in current_url, "URL не содержит информации о Камчатском крае."
    
        # Проверка, что title содержит информацию о регионе
        page_title = driver.title
        assert "Saby Контакты — Камчатский край" in page_title, "Title не содержит информации о Камчатском крае."

    finally:
        driver.quit()





    



    

    



    
    
    
    
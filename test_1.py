from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_1():
    # Настройка драйвера браузера
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Переход на сайт sbis.ru и переход в раздел "Контакты"
        driver.get("https://sbis.ru/")
        contacts_link_1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="sbisru-Header__menu-link sbis_ru-Header__menu-link sbisru-Header__menu-link--hover"]')))
        contacts_link_1.click()
        contacts_link_2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/contacts" ] span')))
        contacts_link_2.click()

        # Поиск баннера Тензора и кликаем по нему
        tensor_banner = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#contacts_clients [alt="Разработчик системы Saby — компания «Тензор»"]')))
        tensor_banner.click()
    
        # Переход на сайт tensor.ru
        driver.switch_to.window(driver.window_handles[-1])
    
        # Проверка наличия блока "Сила в людях"
        block_sila_v_lyudyah = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg p:nth-child(1)')))
        assert block_sila_v_lyudyah.is_displayed(), "Блок 'Сила в людях' отсутствует."
    
        # Клик по ссылке "Подробнее" и проверка перехода на https://tensor.ru/about
        more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg a[class="tensor_ru-link tensor_ru-Index__link"]')))
        more_button.click()
        assert "https://tensor.ru/about" in driver.current_url, "При нажатии на 'Подробнее' не открылось https://tensor.ru/about"

        # Проверка размеров фотографий в разделе "Работаем"
        work_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')))
        images = work_section.find_elements(By.TAG_NAME, 'img')
    
        heights = set(img.get_attribute('naturalHeight') for img in images)
        widths = set(img.get_attribute('naturalWidth') for img in images)
    
        assert len(heights) == 1, "Высота изображений различается."
        assert len(widths) == 1, "Ширина изображений различается." 
    
    finally:
        driver.quit()

    

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time


def fetch_flashscore_data() -> list:
    chrome_options = Options()
    chrome_options.binary_location = r"your_path"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")  # Порт для DevTools

    driver_path = ChromeDriverManager().install()  # Автоматическая загрузка драйвера
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://www.flashscorekz.com/hockey/"
        driver.get(url)

        time.sleep(5)

        matches = []
        match_elements = driver.find_elements(By.CLASS_NAME, "event__match")

        for match in match_elements:
            try:
                # Названия команд
                home_team = match.find_element(By.CLASS_NAME, "event__participant--home").text.strip()
                away_team = match.find_element(By.CLASS_NAME, "event__participant--away").text.strip()

                # Очки
                home_score = match.find_element(By.CLASS_NAME, "event__score--home").text.strip()
                away_score = match.find_element(By.CLASS_NAME, "event__score--away").text.strip()

                # Проверяем наличие статуса
                try:
                    status = match.find_element(By.CLASS_NAME, "event_stage").text.strip()
                except:
                    status = ""

                matches.append({
                    "home_team": home_team,
                    "away_team": away_team,
                    "home_score": home_score,
                    "away_score": away_score,
                    "status": status
                })

            except Exception as e:
                print(f"Ошибка при обработке матча: {e}")
                continue

        return matches

    finally:
        driver.quit()


if __name__ == "__main__":
    data = fetch_flashscore_data()
    for match in data:
        print(match)

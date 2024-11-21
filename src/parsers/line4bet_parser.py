from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

from flashscore_parser import fetch_flashscore_data

matches_from_flashscore = fetch_flashscore_data()

notifications = []


def fetch_line4bet_data(matches) -> list:
    # Настройка Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://line4bet.ru/1x-05-11-2024-football/"
        driver.get(url)
        time.sleep(5)

        driver.find_element(By.ID, "tab_fb").click()
        time.sleep(3)
        driver.find_element(By.ID, "ice_btn").click()
        time.sleep(5)

        for match in matches:
            home_team = match["home_team"]
            away_team = match["away_team"]

            print(f"Ищем матч: {home_team} - {away_team}")

            match_found = False
            while not match_found:
                rows = driver.find_elements(By.CSS_SELECTOR,
                                            ".table_class tr")
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) > 1 and home_team in cells[0].text and away_team in cells[1].text:
                        print(f"Найден матч: {home_team} - {away_team}")
                        match_found = True

                        process_odds(row, match, notifications)
                        break

                if not match_found:
                    try:
                        next_button = driver.find_element(By.ID, "next_page_btn")
                        next_button.click()
                        time.sleep(3)
                    except Exception as e:
                        print("Матч не найден в таблице.")
                        break

    finally:
        driver.quit()


def process_odds(row, match, notifications):
    """Обрабатывает коэффициенты для заданного матча."""
    cells = row.find_elements(By.TAG_NAME, "td")
    odds = {
        "P1": float(cells[2].text),
        "P2": float(cells[3].text),
        "X": float(cells[4].text)
    }

    print(f"Коэффициенты: {odds}")

    if match["home_score"] > match["away_score"]:
        result = "P1"
    elif match["home_score"] < match["away_score"]:
        result = "P2"
    else:
        result = "X"

    if odds[result] > 2.45:  # Пример среднего коэффициента
        print(f"Ставка зашла для {match['home_team']} - {match['away_team']}.")
    else:
        print(f"Ставка не зашла для {match['home_team']} - {match['away_team']}.")
        notifications.append(f"Не заход для {match['home_team']} - {match['away_team']}.")


if __name__ == "__main__":
    fetch_line4bet_data(matches_from_flashscore)

    for notification in notifications:
        print(notification)


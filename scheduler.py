import schedule
import time
from main import main


def job():
    print("Запуск парсинга и обработки данных...")
    main()


def run_scheduler():
    # Запуск парсинга каждую минуту (можно настроить по своему усмотрению)
    schedule.every(1).minute.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_scheduler()
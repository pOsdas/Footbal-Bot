from utils.database.py import create_connection, create_table, insert_match, fetch_matches
from utils.notifications import send_telegram_message
from utils.helpers import calculate_average_odds, parse_match_result, format_match_result


def main():
    conn = create_connection("matches.db")
    create_table(conn)

    match = ("Торонто", "Вегас", 3, 0, "Завершен")
    insert_match(conn, match)

    matches = fetch_matches(conn)
    print("Все матчи из базы данных:", matches)

    odds = [2.45, 1.90, 3.10]
    avg_odds = calculate_average_odds(odds)
    print(f"Средний коэффициент: {avg_odds}")

    result = parse_match_result(3, 0)
    formatted_result = format_match_result("Торонто", "Вегас", result)
    print(formatted_result)

    send_telegram_message(formatted_result, "your_telegram_bot_token", "your_chat_id")


if __name__ == "__main__":
    main()

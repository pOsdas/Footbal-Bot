def calculate_average_odds(odds):
    """Вычисление среднего коэффициента из списка"""
    return sum(odds) / len(odds) if odds else 0


def parse_match_result(home_score, away_score):
    """Определение результата матча"""
    if home_score > away_score:
        return "Победа дома"
    elif home_score < away_score:
        return "Победа гостей"
    else:
        return "Ничья"


def format_match_result(home_team, away_team, result):
    """Форматирование строки с результатом матча"""
    return f"{home_team} - {away_team}: {result}"

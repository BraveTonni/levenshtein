"""
Расстояние левештейна. Неявный поиск с использованием расстояния левенштейна.
"""

def load_text(file_name: str) -> str:
    """
    Returns text from file in line
    """
    with open(file_name, "r", encoding="utf-8") as f:
        return "".join(f.readlines()).strip()


def get_distance(word1: str, word2: str) -> int:
    # для экономии памяти короткое слово кладём в строки
    if len(word1) > len(word2):
        word1, word2 = word2, word1

    m, n = len(word1), len(word2)

    # матрица (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # границы матрицы
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # основная часть
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # удаление
                dp[i][j - 1] + 1,      # вставка
                dp[i - 1][j - 1] + cost  # замена
            )

    return dp[m][n]


def search(text: str, query: str) -> list[tuple[str, int]]:
    """неявный поиск с использованием расстояния левенштейна"""
    distances = {}
    words = text.split()

    for word in words:
        distances[word] = get_distance(word, query)

    min_dist = min(distances.values())

    results = [(k, v) for k, v in distances.items() if v == min_dist and v <= 3]

    return results


def main():
    text = load_text("file.txt")

    while True:
        query = input("> ")
        
        responses = search(text, query)

        if not responses:
            print("Not found.")
    
        for word, distance in responses:
            print(f"{word} - {distance}")


if __name__ == "__main__":
    main()
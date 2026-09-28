"""
Расстояние левештейна. Неявный поиск с использованием расстояния левенштейна.
"""

import pandas as pd

def get_distance(word1: str, word2: str) -> int:
    # для экономии памяти короткое слово ложим в столбцы
    if len(word1) > len(word2):
        word1, word2 = word2, word1

    # переменные из формулы m, n
    m, n = len(word1), len(word2)

    # матрица (m+1) (n+1), заполнена нулями
    # индексы и столбцы символы слов, чтобы было видно глазами
    df = pd.DataFrame(
        0,
        index=[""] + list(word1),
        columns=[""] + list(word2),
        dtype=int,
    )

    # границы матрицы
    for i in range(m + 1):
        df.iat[i, 0] = i
    for j in range(n + 1):
        df.iat[0, j] = j

    # print(df)

    # основная часть
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1  # цена действия

            df.iat[i, j] = min(
                df.iat[i - 1, j] + 1, # удаление
                df.iat[i, j - 1] + 1, # вставка
                df.iat[i - 1, j - 1] + cost  # замена
            )

    return int(df.iat[m, n])
    


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
    text = "У Лукоморья дуб зелёный златая цепь на дубе том и днём и ночьюкот учёный все ходит по цепи кругом."

    while True:
        query = input("> ")
        
        responses = search(text, query)

        if not responses:
            print("Not found.")
    
        for word, distance in responses:
            print(f"{word} - {distance}")


if __name__ == "__main__":
    main()

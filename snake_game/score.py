import json


class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.read_score()

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def reset_score(self):
        self.score = 0

    def save_score(self):
        data = {"high_score": self.high_score}
        with open("snake_game/score.json", "w") as file:
            json.dump(data, file)

    def game_over(self) -> None:
        self.save_score()
        self.reset_score()

    def read_score(self) -> None:
        try:
            with open("snake_game/score.json", "r") as file:
                data: dict[str, str] = json.load(file)
                self.high_score = data.get("high_score", 0)
        except FileNotFoundError:
            # Если файл не существует, обрабатываем исключение
            print("Файл 'score.json' не найден. Устанавливаю high_score в значение по умолчанию.")
            self.save_score()

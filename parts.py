from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


class Game:
    """
    Класс, который описывает игру "Угадай число"
    """
    start_time = dt.now()

    def __init__(self) -> None:
        self.username = 'Anonimus'
        self.total_games = 0

    def __str__(self) -> str:
        return f'Игра - "Угадай число". Игрок - "{self.username}".'

    @access_control
    def _get_statistics(self) -> None:
        game_time = dt.now() - self.start_time
        print(f'Общее время игры: {game_time}, '
              f'текущая игра - №{self.total_games}')

    @access_control
    def _get_right_answer(self, number: int, *args, **kwargs) -> None:
        print(f'Правильный ответ: {number}')

    def get_username(self) -> None:
        username = input(
            'Представьтесь, пожалуйста, как Вас зовут?\n'
        ).strip()
        self.username = username if username != '' else self.username
        if self.username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{self.username}, добро пожаловать в игру!')

    def start(self) -> None:
        # Счётчик игр в текущей сессии.
        self.total_games += 1
        # Получаем случайное число в диапазоне от 1 до 100.
        number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            # Получаем пользовательский ввод,
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self._get_statistics()
                case 'answer':
                    self._get_right_answer(number)
                case _:
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self._check_number(guess, number):
                        break

    def _check_number(self, guess: int, number: int) -> bool:
        # Если число угадано...
        if guess == number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            # ...возвращаем True
            return True
        elif guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

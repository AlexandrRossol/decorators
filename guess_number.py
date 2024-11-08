from parts import Game


def main() -> None:
    game = Game()
    game.get_username()
    while True:
        game.start()
        play_again = input('\nХотите сыграть ещё? (yes/no) ')
        if play_again.strip().lower() not in ('y', 'yes'):
            break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    main()

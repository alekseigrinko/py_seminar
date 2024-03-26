from sys import argv
import data_check


# Модуль для запуска в терминале с передачей даты на проверку


def main():
    data_check.input_date(argv)


if __name__ == '__main__':
    main()

# coding=utf8
import logging


def create_logs():
    logger_one = logging.getLogger("api_logs.txt")
    logger_one.setLevel("DEBUG")

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('logs/api_logs.txt')

    logger_one.addHandler(console_handler)
    logger_one.addHandler(file_handler)

    formatter_one = logging.Formatter("%(asctime)s  :  %(message)s")
    # ("% (asctime) s[ % (levelname) s] % (message) s %")

    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)
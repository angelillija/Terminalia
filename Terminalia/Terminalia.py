import os
import time
import ctypes
import locale
import requests

from langdetect import detect
from textblob import TextBlob
from textblob.exceptions import NotTranslated


class Color:
    """Color class for ANSI color codes"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\033[90m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_PURPLE = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    RESET = "\033[0m"


class Terminal:
    @staticmethod
    def set_title(title: str) -> None:
        """
        Sets the console window title to the given title.

        Args:
        title (str): The title to set for the console window.
        """
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            print(f"\033]0;{title}\a", end='', flush=True)

    @staticmethod
    def clear() -> None:
        """
        Clears the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def hide_cursor() -> None:
        """
        Shows the cursor in the console.
        """
        if os.name == 'nt':
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            ctypes.windll.kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            ctypes.windll.kernel32.SetConsoleMode(handle, mode.value & ~0x20)
        else:
            print("\033[?25l", end='', flush=True)

    @staticmethod
    def show_cursor() -> None:
        """
        Hides the cursor in the console.
        """
        if os.name == 'nt':
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            ctypes.windll.kernel32.GetConsoleMode(handle, ctypes.byref(mode))

            mode.value |= 1 | 2 | 4
            ctypes.windll.kernel32.SetConsoleMode(handle, mode)
        else:
            print(f"\033[?25h", end="", flush=True)

    @staticmethod
    def translate(text: str) -> str:
        """
        Translates the given text from English to another language.

        Args:
        text (str): The text to be translated.

        Returns:
        str: The translated text.
        """
        try:
            return TextBlob(text).translate(from_lang=detect(text),
                                            to=str(locale.getdefaultlocale())
                                            .split("_")[0].replace("('", ""))
        except NotTranslated:
            return text

    @staticmethod
    def write(text: str, interval: float = 0.01, hide_cursor: bool = True) -> str:
        """
        Simulates typing out the given text with a specified interval between characters.

        Args:
        text (str): The text to be "typed" out.
        interval (float, optional): The amount of time to wait between typing each character, in seconds. Defaults to 0.01.
        hide_cursor (bool, optional): Whether to hide the cursor while typing. Defaults to True.

        Returns:
        str: The final typed out string.
        """
        Terminal.hide_cursor() if hide_cursor else None

        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(interval)
        return ""

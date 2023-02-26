import os
import sys
import time
import locale
import requests

from langdetect import detect
from textblob import TextBlob
from textblob.exceptions import NotTranslated

""" Terminalia: A Python Library for Command Line Interface (CLI) Development """

class Color: 
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\033[90m"
    
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_PURPLE = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


class Terminal:
    @staticmethod
    def Title(self, title: str) -> None:
        """
        Sets the title of the terminal window.
        
        Args:
            title (str): The title to set for the terminal window.
        Returns:
            None
        """
        print(f"\33]0;{title}\a", end="", flush=True)

    @staticmethod
    def Clear() -> None:
        """
        Clears the terminal screen.

        Args:
            None
        Returns:
            None
        """
        os.system("cls||clear")

    @staticmethod
    def Hide_Cursor() -> None:
        """
        Hides the cursor on the terminal.

        Arguments:
            None
        Returns:
            None
        """
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    @staticmethod
    def Show_Cursor() -> None:
        """
        Displays the cursor on the terminal.

        Arguments:
            None
        Returns:
            None
        """
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


    @staticmethod
    def Translate(text: str) -> str:
        """
        Translate text from one language to another. Auto detects the specified text's language as well as the users language.

        Args:
            text (str): The text to translate.
        Returns:
            str: The translated text.
        """
        try:
            return TextBlob(text).translate(from_lang=detect(text), to=str(locale.getdefaultlocale()).split("_")[0].replace("('", ""))
        except NotTranslated:
            return text

    @staticmethod
    def Write(self, text: str, interval: float = 0.01, hide_cursor: bool = True) -> str:
        """
        Writes the specified text to the console, one character at a time, with an optional delay between characters.

        Args:
            text (str): The text to write.
            interval (float, optional): The delay between characters, in seconds. Default is 0.01 seconds.
            hide_cursor (bool, optional): Whether to hide the cursor while writing the text. Default is True.

        Returns:
            str: The full text that was written to the console.
        """
        self.Hide_Cursor() if hide_cursor else None

        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(interval)
        return ""

    @staticmethod
    def Color(text: str, color: Color, reset: bool = True) -> str: 
        """
        Colors text with the specified color.

        Args:
            text (str): The text to color.
            color (Color): The color to use. 
            reset (bool, optional): Whether to reset the color after the text is printed. Default is True.
        Returns:
            str: The colored text.
        """

        return f"{color}{text}{Color.RESET}" if reset else f"{color}{text}"

    @staticmethod
    def Center(text: str) -> str: 
        """
        Centers the specified text.

        Args:
            text (str): The text to center.
        Returns:
            str: The centered text.
        """
        return text.center(os.get_terminal_size().columns)
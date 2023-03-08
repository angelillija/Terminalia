<h1 align="center">Terminalia</h1>
<h3 align="center">A Python Library for Command Line Interface (CLI) Development</h3>
<br>
<br>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.3-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/aithedev/Terminalia/blob/main/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/Documentation-True-blue.svg" />
  </a>
  <a href="https://github.com/aithedev/Terminalia/" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained-True-blue.svg" />
  </a>
  </a>
  <a href="https://pepy.tech/project/terminalia" target="_blank">
    <img alt="Downloads" src="https://static.pepy.tech/personalized-badge/terminalia?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" />
  </a>
</p>

Terminalia provides a collection of useful functions for working with terminals, including:

- `Terminal.set_title(title: str)`: sets the title of the console window to the given title.
- `Terminal.clear()`: clears the terminal screen.
- `Terminal.hide_cursor()`: hides the cursor in the console.
- `Terminal.show_cursor()`: shows the cursor in the console.
- `Terminal.translate(text: str)`: translates the given text from English to another language.
- `Terminal.write(text: str, interval: float = 0.01, hide_cursor: bool = True)`: simulates typing out the given text with a specified interval between characters.

## Install
```
pip3 install Terminalia
```

# Usage
To use this package, simply import it as follows:
```py
from Terminalia import Terminal, Color # importing color is optional
```

### Title
**Sets the title of the terminal window.**

```py
from Terminalia import Terminal

Terminal.Title("This is a test title")
```
- `Args:`
  - **title (str)**: The title to set for the terminal window.
        
### Clear 
**Clears the terminal screen.**

```py
from Terminalia import Terminal

Terminal.Clear()
```

### Hide_Cursor
**Hides the cursor on the terminal.**
```py
from Terminalia import Terminal

Terminal.Hide_Cursor()
```

### Show_Cursor
**Displays the cursor on the terminal.**
```py
from Terminalia import Terminal

Terminal.Show_Cursor()
```

### Translate
**Translate text from one language to another. Auto detects the specified text's language as well as the users language.**
```py
from Terminalia import Terminal

print(Terminal.Translate("Ceci est un exemple de texte"))
```
- `Args:` 
  - **text (str)**: The text to translate.
- `Returns:` 
  - **str**: The translated text.


### Write
**Writes the specified text to the console, one character at a time, with an optional delay between characters.**
```py
from Terminalia import Terminal

print(Terminal.Write(text="This is an example text", interval=0.5, hide_cursor=True))
```
- `Args:`
  - **text (str)**: The text to write out.
  - **interval (float, optional)**: The delay between characters, in seconds. Default is 0.01 seconds.
  - **hide_cursor (bool, optional)**: Whether to hide the cursor while writing the text. Default is True.
- `Returns:`
  - **str**: The final typed out string.
  
### Color
Colors text with the specified color.
```py
from Terminalia import Color

print(f"{Color.BLUE}Hello, world!{Color.RESET}")
```

- `Colors`
  - **BLACK**
  - **RED**
  - **GREEN**
  - **YELLOW**
  - **BLUE**
  - **PURPLE**
  - **CYAN**
  - **WHITE**
  - **GREY**
  - **BOLD**
  - **UNDERLINE**
  - **BG_BLACK**
  - **BG_RED**
  - **BG_GREEN**
  - **BG_YELLOW**
  - **BG_BLUE**
  - **BG_MAGENTA**
  - **BG_CYAN**
  - **BG_WHITE**
  - **BRIGHT_RED**
  - **BRIGHT_GREEN**
  - **BRIGHT_YELLOW**
  - **BRIGHT_BLUE**
  - **BRIGHT_PURPLE**
  - **BRIGHT_CYAN**
  - **BRIGHT_WHITE**
  - **RESET**
  
## `🧑‍💻` Contact
- **Website**: https://aithe.dev/
- **Telegram**: t.me/aithedev
- **Discord**: ai#4444

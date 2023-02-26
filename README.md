# Terminalia
A Python Library for Command Line Interface (CLI) Development

## Features
- [Sets the title of the terminal window.](https://github.com/aithedev/Terminalia#Title)
- [Clears the terminal screen.](https://github.com/aithedev/Terminalia#Clear)
- [Hides the cursor on the terminal.](https://github.com/aithedev/Terminalia#Hide_Cursor)
- [Displays the cursor on the terminal.](https://github.com/aithedev/Terminalia#Show_Cursor)
- [Translate text from one language to another. Auto detects the specified text's language as well as the users language.](https://github.com/aithedev/Terminalia#Translate)
- [Prints text by writing it out letter by letter with an interval.](https://github.com/aithedev/Terminalia#Write)
- [Colors text with the specified color.](https://github.com/aithedev/Terminalia#Color)
- [Centers the specified text in a line of width 80 characters.](https://github.com/aithedev/Terminalia#Center)


### Title
**Sets the title of the terminal window.**

```py
from Terminalia import Terminal

Terminal.Title("This is a test title")
```
- `Args:`
  - **title (str)**: The title to set for the terminal window.
- `Returns:`
  - None
        
### Clear 
**Clears the terminal screen.**

```py
from Terminalia import Terminal

Terminal.Clear()
```
- `Args:` 
  - None
- `Returns:` 
  - None

### Hide_Cursor
**Hides the cursor on the terminal.**
```py
from Terminalia import Terminal

Terminal.Hide_Cursor()
```
- `Args:` 
  - None
- `Returns:` 
  - None

### Show_Cursor
**Displays the cursor on the terminal.**
```py
from Terminalia import Terminal

Terminal.Show_Cursor()
```
- `Args:` 
  - None
- `Returns:` 
  - None

### Translate
**Translate text from one language to another. Auto detects the specified text's language as well as the users language.**
```py
from Terminalia import Terminal

Terminal.Show_Cursor()
```
- `Args:` 
  - **text (str)**: The text to translate.
- `Returns:` 
  - **str**: The translated text.


### Write
**Writes the specified text to the console, one character at a time, with an optional delay between characters.**
```py
from Terminalia import Terminal

Terminal.Write(text="This is an example text", interval=0.5, hide_cursor=True)
```
- `Args:`
  - **text (str)**: The text to write out.
  - **interval (float, optional)**: The delay between characters, in seconds. Default is 0.01 seconds.
  - **hide_cursor (bool, optional)**: Whether to hide the cursor while writing the text. Default is True.
- `Returns:`
  - **str**: The translated text.
  
### Color
Colors text with the specified color.
```py
from Terminalia import Terminal

Terminal.Color(text="This is an example text", color=Colors.BLUE, reset=True)
```
- `Args:`
  - **text (str)**: The text to color.
  - **color (Color)**: The color to use. 
  - **reset (bool, optional)**: Whether to reset the color after the text is printed. Default is True.
- `Returns:`
  - **str**: The colored text.
  

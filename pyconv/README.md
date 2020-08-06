# pyconv - binary ninja plugin

Converts Binary Ninja arrays, strings, and ints to Python data on your clipboard.

![gif](https://i.imgur.com/tcXTnnV.gif)

## Why
I made this simple plugin because it was pretty annoying having to copy arrays and strings in Binary Ninja and changing it into Python data. I use Binary Ninja mostly for CTFs and easily extracting data from Binja to my Python scripts like this allows for rapid prototyping.


## Dependencies
`pip install pyperclip`

### //TODO
- Add support for more types
- Remove annoying null bytes from strings
- Use API more effectively (?)

"""
A text-based (command line) program that takes
any string input and converts it to Morse Code
"""

# PasswordManager and FlashCardProject project are examples of text input with TKinter
# TODO Add to Git
# TODO Add to GitHub

from tkinter import *
from tkinter import messagebox

# Morse code dictionary
morse_dict_actual_dot_actual_dash = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '＄': '...-..-', '@': '.--.-.', ' ': '/'
}
morse_dict_dot_dash = {
    'A': 'dot dash ', 'B': 'dash dot dot dot ', 'C': 'dash dot dash dot ', 'D': 'dash dot dot ', 'E': 'dot ', 'F': 'dot dot dash dot ', 'G': 'dash dash dot ', 'H': 'dot dot dot dot ',
    'I': 'dot dot ', 'J': 'dot dash dash dash ', 'K': 'dash dot dash ', 'L': 'dot dash dot dot ', 'M': 'dash dash ', 'N': 'dash dot ', 'O': 'dash dash dash ', 'P': 'dot dash dash dot ',
    'Q': 'dash dash dot dash ', 'R': 'dot dash dot ', 'S': 'dot dot dot ', 'T': 'dash ', 'U': 'dot dot dash ', 'V': 'dot dot dot dash ', 'W': 'dot dash dash ', 'X': 'dash dot dot dash ',
    'Y': 'dash dot dash dash ', 'Z': 'dash dash dot dot ', '0': 'dash dash dash dash dash ', '1': 'dot dash dash dash dash ', '2': 'dot dot dash dash dash ', '3': 'dot dot dot dash dash ', '4': 'dot dot dot dot dash ',
    '5': 'dot dot dot dot dot ', '6': 'dash dot dot dot dot ', '7': 'dash dash dot dot dot ', '8': 'dash dash dash dot dot ', '9': 'dash dash dash dash dot ', '. ': 'dot dash dot dash dot dash ', ',': 'dash dash dot dot dash dash ',
    '?': 'dot dot dash dash dot dot ', "'": 'dot dash dash dash dash dot ', '!': 'dash dot dash dot dash dash ', '/': 'dash dot dot dash dot ', '(': 'dash dot dash dash dot ', ')': 'dash dot dash dash dot dash ', '&': 'dot dash dot dot dot ',
    ':': 'dash dash dash dot dot dot ', ';': 'dash dot dash dot dash dot ', '=': 'dash dot dot dot dash ', '+': 'dot dash dot dash dot ', '- ': 'dash dot dot dot dot dash ', '_': 'dot dot dash dash dot dash ', '"': 'dot dash dot dot dash dot ',
    '＄': 'dot dot dot dash dot dot dash ', '@': 'dot dash dash dot dash dot ', ' ': '/'
}
morse_dict = {
    'A': '▄ ▄▄▄ ', 'B': '▄▄▄ ▄ ▄ ▄ ', 'C': '▄▄▄ ▄ ▄▄▄ ▄ ', 'D': '▄▄▄ ▄ ▄ ', 'E': '▄ ', 'F': '▄ ▄ ▄▄▄ ▄ ', 'G': '▄▄▄ ▄▄▄ ▄ ', 'H': '▄ ▄ ▄ ▄ ',
    'I': '▄ ▄ ', 'J': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 'K': '▄▄▄ ▄ ▄▄▄ ', 'L': '▄ ▄▄▄ ▄ ▄ ', 'M': '▄▄▄ ▄▄▄ ', 'N': '▄▄▄ ▄ ', 'O': '▄▄▄ ▄▄▄ ▄▄▄ ', 'P': '▄ ▄▄▄ ▄▄▄ ▄ ',
    'Q': '▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 'R': '▄ ▄▄▄ ▄ ', 'S': '▄ ▄ ▄ ', 'T': '▄▄▄ ', 'U': '▄ ▄ ▄▄▄ ', 'V': '▄ ▄ ▄ ▄▄▄ ', 'W': '▄ ▄▄▄ ▄▄▄ ', 'X': '▄▄▄ ▄ ▄ ▄▄▄ ',
    'Y': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 'Z': '▄▄▄ ▄▄▄ ▄ ▄ ', '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ', '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄ ', '4': '▄ ▄ ▄ ▄ ▄▄▄ ',
    '5': '▄ ▄ ▄ ▄ ▄ ', '6': '▄▄▄ ▄ ▄ ▄ ▄ ', '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄ ', '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ', '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', '▄ ': '▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ', ',': '▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄ ',
    '?': '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄ ', "'": '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', '!': '▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', '/': '▄▄▄ ▄ ▄ ▄▄▄ ▄ ', '(': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ', ')': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', '&': '▄ ▄▄▄ ▄ ▄ ▄ ',
    ':': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄ ', ';': '▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄ ', '=': '▄▄▄ ▄ ▄ ▄ ▄▄▄ ', '+': '▄ ▄▄▄ ▄ ▄▄▄ ▄ ', '▄▄▄ ': '▄▄▄ ▄ ▄ ▄ ▄ ▄▄▄ ', '_': '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', '"': '▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄ ',
    '＄': '▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄▄▄ ', '@': '▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄ ', ' ': '/'
}

BACKGROUND_COLOR = "#B1DDC6"
ERROR_LABEL_COLOR = "#FF5733"


# Convert to Morse Code
def convert_text():
    canvas.delete('all')
    latin_phrase = text_entry.get().upper()
    try:
        morse_code = ''.join([morse_dict[l] for l in latin_phrase])
    except KeyError:
        error_label.config(text="You entered an invalid value! Try again", fg='red')
    else:
        morse_code_dot_dash = ''.join([morse_dict_dot_dash[l] for l in latin_phrase])
        canvas.create_text(200, 80, width=360, text=morse_code)
        canvas.create_text(200, 160, width=360, text=morse_code_dot_dash)


# Setup UI
window = Tk()
window.title("Text to Morse Code Converter")
window.config(padx=40, pady=30, bg=BACKGROUND_COLOR)

# Setup canvas and widgets
canvas = Canvas(width=400, height=200, bd=20)
text_label = Label(text="Enter text in latin script:", bg=BACKGROUND_COLOR)
text_entry = Entry(width=40)
padding_one = Label(text="", bg=BACKGROUND_COLOR)
error_label = Label(text="", bg=BACKGROUND_COLOR)
convert_text_button = Button(text="Convert Text to Morse Code", command=convert_text)
text_entry.focus()

# Display widgets on window
canvas.grid(column=0, row=0)
padding_one.grid(column=0, row=1)
text_label.grid(column=0, row=2)
text_entry.grid(column=0, row=3)
error_label.grid(column=0, row=4)
convert_text_button.grid(column=0, row=5)

# Keep window visible
window.mainloop()


# # Morse code converter program
# run_program = True
# while run_program:
#     morse_phrase = ''
#     print('Welcome to the text to morse code converter!')
#     latin_phrase = input("Enter a string in latin script or 'sos' to exit: \n").upper()
#     try:
#         morse_phrase = ''.join([morse_dict[l] for l in latin_phrase])
#     except KeyError:
#         print("You entered an invalid value.")
#     else:
#         print(morse_phrase)
#     if latin_phrase == 'SOS':
#         run_program = False
# print('Thank you come again!')

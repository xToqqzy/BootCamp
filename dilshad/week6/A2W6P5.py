def message_to_morse_dict(sentence):
    morse = {
        ',': '--..--',
        '?': '..--..',
        '.': '.-.-.-',
        ' ': ' ',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }


def message_to_morse(bericht):
    uitkomst = ""
    for teken in bericht.upper():
        if teken == " ":
            uitkomst += "   "
        elif teken not in message_to_morse_dict:
            print(f"Cant convert [{teken}]")
        else:
            uitkomst += message_to_morse_dict[teken] + " "

    return uitkomst


def morse_to_message(morse):
    omgedraaide_dict = {}
    for item in message_to_morse_dict.items():
        key, value = item
        omgedraaide_dict.update({value: key})

    uitkomst = ""
    morse = morse.replace("   ", " ( ")
    for teken in morse.split(" "):
        if teken == "(":
            uitkomst += " "
        elif teken not in omgedraaide_dict:
            return


def translate_text(tekts):
    morse = True

    for letter in tekts:
        if letter not in ["-", " ", "."]:
            morse = False

    if morse == False:
        uitkomst = message_to_morse(tekts)
    else:
        uitkomst = morse_to_message(tekts)

    return uitkomst


if __name__ == "__main__":
    input = input("voer je tekts in")

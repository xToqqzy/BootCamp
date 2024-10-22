def message_to_morse(sentence):
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ',': '--..--', '?': '..--..', '.': '.-.-.-', ' ': '    '
    }

    morse_output = []
    for char in sentence:
        if char.upper() in morse:
            morse_output.append(morse[char.upper()])
        else:
            print(f"Can't convert char [{char}]")
            return

    return ' '.join(morse_output)


def morse_to_message(morse_code):
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ',': '--..--', '?': '..--..', '.': '.-.-.-', ' ': ' '
    }

    reversed_morse = {v: k for k, v in morse.items()}
    message = ''

    for code in morse_code.split(' '):
        if code in reversed_morse:
            message += reversed_morse[code]
        else:
            print(f"Can't convert Morse code [{code}]")
            return

    return message


def translate_text(text):
    if all(char in ['.', '-', ' '] for char in text):
        return morse_to_message(text)
    else:
        return message_to_morse(text)


if __name__ == "__main__":
    userInput = input('Enter your message: ')
    translatedOutput = translate_text(userInput)

    if translatedOutput is not None:
        print(translatedOutput)

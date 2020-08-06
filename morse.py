"""
In this kata you have to write a simple Morse code decoder.
While the Morse code is now mostly superseded by voice and digital
data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes".
For example, the letter A is coded as ·−, letter Q is coded as −−·−,
and digit 1 is coded as ·−−−−.
The Morse code is case-insensitive, traditionally capital letters are used.
When the message is written in Morse code, a single space is used to separate
the character codes and 3 spaces are used to separate words.
For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes,
the most notorious of those is the international distress signal SOS (that was first issued by Titanic),
that is coded as ···−−−···.
These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:
decodeMorse('.... . -.--   .--- ..- -.. .')
should return "HEY JUDE"
"""


def decodeMorse(morse):
    morse_code_dict = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                       'SOS': '...---...'}
    morse_code = morse.strip()
    chars_for_word = []
    words = []
    split_by_words = morse_code.split('   ')
    for i in range(len(split_by_words)):
        morse_word = split_by_words[i].split()
        for unit in morse_word:
            if unit.isalnum():
                chars_for_word.append(" " + unit + " ")
            for char, morse in morse_code_dict.items():
                if unit == morse:
                    chars_for_word.append(char)
        words.append("".join(chars_for_word))
        chars_for_word.clear()
    result = " ".join(words)

    return result.strip()
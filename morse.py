
def is_morse(letter):
    morsedict = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.", 'H': "....",
                 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 'P': ".--.",
                 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
                 'Y': "-.--", 'Z': "--..", '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-",
                 '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.", '.': ".-.-.-", ',': "--..--",
                 '?': "..--.."}
    if letter in morsedict.values():
        return list(morsedict.keys())[list(morsedict.values()).index(letter)]
    else:
        return "wrong"


def morse_file(file):
    unencrypted = ''
    with open(file, 'r') as file:
        file_string = file.read().replace('\n', '')
    file_list = file_string.split(' / ')
    for word in file_list:
        letters = word.split(' ')
        for letter in letters:
            if is_morse(letter) != "wrong":
                unencrypted = unencrypted + is_morse(letter)
            else:
                return "Error in Morse Code"
        unencrypted = unencrypted + ' '
    unencrypted = unencrypted[:-1]
    return unencrypted


def count_symbols(file):
    symbols_dict = {}
    file_string = morse_file(file)
    file_string = file_string.replace(' ', '')
    while file_string != '':
        symbols_dict[file_string[0]] = file_string.count(file_string[0])
        file_string = file_string.replace(file_string[0], '')
    sorted_dict = dict(sorted(symbols_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def print_count(file):
    symbols_dict = count_symbols(file)
    key_list = []
    for item in symbols_dict:
        key_list.append(symbols_dict[item])
    key_list = sorted(list(set(key_list)), reverse=True)
    print(key_list)
    for item in key_list:
        symbols_list = [i for i, j in symbols_dict.items() if j == item]
        print("".join(symbols_list) + " - " + str(item))


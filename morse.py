
def isMorse(letter):
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
        fileString = file.read().replace('\n', '')
    fileList = fileString.split(' / ')
    for word in fileList:
        letters = word.split(' ')
        for letter in letters:
            if isMorse(letter) != "wrong":
                unencrypted = unencrypted + isMorse(letter)
            else:
                return "Error in Morse Code"
        unencrypted = unencrypted + ' '
    unencrypted = unencrypted[:-1]
    return unencrypted


def count_symbols(file):
    symbolsDict = {}
    with open(file, 'r') as file:
        fileString = file.read().replace('\n', '')
        fileString = fileString.replace(' ', '')
    while fileString != '':
        symbolsDict[fileString[0]] = fileString.count(fileString[0])
        fileString = fileString.replace(fileString[0], '')
    sorted_dict = dict(sorted(symbolsDict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def print_count(file):
    symbolsDict = count_symbols(file)
    keyList = []
    for item in symbolsDict:
        keyList.append(symbolsDict[item])
    keyList = sorted(list(set(keyList)), reverse=True)
    print(keyList)
    for item in keyList:
        symbolsList = [i for i, j in symbolsDict.items() if j == item]
        print("".join(symbolsList) + " - " + str(item))

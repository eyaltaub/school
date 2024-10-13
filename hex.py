def is_valid_letter(letter):
    hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
           "d": 13, "e": 14, "f": 15}
    return letter in hex


def hex_to_dec(string):
    hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
           "d": 13, "e": 14, "f": 15}
    dec = 0
    power = 0
    if string.startswith("0x"):
        string = string[2:]
    string = string[::-1]
    for letter in string:
        if is_valid_letter(letter):
            if letter.isalpha():
                letter.lower()
            dec = dec + (hex[letter] * pow(16, power))
            power = power + 1
        else:
            return "Error: invalid hexadecimal"
    return dec


def hex_sum(string):
    sum = 0
    temp = ""
    while string != "":
        first  = True
        for letter in string:
            if is_valid_letter(letter) and first:
                temp = temp + letter
            else:
                first = False
        string = string[string.index(temp) + len(temp) + 1:]
        sum += hex_to_dec(temp)
        temp = ""
        first = True
    return sum


def print_average():
    hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
           "d": 13, "e": 14, "f": 15}
    sum = 0
    num = 0
    enter = input()
    while hex_to_dec(enter) != "Error: invalid hexadecimal":
        sum += hex_to_dec(enter)
        num += 1
        enter = input()
    print(sum / num)

print_average()
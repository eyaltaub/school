def rotate(image, degrees):
    if degrees == 0:
        return image

    if degrees == 90:
        finalImage = ""
        imageList = image.split("\n")
        imageList = imageList[::-1]
        count = 1
        for char in range(len(imageList[0])):
            for element in imageList:
                finalImage += element[char]
            if count != len(imageList):
                finalImage += "\n"
            count += 1
        return finalImage

    if degrees == 180:
        finalImage = ""
        imageList = image.split("\n")
        imageList = imageList[::-1]
        imageList = [i[::-1] for i in imageList]
        count = 1
        for item in imageList:
            if count != len(imageList):
                finalImage += item + "\n"
            else:
                finalImage += item
            count += 1
        return finalImage

    if degrees == 270:
        finalImage = ""
        imageList = image.split("\n")
        imageList = [i[::-1] for i in imageList]
        count = 1
        for char in range(len(imageList[0])):
            for element in imageList:
                finalImage += element[char]
            if count != len(imageList):
                finalImage += "\n"
            count += 1
        return finalImage

    if degrees == 360:
        finalImage = ""
        imageList = image.split("\n")
        imageList = [i[::-1] for i in imageList]
        count = 1
        for element in imageList:
            if count != len(imageList):
                finalImage += element + "\n"
            else:
                finalImage += element
            count += 1
        return finalImage


def convert(image, convertion_table, conv_choice):
    def find_string_with_first_char(char1, string_list):
        for string in string_list:
            if string and string[0] == char1:
                return string
        return None

    if conv_choice == 0:
        return image

    imageList = image.split("\n")
    modified_image_list = []

    for line in imageList:
        modified_line = ""
        for char in line:
            conversion = find_string_with_first_char(char, convertion_table)
            if conversion is not None:
                modified_line += conversion[conv_choice]
            else:
                modified_line += 'X'
        modified_image_list.append(modified_line)
    finalImage = "\n".join(modified_image_list)
    return finalImage


def serialize(string, rotation, conv_choice, convertion_table, to_print=False):
    def count_occurrences(input_string):
        if not input_string:
            return ""
        result = ""
        current_char = input_string[0]
        count1 = 1
        for char in input_string[1:]:
            if char == current_char:
                count1 += 1
            else:
                result += f"{count1}{current_char}"
                current_char = char
                count1 = 1
        result += f"{count1}{current_char}"
        return result

    image = rotate(string, rotation)
    image = convert(image, convertion_table, conv_choice)
    imageList = image.split("\n")
    modified_image_list = []
    for line in imageList:
        modified_line = count_occurrences(line)
        if modified_image_list and modified_image_list[-1] == modified_line:
            modified_image_list[
                -1] = f"{int(modified_image_list[-1][:-1]) + int(modified_line[:-1])}{modified_line[-1]}"
        else:
            modified_image_list.append(modified_line)

    serialized = "\n".join(modified_image_list).rstrip()
    if not to_print:
        with open("ascii.txt", "w") as file:
            file.write(serialized)
        return "ascii.txt"
    else:
        return serialized


def deserialize(string, rotation, conv_choice, conversion_table, to_print=False):
    imageList = string.split("\n")
    result = ""
    for item in imageList:
        i = 0
        while i < len(item):
            if item[i].isdigit() and i + 1 < len(item):
                count_value = int(item[i])
                i += 1
                while i < len(item) and item[i].isdigit():
                    count_value = count_value * 10 + int(item[i])
                    i += 1
                if i < len(item):
                    result += item[i] * count_value
                    i += 1
            else:
                i += 1
        result += "\n"
    result = result.rstrip("\n")
    result = convert(result, conversion_table, conv_choice)
    deserialized = rotate(result, rotation)
    if not to_print:
        with open("ascii.txt", "w") as file:
            file.write(deserialized)
        return "ascii.txt"
    else:
        return deserialized


def compress(text):
    result = []

    current_char = '0'
    result.append(0)

    for i in range(len(text)):
        if text[i] == current_char:
            result[len(result)-1] += 1
        else:
            current_char = text[i]
            result.append(1)

    return result



input = '000000111111100111000000001111'

print(compress(input))

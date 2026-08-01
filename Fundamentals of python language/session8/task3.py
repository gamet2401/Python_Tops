def reverse_message(message):
    result = ""
    i = len(message) - 1
    while i >= 0:
        result += message[i]
        i -= 1
    return result

print(reverse_message("Hello World"))

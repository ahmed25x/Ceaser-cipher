def encypt_func(txt, s):
    result = ""

    for i in range(len(txt)):
        char = txt[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 64) % 26 + 65)

        else:
            result += chr((ord(char) + s - 96) % 26 + 97)
    return result


def decrypt_func(text, x):
    result2 = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result2 += chr((ord(char) - x - 64) % 26 + 65)

        else:
            result2 += chr((ord(char) - x - 96) % 26 + 97)
    return result2


# check the above function
txt = "CEASER CIPHER EXAMPLE"
s = 7

print("Plain txt : " + txt)
print("Shift pattern : " + str(s))
print("Cipher: " + encypt_func(txt, s))

text = "Ceaser cypher decryption example"
x = 7

print("Plain text : " + text)
print("Shift pattern : " + str(x))
print("Decipher: " + decrypt_func(text, x))


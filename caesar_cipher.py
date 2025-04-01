def caesar_cipher(text):
    #this is a simple caesar cipher
    #it shifts the letters by 3
    key = 3000
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    text = text.upper()
    for char in text:
        if char in letters:
            index = (letters.index(char) + key) % 26
            result += letters[index]
        else:
            result += char    
    return result


print(caesar_cipher("i hate mathematics"))
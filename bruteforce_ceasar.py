print("Enter the secrete message")
message = input(">")
def bruteforce(text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    result = ''
    for key in range(len(letters)):
        
        for char in text:
            if char in letters:
                index = letters.index(char)
                enc = index - key
                if enc < 0:
                    enc = enc + 26
                else:
                    enc = enc   
                result += letters[enc]
            else:
                result += char    
   
    return result                 

print(bruteforce(message+"\n"))
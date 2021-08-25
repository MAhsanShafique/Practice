
def Palindrom(w):
    if w[::-1] == w:
        return True
    else:
        return False

Word = input("Enter a word: ")
print(Palindrom(Word))
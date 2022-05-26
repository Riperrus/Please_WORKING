def translate(text):
    word_ban="ёуеыаоэяиюЁУЕЫАОЭЯИЮ"
    word = ''
    for i in text:
        if i not in word_ban:
            word+=i
    return word.replace("  "," ")
word=input()
print(translate(word))
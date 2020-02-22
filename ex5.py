f = open("python.txt", "r")
words = f.read().split()
max_len = len(max(words, key=len))
for word in words:
    if len(word) > 3:
        word = word[1:] + word[0] + 'ay'

    print(word)




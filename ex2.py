consonants = "bdghjlmnpqstvwxyzBDGHJKLMNBVXZQWTP"
bad_letters = "fckr"
count1 = 0
count2 = 0
f = open("python.txt", "r")
words = f.read().split()
for word in words:
    for c in word:
        if c == 'f'or c == 'c' or c == 'k' or c == 'r':
            count1 = count1 + 1
        if c in consonants:
                count2 = count2 + 1
    if count2 > count1:
        print('καλη')
        count1 = 0
        count2 = 0

    else:
        print('κακη')
        count1 = 0
        count2 = 0















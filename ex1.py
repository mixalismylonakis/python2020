vowels = "aeyuioAEYUIO"
f = open("python.txt", "r")
my_list=[]

words = f.read().split()

for word in words:

    for ch in vowels:
            word = word.replace(ch, '') #afairei ta fwnhenta apo thn ka8e leksh
    my_list.append(word[::-1]) # tis fortwnei sthn lista anapoda
    my_list.sort(key=len)  # kanei sort apo mikritero se  megalytero
    my_list.reverse()  # kanei reverse olh thn lista



print(my_list[0:5]) #print tis 5 megalyteres lekseis







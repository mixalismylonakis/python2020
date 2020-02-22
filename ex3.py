def ex3():
    supermarket={}
    supermarket2 = []
    flag = False

    while not flag:
        name = input("Product name:\n")
        price = input("product Price:\n")
        fpa = input("Product tax:\n")
        #Δεν γνώριζα πως θα δώσει ο χρήστης το Φ.Π.Α οπότε το έβαλα σαν int
        supermarket={'product':name,'price':float(price),'fpa':int(fpa)}
        # #pπροσθέτω τα πράγματα στη λεξικό
        supermarket2.append(supermarket)
        quest = input("Do you want to add another item in your list ?\n Type 'yes'or 'no':\n")
        if quest=='yes':
            flag = False
        else:
            flag = True

    sum1 = 0
    for item in supermarket2:
        sum1=(item['price']*item['fpa']/100 +item['price']) + sum1
    print("Το συνολικό σας ποσό είναι: " ,sum1)

ex3()


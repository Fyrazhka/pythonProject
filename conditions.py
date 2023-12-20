def leapyear():
    dict={"annieBorn":1996,"janeBorn":1999}
    for key,value in dict.items():
        if value%4==0:
           print(key+ " Leap Year")
        else:
           print(key+ " Default Year")


def conteen():
    personAge=10
    if(personAge<=9):
        print("milk")
    elif(personAge>9 and personAge<15):
        print("sandwich")
    else:
        print("burger")


if __name__ == '__main__':
    leapyear()
    conteen()

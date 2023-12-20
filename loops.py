def task1():
    for i in range(-4,5):
        print (i)

def task2():
    Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
    for genre in Genres:
        print(genre)
    squares = ['red', 'yellow', 'green', 'purple', 'blue']
    for square in squares:
        print(square)

def task3():
    PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
    i=0
    while PlayListRatings[i]>6 and i<len(PlayListRatings):
        print(PlayListRatings[i])
        i+=1

def task4():
    i=0
    squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
    new_squares = []
    while squares[i]=='orange':
        new_squares.append('orange')
        i+=1
    print(new_squares)

def task5():
    t=6
    for i in range(1,11):
        print(str(t)+"*"+str(i)+"="+str(t*i))
    t=7
    for i in range(1,11):
        print(str(t)+"*"+str(i)+"="+str(t*i))
def task6():
    Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]
    newAnimal=[]
    i=0
    while len(Animals)>i:
        if(len(Animals[i])==7):
            newAnimal.append(Animals[i])
        i+=1
    print(newAnimal)

if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

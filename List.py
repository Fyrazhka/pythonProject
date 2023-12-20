def main():
    list = []
    list.extend(["Watch", "Laptop", "Shoes", "Pen", "Clothes"])
    list.append("Football")
    print(list[0])
    print(list[-1])
    print(list)
    print(list[1:3])
    list[-2] = "NoteBook"
    del (list[-1])
    print(list)

if __name__ == '__main__':
    main()
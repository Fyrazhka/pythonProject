def main():
    products={"ProductN1":"Mobile Phone","ProductN1Quantity":5,"ProductN1Price":20000,"ProductN1ReleaseYear":2020}
    ProductN2 = "Laptop"
    ProductN2Quantity = 10
    ProductN2Price = 50000
    ProductN2ReleaseYear = 2023
    products["ProductN2"]=ProductN2
    products["ProductN2Quantity"] = ProductN2Quantity
    products["ProductN2Price"] = ProductN2Price
    products["ProductN2ReleaseYear"] = ProductN2ReleaseYear

    print(products)

    print("ProductN1ReleaseYear" in products)
    print("ProductN2ReleaseYear" in products)

    del(products["ProductN1ReleaseYear"])
    del (products["ProductN2ReleaseYear"])

    print("ProductN1ReleaseYear" in products)
    print("ProductN2ReleaseYear" in products)

if __name__ == '__main__':
    main()
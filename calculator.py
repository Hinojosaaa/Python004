costumer = input("What is your name?: ")
print("Hello " + costumer + ", Welcome to our shop!")
print("This is our catalog: ")

while True:
    print("\n1. Python for Beginners --> $15.00")
    print("2. HTML and CSS --> $10.00")
    print("3. The Linux Command Line --> $20.00")
    print("4. Checkout")
    print("5. Exit")

    choice = input("\nSelect an option (1-5): ")

    if choice == "1" or choice == "2" or choice == "3":
        if choice == "1":
            title = "Python for Beginners"
            price = 15.00
        elif choice == "2":
            title = "HTML and CSS"
            price = 10.00
        else:
            title = "The Linux Command Line"
            price = 20.00

            quantity = int(input("How many copies do you want? "))
        cost = price * quantity
        total = cost + cost

        if choice == "1":
            qty_python = quantity + quantity
        elif choice == "2":
            qty_html = quantity + quantity
        else:
            qty_linux = quantity + quantity

        print(title + " x " + str(quantity) + ": $" + ("%.2f" % cost))

    elif choice == "4":
        print("\n----------YOUR RECEIPT----------")
        print("Customer: " + costumer)

        # Imprimimos solo los libros que el cliente compro (cantidad > 0)
        if qty_python > 0:
            print("Python for Beginners x " + str(qty_python) + ": $" + ("%.2f" % (qty_python * 15.00)))
        if qty_html > 0:
            print("HTML and CSS x " + str(qty_html) + ": $" + ("%.2f" % (qty_html * 10.00)))
        if qty_linux > 0:
            print("The Linux Command Line x " + str(qty_linux) + ": $" + ("%.2f" % (qty_linux * 20.00)))

        print("--------------------------------")

        
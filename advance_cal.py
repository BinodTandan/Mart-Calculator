
sum = 0
goods = ["Sugar", "Rice", "Biscutes", "Noodles", "Gram Masala", "Choclate", "Pasta", "Breed", "Chips"]
while(True):
    item = input("Enter the item: ")
    if item != "q":
        if item in goods:
            price = float(input(f"Enter the price of {item}: "))
            quantity = int(input("Enter the quantity: "))
            product = price * quantity
            print(f"The price of {item} is Rs.{product}")
            sum += product

        else:
            print("This item is not availabe in our store.\n -------Thank You!!!!!-------")
            

    else:
        print("-----Thankyou for visiting our store.-------- ")
        break


print(f"The price of all goods is Rs.{sum}")
        
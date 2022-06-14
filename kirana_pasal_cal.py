sum = 0

try:
    while(True):
        item = input("Enter the name of item: ")
        if(item!='q'):
            user = int(input("Enter the price of item: "))
            sum += user
            print(f"The price of the {item} is Rs.{user}.")

        else:
            print(f"The total cost of goods is Rs.{sum}")
            print("-----Thankyou!!-----")
            break
except Exception as e:
    pass




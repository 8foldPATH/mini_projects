order_list = [("tom", 0.87, 4), ("sug", 0.4, 3), ("ws", 0.29, 4), ("juc", 1.5, 1), ("fo", 0.8, 3), ("cat", 0.3, 5)]

names = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "juc":"Juice", "fo":"Foil", "cat":" Cat Litter Bags"}

budget = 10.00
running_total = 0

receipt = []

for item in order_list:        
    items_price = (item[2]*item[1])
    receipt += {names[item[0]]}

    if budget > items_price:
        print("-------------")
        print(f"Current budget is £{round(budget, 2)}")
        running_total += items_price
        budget -= items_price
        print(f"Adding {names[item[0]]}. Quantity: {item[2]}")
        print(f"Item price is £{item[1]} each, and £{round(items_price, 2)} for {item[2]} of them")
        print(f"Current items are: {receipt}")
        print("")
        print(f"Running total is £{round(running_total, 2)}")
        print(f"New budget is £{round(budget, 2)}")
        
    else:
        print("-------------")
        print(f"Budget exceeded! Grand total is £{running_total}")
        break
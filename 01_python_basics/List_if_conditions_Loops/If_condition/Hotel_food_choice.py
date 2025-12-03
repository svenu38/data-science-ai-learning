print("Welcome to the Food Court!")

indian_foods = ['biryani', 'paneer butter masala', 'dal makhani', 'chole bhature']
italian_foods = ['pasta', 'pizza', 'lasagna', 'risotto']
chinese_foods = ['noodles', 'fried rice', 'manchurian', 'spring rolls']

food_choice = input("Enter your food choice (indian / italian / chinese): ")

# Show list based on choice
if food_choice == "indian":
    print("Indian food menu:", indian_foods)
    item = input("Please choose a food item: ")
    if item in indian_foods:
        print("Your order will be ready soon!")
    else:
        print("Sorry, we do not have that item right now.")

elif food_choice == "italian":
    print("Italian food menu:", italian_foods)
    item = input("Please choose a food item: ")
    if item in italian_foods:
        print("Your order will be ready soon!")
    else:
        print("Sorry, we do not have that item right now.")

elif food_choice == "chinese":
    print("Chinese food menu:", chinese_foods)
    item = input("Please choose a food item: ")
    if item in chinese_foods:
        print("Your order will be ready soon!")
    else:
        print("Sorry, we do not have that item right now.")

else:
    print("Sorry, we do not have that cuisine.")






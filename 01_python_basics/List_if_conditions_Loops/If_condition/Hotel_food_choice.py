print("welcome to the food court")


indian_foods = ['biryani', 'paneer butter masala', 'dal makhani', 'chole bhature']
italian_foods = ['pasta', 'pizza', 'lasagna', 'risotto']
chinese_foods = ['noodles', 'fried rice', 'manchurian', 'spring rolls']

food_choice = input("Enter you food Choice (indian/italian/chinese): ")
if food_choice == 'indian':
    print("You have selected Indian food. Here are the options:")
    for item in indian_foods:
        print(f"- {item}")
elif food_choice == 'italian':
    print("You have selected Italian food. Here are the options:")
    for item in italian_foods:
        print(f"- {item}")
elif food_choice == 'chinese':
    print("You have selected Chinese food. Here are the options:")
    for item in chinese_foods:
        print(f"- {item}")
else:
    print("Sorry, we do not have that cuisine available.")
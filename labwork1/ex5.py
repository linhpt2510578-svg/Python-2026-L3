list = ['black', 'yellow', 'white', 'pink']
color = input("What is your favorite color? ")

if color in list:
    color_index = list.index(color)
    print(f"Your color is at index {color_index} in my list")
else:
    print("Sorry, I could not find your color")
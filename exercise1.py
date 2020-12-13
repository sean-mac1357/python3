user_input = input("HO! HO! HO!\n"
"Well Hello there, what would you like for christmas? ")
user_input2 = input("Have you been Naughty or Nice? ")


if user_input2.lower() == "nice":
    print("Since you have been good you will most definitely receive %s!" % user_input)
else:
    print("That is some concerning news, you can except to receive a lump of coal")
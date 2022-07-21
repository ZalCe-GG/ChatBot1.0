def bot():
    print(
        f"Hey {name} im Bot1.0 welcome! \n{color} is a really cool colour. ")


name = input("Hi whats your name? ")
color = input("whats your favourite colour? ")

bot()


def story():
    story = input("Would you like to hear a story? ")
    if story.lower() == ("yes"):
        print(f"Well, here i go! \nMy creator ZalCe was just 13 years old when he created me!\nhe enjoyed making me and i was only the start.")


story()
print(f"Conversation \nEnded")

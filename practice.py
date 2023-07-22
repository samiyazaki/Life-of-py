import random

def greeting_generator():
    greetings = [
        "Hello, {}! It's great to see you.",
        "Hi, {}! Hope you're having a good day.",
        "Hey, {}! What's up?",
        "Good to see you, {}! How have you been?",
        "Hello, {}! Nice to meet you."
    ]

    while True:
        user_info = []

        name = input("\nPlease enter your name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            print("Goodbye!")
            break

        random_greeting = random.choice(greetings)
        print(random_greeting.format(name))

        user_info.append(f"Name: {name}")

        color = input("What's your favorite color? ")
        user_info.append(f"Favorite Color: {color}")

        food = input("What's your favorite food? ")
        user_info.append(f"Favorite Food: {food}")

        hobby = input("What's your favorite hobby? ")
        user_info.append(f"Favorite Hobby: {hobby}")

        print("\nHere is your information:")
        for info in user_info:
            print(info)

greeting_generator()

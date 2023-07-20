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
        name = input("\nPlease enter your name (or type 'exit' to stop): ")
        
        if name.lower() == 'exit':
            print("Goodbye!")
            break

        random_greeting = random.choice(greetings)
        print(random_greeting.format(name))

greeting_generator()

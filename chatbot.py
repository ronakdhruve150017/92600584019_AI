print("Welcome to AI Chatbot")
print("Type 'YES' to chat or EXIT to 'quit'")

you = input("YOU:- ").lower()

if you == "yes":
    print("You can chat now!")

    while True:
        you = input("YOU:- ").lower()
        #if you write exit so goodbye!
        if you == "exit":
            print("BOT:- Goodbye!")
            break

        if(you=="hello"):
            print("BOT:- How are you?")
        elif(you=="fine!"):
            print("BOT:- Great to hear that! What can i help you?")
        elif you == "what is your name?":
            print("BOT:- My name is AI Chatbot.")
        elif you == "who made you?":
            print("BOT:- I was created using Python.")
        elif you == "what is python?":
            print("BOT:- Python is a popular programming language.")
        elif you == "which course?":
            print("BOT:- You have selected AI Course.")
        elif you == "what is ai?":
            print("BOT:- AI stands for Artificial Intelligence.")
        elif you == "what is your favorite color?":
            print("BOT:- I like blue!")
        elif you == "what time is it?":
            print("BOT:- Sorry, I cannot tell the current time.")
        elif you == "tell me a joke":
            print("BOT:- Why do programmers prefer Python? Because it's easy to code!")
        elif you == "thank you":
            print("BOT:- You're welcome! Have a great day.")
        elif you == "can you sing?":
            print("BOT:- I can't sing, but I can write song lyrics!")
        elif you == "who is the prime minister of india?":
            print("BOT:- The Prime Minister of India is Narendra Modi.")
#any other word write so goodbye!
else:
    print("Goodbye!")

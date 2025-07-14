
def chatbot():
    print("Welcome to basic chatbot!.(type bye to exist)/n")
    

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("chatbot: Hi!")

        elif user_input == "how are you":
            print("chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("chatbot: Goodbye!")
            break

        else:
            print("chatbot: Sorry, I didn't understand that.")
        
chatbot()


    
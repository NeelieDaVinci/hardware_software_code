def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input()
    if answer == "yes":
        print("That's good - the United States needs more coders!!")
    if answer == "no":
        print("Perhaps you will change your your mind")
    else:
        print("I dont understand?")
    print("Goodbye")

def main():
    print("Welcome to my conversation program")
    conversation()
    print("Thanks for chatting with me")

if __name__ == "__main__":
    main()

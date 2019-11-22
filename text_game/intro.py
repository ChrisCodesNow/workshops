def welcome_message():
    print("DO NOT ENTER")

def person_enters():
    person_enter = input("Are you up for a challenge? (y/n):")
    if person_enter == "y":
        return True
    else:
        return False

def show_activities():
    print("-----------------------")
    print("What you wanna do?")
    print("A. Swim with Sharks")
    print("B. Dance with Wolves")
    print("C. Sleep with Fish")

def perform_activity(chosen_option):
    if chosen_option == "A":
        url = "https://cdn.cnn.com/cnnnext/dam/assets/190728114701-shark-1-exlarge-169.jpg"
        print(url)

welcome_message()
if person_enters():
    show_activities()
    chosen_option = input("Select one: ")
    perform_activity(chosen_option)
else:
   print("come back soon!")
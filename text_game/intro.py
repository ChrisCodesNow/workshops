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

welcome_message()
if person_enters():
    show_activities()
else:
   print("come back soon!")
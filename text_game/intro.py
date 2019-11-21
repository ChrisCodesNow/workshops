def welcome_message():
    print("DO NOT ENTER")

def person_enters():
    person_enter = input("Are you up for a challenge? (y/n):")
    if person_enter == "y":
        return True
    else:
        return False

welcome_message()
if person_enters():
   print("Welcome!")
else:
   print("come back soon!")
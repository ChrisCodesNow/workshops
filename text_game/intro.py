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
        url = "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F1004792742%2F960x0.jpg%3Ffit%3Dscale"
        print(url)

welcome_message()
if person_enters():
    show_activities()
    chosen_option = input("Select one: ")
    perform_activity(chosen_option)
else:
   print("come back soon!")
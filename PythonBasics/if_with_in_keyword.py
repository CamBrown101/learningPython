# movies_watched = {"a", "b", "c"}
# user_movie = input("Enter something you've watched latley: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't seen that one.")

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == 'y':
    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1")
        print("hello")
    else:
        print("Wrong!")

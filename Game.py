import random

# # correctGuess =random.randint(1,100)
# # gameOver = True


# # while gameOver:
# #     guess = int(input("Guess a number between 1 and 100: "))
# #     if guess == correctGuess:
# #         print(f"Correct Guess, the correct answer was {correctGuess}")

# #     elif guess > correctGuess:
# #         print("Your guess is higher, please guess lower")

# #     else:
# #         print("Your guess is low, guess higher")


# correctGuess = random.randint(1, 100)
# # game_over = True
# attempts = 6
# while attempts >0 :
#     guess = int(input("Guess a figure between 1 to 100: "))
#     if guess == correctGuess:
#       print(f"Congratulations correct value is {correctGuess} in {7 - attempts + 1} attempts.  ")
#       break
    
#     elif guess > correctGuess:
#       print("Enter a lower value")
#       attempts -= 1
#     else:
#       print("Enter a bigger value")
#       attempts -= 1
#       print(f"Attempts remaining: {attempts}")
#     if attempts == 0:
#          print(f"Sorry,you didn't guess the number. The figure was {correctGuess}. ")



# correctGuess = random.randint(1, 100)
# # game_over = True
# attempts = 6
# while attempts >0 :
#     guess = int(input("Guess a figure between 1 to 100: "))
#     if guess == correctGuess:
#       print(f"Congratulations correct value is {correctGuess} in {7 - attempts + 1} attempts.  ")
#       break
    
#     elif guess > correctGuess:
#       print("Enter a lower value")
#       attempts -= 1
#     else:
#       print("Enter a bigger value")
#       attempts -= 1
#       print(f"Attempts remaining: {attempts}")
#     if attempts == 0:
#          print(f"Sorry,you didn't guess the number. The figure was {correctGuess}. ")




# correctGuess = random.randint(1, 100)
# # game_over = True
# attempts = 6
# while attempts >0 :
#     guess = int(input("Guess a figure between 1 to 100: "))
#     if guess == correctGuess:
#       print(f"Congratulations correct value is {correctGuess} in {7 - attempts + 1} attempts.  ")
#       break
    
#     elif guess > correctGuess:
#       print("Enter a lower value")
#       attempts -= 1
#     else:
#       print("Enter a bigger value")
#       attempts -= 1
#       print(f"Attempts remaining: {attempts}")
#     if attempts == 0:
#          print(f"Sorry,you didn't guess the number. The figure was {correctGuess}. ")



# def GuessGame(min, max):
#     correctGuess = random.randint(min, max)
#     print(correctGuess)
#     # game_over = True
#     attempts = 6
#     while attempts >0 :
#         guess = int(input("Guess a figure between 1 to 100: "))
#         if guess == correctGuess:
#             print(f"Congratulations correct value is {correctGuess} in {7 - attempts + 1} attempts.  ")
#             break
        
#         elif guess > correctGuess:
#             print("Enter a lower value")
#             attempts -= 1
#         else:
#             print("Enter a bigger value")
#             attempts -= 1
#             print(f"Attempts remaining: {attempts}")
#     if attempts == 0:
#         print(f"Sorry,you didn't guess the number. The figure was {correctGuess}. ")


# # GuessGame(50,90)





# def calculator(num1, num2, operation):
#     if operation == "divide":

#         if num2 == 0:
#             print("Error")
#         else:
#             return (num1/num2)


#     if 10%2 == 0 and 9%3==1:
#         print("yes all is true")
#     else:
#         print("false")

    


# print(calculator(0,2, "divide"))




# letter = [1,3,"how are yoy"]

# NUMBER = [1]

mylist = list(range(1,50))

print(mylist[3:-1:1])

# me = "hello world"

# print(me[0])

# print(len(me))

# print(list(me))


# myclass = ["Bene", "Sonia", "Bless", "Emmanuella", "Sarah", "Rufina"]
# print(myclass[1])

# for index,names in enumerate(myclass):
#     print(index, names) 

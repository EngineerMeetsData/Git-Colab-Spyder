
name = input("Enter your name:\n")
name = name.title()
print("Hey,",name+"!\n")
message = "Start answering the quiz. Hope you'll enjoy!"
print(message)

score = 0
score = int(score)

Question_1 = "\n1. What city is considered as the Queen City of the South?\n"
Choices_1 = "a. Quezon Province\nb. Cebu City\nc. Davao City\nd. Bacolod City\n"
print(Question_1)
print(Choices_1)

Choices_1 = input("\n")

if Choices_1 == 'b':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")

message = "\nProceed to the next question.\n"
print(message)

Question_2 = "2.Where is Mayon volcano located?\n"
Choices_2 = "a. Albay\nb. Tagaytay\nc. Sorsogon\nd. Agusan Del Norte\n"
print(Question_2)
print(Choices_2)

Choices_2 = input("\n")

if Choices_2 == 'a':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")

message = "\nProceed to the next question.\n"
print(message)


Question_3 = "3.It is famous for its delicious Durian fruit.\n"
Choices_3 = "a. Albay\nb. Tagaytay\nc. Sorsogon\nd. Davao City\n"
print(Question_3)
print(Choices_3)

Choices_3 = input("\n")

if Choices_3 == 'd':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")

message = "\nProceed to the next question.\n"
print(message)


Question_4 = "4.A city known for the Masskara Festival.\n"
Choices_4 = "a. Albay\nb. Quezon City\nc. Bacolod City\nd. Davao City\n"
print(Question_4)
print(Choices_4)

Choices_4 = input("\n")

if Choices_4 == 'c':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")


message = "\nProceed to the next question.\n"
print(message)


Question_5 = "5.Where is the smallest volcano in the Philippines located?.\n"
Choices_5 = "a. Albay\nb. Tagaytay City\nc. Bacolod City\nd. Davao City\n"
print(Question_5)
print(Choices_5)

Choices_5 = input("\n")

if Choices_5 == 'b':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")


message = "\nProceed to the next question.\n"
print(message)


Question_6 = "6.Where is Mines View Park located?.\n"
Choices_6 = "a. Benguet\nb. Baguio City\nc. Batanes\nd. Ilocos Norte\n"
print(Question_6)
print(Choices_6)

Choices_6 = input("\n")

if Choices_6 == 'b':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")


message = "\nProceed to the next question.\n"
print(message)


Question_7 = "7.What is the National Flower of the Philippines?.\n"
Choices_7 = "a. Sampaguita\nb. Rose\nc. Gumamela \nd. Sunflower\n"
print(Question_7)
print(Choices_7)

Choices_7 = input("\n")

if Choices_7 == 'a':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")


message = "\nProceed to the next question.\n"
print(message)


Question_8 = "8.The city known for its Pahiyas Festival is -\n"
Choices_8 = "a. Antipolo\nb. Tanay\nc. Lucban \nd. Sariaya\n"
print(Question_8)
print(Choices_8)

Choices_8 = input("\n")

if Choices_8 == 'c':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")

message = "\nProceed to the next question.\n"
print(message)


Question_9 = "9.What is considered as the famous delicacy of Laguna?\n"
Choices_9 = "a. Chicharon\nb. Napoleones\nc. Piaya \nd. Buko Pie\n"
print(Question_9)
print(Choices_9)

Choices_9 = input("\n")

if Choices_9 == 'd':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")

message = "\nProceed to the next question.\n"
print(message)


Question_10 = "10.Known as the Surfing Capital of the Philippines.\n"
Choices_10 = "a. Leyte\nb. Samar\nc. Siargao \nd. Ilocos Sur\n"
print(Question_10)
print(Choices_10)

Choices_10 = input("\n")

if Choices_10 == 'c':
    print("\nGood job! You got the right answer!\n")
    score = score + 1
else:
    print("\nSorry,you chose the incorrect answer.\n")

print("Your Total score is " + str(score) + " out of 10")

grade = int((score/10)*100)
if grade >= 70:
  print("You passed the quiz! Congratulations!\n")
else:
  print("Better luck next time.\n")


import random

name = "You"
question = "Will I win the Lottery?"
answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes - definately."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again Later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " ask: " + question)

if question == "":
  print("No question was asked.")
else:
  print("Magic 8-Ball's answer: " + answer)
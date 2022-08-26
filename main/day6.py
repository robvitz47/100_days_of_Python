#variables
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

gradebook = [
  ["physics", 98],  ["calculus", 97], ["poetry", 85],  ["history", 88],
]
#add computer science grade
gradebook.append(["computer science", 100])
#add visual arts grade
gradebook.append(["visual arts", 93])
#add 5 points extra credit to visual arts
gradebook[-1][-1] = 93 + 5
#change grades to pass/fail
gradebook[0].remove(98)
gradebook[1].remove(97)
gradebook[2].remove(85)
gradebook[3].remove(88)
gradebook[4].remove(100)
gradebook[5].remove(98)
gradebook[2].append("Pass")
#add both gradebooks
full_gradebook = last_semester_gradebook + gradebook
#print results
print(full_gradebook)
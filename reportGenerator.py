#Student report card generator
#name = input(print("Please enter your name: "))

#print("Hello there " , name)



#funtions
def calcAve(average):
  return sum(average)/len(average)

#name  = 'Tishetso'

name = input("Please enter your name: ")
marks = []
subjects = []

print()
print(f"Hello there {name}!!")

print()
print("We welcome you to the system👋👋👋")
print()

print("-" * 50)
print("You will be required to enter your subjects and their scores. A report will be generated for you.")
print("-" * 50)

#input from user
print()
numSubject = int(input("Please enter the number of subjects you have: "))
print()

print("Please enter the Subject name and the Score of each subject")
print()

for i in range(numSubject):
  subjects.append(input("Enter the subject name: " ))
  print()
  marks.append(int(input("Enter the mark for the subject: " )))
  print()


print()
#function call
ave = calcAve(marks)

print()
print("-" * 25)
print("Here is your report card")
print("-" * 25)
print()


print(f"{'Subjects':<20} {'Marks':<10}")

print("-" * 50)
for i in range(len(marks)):
  print(f"{subjects[i]:<20} {marks[i]:<10}")

print()
print("-" * 50)
print('\n')

if ave >=75:
  print( name + ", Your average is "+ str(ave) + "!! You have passed with a distinction, Congratulations!!!")
elif ave >= 50:
  print( name + ", Your average is "+ str(ave) + '!! Congratulations!!!')
else:
  print( name + ", Your average is "+ str(ave) + "!! Better luck next time!!!")
print()
print("-" * 50)
  


#print("Greetings there")
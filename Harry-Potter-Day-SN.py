print("Harry Potter Day: Hogwarts House Quiz \nby SN'23")

from IPython.display import Image,  clear_output

!wget https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/original/products/88363/91130/Harry-Potter-Ravenclaw-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__86173.1507640763.jpg?c=2&imbypass=on
!mv Harry-Potter-Ravenclaw-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__86173.1507640763.jpg?c=2 ravenclaw.png

!wget https://i.pinimg.com/originals/14/16/dd/1416dd9008fa632ab367dffc804e9ce4.jpg
!mv 1416dd9008fa632ab367dffc804e9ce4.jpg gryffindor.jpg

!wget https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/original/products/88362/91127/Harry-Potter-Slytherin-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__31920.1507640497.jpg?c=2&imbypass=on
!mv Harry-Potter-Slytherin-Crest-Official-wall-mounted-cardboard-cutout-buy-now-at-star__31920.1507640497.jpg?c=2 slytherin.jpg

!wget https://i.pinimg.com/originals/27/a2/24/27a2243b7476ce34784a7a492f860187.jpg
!mv 27a2243b7476ce34784a7a492f860187.jpg hufflepuff.jpg

clear_output()

import random
house = ['slytherin.jpg', 'hufflepuff.jpg', 'gryffindor.jpg', 'ravenclaw.png']

def score_counter(question,slytherin,hufflepuff,gryffindor,ravenclaw):
  
  #slytherin = 0
  if question == "A":
    slytherin = slytherin + 1

 #hufflepuff = 0
  if question == "B":
    hufflepuff = hufflepuff + 1

  #gryffindor = 0
  if question == "C":
    gryffindor = gryffindor + 1

  #ravenclaw = 0 
  if question == "D":
    ravenclaw = ravenclaw + 1

 #print(hufflepuff,slytherin,gryffindor,ravenclaw)  
  return (slytherin,hufflepuff,gryffindor,ravenclaw)


slytherin = 0
hufflepuff = 0
gryffindor = 0
ravenclaw = 0

quiz = "Welcome to the Hogwarts House Quiz!"
print(quiz)
print("\n")
name = input("Enter your name: ")
print("Hello and welcome to Hogwarts "+name+ "!")
print("\n")
openingstatement = ("Let's get you sorted into your house shall we?")
print(openingstatement)
print("\n")

rules = ("Make sure you write the answer in a capital letter!" + "\n" + "Use the keyboard to type in your answers as well." + "\n" + " Have fun and enjoy the test! :)")
print(rules)
print("\n")

Q1 = ("Q1: Which class would you like to take at Hogwarts? " + "\n" + " A.Potions" + "\n" + " B.Charms" + "\n" + " C.Defense Against the Darks Arts " + "\n" + " D.History of Magic" +"\n")

Q2 = ("Q2: Which extracurricular activity would you like to take at Hogwarts?"+ "\n" + " A.Duelling Club" + "\n" + " B.Wizard Card Collectors' Club" + "\n" + " C.Quidditch" + "\n" + " D.Astronomy Club" + "\n")

Q3 = ("Q3: Which animal would you like for your pet?" + "\n" + " A.Cat" + "\n" + " B.Rat" + "\n" + " C.Frog" + "\n" + " D.Owl" + "\n")

Q4 = ("Q4: When relaxing in your house commons, how would you spending your time?" + "\n" + " A.Casting trick spells on other students." + "\n" + " B.Baking Sweets" + "\n" + " C.Training For The TriWizard Tournement " + "\n" + " D.Playing Wizards Chess" +"\n")

Q5 = ("Q5: Which Harry Potter dish would you like to try the most?" + "\n" + " A.Sherbert Lemon" + "\n" " B.Knickerbocker Glory" + "\n" + " C.Cauldron Cakes" + "\n" + " D.Bouillabaisse" + "\n")

Q6 = ("Q6: How would you open a locked door?" + "\n" + " A.Pick the lock" + "\n" + " B.Knock" + "\n" + " C.Kick the door down" + "\n" + " D.Find the key")

Q7 = ("Q7: What would you do if someone lost something and you knew where it was?" + "\n" + " A.Don't tell them, it's their fault not yours" + "\n" + " B.Tell them, no one deserves to be in the dark" + "\n" + " C.Help them find it, it can be an adventure" + "\n" + " D.Why should I care?" + "\n")

Q8 = ("Q8: I would rather be friends wtih..." + "\n" + " A.Tom Riddle" + "\n" + " B.Neville Longbottom" + "\n" + " C.Hermione Granger" + "\n" + " D.Luna Lovegood" + "\n")

Q9 = ("Q9: Who is your favorite villian?" + "\n" + " A.Bellatrix Lestrange" +"\n" + " B.Karkus Bulstrode" + "\n" + " C.Peter Pettigrew" + "\n" + " D.Gilderoy Lockhart" + "\n")

Q10 = ("Q10: What house do YOU think you belong in?" + "\n" + " A.Slytherin" + "\n" + " B.Hufflepuff" + "\n" + " C.Gryffindor" + "\n" + " D.Ravenclaw" + "\n")

Question_List = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]
x = 0
for x in range(10):
  Question_List[x]
  print(Question_List[x])
  answer = input()
  score = score_counter(answer,slytherin,hufflepuff,gryffindor,ravenclaw)
  slytherin = score[0]
  hufflepuff = score[1]
  gryffindor = score[2]
  ravenclaw = score[3]
  #print(score_counter(slytherin,hufflepuff,gryffindor,ravenclaw))
  print(slytherin,hufflepuff,gryffindor,ravenclaw)
  print("\n")

if slytherin > hufflepuff and slytherin > ravenclaw and slytherin > gryffindor:
  print ("Congratulations! You've been sorted into Slytherin.")
  i=0

if hufflepuff > slytherin and hufflepuff > ravenclaw and hufflepuff > gryffindor:
  print ("Congratulations! You've been sorted into Hufflepuff.")
  i=1

if gryffindor > slytherin and gryffindor > ravenclaw and gryffindor > ravenclaw:
  print ("Congratulations! You've been sorted into Gryffindor.")
  i=2

if ravenclaw > slytherin and ravenclaw > gryffindor and ravenclaw > hufflepuff:
  print ("Congratulations! You've been sorted into Ravenclaw.")
  i=3

Image(house[i], height=200, width=200)

def main():
    global sys
    import sys
    global time
    import time
    global score
    score = 0
    print("Loading Quiz")
    time.sleep(0.4)
    print("10%")
    time.sleep(0.4)
    print("20%")
    time.sleep(0.4)
    print("30%")
    time.sleep(0.4)
    print("40%")
    time.sleep(0.4)
    print("50%")
    time.sleep(0.4)
    print("60%")
    time.sleep(0.4)
    print("70%")
    time.sleep(0.4)
    print("80%")
    time.sleep(0.4)
    print("90%")
    time.sleep(0.4)
    print("100%")
    time.sleep(0.4)
    print("Loading Compleat")

    time.sleep(1.5)
    print("Welcome To The Quiz!")
    time.sleep(1.5)
    begin = input("would you like to take the quiz?.\n")
    if begin == "yes":
        print("Awsome lets get started")
    else:
        print("Well that sucks")
        time.sleep(0.5)
        print("Terminating program")
        sys.exit()
    time.sleep(1.5)
    name = input("First off lets get your name.\n")
    print("Hello, {}".format(name))
    time.sleep(1.5)
    print("Ok lets get this started....")
    time.sleep(1.5)
    print("What category would you like")
    time.sleep(1.0)
    print("A, Animals")
    type = input("B, Food.\n")
    if type == "A":
       animal_quiz()
    if type == "B":
        food_quiz()

def animal_quiz():
    global score
    print("Animals it is")
    time.sleep(1.5)
    print("Question 1")
    time.sleep(1.5)
    print("What is animal likes to climb trees")
    time.sleep(1.0)
    print("A. Cat")
    print("B. squirrel")
    question1 = input("C. Llama.\n")
    if question1 == "B":
        print("Correct!")
        score = score + 1
        time.sleep(1.5)
        print("Current score is {}".format(score))      
    else:
        print("Wrong")
        score = score + 0
        print("Current score is {}".format(score))
    time.sleep(1.5)
    print("Question 2")
    time.sleep(1.5)
    print("What animal has a long neck")
    time.sleep(1.0)
    print("A. Frog")
    print("B. Giraffe")
    question2 = input("C. Toad.\n")
    if question2 == "B":
        print("Correct!")
        score = score + 1
        print("Current score is {}".format(score))
    else:
        print("Wrong")
        score = score + 0
        print("Current score is {}".format(score))
    print("Question 3")
    time.sleep(1.5)
    print("What animal has wings")
    time.sleep(1.0)
    print("A. Frog")
    print("B. Tiger")
    question3 = input("C. Bird.\n")
    if question3 == "C":
        print("Correct!")
        score = score + 1
        time.sleep(1.5)
        print("Current score is {}".format(score))
    else:
        print("Wrong")
        score = score + 0
        print("Current score is {}".format(score))
        time.sleep(1.5)
    End()




def food_quiz():
    global score
    print("Food quiz it is")
    time.sleep(1.5)
    print("Question 1")
    time.sleep(1.5)
    print("What food comes from an chicken")
    time.sleep(1.0)
    print("A, Egg")
    print("B, Steak")
    foodquestion1 = input("C, Bacon.\n")
    if foodquestion1 == "A" or "a":
        print("Correct")
        score = score + 1
        print("Current score is {}".format(score))
        time.sleep(1.5)
    else:
        print("Wrong")
        score = score + 0
        print("Current score is {}".format(score))
    print("Question 2")
    time.sleep(1.5)
    print("What fruit grows on a tree")
    time.sleep(1.0)
    print("A, Apple")
    print("B, Grapes")
    foodquestion2 = input("C, Blue Berries.\n")
    if foodquestion2 == "A":
        print("Correct")
        score = score + 1
        print("Current score is {}".format(score))
        time.sleep(1.5)
    else:
        print("Wrong")
        score = score + 0
        print("Current score is {}".format(score))
        time.sleep(1.5)
    print("Question 3")
    time.sleep(1.5)
    print("What is the worst tasting food out of the selection")
    time.sleep(1.0)
    print("A, Eggs")
    print("B, Bacon")
    foodquestion3 = input("C, Steak.\n")
    if foodquestion3 == "A":
        print("Correct!")
        score = score + 1
        print("Current score is {}".format(score))
        time.sleep(1.5)
    else:
        print("Wrong")
        score = score + 0
        print("Current score is {}".format(score))
        time.sleep(1.5)
    End()



def End():
    global score
    time.sleep(1.0)
    if score == 2 or 3:
        print("Congrats you finished the test with a score of {}".format(score))
    else:
        print("Well that sucks you finished the quiz with a score of {}".format(score))
    

if __name__ == "__main__": main()

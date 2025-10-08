#Building quiz using if statements and all commands we have thus learnt about
from question_class import Question 

question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", 
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n" 
] #Creating data type for question prompts to use to use in another file of question class

questions = [ 
    Question(question_prompts[0], "a"), 
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
      ] #Here we are creating three questions with three question prompts and each have a different answer 

#Next, we create a function that will run the test 

def run_test(questions): 
    score = 0
    for question in questions: #creating a loop function that will loop through all the questions in that questions array/list
        answer = input(question.prompt) 
        if answer == question.answer: #Checking to see if the answer that the student gave is equal to answer I inputed in the questions array
            score += 1 
    print("You got" + str(score) +"/" + str(len(questions)) + "correct")
run_test(questions)

       
        
         
        
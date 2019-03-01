#Protein Intake Calculator
#Python version 3.7.2
import time

print('''Hello, I am new to programming and wanted to create an exercise.
We are going to calculate the amount of protein you need to consume based on
your goals. You must be 14 years or older to participate.
Please select from the following fitness goals:
1. Bulking and Strength Conditioning
2. Cutting and Aerobic Conditioning
''')
#User inputs their fitness goal
fitness_goal_text = input('Please enter the fitness goal you want: ')
fitness_goal = int(fitness_goal_text)
#User inputs their age
age_number_text = input('Please enter your age: ')
age_number = int(age_number_text)

if fitness_goal == 1:
    print('You have selected Bulking and Strength Conditioning') 
    if age_number <14: #age verification
        print('you are not old enough to participate in this exercise.')
    else:
        print('you are old enough to participate.')
    #set variable for weight input
    bulk = float(input('Please enter your current weight in pounds: '))
    #function for bulk equation
    def bulking_routine(bulk):
        equation = ((bulk/2.2)*2.3)
        round_equation = round(equation, 2)
        return (f'you must consume {round_equation} grams of protein to achieve your goals'.format(round_equation))
    #prints users protein goals    
    print(bulking_routine(bulk)) 
    
if fitness_goal == 2:
    print('You have selected Cutting and Aerobic Conditioning.')
    if age_number <14:
        print('you are not old enough to participate in this exercise.')
    else:
        print('you are old enough to participate.')
    #set variable for weight input    
    cut = float(input('Please enter your current weight in pounds: '))
    #function for cut equation
    def cutting_routine(cut):
        equation = ((cut/2.2)*1.2)
        round_equation = round(equation, 2)
        return (f'you must consume {round_equation} grams of protein to achieve your goals'.format(round_equation))
    #prints users protein goals    
    print(cutting_routine(cut))
    

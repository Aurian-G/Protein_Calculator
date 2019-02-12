#Protein Intake Calculator

import time

print('''Hello, I am new to programming and wanted to create an exercise.

We are going to calculate the amount of protein you need to consume based on
your goals. You must be 14 years or older to participate.

Please select from the following fitness goals:

1. Bulking and Strength Conditioning
2. Cutting and Aerobic Conditioning
''')

fitness_goal_text = input('Please enter the fitness goal you want: ')
fitness_goal = int(fitness_goal_text)

age_number_text = input('Please enter your age: ')
age_number = int(age_number_text)

if fitness_goal == 1:
    time.sleep(1)
    print('You have selected Bulking and Strength Conditioning')
    time.sleep(0.5)
    if age_number < 14:
        print('You are not old enough to participate in this exercise.')
    else:
        time.sleep(1)
        print('You are old enough to participate.')
        time.sleep(1)
        weight_text = input('Please enter your current weight in pounds: ')
        weight = float(weight_text)
        protein_formula_bulking = round(float((weight/2.2)*2.3), 2)
        time.sleep(1)
        print('Thinking...')
        time.sleep(2)
        print('You need to consume', protein_formula_bulking, 'grams of protein to achieve your goals.')

if fitness_goal == 2:
    time.sleep(1)
    print('You have selected Cutting and Aerobic Conditioning.')
    time.sleep(2)
    if age_number <=14:
        print('You are not old enough to participate.')
    else:
        time.sleep(1)
        print('You are old enough to participate in this exercise.')
        time.sleep(1)
        weight_text = input('Please enter your current weight in pounds: ')
        weight = float(weight_text)
        protein_formula_cutting = round(float((weight/2.2))*1.2), 2)
        time.sleep(1)
        print('Thinking...')
        time.sleep(2)
        print('You need to consume', protein_formula_cutting, 'grams of protein to achieve your goals.')






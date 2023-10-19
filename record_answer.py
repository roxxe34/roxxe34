#!/usr/bin/python3
# Python Code to check my AWS practice exams answers and correct them and give a final score

# Read Correct Answers File and store the answers in correct.txt to use later
import os
with open('answers.txt', 'r') as r:
    with open('correct.txt', 'w') as w:
        for line in r:
            if 'Answer' in line:
                w.write(line)
# Remove the last newline character in the 'correct.txt' file
with open('correct.txt', 'rb+') as correct_file:
    correct_file.seek(-1, os.SEEK_END)
    last_char = correct_file.read(1)
    if last_char == b'\n':
        correct_file.seek(-1, os.SEEK_END)
        correct_file.truncate()
i = 1
resultat = 0  # Initialize the score variable
incorrect = []  # Initialize a list to store incorrect question numbers

# Open the 'correct.txt' file to read answers and evaluate user input
with open('correct.txt', 'r') as r:
    for line in r:
        if ',' in line:
            # Multiple-answer question
            print(f'Question N {i}(Select Two): ', end='')
        else:
            # Single-answer question
            print(f'Question N {i}: ', end='')
        check_input = input()
        listed = list(check_input)

        # Construct the user's answer string
        if len(listed) > 1:
            answer = f'Answer: ' + listed[0] + ', ' + listed[1]
        else:
            answer = f'Answer: ' + listed[0]

        # Check if the user's answer matches the correct answer
        if answer.strip() == line.strip():
            resultat += 1  # Increment the score for correct answers
        else:
            incorrect.append(f'Q{i}')  # Add incorrect question number to the list
        i += 1  # Increment the question number

# Print the list of incorrect questions and the final score
print(f'Your Final Score is {resultat * 1.54}%')
print('Incorrect answers are: ', end='')
print(f"-".join(incorrect))
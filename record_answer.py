#!/usr/bin/python3
i = 1
resultat = 0
incorrect = []
with open('correct.txt', 'r') as r:
    for line in r:
        if ',' in line:
            print(f'Question N {i}(Select Two): ', end='')
        else:
            print(f'Question N {i}: ', end='')
        check_input = input()
        listed = list(check_input)
        if len(listed) > 1:
            answer = f'Answer: ' + listed[0] + ', ' + listed[1]
        else:
            answer = f'Answer: ' + listed[0]
        if answer.strip() == line.strip():
            resultat += 1
        else:
            incorrect.append(f'Q{i}')
        i += 1
print("-".join(incorrect))
print(f'Your Finale Score is {resultat * 1.54}%')
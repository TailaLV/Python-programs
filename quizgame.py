print('Welcoe to my compute quiz')
print('######################################')

playing = input('Do you want to play?')

if playing != 'yes':
    quit()

print('Okay, Lets play ')
score = 0
print('################################')


answer = input('What does CPU stand for? ')
if answer == 'Central processing unit':
    print('Correct!')
    score += 1
    
else:
 print('Incorrect!')

answer = input('What does GPU stand for? ')
if answer == 'Graphics processing unit':
    print('Correct!')
    score +=1

else:
 print('Incorrect!')

answer = input('What does RAM stand for? ')
if answer == 'Random Acess Memory':
    print('Correct!')
    score += 1

else:
 print('Incorrect!')

answer = input('What does PSU stand for? ')
if answer == 'Power Supply':
    print('Correct!')
    score += 1
else:
 print('Incorrect!')

print('You got ' + str(score) + ' questions correct')
 
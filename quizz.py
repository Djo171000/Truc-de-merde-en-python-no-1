score = 0
print('Bonjour et bienvenue dans ce quizz ')
print('pour commencer, donnez moi vos prénom')
Nom = input()
print('très bien '+Nom+' commencons le quizz!')
print()
print('QUESTION N°1')
print('quel est le nom de ce programme?')
if input() == 'quizz':
    print('Bonne réponse')
    score = score + 1
else:
    print('mauvaise réponse')
print()
print('QUESTION N°2')
print('quel est le prénom du programmeur qui a crée ce programme?')
if input() == 'David':
    print('Bonne réponse')
    score = score + 1
else:
    print('mauvaise réponse')
print()
print('QUESTION N°3')
print('Quelle est le nom du logiciel que utilise ce programme?')
if input() == 'Python':
     print('Bonne réponse')
     score = score + 1
else:
    print('Mauvaise réponse')
print()
print('tu as ' + str(int(score)) + ' points')
if score == 3 :
    print('Felicitations')
elif score == 2 :
    print('Bien joué')
elif score == 1 :
    print('Vous pouvez faire mieux')
elif score == 0 :
    print('Ressayez encore')
input()

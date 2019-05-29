import random

nephTest = {'please select all the factor increase Na,Cl reabsorption:\n1)low AngII in PCT), 2)Dopamine, 3)insulin, 4)PTH in PCT, \n5)PTH in TAL, 6)Glucorticoid, 7)High AngII in PCT, 8)AVP, \n9)calcitonin, 10)PGE2, 11)Endothelin, 12)Bradykinin, \n13)ANP, 14)platelet-activating factor, \n14)alpha 2 adrrenergic agonist, 15)mineralocorticoids \n': '1,3,5,6,8,9,15',
            }


def list_all_disease():
    print('Your word list:\n')
    for key, value in nephTest.items():
        print('{} -> {}'.format(key, value))


def create_exam_paper():
    exam_paper = set()
    for key, value in nephTest.items():
        while len(exam_paper)<1:
            exam_paper.add(random.choice(list(nephTest.items())))
    exam_paper_dict = dict(exam_paper)
    return exam_paper_dict


def test_yourself():
    quit_the_test = False
    points = 0
    incorrect_gene_list = []
    exam_paper_dict = create_exam_paper()
    for key, value in exam_paper_dict.items():
        while True:
            answer = input('\nWhich gene mutation result of the disease? [p]ass, [q]uit\n{}'.format(key))
            if answer == 'p':
                print('The correct answer is {}'.format(value))
                incorrect_gene_list.append(key)
                break
            elif answer == 'q':
                quit_the_test = True
                break
            elif answer == value:
                points +=1
                print('Correct!')
                break
            else:
                print('It\'s not correct' )

        if quit_the_test == True:
            break

    print('\nScore: {}/{}'.format(points, len(exam_paper_dict)))
    print('Incorrect word list: ')
    for key in incorrect_gene_list:
        value = exam_paper_dict[key]
        print('{} ({})'.format(key, value))

    if points < 2:
        print('The brain is a good organ, but not everyone has it, right?')
    elif points >=2 and points <4 :
        print('The weather is good, right!')
    elif points >=4 and points<6 :
        print('Do more effort, you can do it!')
    elif points >=6 and points<8 :
        print('It\'s the last mile, you need to walk')
    elif points >= 8:
        print('It\'s time to fight!!!')


def run():
    while True:
        cmd = input("""\nWelcome to my Gene dictionary
        1)Test your self!
        2)List all disease
        3)Exit
        4)Help\n""")
        if cmd == '1':
            test_yourself()
        if cmd == '2':
            list_all_disease()
        if cmd == '3':
            break
        if cmd == '4':
            print('If you have any question, please write an email to \nchiehandlu@gmail.com\nMaybe i will help you XD')

run()
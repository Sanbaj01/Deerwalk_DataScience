# ram 82, shyam 65, hari 43, gita 23
# if name in dictionary
# grade >= 80 distinction
# grade >= 60 and < 80 first division
# grade >= 50 and < 60 second division
# grade < 50 Mom's flying chappal received

grades = {'ram':56, 'shyam':78, 'hari':89, 'krishna':77, 'sita':49}

i = 1
while i > 0:
    name = input('Enter name - ').lower()
    if name in grades:
        if grades[name] >= 80 :
            print(f'Hi {name.capitalize()}, you got distinction with {grades[name]} grades.')
        elif grades[name] >= 60:  # 60 <= grades[name] <80  no need
            print(f'Hi {name.capitalize()}, you got first division with {grades[name]} grades.')
        elif grades[name] >= 50:  # 50 <= grades[name] <60
            print(f'Hi {name.capitalize()}, you got second division with {grades[name]} grades.')
        elif grades[name] < 50:
            print(f"Hi {name.capitalize()}, you got Mom's flying chappal.")
    else:
        print('The name does not exist')
    
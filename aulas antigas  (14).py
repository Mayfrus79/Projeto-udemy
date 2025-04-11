
while True:
    try:
        age = int(input('Enter your age here: '))
        if age <= 0:
            print('Your age can not be less than 1!')
        elif age <= 9:
            print('You are a child!')
        elif age <= 17:
            print('You are a teenager!')
        elif age <= 21:
            print('You are a young adult!')
        elif age <= 60:
            print('You are adult!')
        else: 
            print('You are too old!')
        continue
    except ValueError:   
        print('You have to enter a number!')  









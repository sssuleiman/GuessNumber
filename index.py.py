import random
print ('welcome to guess a number game')
def guess(x):
    random_number = random.randint (1,x)
    guess = 0
    tries =1 
    while guess != random_number:
        if tries==4:
            break
        else:
            guess = int (input( f"guess a number between 1 and {x}: "))
            if guess < random_number:
                print( "sorry guess again. too low")
            elif guess > random_number:
                print ( 'sorry guess again. is too high')
        tries+=1
    if guess != random_number:
        print(f' you loose corect answer is {random_number}')
    else:
        print(f' yaah, congrats. You have guessed the number {random_number} ')
    
guess(100)
import turtle

pen = turtle.Turtle()

print("welcome AROB to your quiz game !!")
print('first of all, congrats queen of chess! and also congrats in your graduation <3')
print('because of this occasions i made a little test for you.')

score = 0
question_no = 0
playing = input('SO, Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}.which player starts first in chess? The one with white or black pieces?').lower()
    if ques == 'white':
        score += 1
        print('correct Robi! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> White')

    # ------1
    question_no += 1
    ques = input(f'\n{question_no}. How many squares does a chessboard have? ').lower()

    if ques == '64':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> 64')

    # -----2
    question_no += 1
    ques = input(f'\n{question_no}. What is it called when a player cant defend an attack against their king? ').lower()

    if ques == 'checkmate':
        score += 1
        print('correct queeen! you got 1 point')

    else:
        print('Incorrect!')
        print(f'current answer is --> checkmate')

    # -----3
    question_no += 1
    ques = input(f'\n{question_no}. Now, how many years weve known each other? ').lower()

    if ques == '14':
        score += 1
        print('correct! you got 1 point')

    else:
        print('!!!!!!!!!!Incorrect!!!!!!!!!!')
        print(f'current answer is -->  14  :<')

    # -----4
    question_no += 1
    ques = input(f'\n{question_no}. something we always want to be ').lower()

    if ques == 'rich':
        score += 1
        print('correct! you got 1 point')

    else:
        print('ARE YOU KIDDING ME???? Incorrect!')
        print(f'current answer is --> RICH! dah')


# ------5

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def heart():
    pen.fillcolor('pink')

    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()


# Defining method to write text
def txt():
    # Move turtle to air
    pen.up()

    # Move turtle to a given position
    pen.setpos(-68, 95)

    # Move the turtle to the ground
    pen.down()

    pen.color('black')

    # Write the specified text in
    # specified font style and size
    pen.write("CONGRATS AROBI", font=(
        "Verdana", 11, "bold"))


# Draw a heart
heart()

# Write text
txt()
# To hide turtle
pen.ht()
turtle.done()

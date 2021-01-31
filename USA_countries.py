import pandas as pd
import turtle, os
from os import path

states = pd.read_csv('us-states-game-start//us-states-game-start//50_states.csv')
all_states = states.state.to_list()

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'us-states-game-start//us-states-game-start//blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

if path.exists('guessed_state.csv'):
    guessed_state = pd.read_csv('guessed_state.csv')
    print(guessed_state['values'])
    guessed_state = guessed_state['values'].to_list()
    for s in guessed_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == s]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(s)

else:
    guessed_state = []


while len(guessed_state)<50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 Guessed', prompt="What's another state?").title()

    if answer_state == 'Exit':
        df = pd.DataFrame(guessed_state, columns=['values'])
        df.to_csv('guessed_state.csv')
        break
    if answer_state == 'Reset':
        if path.exists('guessed_state.csv'):
            os.remove('guessed_state.csv')
            break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




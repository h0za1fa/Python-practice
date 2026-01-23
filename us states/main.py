import turtle as tr
import pandas as pd

states_data = pd.read_csv('50_states.csv')
tim = tr.Turtle()
tim.penup()
tim.ht()
screen = tr.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
tr.shape(image)
total_ans = 0

state_list = states_data['state'].to_list()
guessed_states = []
# not_guessed_states = []


game_on = True
while total_ans <= 50 :
    
    ans_state = screen.textinput(title = 'Enter state name', prompt = 'Write the name of a state').title()
    
    if ans_state == 'Exit':
        # for state in state_list :
        #     if state not in guessed_states :
        #         not_guessed_states.append(state)
        not_guessed_states = [state for state in state_list if state not in guessed_states]
        break
    
    
    if ans_state in state_list and ans_state not in guessed_states :
    
        state_pos = states_data[states_data['state'] == ans_state]
        x_pos = int(state_pos['x'])
        y_pos = int(state_pos['y'])
        tim.goto(x_pos,y_pos)
        tim.write(ans_state, False, 'center', ('Ariel',8,'normal'))
        guessed_states.append(ans_state)
        total_ans +=1
        
states_to_learn = pd.DataFrame(not_guessed_states, columns = ['states'] )
states_to_learn.to_csv('us states/states_to_learn.csv')
screen.mainloop()
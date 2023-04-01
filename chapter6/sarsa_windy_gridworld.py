import numpy as np
import random

class WindyGridWorld:
    def __init__(self, rows, cols, wind):
        self.rows = rows
        self.cols = cols
        self.wind = wind
        self.start = (3, 0)
        self.goal = (3, 7)
 
    def move(self, state, action):
        row, col = state
        if action == 0:  # up
            row = max(row - 1 - self.wind[col] , 0)
        elif action == 1:  # down
            row = min(row + 1 - self.wind[col], self.rows - 1)
        elif action == 2:  # left
            col = max(col - 1, 0)
            row = max(row - self.wind[col], 0) 
        elif action == 3:  # right
            col = min(col + 1, self.cols - 1)
            row = max(row - self.wind[col], 0) 
        return (row, col)

class SarsaAgent:
    def __init__(self, num_rows, num_cols, num_actions, alpha, gamma, epsilon):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_actions = num_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = np.zeros((num_rows, num_cols, num_actions))

    def get_action(self, state):
        if np.random.uniform() < self.epsilon:
            action = random.randint(0, self.num_actions - 1)
            #print('returning random action:', action)
        else:
            action = np.argmax(self.Q[state])
            #print('Q:', self.Q)
            print('returning selected action:', action)
        return action

    def update(self, state, action, reward, next_state, next_action):
        print(f'S: {state}, Sp: {next_state}, A: {action}, Ap: {next_action}')
        td_error = reward + self.gamma * self.Q[next_state, next_action] - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error


env = WindyGridWorld(7, 10, [0, 0, 0, 1, 1, 1, 2, 2, 1, 0])
agent = SarsaAgent(7, 10, 4, 0.5, 0.9, 0.1)

num_episodes = 1000
for i in range(num_episodes):
    # Get S,A
    state = env.start
    action = agent.get_action(state)

    while state != env.goal:
        # Get S',A'
        next_state = env.move(state, action)
        next_action = agent.get_action(next_state)

        # Observe R 
        reward = -1 if next_state != env.goal else 0

        # Update Q, A<-A', S<-S'
        agent.update(state, action, reward, next_state, next_action)
        state = next_state
        action = next_action

    print(f'Episode: {i+1}')

print('Q:', agent.Q)


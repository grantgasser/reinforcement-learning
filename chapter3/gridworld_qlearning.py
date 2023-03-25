"""
Simple GridWorld environment using Q-learning to learn a policy.
"""
import numpy as np
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.ones((rows, cols))*-1
        self.start = (0, 0)  # top left
        self.goal = (rows-1, cols-1)  # bottom right

    """
    Moves the agent based on the current state and the action constrianed by the world and obstacles.

    Returns new/updated state (i, j)
    """
    def move(self, state, action):
        i, j = state  # location in the grid

        # Move according to one of the four actions
        if action == 'left':
            j -= 1
        elif action == 'right':
            j += 1
        elif action == 'up':
            i -= 1
        elif action == 'down':
            i += 1

        # Check if state is in bounds and not an obstacle, otherwise don't move
        if i >= 0 and i < self.rows and j >= 0 and j < self.cols and (i,j):
            return (i, j)
        else:
            return state


class QLearningAgent:
    def __init__(self, num_states, num_actions, alpha, gamma, epsilon):
        self.Q = np.zeros((num_states, num_actions))  # Q(s,a)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.reward_history = []

    """The policy: gets pi(a|s)"""
    def get_action(self, state):
        if np.random.uniform() < self.epsilon:
            return np.random.choice(4)
        else:
            return np.argmax(self.Q[state])

    """
    Q-learning update step

    Q(s,a) = Q(s,a) + alpha
    """
    def update(self, state, action, next_state, reward):
        self.Q[state, action] = self.Q[state, action] + self.alpha * (reward + self.gamma * np.max(self.Q[next_state] - self.Q[state, action]))
        self.reward_history[-1] += reward

env = GridWorld(5, 5)
agent = QLearningAgent(env.rows*env.cols, 4, 0.5, 0.9, 0.1)
num_episodes = 1000

for i in range(num_episodes):
    state = env.start
    agent.reward_history.append(0)

    # While we haven't achieved our goal...
    while state != env.goal:
        # Take action and get next state
        action = agent.get_action(state)
        next_state = env.move(state, action)

        # Update step
        agent.update(state, action, next_state, env.grid[state])
        state = next_state

    print(f"Episode {i+1} reward: {agent.reward_history[-1]}")

# Plot the reward history
plt.plot(agent.reward_history)
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Reward over Time')
plt.show()
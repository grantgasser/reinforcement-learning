# Chapter 3 - Markov Decision Processes (MDP)

### Exercise 3.1 
"Devise three example tasks of your own that fit into the MDP framework, identifying for each its states, actions, and rewards. Make the three examples as different from each other as possible. The framework is abstract and flexible and can be applied in many different ways. Stretch its limits in some way in at least one of your examples."

1. Stock Trader
- States: Price of asset
- Actions: Buy/Sell/Hold (3)
- Rewards: realized gains/losses

2. Car Autopilot on Highway
- States: Camera images from front of car
- Actions: Turn wheel left/right 10 degrees (2)
- Rewards: +Dist from left and right lane lines

3. Coding Agent
- States: The goal of the program defined by input to function and output with examples (all stringified?); The code (stringified?)
- Actions: Type character (letter, space, digit, etc.); 100+
- Rewards: Successful I/O on test cases; will we need more intermediate rewards here?


Harder than it seems to design the system well.

### Exercise 3.2
"Is the MDP framework adequate to usefully represent all goal-directed
learning tasks? Can you think of any clear exceptions?"

Well we know MDP is limited by the Markov Assumption. So it would fail when it's important to remember states in the past.

### Exercise 3.6 
"Suppose you treated pole-balancing as an episodic task but also used
discounting, with all rewards zero except for −1 upon failure. What then would the
return be at each time? How does this return differ from that in the discounted, continuingformulation of this task?"


Each episode would end with a cumulative reward of gamma^(num_steps) * -1

So reward would be between [-1, 0)

### Exercise 3.7 
"Imagine that you are designing a robot to run a maze. You decide to give it a
reward of +1 for escaping from the maze and a reward of zero at all other times. The task
seems to break down naturally into episodes—the successive runs through the maze—so
you decide to treat it as an episodic task, where the goal is to maximize expected total
reward (3.7). After running the learning agent for a while, you find that it is showing
no improvement in escaping from the maze. What is going wrong? Have you effectively
communicated to the agent what you want it to achieve?"

I think you need to incentivize solving the maze quickly. Thus, it may be better to penalize each step the robot takes with a reward of -1. Then solving the maze could be rewarded with +1 or a larger value.

### Exercise 3.8 
Suppose gamma = 0.5 and the following sequence of rewards is received R1 = −1,
R2 = 2, R3 = 6, R4 = 3, and R5 = 2, with T = 5. What are G0, G1, . . ., G5? Hint:
Work backwards.

G5 = 0 

G4 = R5 + (gamma)*G5

G4 = 2

G3 = R4 + (gamma)*G4

G3 = 3 + (0.5)*2

G3 = 4

...


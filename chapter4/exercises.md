# Chapter 4 - Dynamic Programming

### Exercise 4.1 
In Example 4.1, if pi is the equiprobable random policy, what is q(11, down)?
What is q(7, down)?

_Solution_

`q(s,a) = SUM_s',r(p(s',r | s,a)) * [r + gamma * max_a q(s', a')]`

`q(11,down) = -1` (terminal state)

`q(7, down) = p(11, -1 | 7, down) * ...`

`q(7, down) = -1 + v(11)`

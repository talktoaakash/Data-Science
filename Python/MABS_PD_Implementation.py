#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:59:49 2023

@author: akashverma
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

num_agents = 10
p_default = 0.01
num_steps = 50

class Agent:
    def __init__(self, money):
        self.money = money
        self.defaulted = False
        

def initialize_agents(num_agents):
    agents = []
    for i in range(num_agents):
        money = random.randint(0, 10000)
        agent = Agent(money)
        agents.append(agent)
    return agents

def update_defaults(agents, p_default):
    for agent in agents:
        if not agent.defaulted:
            if random.random() < p_default:
                agent.defaulted = True
                agent.money = 0
                
def update_money(agents):
    for i, agent in enumerate(agents):
        if not agent.defaulted:
            for j, other_agent in enumerate(agents):
                if i != j and other_agent.defaulted:
                    agent.money -= 100
                    if agent.money < 0:
                        agent.money = 0
                        
def run_simulation(num_agents, p_default, num_steps):
    agents = initialize_agents(num_agents)
    money_history = []
    for i in range(num_steps):
        update_defaults(agents, p_default)
        update_money(agents)
        money_history.append([agent.money for agent in agents])
    return money_history

money_history = run_simulation(num_agents, p_default, num_steps)


plt.plot(money_history)
plt.show()

# Plot 1
avg_money_history=[sum(money)/num_agents for money in money_history]
plt.plot(range(num_steps),avg_money_history)
plt.xlabel('Time Steps')
plt.ylabel('Average Amount of Money')
plt.title('Multi Agent Based SImulation for PD')


#Plot 2

end_money = [money[-1] for money in money_history]
end_money
# Create a scatter plot of the probability of default and the amount of money held at the end of the simulation
plt.scatter(p_default, end_money)
plt.xlabel('Probability of Default')
plt.ylabel('Money')
plt.title('Relationship Between Probability of Default and Amount of Money Held')
plt.show()




plt.show()






#Plot 4

import matplotlib.pyplot as plt
import numpy as np

# Define the parameters for the simulation
num_agents = 50
default_prob = 0.05
num_time_steps = 100

# Run the simulation and record the money held by all agents at each time step
money_history = run_simulation(num_agents, default_prob, num_time_steps)

# Calculate the average amount of money held by all agents at each time step
avg_money_history = [sum(money)/num_agents for money in money_history]

# Create a line plot of the average amount of money held by all agents over time
plt.plot(range(num_time_steps), avg_money_history)
plt.xlabel('Time Step')
plt.ylabel('Average Money Held')
plt.title('Change in Average Amount of Money Held Over Time')
plt.show()


#Plot 5


import matplotlib.pyplot as plt

# Define the parameters for the simulation
num_agents = 50
default_prob = 0.05
num_time_steps = 100

def count_defaults(num_agents, default_prob, num_time_steps):
    default_counts=[0]*num_time_steps
    
    for t in range(num_time_steps):
        num_defaults=sum(np.random.uniform(size=num_agents)<default_prob)
        
        default_counts[t]=num_defaults
    return default_counts

# Run the simulation and record the number of default events that occur
default_count_history = count_defaults(num_agents, default_prob, num_time_steps)

# Create a histogram of the number of default events that occur during the simulation
plt.hist(default_count_history, bins=range(num_time_steps+1))
plt.xlabel('Number of Default Events')
plt.ylabel('Frequency')
plt.title('Distribution of Default Events')
plt.show()

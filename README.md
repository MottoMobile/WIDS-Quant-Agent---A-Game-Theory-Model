
## Mesa Tutorial – Concept and Usage

Mesa is a Python-based framework that provides an environment in which to build agent-based models. In such models, complex behavior at the system level emerges from the interactions between individual agents following simple, local decision rules. This tutorial will give an excellent introduction to the core abstractions necessary to construct such models in a modular and extensible way using Mesa.

In this tutorial, an Agent is introduced as the fundamental unit of the system. Every agent encompasses a set of state variables and defines a step() method that describes its behavior during each time step. Agents typically have very limited information and take decentralized decisions, making them nicely applicable for modeling market participants in a financial system.

The Model class represents the global environment in which agents exist. It is responsible for the initialization of agents, shared state variables such as prices or global signals, and the flow of the simulation in general. This separation between agent-level logic and model-level logic ensures clarity and allows the system to scale while complexity increases.

Mesa uses Schedulers to control how and when agents are activated. The tutorial speaks about different scheduling mechanisms like random activation. And they highlight that the order of agent execution can make a big difference in emergent outcomes, something very important in truly interactive systems such as markets where timing and ordering plays a big role in determining aggregate behavior.

The DataCollector component allows the systematic tracking of both agent-level and model-level variables across timesteps. This enables the quantitative analysis of emergent phenomena, such as changes in wealth distribution, price dynamics, or volatility, rather than purely qualitative observation.

The tutorial then covers Mesa's built-in visualization and server tools, which allow for real-time observation of agent behavior and system evolution. While visualization is not central to model logic, it is useful for debugging and developing intuition about how local interactions generate global patterns.

The Mesa tutorial establishes a structured framework for modeling complex adaptive systems, and it is particularly well-suited for the simulation of economic and financial systems when the emergent behavior is of primary interest.

---

## Understanding Game Theory Strategies

In 1928

### 1. Minority Game Strategy

In this strategy, it is beneficial for the agent to make decisions contrary to the majority of the market. If the majority of the agents is purchasing, then selling is a beneficial action, and if the majority is selling, then purchasing is a beneficial action.

My understanding is it captures the competitive scenarios where payoff is based on the exploitation of the crowd behavior rather than being fed back as it happens in the crowd. It injects negative feedback into the process, which helps to prevent the prices from being uncontrolled. But there needs to be an estimate of the crowd behavior on the part of the agents.

### 2. Trend-Follow

In a trend-following model, agents make decisions about buying or selling based on the recent trend of the price. Agents buy when prices are rising and sell when prices are falling.

Based on my understanding, it appears that this is close to a game that involves coordination, with agents accumulating benefits if they are aiming toward each other. Although such a game appears lucrative, it also creates self-reinforcing trends. In a situation where most agents are following this game, the system becomes more volatile.

The coupling of these two strategies demonstrates how different schemes of incentives can result in equally different market behavior at the market level despite simple rules for individual agents.

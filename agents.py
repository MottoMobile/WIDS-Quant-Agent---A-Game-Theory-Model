
import mesa
import random
import numpy as np
from .strategies import StrategyGene

class BaseTrader(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 100
        self.last_action = 0

    def step(self): raise NotImplementedError
    def feedback(self, winning_side):
        if self.last_action == winning_side: self.wealth += 1
        else: self.wealth -= 1

class NoiseTrader(BaseTrader):
    def step(self): self.last_action = random.choice([0, 1])

class TrendTrader(BaseTrader):
    def step(self):
        # Follows the majority of the last 5 steps
        history = list(self.model.history)[-5:]
        avg = sum(history) / len(history) if history else 0.5
        self.last_action = 1 if avg > 0.5 else 0

class QuantAgent(BaseTrader):
    def __init__(self, unique_id, model, m, num_strats):
        super().__init__(unique_id, model)
        self.strategy_bank = [StrategyGene(m) for _ in range(num_strats)]
    
    def step(self):
        hist_int = self.model.get_history_as_int()
        if hist_int is None:
            self.last_action = random.choice([0, 1])
            return
        
        # Greedy Selection
        scores = [s.virtual_score for s in self.strategy_bank]
        best_idx = np.argmax(scores)
        self.last_action = self.strategy_bank[best_idx].predict(hist_int)

    def feedback(self, winning_side):
        super().feedback(winning_side)
        # Learning: Update ALL strategies
        prev_hist_int = self.model.get_history_as_int(lag=1)
        if prev_hist_int is not None:
            for strat in self.strategy_bank:
                strat.update_score(prev_hist_int, winning_side)

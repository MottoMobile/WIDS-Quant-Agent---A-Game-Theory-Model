
import numpy as np

class StrategyGene:
    """Represents a single Strategy (Gene) in the Minority Game."""
    def __init__(self, memory_m):
        self.m = memory_m
        self.table_size = 2 ** self.m
        # Random initialization
        self.prediction_table = np.random.randint(0, 2, self.table_size)
        self.virtual_score = 0
    
    def predict(self, history_int):
        return self.prediction_table[history_int]

    def update_score(self, history_int, winning_outcome):
        prediction = self.prediction_table[history_int]
        if prediction == winning_outcome:
            self.virtual_score += 1
        else:
            self.virtual_score -= 1


import mesa
from collections import deque
import random
from .agents import NoiseTrader, TrendTrader, QuantAgent

class MinorityGameEngine(mesa.Model):
    def __init__(self, config):
        self.conf = config
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.history = deque([random.choice([0, 1]) for _ in range(config.MEMORY_SIZE + 5)], maxlen=100)
        self._spawn_agents()
        
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Buyers": "n_buyers",
                "Inefficiency_Alpha": lambda m: ((m.n_buyers - m.conf.N_AGENTS/2)**2) / m.conf.N_AGENTS
            },
            agent_reporters={"Wealth": "wealth"}
        )
        self.n_buyers = 0

    def _spawn_agents(self):
        idx = 0
        for _ in range(int(self.conf.N_AGENTS * self.conf.PCT_NOISE)):
            self.schedule.add(NoiseTrader(idx, self)); idx+=1
        for _ in range(int(self.conf.N_AGENTS * self.conf.PCT_TREND)):
            self.schedule.add(TrendTrader(idx, self)); idx+=1
        for _ in range(int(self.conf.N_AGENTS * self.conf.PCT_SMART)):
            self.schedule.add(QuantAgent(idx, self, self.conf.MEMORY_SIZE, self.conf.STRATEGIES_PER_AGENT)); idx+=1

    def get_history_as_int(self, lag=0):
        start = -(self.conf.MEMORY_SIZE + lag)
        end = -lag if lag > 0 else None
        if len(self.history) < self.conf.MEMORY_SIZE + lag: return None
        bits = list(self.history)[start:end]
        return int("".join(map(str, bits)), 2)

    def step(self):
        self.schedule.step()
        actions = [a.last_action for a in self.schedule.agents]
        self.n_buyers = sum(actions)
        minority_side = 1 if self.n_buyers < (self.conf.N_AGENTS / 2) else 0
        for a in self.schedule.agents: a.feedback(minority_side)
        self.history.append(minority_side)
        self.datacollector.collect(self)

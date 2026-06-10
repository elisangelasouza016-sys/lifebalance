import random


class LifeBalanceEnvironment:
    def __init__(self):
        self.max_days = 7
        self.periods_per_day = 3
        self.max_steps = self.max_days * self.periods_per_day
        self.actions = [
            "TRABALHAR",
            "ESTUDAR",
            "DESCANSAR",
            "EXERCITAR",
            "CUIDAR_FAMILIA",
            "TAREFA_DOMESTICA",
        ]
        self.reset()

    def reset(self):
        self.energy = 70
        self.health = 70
        self.stress = 30
        self.pending_tasks = 60
        self.step_count = 0
        self.done = False
        return self.get_state()

    def discretize(self, value):
        if value <= 33:
            return 0  # baixo
        elif value <= 66:
            return 1  # médio
        return 2  # alto

    def get_period(self):
        return self.step_count % 3  # 0 manhã, 1 tarde, 2 noite

    def get_state(self):
        return (
            self.discretize(self.energy),
            self.discretize(self.health),
            self.discretize(self.stress),
            self.discretize(self.pending_tasks),
            self.get_period(),
        )

    def clamp_values(self):
        self.energy = max(0, min(100, self.energy))
        self.health = max(0, min(100, self.health))
        self.stress = max(0, min(100, self.stress))
        self.pending_tasks = max(0, min(100, self.pending_tasks))

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True, {}

        reward = 0

        if action == "TRABALHAR":
            self.pending_tasks -= 18
            self.energy -= 15
            self.stress += 12
            self.health -= 5

        elif action == "ESTUDAR":
            self.pending_tasks -= 8
            self.energy -= 10
            self.stress += 6

        elif action == "DESCANSAR":
            self.energy += 22
            self.stress -= 12
            self.pending_tasks += 5

        elif action == "EXERCITAR":
            self.health += 15
            self.energy -= 8
            self.stress -= 8
            self.pending_tasks += 3

        elif action == "CUIDAR_FAMILIA":
            self.energy -= 10
            self.stress += 4
            self.pending_tasks += 2

        elif action == "TAREFA_DOMESTICA":
            self.pending_tasks -= 10
            self.energy -= 12
            self.stress += 5

        self.step_count += 1
        self.clamp_values()

        reward += self.calculate_balance_reward()

        if self.energy <= 0:
            reward -= 100
            self.done = True

        if self.step_count >= self.max_steps:
            reward += self.calculate_final_reward()
            self.done = True

        info = {
            "energy": self.energy,
            "health": self.health,
            "stress": self.stress,
            "pending_tasks": self.pending_tasks,
            "step": self.step_count,
            "period": self.get_period(),
            "action": action,
        }

        return self.get_state(), reward, self.done, info

    def calculate_balance_reward(self):
        reward = 0

        if self.energy >= 40:
            reward += 4
        else:
            reward -= 10

        if self.health >= 50:
            reward += 4
        else:
            reward -= 10

        if self.stress <= 60:
            reward += 4
        else:
            reward -= 10

        if self.pending_tasks <= 60:
            reward += 4
        else:
            reward -= 10

        return reward

    def calculate_final_reward(self):
        reward = 20

        if self.energy >= 40:
            reward += 20

        if self.health >= 50:
            reward += 20

        if self.stress <= 60:
            reward += 20

        if self.pending_tasks <= 40:
            reward += 20

        return reward

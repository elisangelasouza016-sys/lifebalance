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
        self.energy = random.randint(50, 90)
        self.health = random.randint(50, 90)
        self.stress = random.randint(10, 50)
        self.pending_tasks = random.randint(30, 70)
        self.invisible_load = random.randint(20, 60)

        self.step_count = 0
        self.done = False

        return self.get_state()

    def discretize_low_good(self, value):
        if value <= 33:
            return 0
        elif value <= 66:
            return 1
        return 2

    def get_period(self):
        return self.step_count % self.periods_per_day

    def get_day(self):
        return self.step_count // self.periods_per_day

    def get_state(self):
        return (
            self.discretize_low_good(self.energy),
            self.discretize_low_good(self.health),
            self.discretize_low_good(self.stress),
            self.discretize_low_good(self.pending_tasks),
            self.discretize_low_good(self.invisible_load),
            self.get_period(),
        )

    def clamp_values(self):
        self.energy = max(0, min(100, self.energy))
        self.health = max(0, min(100, self.health))
        self.stress = max(0, min(100, self.stress))
        self.pending_tasks = max(0, min(100, self.pending_tasks))
        self.invisible_load = max(0, min(100, self.invisible_load))

    def add_daily_demands(self):
        if self.get_period() == 0:
            new_demands = random.randint(0, 10)
            self.pending_tasks += new_demands
            self.invisible_load += random.randint(0, 5)

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True, {}

        self.add_daily_demands()

        if action == "TRABALHAR":
            self.pending_tasks -= 15
            self.energy -= 12
            self.stress += 8
            self.invisible_load += 5

        elif action == "ESTUDAR":
            self.pending_tasks -= 5
            self.energy -= 8
            self.stress += 4
            self.invisible_load += 3

        elif action == "DESCANSAR":
            self.energy += 18
            self.stress -= 12
            self.invisible_load -= 8

        elif action == "EXERCITAR":
            self.health += 12
            self.energy -= 5
            self.stress -= 8
            self.invisible_load -= 5

        elif action == "CUIDAR_FAMILIA":
            self.energy -= 4
            self.stress -= 4
            self.invisible_load -= 12

        elif action == "TAREFA_DOMESTICA":
            self.pending_tasks -= 10
            self.energy -= 8
            self.invisible_load -= 8

        self.step_count += 1
        self.clamp_values()

        reward = self.calculate_balance_reward()

        if self.energy <= 0:
            reward -= 100
            self.done = True

        if self.step_count >= self.max_steps:
            reward += self.calculate_final_reward()
            self.done = True

        info = {
            "day": self.get_day() + 1,
            "period": self.get_period(),
            "step": self.step_count,
            "action": action,
            "energy": self.energy,
            "health": self.health,
            "stress": self.stress,
            "pending_tasks": self.pending_tasks,
            "invisible_load": self.invisible_load,
            "burnout": self.energy <= 0,
        }

        return self.get_state(), reward, self.done, info

    def calculate_balance_reward(self):
        reward = 0

        reward += 5 if self.energy >= 40 else -10
        reward += 5 if self.health >= 50 else -10
        reward += 5 if self.stress <= 60 else -10
        reward += 5 if self.pending_tasks <= 60 else -10
        reward += 5 if self.invisible_load <= 60 else -10

        return reward

    def calculate_final_reward(self):
        reward = 20

        if self.energy >= 40:
            reward += 20
        if self.health >= 50:
            reward += 20
        if self.stress <= 60:
            reward += 20
        if self.pending_tasks <= 60:
            reward += 20
        if self.invisible_load <= 60:
            reward += 20

        return reward

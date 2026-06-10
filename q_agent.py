import random


class QLearningAgent:
    def __init__(
        self,
        actions,
        alpha=0.1,
        gamma=0.95,
        epsilon=1.0,
        epsilon_decay=0.995,
        epsilon_min=0.05,
    ):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = {}

    def state_to_key(self, state):
        return str(state)

    def get_q_values(self, state):
        key = self.state_to_key(state)

        if key not in self.q_table:
            self.q_table[key] = {action: 0.0 for action in self.actions}

        return self.q_table[key]

    def choose_action(self, state, training=True):
        if training and random.random() < self.epsilon:
            return random.choice(self.actions)

        q_values = self.get_q_values(state)
        return max(q_values, key=q_values.get)

    def learn(self, state, action, reward, next_state):
        q_values = self.get_q_values(state)
        next_q_values = self.get_q_values(next_state)

        current_q = q_values[action]
        max_next_q = max(next_q_values.values())

        new_q = current_q + self.alpha * (
            reward + self.gamma * max_next_q - current_q
        )

        q_values[action] = new_q

    def decay_epsilon(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        if self.epsilon < self.epsilon_min:
            self.epsilon = self.epsilon_min

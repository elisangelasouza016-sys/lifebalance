from .environment import LifeBalanceEnvironment
from .q_agent import QLearningAgent


def train_agent(episodes=1000):
    env = LifeBalanceEnvironment()
    agent = QLearningAgent(env.actions)

    training_log = []

    for episode in range(episodes):

        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.choose_action(state)

            next_state, reward, done, info = env.step(action)

            agent.learn(
                state,
                action,
                reward,
                next_state
            )

            state = next_state
            total_reward += reward

        agent.decay_epsilon()

        training_log.append({
            "episode": episode + 1,
            "reward": total_reward,
            "energy": env.energy,
            "health": env.health,
            "stress": env.stress,
            "pending_tasks": env.pending_tasks,
            "burnout": env.energy <= 0,
            "steps": env.step_count
        })

    return agent, training_log

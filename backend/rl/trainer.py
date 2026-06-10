from .environment import LifeBalanceEnvironment
from .q_agent import QLearningAgent


def train_agent(episodes=1000):
    env = LifeBalanceEnvironment()
    agent = QLearningAgent(env.actions)

    training_log = []

    for episode in range(1, episodes + 1):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.choose_action(state, training=True)
            next_state, reward, done, info = env.step(action)

            agent.learn(state, action, reward, next_state)

            state = next_state
            total_reward += reward

        agent.decay_epsilon()

        training_log.append(
            {
                "episode": episode,
                "total_reward": total_reward,
                "steps": env.step_count,
                "energy": env.energy,
                "health": env.health,
                "stress": env.stress,
                "pending_tasks": env.pending_tasks,
                "burnout": env.energy <= 0,
            }
        )

    return {
        "episodes": episodes,
        "q_table": agent.q_table,
        "training_log": training_log,
        "epsilon_final": agent.epsilon,
    }


def simulate_trained_agent(q_table):
    env = LifeBalanceEnvironment()
    agent = QLearningAgent(env.actions)
    agent.q_table = q_table
    agent.epsilon = 0

    state = env.reset()
    done = False
    total_reward = 0
    history = []

    while not done:
        action = agent.choose_action(state, training=False)
        next_state, reward, done, info = env.step(action)

        history.append(
            {
                "state": state,
                "action": action,
                "reward": reward,
                "info": info,
            }
        )

        state = next_state
        total_reward += reward

    return {
        "total_reward": total_reward,
        "steps": env.step_count,
        "final": {
            "energy": env.energy,
            "health": env.health,
            "stress": env.stress,
            "pending_tasks": env.pending_tasks,
            "burnout": env.energy <= 0,
        },
        "history": history,
    }

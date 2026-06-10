from flask import Flask, jsonify, request
from flask_cors import CORS

from rl.trainer import train_agent, simulate_trained_agent

app = Flask(__name__)
CORS(app)

LAST_TRAINING = {
    "q_table": {},
    "training_log": [],
}


@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "status": "ok",
        "project": "Athena Life Balance RL"
    })


@app.route("/api/train", methods=["POST"])
def train():
    data = request.get_json() or {}
    episodes = int(data.get("episodes", 1000))

    result = train_agent(episodes)

    LAST_TRAINING["q_table"] = result["q_table"]
    LAST_TRAINING["training_log"] = result["training_log"]

    return jsonify({
        "message": "Treinamento concluído",
        "episodes": result["episodes"],
        "epsilon_final": result["epsilon_final"],
        "last_10_episodes": result["training_log"][-10:],
    })


@app.route("/api/metrics", methods=["GET"])
def metrics():
    log = LAST_TRAINING["training_log"]

    if not log:
        return jsonify({
            "message": "Nenhum treinamento executado ainda."
        })

    rewards = [item["total_reward"] for item in log]
    burnouts = [item["burnout"] for item in log]
    steps = [item["steps"] for item in log]

    return jsonify({
        "episodes": len(log),
        "average_reward": sum(rewards) / len(rewards),
        "average_steps": sum(steps) / len(steps),
        "burnout_rate": sum(burnouts) / len(burnouts),
        "first_10": log[:10],
        "last_10": log[-10:],
    })


@app.route("/api/simulation", methods=["GET"])
def simulation():
    q_table = LAST_TRAINING["q_table"]

    if not q_table:
        return jsonify({
            "message": "Treine o agente antes de simular."
        })

    result = simulate_trained_agent(q_table)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

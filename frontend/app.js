const API_URL = "http://127.0.0.1:5000";

async function trainAgent() {
  document.getElementById("metrics").textContent = "Treinando agente...";

  const response = await fetch(`${API_URL}/api/train`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ episodes: 1000 })
  });

  const data = await response.json();

  document.getElementById("metrics").textContent =
    JSON.stringify(data, null, 2);
}

async function loadMetrics() {
  const response = await fetch(`${API_URL}/api/metrics`);
  const data = await response.json();

  document.getElementById("metrics").textContent =
    JSON.stringify(data, null, 2);
}

async function simulateAgent() {
  const response = await fetch(`${API_URL}/api/simulation`);
  const data = await response.json();

  if (data.message) {
    document.getElementById("metrics").textContent = data.message;
    return;
  }

  const final = data.final;

  document.getElementById("state").innerHTML = `
    <p>Energia: ${final.energy}</p>
    <p>Saúde: ${final.health}</p>
    <p>Estresse: ${final.stress}</p>
    <p>Pendências: ${final.pending_tasks}</p>
  `;

  const actionsList = document.getElementById("actions");
  actionsList.innerHTML = "";

  data.history.forEach((step, index) => {
    const item = document.createElement("li");
    item.textContent = `Passo ${index + 1}: ${step.action} | Recompensa: ${step.reward}`;
    actionsList.appendChild(item);
  });
}

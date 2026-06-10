import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from rl.trainer import train_agent

st.set_page_config(
    page_title="Athena Life Balance RL",
    layout="wide"
)

st.title("Athena Life Balance RL")

st.markdown("""
Agente treinado com Q-Learning para equilibrar:

- Energia
- Saúde
- Estresse
- Pendências

Objetivo:
maximizar produtividade sem entrar em burnout.
""")

episodes = st.slider(
    "Quantidade de episódios",
    100,
    10000,
    2000,
    100
)

if st.button("Treinar Athena"):

    with st.spinner("Treinando agente..."):

        agent, log = train_agent(episodes)

    df = pd.DataFrame(log)

    st.success("Treinamento concluído")

    col1, col2, col3 = st.columns(3)

col1.metric(
    "Recompensa Média",
    round(df["reward"].mean(), 2)
)

col2.metric(
    "Burnout %",
    round(df["burnout"].mean() * 100, 2)
)

col3.metric(
    "Passos Médios",
    round(df["steps"].mean(), 2)
)

    st.subheader("Evolução da recompensa")

    fig, ax = plt.subplots()

    ax.plot(df["episode"], df["reward"])

    ax.set_xlabel("Episódio")
    ax.set_ylabel("Recompensa")

    st.pyplot(fig)

    st.subheader("Últimos episódios")

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

    st.subheader("Melhor episódio")

    best = df.loc[df["reward"].idxmax()]

    st.json(best.to_dict())

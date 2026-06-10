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
Simulação acadêmica de **Aprendizado por Reforço com Q-Learning**.

A agente Athena aprende, por tentativa e erro, a equilibrar uma rotina de múltiplas jornadas, considerando:

- energia;
- saúde;
- estresse;
- pendências;
- carga invisível.

O objetivo é maximizar equilíbrio e reduzir a ocorrência de burnout.
""")


episodes = st.slider(
    "Quantidade de episódios para treinamento",
    min_value=100,
    max_value=10000,
    value=2000,
    step=100,
)


if st.button("Treinar Athena"):

    with st.spinner("Treinando agente..."):
        agent, log = train_agent(episodes)

    df = pd.DataFrame(log)

    st.success("Treinamento concluído.")

    st.subheader("Métricas Gerais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Recompensa Média",
        round(df["reward"].mean(), 2)
    )

    col2.metric(
        "Burnout (%)",
        round(df["burnout"].mean() * 100, 2)
    )

    col3.metric(
        "Passos Médios",
        round(df["steps"].mean(), 2)
    )

    st.subheader("Indicadores Finais Médios")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Energia",
        round(df["energy"].mean(), 1)
    )

    col2.metric(
        "Saúde",
        round(df["health"].mean(), 1)
    )

    col3.metric(
        "Estresse",
        round(df["stress"].mean(), 1)
    )

    col4.metric(
        "Pendências",
        round(df["pending_tasks"].mean(), 1)
    )

    col5.metric(
        "Carga Invisível",
        round(df["invisible_load"].mean(), 1)
    )

    st.subheader("Evolução da Recompensa")

    fig, ax = plt.subplots()
    ax.plot(df["episode"], df["reward"])
    ax.set_xlabel("Episódio")
    ax.set_ylabel("Recompensa")
    st.pyplot(fig)

    st.subheader("Burnout por Episódio")

    fig2, ax2 = plt.subplots()
    ax2.plot(df["episode"], df["burnout"].astype(int))
    ax2.set_xlabel("Episódio")
    ax2.set_ylabel("Burnout")
    st.pyplot(fig2)

    st.subheader("Últimos 20 Episódios")

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

    st.subheader("Melhor Episódio")

    best = df.loc[df["reward"].idxmax()]
    st.json(best.to_dict())

else:
    st.info("Escolha a quantidade de episódios e clique em **Treinar Athena**.")

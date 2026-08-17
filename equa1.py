import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)


# ============================================================
# CAMINHO DA APLICAÇÃO E DA IMAGEM
# ============================================================

PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "mat.jpeg"


# ============================================================
# EXIBIÇÃO DA IMAGEM
# ============================================================

if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:
    st.warning(
        "A imagem 'mat.jpeg' não foi encontrada. ⚠️"
    )


# ============================================================
# TÍTULO
# ============================================================

st.title("Equação do 1º Grau 📈")

st.write("Resolva uma equação no formato:")

st.latex(r"ax + b = 0")


# ============================================================
# ENTRADA DOS VALORES
# ============================================================

a = st.number_input(
    "Digite o valor de a:",
    value=1.0,
    step=1.0
)

b = st.number_input(
    "Digite o valor de b:",
    value=0.0,
    step=1.0
)


# ============================================================
# FUNÇÃO PARA FORMATAR NÚMEROS
# ============================================================

def formatar_numero(numero):
    """Retorna o número sem casas decimais desnecessárias."""

    if numero == int(numero):
        return str(int(numero))

    return f"{numero:.2f}"


# ============================================================
# BOTÃO CALCULAR
# ============================================================

if st.button("Calcular", use_container_width=True):

    # --------------------------------------------------------
    # CASO 1: a = 0
    # --------------------------------------------------------

    if a == 0:

        # 0x + 0 = 0
        if b == 0:

            st.warning(
                "A equação possui infinitas soluções. ♾️"
            )

            st.latex(r"0x + 0 = 0")

            st.info(
                "Todo número real satisfaz essa equação."
            )

        # 0x + b = 0, com b diferente de zero
        else:

            st.error(
                "A equação não possui solução. ❌"
            )

            st.latex(
                f"{formatar_numero(b)} = 0"
            )

            st.info(
                "Essa igualdade é impossível."
            )


    # --------------------------------------------------------
    # CASO 2: a ≠ 0
    # --------------------------------------------------------

    else:

        # ----------------------------------------------------
        # CÁLCULO DA RAIZ
        # ----------------------------------------------------

        x_raiz = -b / a

        a_fmt = formatar_numero(a)
        b_fmt = formatar_numero(abs(b))
        raiz_fmt = formatar_numero(x_raiz)

        # ----------------------------------------------------
        # RESULTADO
        # ----------------------------------------------------

        st.subheader("Resultado ✅")

        st.write("A raiz da equação é:")

        st.success(
            f"x = {raiz_fmt}"
        )


        # ----------------------------------------------------
        # EQUAÇÃO
        # ----------------------------------------------------

        st.subheader("Equação")

        if b > 0:

            st.latex(
                rf"{a_fmt}x + {b_fmt} = 0"
            )

        elif b < 0:

            st.latex(
                rf"{a_fmt}x - {b_fmt} = 0"
            )

        else:

            st.latex(
                rf"{a_fmt}x = 0"
            )


        # ----------------------------------------------------
        # RESOLUÇÃO
        # ----------------------------------------------------

        st.subheader("Resolução")

        # Equação original
        if b > 0:

            st.latex(
                rf"{a_fmt}x + {b_fmt} = 0"
            )

        elif b < 0:

            st.latex(
                rf"{a_fmt}x - {b_fmt} = 0"
            )

        else:

            st.latex(
                rf"{a_fmt}x = 0"
            )


        # Passando b para o outro lado
        if b != 0:

            st.latex(
                rf"{a_fmt}x = {-b:g}"
            )

        # Divisão por a
        st.latex(
            rf"x = \frac{{{-b:g}}}{{{a_fmt}}}"
        )

        # Resultado final
        st.latex(
            rf"x = {raiz_fmt}"
        )


        # ----------------------------------------------------
        # GRÁFICO
        # ----------------------------------------------------

        st.subheader("Gráfico da função 📊")

        # Cria valores de x próximos da raiz
        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        # Função y = ax + b
        y = a * x + b


        # Criação da figura
        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        # ----------------------------------------------------
        # LINHA DA FUNÇÃO
        # ----------------------------------------------------

        ax.plot(
            x,
            y,
            color="blue",
            linewidth=2,
            label=(
                rf"$y = {a_fmt}x "
                + (f"+ {b_fmt}$" if b >= 0 else f"- {b_fmt}$")
            )
        )


        # ----------------------------------------------------
        # EIXOS
        # ----------------------------------------------------

        ax.axhline(
            y=0,
            color="black",
            linewidth=1
        )

        ax.axvline(
            x=0,
            color="black",
            linewidth=1
        )


        # ----------------------------------------------------
        # PONTO DA RAIZ
        # ----------------------------------------------------

        ax.scatter(
            [x_raiz],
            [0],
            color="red",
            s=100,
            zorder=5,
            label=f"Raiz: x = {raiz_fmt}"
        )


        # ----------------------------------------------------
        # CONFIGURAÇÕES DO GRÁFICO
        # ----------------------------------------------------

        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.set_title(
            "Gráfico da Função do 1º Grau"
        )

        ax.grid(
            True,
            alpha=0.3
        )

        ax.legend()

        # Exibe o gráfico
        st.pyplot(
            fig,
            use_container_width=True
        )

        # Libera a memória da figura
        plt.close(fig)


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    "Calculadora de Equação do 1º Grau 📚"
)

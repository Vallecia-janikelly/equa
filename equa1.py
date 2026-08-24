import streamlit as st
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)

# =========================
# FUNDO ROSA
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #FFC0CB;
}

/* Títulos e textos */
h1, h2, h3, p, label, .stMarkdown {
    color: #5A0033 !important;
}

/* Caixa dos campos */
div[data-baseweb="input"] {
    background-color: #FFE4EC;
    border-radius: 10px;
}

/* Botão */
.stButton > button {
    background-color: #FF69B4;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #FF1493;
    color: white;
}

/* Linha divisória */
hr {
    border-color: #FF69B4;
}

</style>
""", unsafe_allow_html=True)


# =========================
# CAMINHO DO APLICATIVO
# =========================

PASTA_APP = Path(__file__).parent

# Caminho da imagem
CAMINHO_LOGO = PASTA_APP / "mat.jpg"

# Exibe a imagem, se existir
if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:
    st.warning(
        "A imagem mat.jpg não foi encontrada. ⚠️"
    )


# =========================
# TÍTULO
# =========================

st.title("Equação do 1º Grau 📈")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")


# =========================
# ENTRADA DOS VALORES
# =========================

a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)


# =========================
# BOTÃO CALCULAR
# =========================

if st.button("Calcular", use_container_width=True):

    # =========================
    # CASO a = 0
    # =========================

    if a == 0:

        # 0x + 0 = 0
        if b == 0:

            st.warning(
                "A equação possui infinitas soluções."
            )

        # 0x + b = 0
        else:

            st.error(
                "A equação não possui solução."
            )

    # =========================
    # CASO a ≠ 0
    # =========================

    else:

        # Cálculo da raiz
        x_raiz = -b / a

        # =========================
        # RESULTADO
        # =========================

        st.subheader("Resultado ✅")

        st.write(
            "A raiz da equação é:"
        )

        st.success(
            f"x = {x_raiz:.2f}"
        )

        # =========================
        # EQUAÇÃO
        # =========================

        st.subheader("Equação")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        # =========================
        # RESOLUÇÃO
        # =========================

        st.subheader("Resolução")

        # Primeira linha
        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        # Segunda linha
        st.latex(
            f"{a}x = {-b}"
        )

        # Terceira linha
        st.latex(
            rf"x = \frac{{{-b}}}{{{a}}}"
        )

        # Resultado final
        st.latex(
            f"x = {x_raiz:.2f}"
        )

        # =========================
        # EXPLICAÇÃO
        # =========================

        st.subheader("💡 Como foi calculado?")

        st.write(
            "Para encontrar a raiz, isolamos o x:"
        )

        st.write(
            "1. Passamos o valor de b para o outro lado."
        )

        st.write(
            "2. Dividimos o resultado pelo valor de a."
        )

        st.write(
            "3. Assim encontramos o valor de x."
        )


# =========================
# RODAPÉ
# =========================

st.divider()

st.caption(
    "Calculadora de Equação do 1º Grau 📚"
)

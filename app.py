import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="MusicHub",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "musicas.csv"

# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1516280440614-37939bbacd81"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_MUSICA = (
    "https://images.unsplash.com/"
    "photo-1511379938547-c1f69419868d"
    "?auto=format&fit=crop&w=1200&q=85"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* FUNDO */

.stApp {
    background:
        linear-gradient(
            135deg,
            #f4efff 0%,
            #e9d5ff 50%,
            #ddd6fe 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #160d24,
            #29143f
        );

    border-right:
        2px solid #9333ea;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* LOGO */

.logo-title {
    font-size: 30px;
    font-weight: 800;
    color: #FFFFFF !important;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #d8b4fe !important;
    letter-spacing: 1px;
}

/* TÍTULOS */

.page-title {
    font-size: 40px;
    font-weight: 800;
    color: #3b1763 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #5b3477 !important;
    margin-bottom: 30px;
}

/* HERO */

.hero-container {
    position: relative;
    height: 420px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(65, 20, 100, 0.25);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(20, 8, 32, 0.97) 0%,
            rgba(35, 12, 55, 0.88) 45%,
            rgba(35, 12, 55, 0.15) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 600px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #c084fc !important;
    line-height: 1;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #f3e8ff !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #9333ea;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}

/* CARDS */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid #d8b4fe;

    box-shadow:
        0 10px 25px rgba(70, 25, 100, 0.10);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #3b1763 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #70469a !important;

    margin-top: 5px;
}

/* CARD ESCURO */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #1a0c27,
            #32144b
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(45, 10, 70, 0.20);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #eadcff !important;
    line-height: 1.7;
}

/* FORMULÁRIO */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.90);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #c084fc;

    box-shadow:
        0 10px 30px rgba(70, 20, 100, 0.10);
}

/* LABELS */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #3b1763 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #26132f !important;

    -webkit-text-fill-color:
        #26132f !important;

    border:
        2px solid #a855f7 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #7e22ce !important;

    box-shadow:
        0 0 0 3px rgba(126,34,206,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #80698f !important;
    opacity: 1 !important;
}

/* SELECTBOX */

[data-baseweb="select"] > div {
    background-color: #2b1838 !important;

    border:
        2px solid #9333ea !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
}

/* MENU */

[data-baseweb="popover"] {
    background-color: #2b1838 !important;
}

[data-baseweb="menu"] {
    background-color: #2b1838 !important;
}

[role="option"] {
    background-color: #2b1838 !important;

    color: #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #7e22ce !important;

    color: #FFFFFF !important;
}

/* BOTÕES */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    background:
        linear-gradient(
            135deg,
            #7e22ce,
            #a855f7
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(126,34,206,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    background:
        linear-gradient(
            135deg,
            #6b21a8,
            #9333ea
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}

/* TABELA */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #c084fc;
}

/* RODAPÉ */

.footer {

    margin-top: 50px;

    text-align: center;

    color: #70469a !important;

    font-size: 14px;

    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Musica",
        "Artista",
        "Album",
        "Ano",
        "Genero",
        "Duracao"
    ]

    if os.path.exists(ARQUIVO):

        try:
            return pd.read_csv(ARQUIVO)

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# =========================================================
# GARANTIR COLUNAS
# =========================================================

colunas_necessarias = [
    "Musica",
    "Artista",
    "Album",
    "Ano",
    "Genero",
    "Duracao"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
🎵 MusicHub
</div>

<div class="logo-subtitle">
SUA MÚSICA, ORGANIZADA
</div>
""",
unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Música",
        "🎧 Músicas Cadastradas"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "MusicHub • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Sua música.<br>
Seu universo.
</div>

<div class="hero-text">

Organize suas músicas, artistas e álbuns
em um único lugar.

Cadastre, pesquise e acompanhe sua coleção
musical de forma simples e organizada.

</div>

<div class="hero-badge">
🎵 MUSIC MANAGEMENT
</div>

</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
"""
<div class="page-title">
🎧 Sua biblioteca musical
</div>

<div class="page-subtitle">
Veja um resumo das músicas cadastradas no MusicHub.
</div>
""",
unsafe_allow_html=True
)


    total_musicas = len(df)

    total_artistas = (
        df["Artista"]
        .replace("", pd.NA)
        .dropna()
        .nunique()
    )

    total_generos = (
        df["Genero"]
        .replace("", pd.NA)
        .dropna()
        .nunique()
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🎵
</div>

<div class="card-number">
{total_musicas}
</div>

<div class="card-label">
MÚSICAS CADASTRADAS
</div>

</div>
""",
unsafe_allow_html=True
)


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🎤
</div>

<div class="card-number">
{total_artistas}
</div>

<div class="card-label">
ARTISTAS
</div>

</div>
""",
unsafe_allow_html=True
)


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🎶
</div>

<div class="card-number">
{total_generos}
</div>

<div class="card-label">
GÊNEROS MUSICAIS
</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
💜 Música em um só lugar
</h2>

<p>
O MusicHub foi desenvolvido para organizar
uma coleção musical de maneira simples,
bonita e prática.
</p>

<p>
Cadastre suas músicas, artistas e álbuns,
pesquise sua biblioteca e mantenha tudo
organizado em um único lugar.
</p>

</div>
""",
unsafe_allow_html=True
)


    with coluna2:

        st.image(
            IMAGEM_MUSICA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR MÚSICA
# =========================================================

elif menu == "➕ Cadastrar Música":

    st.markdown(
"""
<div class="page-title">
➕ Nova música
</div>

<div class="page-subtitle">
Adicione uma nova música à sua biblioteca.
</div>
""",
unsafe_allow_html=True
)


    with st.form(
        "cadastro_musica",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            musica = st.text_input(
                "🎵 Nome da música"
            )

            artista = st.text_input(
                "🎤 Artista"
            )

            album = st.text_input(
                "💿 Álbum"
            )


        with col2:

            ano = st.number_input(
                "📅 Ano de lançamento",
                min_value=1900,
                max_value=2035,
                value=2024,
                step=1
            )

            genero = st.selectbox(
                "🎶 Gênero musical",
                [
                    "K-pop",
                    "Pop",
                    "Rock",
                    "MPB",
                    "Rap",
                    "Hip Hop",
                    "R&B",
                    "Indie",
                    "Eletrônica",
                    "Clássica",
                    "Metal",
                    "Outro"
                ]
            )

            duracao = st.text_input(
                "⏱️ Duração",
                placeholder="Ex.: 3:45"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR MÚSICA"
        )


    if cadastrar:

        if (
            musica.strip()
            and artista.strip()
        ):

            nova_musica = pd.DataFrame(
                [{
                    "Musica": musica.strip(),
                    "Artista": artista.strip(),
                    "Album": album.strip(),
                    "Ano": int(ano),
                    "Genero": genero,
                    "Duracao": duracao.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    nova_musica
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🎵 Música cadastrada com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha o nome da música e o artista."
            )


# =========================================================
# MÚSICAS CADASTRADAS
# =========================================================

elif menu == "🎧 Músicas Cadastradas":

    st.markdown(
"""
<div class="page-title">
🎧 Minha biblioteca
</div>

<div class="page-subtitle">
Consulte e pesquise suas músicas cadastradas.
</div>
""",
unsafe_allow_html=True
)


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🎵 Nenhuma música cadastrada
</h2>

<p>
Sua biblioteca ainda está vazia.
Cadastre sua primeira música para começar.
</p>

</div>
""",
unsafe_allow_html=True
)


    else:

        busca = st.text_input(
            "🔎 Pesquisar música",
            placeholder="Digite música, artista, álbum ou gênero..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False,
                        regex=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        opcoes_musicas = df.index.tolist()


        musica_excluir = st.selectbox(
            "🗑️ Selecione uma música para excluir",
            options=opcoes_musicas,
            format_func=lambda indice:
                f"{df.loc[indice, 'Musica']} - "
                f"{df.loc[indice, 'Artista']}"
        )


        if st.button(
            "🗑️ EXCLUIR MÚSICA"
        ):

            df = df.drop(
                musica_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🎵 Música excluída com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

🎵 MusicHub<br>
Sua música, organizada.

</div>
""",
unsafe_allow_html=True
)
# SEÇÃO 1: IMPORTAÇÃO DE BIBLIOTECAS
# streamlit (st): Framework web para criar aplicações interativas com Python
# pandas (pd): Biblioteca para manipulação de dados em formato tabular (como Excel)
# plotly.express (px): Biblioteca para criar gráficos interativos profissionais
import streamlit as st
import pandas as pd
import plotly.express as px

# SEÇÃO 2: INTERFACE INICIAL
# Cria título principal da aplicação usando componente title do Streamlit
st.title('Análise de KPIs de Anúncios') #st.title(): Cria título principal

# Widget para upload de arquivo. Cria um campo para fazer upload de arquivo CSV
# file_uploader: Permite ao usuário fazer upload de arquivos
# type=["csv"]: Restringe tipos de arquivo aceitos apenas para CSV
uploaded_file = st.file_uploader("Envie um arquivo CSV", type=["csv"])

# SEÇÃO 3: PROCESSAMENTO DE DADOS
# Verifica se algum arquivo foi carregado
if uploaded_file is not None:#if uploaded_file is not None: Verifica se arquivo foi enviado
    # Lê o arquivo CSV em um DataFrame pandas
    df = pd.read_csv(uploaded_file)
    '''
    DataFrame (df)
    É uma estrutura de dados tabular (como uma planilha Excel)
    Criado pela biblioteca pandas
    Exemplo: df = pd.read_csv(uploaded_file)
    '''

    # SEÇÃO 3.1: LIMPEZA E CONVERSÃO DE DADOS
    # Converte coluna 'Date' para formato datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
     # Remove o "R$ " da coluna 'Amount_spent' e converte para número decimal
    df['Amount_spent'] = df['Amount_spent'].replace({'R$ ': ''}, regex=True).astype(float)
    # Converte 'Link_clicks' para números inteiros, substituindo valores inválidos por 0
    df['Link_clicks'] = pd.to_numeric(df['Link_clicks'], errors='coerce').fillna(0).astype(int)
    # Converte 'Conversions' para números inteiros, substituindo valores inválidos por 0
    df['Conversions'] = pd.to_numeric(df['Conversions'], errors='coerce').fillna(0).astype(int)

    '''
    Manipulação de Dados

    pd.to_datetime(): Converte texto para formato de data
    astype(): Muda o tipo de dados de uma coluna
    fillna(0): Substitui valores vazios (NA/NaN) por 0
    regex=True: Habilita uso de expressões regulares para busca de padrões em texto
    errors='coerce': Transforma erros em valores nulos ao invés de dar erro
    '''
    
    # SEÇÃO 3.2: CÁLCULO DE KPIs(Indicadores-Chave de Performance) PRINCIPAIS
    # Agrupa dados por mês e calcula somas
    # KPI1: Soma dos gastos por mês
    kpi1 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount_spent'].sum()
    # KPI2: Soma das conversões por mês
    kpi2 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Conversions'].sum()
    # KPI3: Soma dos cliques por mês
    kpi3 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Link_clicks'].sum()
    # KPI4: Custo por conversão mensal (gasto total / número de conversões)
    kpi4 = (df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount_spent'].sum() / 
            df.groupby(df['Date'].dt.strftime('%Y-%m'))['Conversions'].sum()).fillna(0)
    
    '''
    Funções de Agrupamento
    dt.strftime('%Y-%m'): Formata data como ano-mês
    groupby(): Agrupa dados por uma ou mais colunas
    sum(): Soma valores
    max(): Encontra valor máximo
    mean(): Calcula média
    '''
    
    # SEÇÃO 4: VISUALIZAÇÃO DOS DADOS
    # Mostra uma tabela com as primeiras linhas dos dados
    st.write("### Amostra dos Dados")#st.write(): Mostra texto ou dados
    st.dataframe(df.head())

    # SEÇÃO 4.1: DISPLAY DE MÉTRICAS
    # Cria 4 colunas para mostrar KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Mês com Maior Gasto", value=str(kpi1.idxmax()))
    with col2:
        st.metric(label="Total de Conversões no Mês com Mais Gasto", value=int(kpi2.max()))
    with col3:
        st.metric(label="Total de Cliques no Mês com Mais Gasto", value=int(kpi3.max()))
    with col4:
        st.metric(label="Custo por Conversão Médio", value=f"R$ {kpi4.mean():.2f}")
    #st.metric(): Mostra métricas em cards
    #with col1:: Contexto para trabalhar dentro de uma coluna
    #st.columns(): Divide tela em colunas
    
    # SEÇÃO 4.2: GRÁFICOS DE ANÁLISE
    # Gráfico de linha para gastos diários
    st.write("### Gasto Diário com Marketing")#st.write(): Mostra texto ou dados
    st.line_chart(df.groupby('Date')['Amount_spent'].sum())#line_chart(): Gráfico de linha
    
    # Gráfico de barras para gastos por segmentação
    st.write("### Gasto por Segmentação")
    segmentacao_gasto = df.groupby('Segmentação')['Amount_spent'].sum().sort_values(ascending=False)
    st.bar_chart(segmentacao_gasto)#bar_chart(): Gráfico de barras

    # SEÇÃO 5: CÁLCULOS DE KPIs AVANÇADOS
    # CPC (Custo por Clique) = Gasto / Número de Cliques
    df["CPC"] = (df["Amount_spent"] / df["Link_clicks"]).replace([float("inf"), float("nan")], 0)
    # CPM (Custo por Mil Impressões) = (Gasto / Impressões) * 1000
    df["CPM"] = (df["Amount_spent"] / df["Impressions"] * 1000).replace([float("inf"), float("nan")], 0)
    # CPA (Custo por Aquisição) = Gasto / Conversões
    df["CPA"] = (df["Amount_spent"] / df["Conversions"]).replace([float("inf"), float("nan")], 0)
    # CTR (Taxa de Cliques) = (Cliques / Impressões) * 100
    df["CTR (%)"] = (df["Link_clicks"] / df["Impressions"] * 100).replace([float("inf"), float("nan")], 0)
    # Taxa de Conversão = (Conversões / Cliques) * 100
    df["Conversion Rate (%)"] = (df["Conversions"] / df["Link_clicks"] * 100).replace([float("inf"), float("nan")], 0)

    '''
    Cálculos de KPIs (Indicadores-Chave de Performance)

    CPC (Custo por Clique) = Gasto ÷ Número de Cliques
    CPM (Custo por Mil Impressões) = (Gasto ÷ Impressões) × 1000
    CPA (Custo por Aquisição) = Gasto ÷ Conversões
    CTR (Taxa de Cliques) = (Cliques ÷ Impressões) × 100
    Taxa de Conversão = (Conversões ÷ Cliques) × 100
    '''

    # SEÇÃO 6: ANÁLISE MENSAL INTERATIVA
    st.subheader("🔍 Interactive Monthly Analysis")
    # Extrai nome do mês da coluna Date
    df["Month"] = df["Date"].dt.month_name()#dt.month_name(): Extrai nome do mês
    # Lista de meses únicos
    months = df["Month"].unique().tolist()
    # Cria seletor de mês. Cria uma caixa de seleção para escolher o mês
    selected_month = st.selectbox("Select Month for Analysis", months)#st.selectbox(): Cria menu suspenso para seleção

    # Opções de métricas para análise
    column_options = ["Amount_spent", "Link_clicks", "Impressions", "Conversions"]
    selected_column = st.selectbox("Select KPI for Analysis", column_options)#st.selectbox(): Cria menu suspenso para seleção

    # Filtra dados do mês selecionado
    monthly_df = df[df["Month"] == selected_month]
    # Agrupa dados por dia
    daily_summary = monthly_df.groupby(df["Date"].dt.day)[selected_column].sum().reset_index()
    daily_summary.columns = ["Day", selected_column]

    # Cria gráfico de barras interativo
    #px.bar(): Gráfico de barras interativo do Plotly
    fig_monthly = px.bar(
        daily_summary,
        x="Day",
        y=selected_column,
        title=f"Daily {selected_column} in {selected_month}",
        labels={"Day": "Day of Month", selected_column: selected_column},
    )

    # Mostra gráfico na interface
    st.plotly_chart(fig_monthly)#st.plotly_chart(): Mostra gráfico interativo

else:
    # Mensagem quando nenhum arquivo foi carregado
    st.write("Por favor, envie um arquivo CSV para análise.")
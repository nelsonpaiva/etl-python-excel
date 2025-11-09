# Importação das bibliotecas necessárias:
# streamlit (st) - biblioteca para criar interfaces web interativas
# pandas (pd) - biblioteca para manipulação e análise de dados
# plotly.express (px) - biblioteca para criar gráficos interativos
import streamlit as st
import pandas as pd
import plotly.express as px

# Cria um título na página web
st.title('Análise de KPIs de Anúncios')

# Cria um campo para fazer upload de arquivo CSV
# type=["csv"] especifica que só aceita arquivos .csv
uploaded_file = st.file_uploader("Envie um arquivo CSV", type=["csv"])

# Verifica se algum arquivo foi enviado
if uploaded_file is not None:
    # Lê o arquivo CSV e armazena em um DataFrame (tabela de dados)
    df = pd.read_csv(uploaded_file)

    # Processamento dos dados:
    # Converte a coluna 'Date' para formato de data
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Remove o "R$ " da coluna 'Amount_spent' e converte para número decimal
    df['Amount_spent'] = df['Amount_spent'].replace({'R$ ': ''}, regex=True).astype(float)
    # Converte 'Link_clicks' para números inteiros, substituindo valores inválidos por 0
    df['Link_clicks'] = pd.to_numeric(df['Link_clicks'], errors='coerce').fillna(0).astype(int)
    # Converte 'Conversions' para números inteiros, substituindo valores inválidos por 0
    df['Conversions'] = pd.to_numeric(df['Conversions'], errors='coerce').fillna(0).astype(int)
    
    # Cálculo dos KPIs (Indicadores-Chave de Performance):
    # KPI1: Soma dos gastos por mês
    kpi1 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount_spent'].sum()
    # KPI2: Soma das conversões por mês
    kpi2 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Conversions'].sum()
    # KPI3: Soma dos cliques por mês
    kpi3 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Link_clicks'].sum()
    # KPI4: Custo por conversão mensal (gasto total / número de conversões)
    kpi4 = (df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount_spent'].sum() / 
            df.groupby(df['Date'].dt.strftime('%Y-%m'))['Conversions'].sum()).fillna(0)
    
    # Mostra uma tabela com as primeiras linhas dos dados
    st.write("### Amostra dos Dados")
    st.dataframe(df.head())

    # Cria 4 colunas para mostrar métricas importantes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Mês com Maior Gasto", value=str(kpi1.idxmax()))
    with col2:
        st.metric(label="Total de Conversões no Mês com Mais Gasto", value=int(kpi2.max()))
    with col3:
        st.metric(label="Total de Cliques no Mês com Mais Gasto", value=int(kpi3.max()))
    with col4:
        st.metric(label="Custo por Conversão Médio", value=f"R$ {kpi4.mean():.2f}")
    
    # Cria um gráfico de linha mostrando gastos ao longo do tempo
    st.write("### Gasto Diário com Marketing")
    st.line_chart(df.groupby('Date')['Amount_spent'].sum())
    
    # Cria um gráfico de barras mostrando gastos por segmentação
    st.write("### Gasto por Segmentação")
    segmentacao_gasto = df.groupby('Segmentação')['Amount_spent'].sum().sort_values(ascending=False)
    st.bar_chart(segmentacao_gasto)

    # Cálculo de métricas adicionais:
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

    # Análise Mensal Interativa:
    st.subheader("🔍 Interactive Monthly Analysis")
    # Extrai o nome do mês da coluna Date
    df["Month"] = df["Date"].dt.month_name()
    # Lista de meses únicos
    months = df["Month"].unique().tolist()
    # Cria uma caixa de seleção para escolher o mês
    selected_month = st.selectbox("Select Month for Analysis", months)

    # Opções de métricas para análise
    column_options = ["Amount_spent", "Link_clicks", "Impressions", "Conversions"]
    selected_column = st.selectbox("Select KPI for Analysis", column_options)

    # Filtra dados do mês selecionado
    monthly_df = df[df["Month"] == selected_month]
    # Agrupa dados por dia do mês
    daily_summary = monthly_df.groupby(df["Date"].dt.day)[selected_column].sum().reset_index()
    daily_summary.columns = ["Day", selected_column]

    # Cria gráfico de barras interativo usando Plotly
    fig_monthly = px.bar(
        daily_summary,
        x="Day",
        y=selected_column,
        title=f"Daily {selected_column} in {selected_month}",
        labels={"Day": "Day of Month", selected_column: selected_column},
    )

    # Mostra o gráfico na interface
    st.plotly_chart(fig_monthly)

else:
    # Mensagem caso nenhum arquivo tenha sido enviado
    st.write("Por favor, envie um arquivo CSV para análise.")
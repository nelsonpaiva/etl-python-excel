# Validador de Dados de Campanhas

Resumo
- Projeto para validar, analisar e gerar relatórios de profiling de bases CSV de campanhas publicitárias.
- Gera relatórios em HTML (profiling) e fornece uma aplicação web interativa (Streamlit) para visualização e validação de KPIs.

Principais funcionalidades
- Leitura e limpeza de CSVs de campanhas.
- Cálculo de KPIs principais: gastos, conversões, cliques, custo por conversão, CPC, CPM, CPA, CTR e taxa de conversão.
- Relatórios de profiling (offline) e dashboard interativo via Streamlit com gráficos e filtros mensais.
- Exemplo mínimo de validador com Pydantic para testes.

Estrutura do repositório
- main.py — Script para gerar relatório de profiling (HTML) a partir de um CSV.
- requirements.txt — Lista de dependências do projeto.
- data.csv, data_2025.csv — Exemplos de datasets (se presentes).
- output.html — Exemplo de relatório gerado por profiling.
- app_dashboard.py — Dashboard Streamlit comentado e usado para análise interativa.
- app_dashboard_comentado.py — Versão do dashboard com comentários detalhados linha-a-linha.
- src/aplicacao_completa.py — Aplicação Streamlit alternativa (se existente).
- src/validador.py — Validador principal (ex.: PlanilhaVendas) com regras de validação do esquema.
- src/validador_hello_world.py — Exemplo mínimo de uso de validador (Pydantic).

Pré-requisitos
- Python 3.8+ (recomendado 3.9/3.10+)
- Git (opcional)

Instalação (Windows)
1. Clonar repositório (opcional):
   - git clone <url-do-repo>
2. Criar e ativar um ambiente virtual:
   - python -m venv .venv
   - .venv\Scripts\activate
3. Instalar dependências:
   - pip install -r requirements.txt

Como usar

1) Geração de relatório de profiling (offline)
- Objetivo: gerar um relatório HTML com estatísticas automáticas (ydata-profiling ou pandas-profiling dependendo do requirements).
- Como:
  - Coloque seu CSV no diretório do projeto (ou ajuste o caminho em main.py).
  - Execute no terminal:
    - python main.py
  - Saída: arquivo output.html (abra no navegador para visualizar).

2) Dashboard interativo (Streamlit)
- Objetivo: analisar e validar dados de campanhas via interface web.
- Como:
  - Execute:
    - streamlit run app_dashboard.py
    - ou, se usar a versão em src:
      - streamlit run src/aplicacao_completa.py
  - Na interface, faça upload do CSV e use os controles (seleção de mês, KPI) para inspecionar dados e gráficos.

Formato esperado do CSV
- Colunas recomendadas (nomes exatos usados pelo código):
  - Date — data da linha (ex.: 2025-01-15 ou 15/01/2025)
  - Amount_spent — gasto (ex.: "R$ 1234.56" ou "1234.56")
  - Link_clicks — número de cliques no link (inteiro)
  - Conversions — número de conversões (inteiro)
  - Impressions — número de impressões (inteiro)
  - Segmentação — texto indicando o público/segmento (opcional para agrupamento)
- Observações:
  - O código tenta limpar prefixos como "R$ " e converter para float.
  - Datas são convertidas com pd.to_datetime(..., errors='coerce'): valores inválidos viram NaN.
  - Colunas numéricas são convertidas com pd.to_numeric(..., errors='coerce') e NaNs são preenchidos com 0 quando aplicável.

Boas práticas para CSV
- Use ponto (.) como separador decimal (ex.: 1234.56) ou ajuste a leitura caso use vírgula.
- Evite células vazias em colunas críticas (Date, Amount_spent). Se houver, essas linhas podem ser ignoradas ou gerar NaN.
- Certifique-se dos nomes das colunas — o código usa exatamente os nomes acima.

Glossário dos termos técnicos (explicações simples)
- DataFrame (df): tabela de dados (linhas × colunas) fornecida pela biblioteca pandas.
- regex: abreviação para "expressões regulares" — padrão de busca/substituição em texto (ex.: remover "R$ ").
- astype(): método do pandas para alterar o tipo de dados de uma coluna (ex.: transformar string em float ou int).
- pd.to_datetime(): função que converte texto/strings em objetos de data/hora.
- pd.to_numeric(): converte strings para valores numéricos; errors='coerce' transforma entradas inválidas em NaN.
- fillna(0): substitui valores NaN (ausentes) por 0.
- groupby(): agrupa linhas por uma coluna (ex.: por mês) para aplicar agregações como sum(), mean().
- dt.strftime('%Y-%m'): formata datas para texto no formato "YYYY-MM" (útil para agrupar por mês).
- idxmax(): retorna o índice (ex.: mês) onde a série teve o maior valor.
- NaN: "Not a Number" — representa valores ausentes ou inválidos.
- inf: infinito — aparece em divisão por zero; geralmente tratado/convertido para 0.
- KPI: Indicador-Chave de Performance (ex.: CPC, CPM, CPA, CTR).
  - CPC (Custo por Clique) = gasto / cliques
  - CPM (Custo por Mil Impressões) = (gasto / impressões) * 1000
  - CPA (Custo por Aquisição) = gasto / conversões
  - CTR (Click-Through Rate) = (cliques / impressões) * 100

Tratamento de erros / problemas comuns
- Erro: coluna não encontrada
  - Verifique nomes das colunas do CSV; use exatamente os nomes esperados ou ajuste o código.
- Erro: formato de data inválido
  - Ajuste o formato do CSV ou pré-processo antes de subir; o pd.to_datetime com errors='coerce' marcará como NaT (data nula).
- Valores infinitos ou NaN em KPIs
  - O código substitui inf/NaN por 0 em métricas calculadas para evitar falhas na exibição.

Desenvolvimento e contribuição
- Para adicionar novas regras de validação, edite src/validador.py (ou crie novos validadores com Pydantic).
- Para melhorar a UI, altere app_dashboard.py ou src/aplicacao_completa.py.
- Sinta-se livre para abrir issues ou pull requests com sugestões e correções.

Execução de testes (se houver)
- Se o projeto incluir testes, execute:
  - python -m pytest
  - Ajuste conforme a estrutura de testes do repositório.

Licença
- Defina a licença do projeto conforme sua preferência (por exemplo MIT, Apache-2.0). Atualize este arquivo com a informação de licença.

Contato
- Para dúvidas ou alterações, abra uma issue no repositório ou contacte o responsável pelo projeto.

------
Observação final: este README traz orientações práticas para uso e manutenção com base no código presente (dashboard Streamlit, validadores e scripts de profiling). Ajuste caminhos e nomes de arquivos caso tenha personalizado a estrutura do projeto.
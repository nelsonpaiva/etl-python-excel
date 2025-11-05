...existing code...
# Validador de Dados de Campanhas

Resumo curto
- Projeto para validar e gerar relatórios de profiling de bases CSV de campanhas (ex.: [data.csv](data.csv), [data_2025.csv](data_2025.csv)).
- Gera relatório de profiling em HTML ([output.html](output.html)) e fornece uma aplicação web simples para validação via Streamlit.

Arquivos principais
- [main.py](main.py) — script que gera relatório de profiling usando ydata-profiling.
- [requirements.txt](requirements.txt) — dependências do projeto.
- [data.csv](data.csv) e [data_2025.csv](data_2025.csv) — exemplos de datasets usados.
- [output.html](output.html) — exemplo de relatório gerado.
- [src/aplicacao_completa.py](src/aplicacao_completa.py) — aplicação Streamlit; funções principais: [`aplicacao_completa.validar_dados`](src/aplicacao_completa.py) e [`aplicacao_completa.main`](src/aplicacao_completa.py).
- [src/validador.py](src/validador.py) — modelo/validador principal: [`validador.PlanilhaVendas`](src/validador.py).
- [src/validador_hello_world.py](src/validador_hello_world.py) — exemplo de validador mínimo / teste.

Pré-requisitos
- Python 3.x
- Recomenda-se criar um virtualenv:
  - python -m venv .venv
  - .venv\Scripts\activate (Windows) ou source .venv/bin/activate (macOS/Linux)
- Instalar dependências:
  - pip install -r [requirements.txt](requirements.txt)

Como usar

1) Gerar relatório de profiling (offline)
- Coloque seu CSV no diretório do projeto ou ajuste o caminho em [main.py](main.py).
- Executar:
  - python [main.py](main.py)
- Saída: [output.html](output.html)

2) Validar dados via Streamlit (interface web)
- Executar:
  - streamlit run [src/aplicacao_completa.py](src/aplicacao_completa.py)
- Na interface, faça upload do CSV (por exemplo [data.csv](data.csv)) e clique em "Validar Dados".
- A validação usa o validador definido em [`validador.PlanilhaVendas`](src/validador.py) e a função [`aplicacao_completa.validar_dados`](src/aplicacao_completa.py).

Notas rápidas
- As regras e modelo de validação estão em [src/validador.py](src/validador.py). Ajuste [`validador.PlanilhaVendas`](src/validador.py) conforme seus requisitos de esquema/negócio.
- Para gerar profiling com parâmetros personalizados, edite [main.py](main.py).

Contribuição
- Abrir issue ou ajustar código em [src/validador.py](src/validador.py) para adicionar novas checagens de validação.
- Testes e melhorias de UI podem ser adicionados em [src/aplicacao_completa.py](src/aplicacao_completa.py).

Licença
- Definir conforme necessidade do projeto.
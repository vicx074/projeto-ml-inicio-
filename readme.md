# Previsão de Falha de Máquinas

Este projeto utiliza **Machine Learning** para prever falhas em máquinas industriais com base em dados históricos. A aplicação foi desenvolvida com **Streamlit**, uma biblioteca Python que permite criar interfaces web interativas de forma simples e eficiente.

## Novidade: Compatibilidade com Streamlit Cloud e Python 3.13+

- **Agora o projeto utiliza o módulo padrão `pickle` para salvar e carregar arquivos de modelo, scaler e colunas.**
- **O uso de `joblib` foi removido para evitar incompatibilidades com versões recentes do Python (ex.: 3.13+), especialmente no Streamlit Community Cloud.**
- **Certifique-se de que os arquivos `modelo_treinado.pkl`, `scaler.pkl` e `treino_cols.pkl` foram salvos usando `pickle.dump` e carregados com `pickle.load`.**

## Funcionalidades

- **Treinamento de Modelo:** Utiliza **Random Forest** para classificação de falhas.
- **Interface Web:** Aplicação interativa via **Streamlit** para upload de dados e visualização dos resultados.
- **Exportação de Resultados:** Permite baixar as previsões em formato Excel diretamente pela interface.
- **Visualização:** Exibe matriz de confusão, relatório de classificação e importância das variáveis.

## Como Funciona o Streamlit

O **Streamlit** é uma biblioteca que transforma scripts Python em aplicativos web interativos. Ele funciona com base em uma abordagem declarativa, onde cada execução do script atualiza a interface. Alguns pontos importantes:
- **Reatividade:** Qualquer interação do usuário (como upload de arquivos ou ajuste de sliders) dispara uma nova execução do script.
- **Widgets:** Elementos como `st.file_uploader` e `st.slider` permitem capturar entradas do usuário.
- **Renderização:** Funções como `st.write` e `st.dataframe` são usadas para exibir dados e resultados diretamente na interface.

## Como Usar

1. **Preparação dos Dados**
   - Certifique-se de que o arquivo Excel de entrada segue o mesmo formato do arquivo de treino ([`dados_maquinas.xlsx`](dados_maquinas.xlsx )).
   - As colunas devem ser compatíveis com o modelo treinado.

2. **Execução do App**
   - Instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```
   - Execute o aplicativo:
     ```bash
     streamlit run app.py
     ```
   - Acesse o navegador no endereço exibido pelo Streamlit (geralmente `http://localhost:8501`).

3. **Upload e Previsão**
   - Faça upload do arquivo Excel com os dados das máquinas.
   - Ajuste o limiar de probabilidade para falha usando o slider na barra lateral.
   - Visualize os resultados diretamente na interface.
   - Baixe os resultados em formato Excel.

## Estrutura dos Arquivos

- [`app.py`](app.py ): Aplicação principal Streamlit.
- [`treimaneto.ipynb`](treimaneto.ipynb ): Notebook de treinamento e análise exploratória.
- [`dados_maquinas.xlsx`](dados_maquinas.xlsx ): Exemplo de dados de entrada.
- [`modelo_treinado.pkl`](modelo_treinado.pkl ): Modelo treinado (salvo com `pickle`).
- [`scaler.pkl`](scaler.pkl ): Scaler utilizado na normalização dos dados (salvo com `pickle`).
- [`treino_cols.pkl`](treino_cols.pkl ): Lista de colunas usadas no treinamento (salvo com `pickle`).

## Requisitos

- Python 3.8+
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Seaborn
- Matplotlib
- Openpyxl

Instale todos os pacotes com:
```bash
pip install -r requirements.txt
```

> **Nota:** Não é mais necessário instalar o `joblib`. Todos os arquivos `.pkl` devem ser manipulados com o módulo padrão `pickle`.

## Fluxo do Projeto

1. **Treinamento:** Execute o notebook para treinar o modelo e salve os arquivos `.pkl` usando `pickle.dump`.
2. **Previsão:** Use o app Streamlit para realizar previsões em novos dados. Os arquivos são carregados com `pickle.load`.

## Observações Técnicas

- **Compatibilidade de Colunas:** O app ajusta automaticamente as colunas dos dados de entrada para coincidir com as colunas usadas no treinamento, garantindo que o modelo funcione corretamente.
- **Normalização:** Os dados numéricos são escalados usando o `StandardScaler` antes de serem enviados ao modelo.
- **Limiar de Classificação:** O slider permite ajustar o limiar de probabilidade para classificar máquinas como falha ou não, tornando o modelo mais flexível.
- **Exportação:** O arquivo Excel é gerado em memória usando `BytesIO` e pode ser baixado diretamente pela interface.

## Implantação na Streamlit Community Cloud

- O projeto está pronto para ser implantado no [Streamlit Community Cloud](https://streamlit.io/cloud).
- Certifique-se de que o arquivo `requirements.txt` está simplificado e não possui dependências desnecessárias ou restrições de versão.
- Todos os arquivos `.pkl` devem ser salvos e carregados com `pickle`.
- Para outros ambientes (Heroku, Railway, Render), siga as instruções de implantação específicas de cada plataforma.

## Exemplos de Uso

- **Manutenção Preditiva:** Identificar máquinas com maior probabilidade de falha para priorizar manutenção preventiva.
- **Otimização Operacional:** Reduzir custos operacionais ao evitar falhas inesperadas.

## Extensões e Adaptações

Este projeto pode ser adaptado para diferentes cenários de chão de fábrica ou análise de dados industriais:

1. **Integração com Banco de Dados:**
   - Substitua o upload de arquivos Excel por uma conexão direta com um banco de dados (ex.: MySQL, PostgreSQL).
   - Utilize bibliotecas como `sqlalchemy` ou `psycopg2` para realizar consultas e carregar os dados diretamente no app.
   - Exemplo de código para carregar dados:
     ```python
     from sqlalchemy import create_engine
     engine = create_engine("postgresql://usuario:senha@host:porta/banco")
     query = "SELECT * FROM dados_maquinas"
     df_new = pd.read_sql(query, engine)
     ```

2. **Monitoramento em Tempo Real:**
   - Adicione um cron job ou utilize bibliotecas como `apscheduler` para atualizar os dados periodicamente.
   - Integre com APIs de sensores IoT para capturar dados em tempo real.

3. **Análise de Manutenções:**
   - Adicione colunas relacionadas a histórico de manutenção e use-as como features adicionais no modelo.
   - Exemplo: `ultima_manutencao`, `tempo_desde_ultima_manutencao`.

4. **Visualização Avançada:**
   - Utilize bibliotecas como `plotly` ou `altair` para criar gráficos interativos e dashboards mais detalhados.
   - Exemplo de gráfico:
     ```python
     import plotly.express as px
     fig = px.bar(df_result, x='Máquina', y='Probabilidade_Falha', color='Previsao_Falha')
     st.plotly_chart(fig)
     ```

5. **Relatórios Automatizados:**
   - Gere relatórios em PDF com bibliotecas como `reportlab` ou `fpdf`.
   - Envie os relatórios automaticamente por e-mail usando `smtplib`.

---

**Desenvolvido por:**  
Victor Eduardo  
[LinkedIn](https://www.linkedin.com/in/victoreduardopereiramorais/)

---

Sinta-se à vontade para personalizar este README conforme necessário!

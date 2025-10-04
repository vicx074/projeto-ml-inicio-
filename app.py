import streamlit as st
import pandas as pd
import joblib, io
import numpy as np




st.title("Previsão de Falha de Máquinas")

# crregar modelo e scaler
modelo = joblib.load("modelo_treinado.pkl")
scaler = joblib.load("scaler.pkl")

st.write(" Faça upload do arquivo Excel com os dados das máquinas (mesmo formato do treino).")

uploaded_file = st.file_uploader("Escolha o Excel", type=["xlsx"])

if uploaded_file:
    df_new = pd.read_excel(uploaded_file)
    st.write("Dados carregados:")
    st.dataframe(df_new.head())

    # separar features
    if "falhou" in df_new.columns:
        X_new = df_new.drop(columns=['falhou'])
    else:
        X_new = df_new.copy()

    X_num = X_new.select_dtypes(include=['int64','float64'])
    X_cat = X_new.select_dtypes(include=['object','category'])
    X_cat_encoded = pd.get_dummies(X_cat, drop_first=True)
    X_processed = pd.concat([X_num, X_cat_encoded], axis=1)

    # ajustar colunas para coincidir com treino
    treino_cols = joblib.load("treino_cols.pkl")
    treino_cols = pd.Index(treino_cols).drop_duplicates()
    X_processed = X_processed.loc[:, ~X_processed.columns.duplicated()]
    X_processed = X_processed.reindex(columns=treino_cols, fill_value=0)

    X_scaled = scaler.transform(X_processed)

    # previsão
    y_pred = modelo.predict(X_scaled)
    y_prob = modelo.predict_proba(X_scaled)[:,1]

    threshold = st.sidebar.slider("Limiar de probabilidade para falha", 0.0, 1.0, 0.5)
    df_result = X_new.copy()
    df_result['Previsao_Falha'] = (y_prob >= threshold).astype(int)
    df_result['Probabilidade_Falha'] = np.round(y_prob, 2)

    st.write("✅ Resultados da previsão:")
    st.dataframe(df_result)

    # Adicionar interpretação dos resultados
    st.write("💡 Interpretação: 1 = Máquina com previsão de falha, 0 = Máquina sem previsão de falha")
    st.write(f"📊 Total de máquinas analisadas: {len(df_result)}")
    st.write(f"🔴 Máquinas com previsão de falha: {df_result['Previsao_Falha'].sum()}")

    # Verificar se o DataFrame não está vazio antes de gerar o Excel
    if not df_result.empty:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df_result.to_excel(writer, index=False)
        buffer.seek(0)

        st.download_button(
            label="Baixar resultados em Excel",
            data=buffer,
            file_name="previsao_maquinas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.write("⚠️ O DataFrame está vazio. Não foi possível gerar o arquivo Excel.")
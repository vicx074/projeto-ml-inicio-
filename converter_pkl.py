"""
Script para converter arquivos .pkl salvos com joblib para formato pickle puro
"""
import pickle
import joblib
import sys

def convert_joblib_to_pickle(file_path):
    """
    Carrega um arquivo usando joblib e salva novamente usando pickle puro
    """
    print(f"Convertendo {file_path}...")
    try:
        # Tenta carregar com joblib
        data = joblib.load(file_path)
        
        # Salva com pickle
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
        
        print(f"✅ Arquivo {file_path} convertido com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao converter {file_path}: {e}")
        return False

if __name__ == "__main__":
    # Lista de arquivos para converter
    files_to_convert = [
        "modelo_treinado.pkl",
        "scaler.pkl",
        "treino_cols.pkl"
    ]
    
    print("Iniciando conversão dos arquivos .pkl de joblib para pickle...")
    success_count = 0
    
    for file in files_to_convert:
        if convert_joblib_to_pickle(file):
            success_count += 1
    
    print(f"\nConversão finalizada: {success_count}/{len(files_to_convert)} arquivos convertidos com sucesso.")
    print("\nAgora você pode fazer deploy no Streamlit Community Cloud sem problemas de compatibilidade.")

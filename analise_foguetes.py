import pandas as pd

# Carrega o arquivo de dados
df = pd.read_csv('Moonlanding.csv')

# Atividade 1: Frequência de uso
frequencia_foguetes = df['Carrier Rocket'].value_counts()
print("--- Atividade 1: Frequência de uso por modelo de foguete ---")
print(frequencia_foguetes)

# Atividade 2: Média de utilizações
media_uso = frequencia_foguetes.mean()
print("\n--- Atividade 2: Média de utilizações por modelo ---")
print(f"Em média, cada modelo de foguete foi utilizado {media_uso:.2f} vezes.")

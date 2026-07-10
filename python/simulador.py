import sqlite3
import random
import time

def calcular_media_umidade():
    conexao = sqlite3.connect("horta.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT umidade FROM leituras ORDER BY id DESC LIMIT 3")
    resultados = cursor.fetchall()
    conexao.close()
    
    if len(resultados) < 3:
        return 70.0
        
    soma = sum([linha[0] for linha in resultados])
    return soma / len(resultados)

def rodar_simulador():
    conexao = sqlite3.connect("horta.db")
    cursor = conexao.cursor()
    
    # Tabela 2: Histórico de Alertas da Bomba

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_bomba (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT DEFAULT CURRENT_TIMESTAMP,
            acao TEXT,
            justificativa TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

    print("🌱 Simulador Inteligente Iniciado! Pressione Ctrl+C para parar.\n")

    status_bomba_anterior = None
    while True:
        temp = round(random.uniform(22.0, 31.0), 1)
        umidade_atual = round(random.uniform(50.0, 85.0), 1)
        
        media_recentes = round(calcular_media_umidade(), 1)
        
        if media_recentes < 60.0:
            status_bomba = "LIGADA"
        else:
            status_bomba = "DESLIGADA"
            
        conexao = sqlite3.connect("horta.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO leituras (temperatura, umidade, status_bomba) VALUES (?, ?, ?)",
            (temp, umidade_atual, status_bomba)
        )

        if status_bomba != status_bomba_anterior and status_bomba_anterior is not None:
            justificativa = f"Média das últimas 3 leituras foi de {media_recentes}% (Limite: 60%)"
            cursor.execute(
                "INSERT INTO historico_bomba (acao, justificativa) VALUES (?, ?)",
                (f"Bomba foi {status_bomba}", justificativa)
            )
            print(f"⚠️ [ALERTA]: Mudou para {status_bomba}. Motivo: {justificativa}")

        conexao.commit()
        conexao.close()

        status_bomba_anterior = status_bomba

        print(f"📊 Temp: {temp}°C | Umidade Atual: {umidade_atual}% | Média(3L): {media_recentes}% -> Bomba: {status_bomba}")
        
        time.sleep(3)

if __name__ == "__main__":
    rodar_simulador()
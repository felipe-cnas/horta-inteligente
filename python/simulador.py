import sqlite3
import random
import time
from datetime import datetime

# ==========================================
# 🛠️ CONFIGURAÇÕES E CONSTANTES (Sem números mágicos)
# ==========================================
DB_NAME = "horta.db"
LIMIAR_LIGAR = 55.0     # Liga se a umidade cair abaixo disso
LIMIAR_DESLIGAR = 65.0  # Só desliga se a umidade subir acima disso

# ==========================================
# 🗄️ FUNÇÕES DE BANCO DE DADOS
# ==========================================
def inicializar_banco(conn):
    """Cria as tabelas necessárias se elas não existirem."""
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leituras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT NOT NULL,
                temperatura REAL NOT NULL,
                umidade REAL NOT NULL,
                status_bomba TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historico_bomba (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT NOT NULL,
                acao TEXT NOT NULL,
                justificativa TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("✅ Banco de dados inicializado com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ Erro ao inicializar tabelas: {e}")

def recuperar_ultimo_estado(conn):
    """Recupera o último estado da bomba salvo no banco."""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT status_bomba FROM leituras ORDER BY id DESC LIMIT 1")
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        return "DESLIGADA" 
    except sqlite3.Error:
        return "DESLIGADA"

def calcular_media_umidade(conn):
    """CORREÇÃO: Documentação ajustada para refletir as últimas 10 leituras."""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT umidade FROM leituras ORDER BY id DESC LIMIT 10")
        leituras = cursor.fetchall()
        
        if not leituras:
            return None
            
        soma = sum([row[0] for row in leituras])
        return round(soma / len(leituras), 2)
    except sqlite3.Error as e:
        print(f"⚠️ Erro ao calcular média: {e}")
        return None

# ==========================================
# 🧠 LÓGICA DE CONTROLE (Máquina de Estados)
# ==========================================
def decidir_bomba(media_umidade, estado_anterior):
    """Implementação de Histerese para evitar Flapping."""
    if media_umidade is None:
        return estado_anterior

    if media_umidade < LIMIAR_LIGAR:
        return "LIGADA"
    elif media_umidade > LIMIAR_DESLIGAR:
        return "DESLIGADA"
    else:
        return estado_anterior

# ==========================================
# 🚀 LOOP PRINCIPAL DO SISTEMA
# ==========================================
def rodar_simulador():
    print("🌱 Iniciando o Simulador de Horta Inteligente...")
    
    conn = sqlite3.connect(DB_NAME)
    inicializar_banco(conn)
    
    status_bomba_anterior = recuperar_ultimo_estado(conn)
    print(f"💾 Último estado recuperado do banco: {status_bomba_anterior}")

    try:
        while True:
            temp_atual = round(random.uniform(20.0, 35.0), 2)
            umi_atual = round(random.uniform(40.0, 75.0), 2)
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO leituras (data_hora, temperatura, umidade, status_bomba) VALUES (?, ?, ?, ?)",
                    (data_hora_atual, temp_atual, umi_atual, status_bomba_anterior)
                )
                conn.commit()
                
                # BUGFIX: Captura o ID exato da linha que acabou de ser inserida
                id_leitura_atual = cursor.lastrowid
                
            except sqlite3.Error as e:
                print(f"❌ Erro ao salvar leitura: {e}")
                time.sleep(3)
                continue

            media_umi = calcular_media_umidade(conn)
            novo_status_bomba = decidir_bomba(media_umi, status_bomba_anterior)

            if novo_status_bomba != status_bomba_anterior:
                justificativa = (
                    f"Umidade média ({media_umi}%) abaixo do limite de {LIMIAR_LIGAR}%"
                    if novo_status_bomba == "LIGADA"
                    else f"Umidade média ({media_umi}%) acima do limite de {LIMIAR_DESLIGAR}%"
                )
                
                try:
                    cursor.execute(
                        "INSERT INTO historico_bomba (data_hora, acao, justificativa) VALUES (?, ?, ?)",
                        (data_hora_atual, novo_status_bomba, justificativa)
                    )
                    
                    # BUGFIX: Atualiza o status usando o ID único em vez do timestamp
                    cursor.execute(
                        "UPDATE leituras SET status_bomba = ? WHERE id = ?",
                        (novo_status_bomba, id_leitura_atual)
                    )
                    conn.commit()
                    print(f"🚨 ALERTA: Bomba alterada para {novo_status_bomba}. Motivo: {justificativa}")
                except sqlite3.Error as e:
                    print(f"❌ Erro ao registrar histórico da bomba: {e}")

            print(f"[{data_hora_atual}] Temp: {temp_atual}°C | Umi: {umi_atual}% | Média: {media_umi}% | Bomba: {novo_status_bomba}")
            
            status_bomba_anterior = novo_status_bomba
            time.sleep(3)

    except KeyboardInterrupt:
        print("\n🛑 Simulador encerrado pelo usuário.")
    finally:
        conn.close()
        print("🔌 Conexão com o banco de dados fechada com segurança.")

if __name__ == "__main__":
    rodar_simulador()
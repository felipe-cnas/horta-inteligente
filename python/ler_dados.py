import sqlite3

def ler_historico():
    # Conecta ao banco de dados
    conexao = sqlite3.connect("horta.db")
    cursor = conexao.cursor()
    
	# Busca os últimos 10 registros, incluindo o status da bomba
    cursor.execute("SELECT id, data_hora, temperatura, umidade, status_bomba FROM leituras ORDER BY id DESC LIMIT 10")
    linhas = cursor.fetchall()
    
    # Fecha a conexão
    conexao.close()
    
    # Se o banco estiver vazio
    if not linhas:
        print("📭 Nenhum dado encontrado no banco ainda.")
        return
        
    # Imprime o cabeçalho formatado
    print("-" * 75)
    print(f"{'ID':<5} | {'Data / Hora (UTC)':<20} | {'Temp':<7} | {'Umidade':<9} | {'Status Bomba':<12}")
    print("-" * 75)
    
    # Imprime cada linha do banco de dados
    for linha in linhas:
        id_reg, data_hora, temp, umidade, bomba = linha
        # Garante que se o 'bomba' for None (dados antigos), mostra um aviso
        status_bomba = bomba if bomba else "N/A"
        
        print(f"{id_reg:<5} | {data_hora:<20} | {temp:<5}°C | {umidade:<6}% | {status_bomba:<12}")
        
    print("-" * 75)

if __name__ == "__main__":
    print("📊 Buscando as últimas 10 leituras da horta...\n")
    ler_historico()
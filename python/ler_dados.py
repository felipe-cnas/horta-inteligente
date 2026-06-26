import sqlite3

	# Conecta ao banco de dados horta.db
conn = sqlite3.connect("horta.db")
cursor = conn.cursor()

	# Busca as últimas 10 leituras que foram gravadas
cursor.execute("SELECT * FROM leituras ORDER BY id DESC LIMIT 10")
linhas = cursor.fetchall()

print("\n--- HISTÓRICO DE LEITURAS (ÚLTIMAS 10) ---")
print(f"{'ID':<5} | {'Data/Hora':<20} | {'Umidade':<0} | {'Temp':<6} | {'Luz':<4}")
print("-" * 60)


for linha in linhas:
	# linha[0]=id, linha[1]=data_hora, linha[2]=umidade, linha[3]=temperatura, linha[4]=luminosidade
	print(f"{linha[0]:<5} | {linha[1]:<20} | {linha[2]:<7.1f}% | {linha[3]:<4.1f}°C | {linha[4]:<3}%")
	
	
	
# Fecha a conexão
conn.close()

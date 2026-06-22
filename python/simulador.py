import random
import time

print("--- SIMULADOR AVANÇADO DE MONITORAMENTO DA HORTA---")

	#1.Estado Inicial da Horta (Valores começam estáveis)
umidade_solo = 60.0	#Porcentagem (%)
temperatura = 24.0 #Graus Celsius(°C)
luminosidade = 50	#Porcentagem (%)
bomba_ligada = False
	
while True:
	print("\n[Lendo sensores em tempo real...]")
	
	
	#2. Simulação do Clima (Flutuações naturais e graduais)
	# A luminosidade muda pouco a cada ciclo
	luminosidade = max(0, min(100, luminosidade + random.randint(-10, 10)))
	
	# Se estiver com luminosidade alta (sol), a temperatura tende a subir. Se estiver escuro, ela cai...
	if luminosidade > 60:
		temperatura += random.uniform(0.1, 0.5)
	else:
		temperatura -= random.uniform(0.1, 0.3)
		
	# Limita a temperatura pra não congelar e nem virar um deserto no simulador
	temperatura = max(15.0, min(38.0, temperatura))
	
	#3. Lógica de Causa e Efeito (O ambiente afetando a umidade)
	if bomba_ligada:
		# Se a bomba está ligada, a umidade tende a subir rápido.
		umidade_solo += random.uniform(5.0, 10.0)
		print("💧 [BOMBA ATIVA] Injetando água no solo...")
	else:
		# Se a bomba está desligada o solo seca e acaba secando mais rápido se estiver quente!
		fator_secagem = 0.5 if temperatura > 30 else 0.2
		umidade_solo -= random.uniform(0.1, fator_secagem)
		
	# Limita a umidade entre 0% e 100%
	umidade_solo = max(0.0, min(100.0, umidade_solo))
	
	# Exibe os dados formatados com apenas uma casa decimal
	print(f"Umidade do Solo: {umidade_solo:.1f}%")
	print(f"Temperatura Ambiente: {temperatura:.1f}°C")
	print(f"Luminosidade : {luminosidade}%")
	
	#4. Inteligência da Horta (Tomada de decisão)
	if umidade_solo < 40.0:
		if not bomba_ligada:
			print("⚠️Alerta: Solo seco! Ligue a bomba de água automaticamente.")
			bomba_ligada = True
			
	elif umidade_solo > 75.0:
		if bomba_ligada:
			print("Status: Solo perfeitamente úmido. Desligando a bomba")
			bomba_ligada = False
			
	print("-" * 50)
	time.sleep(2)
	
	


import random
import time

print("---SISTEMA DE MONITORAMENTO DA HORTA---")

#Simulando o funcionamento da horta em loop continuo
while True:
	#1.Simulando a leitura dos sensores com valores aleartórios
	umidade_solo = random.randint(20, 80)
	temperatura = random.randint(18, 35)
	luminosidade = random.randint(10, 100)
	
	print("\n[Lendo sensores...]")
	print(f"Umidade do Solo: {umidade_solo}%")
	print(f"Temperatura Ambiente: {temperatura}°C")
	print(f"Luminosidade: {luminosidade}%")
	
	#2.Lógica de tomada de decisão (Cérebro da horta)
	if umidade_solo < 40:
		print("🚨 ALERTA: Solo seco! Ligando bomba de água...💧")
	else:
		print(" Status: Solo umido. Bomba de agua desligada.")
	
	print("-" * 50)
	
	#Espera 3 segundos antes de fazer a proxima leitura
	time.sleep(3)
	
 

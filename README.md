# 🌿 Horta Inteligente - Monitoramento de Umidade (V1.0)

Este é um ecossistema IoT para monitoramento ambiental focado na saúde de plantas botânicas. O projeto simula a coleta de dados de umidade do solo, armazena as informações em um banco de dados local em tempo real e exibe os resultados em um painel interativo (dashboard) que pode ser acessado tanto pelo computador quanto pelo celular.

## 🚀 Funcionalidades da Versão 1.0
* **Simulador Python:** Gera leituras automáticas de umidade (simulando sensores físicos).
* **Banco de Dados SQLite:** Armazenamento seguro e persistentemente de cada leitura com carimbo de data e hora.
* **Dashboard Streamlit:** Interface visual moderna com indicadores de status da horta.
* **Gráfico Responsivo:** Histórico de umidade otimizado com eixos minimalistas (HH:MM:SS) para perfeita leitura em dispositivos móveis (Safari/Chrome Mobile).

## 🏗️ Arquitetura do Projeto
[ simulador.py ] ───(INSERT)───► [ horta.db ] ◄───(SELECT)─── [ dashboard.py ]
                                                                     │
                                                       (Acesso via Wi-Fi/Rede)
                                                                     ▼
                                                         [ Computador / Celular ]

## 🛠️ Tecnologias Utilizadas
* Python 3.14+
* Streamlit (Interface Gráfica)
* Pandas (Tratamento de Dados)
* SQLite3 (Banco de Dados)

## 💻 Como Rodar o Projeto

### 1. Clonar o repositório
git clone https://github.com/felipe-cnas/horta-inteligente.git
cd horta-inteligente/python

### 2. Executar o Simulador (Gera os dados)
Em um terminal, rode:
python simulador.py

### 3. Executar o Dashboard (Visualizar os dados)
Em outro terminal, rode:
python -m streamlit run dashboard.py

📱 Dica para Celular: Para abrir no celular, certifique-se de que ele está no mesmo Wi-Fi do computador e acesse a Network URL informada pelo Streamlit no terminal (ex: http://192.168.1.199:8501).
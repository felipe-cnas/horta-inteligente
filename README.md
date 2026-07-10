#  Horta Inteligente - Sistema de Monitoramento e Automação



Sistema desenvolvido em Python para simulação de uma horta inteligente, realizando o monitoramento de temperatura e umidade, armazenamento das leituras em banco de dados SQLite e acionamento automático de uma bomba de irrigação com base em regras de automação.



O projeto foi concebido com arquitetura modular para facilitar futuras integrações com dispositivos IoT (ESP32), sensores físicos, dashboards web e serviços em nuvem.



---



## 📌 Objetivo



Desenvolver uma plataforma de monitoramento e automação para hortas inteligentes, iniciando por uma simulação local em Python e evoluindo gradualmente para uma solução IoT completa.



---



##  Funcionalidades



Atualmente o sistema é capaz de:



- Simular leituras de temperatura e umidade

- Armazenar os dados em banco SQLite

- Calcular a média das últimas leituras de umidade

- Acionar automaticamente a bomba de irrigação

- Registrar o histórico das mudanças de estado da bomba

- Registrar justificativas para cada acionamento automático



---



# 🏗 Arquitetura Atual



```

Simulador (Python)

│

▼

Banco SQLite

(horta.db)

│

┌──────────────┴──────────────┐

▼ ▼

Leituras Histórico da Bomba

```



---



# 🗄 Banco de Dados



O projeto utiliza o banco **SQLite** (`horta.db`) com duas tabelas.



## Tabela 'leituras'



Armazena todas as leituras realizadas pelo sistema.



| Campo | Tipo |

|--------|------|

| id | INTEGER |

| data_hora | TEXT |

| temperatura | REAL |

| umidade | REAL |

| status_bomba | TEXT |



---



## Tabela 'historico_bomba'



Armazena apenas mudanças de estado da bomba.



| Campo | Tipo |

|--------|------|

| id | INTEGER |

| data_hora | TEXT |

| acao | TEXT |

| justificativa | TEXT |



---



# ⚙ Funcionamento



A cada ciclo de execução o sistema:



1. Gera uma nova leitura simulada.

2. Consulta as últimas leituras armazenadas.

3. Calcula a média da umidade.

4. Decide automaticamente ligar ou desligar a bomba.

5. Salva a leitura no banco.

6. Registra um evento apenas quando houver mudança de estado da bomba.



---



# 📂 Estrutura Atual do Projeto



```

horta-inteligente/



├── python/

│   ├── simulador.py

│   ├── init_db.py

│   └── .gitkeep (opcional)

│

├── docs/

├── .gitignore

├── LICENSE

├── README.md

└── requirements.txt



---



#  Como executar



Clone o repositório:



```bash

git clone <url-do-repositorio>

```



Entre na pasta do projeto:



```bash

cd horta-inteligente

```



Acesse a pasta Python:



```bash

cd python

```



Execute o simulador:



```bash

python simulador.py

```



---



#  Tecnologias



- Python 3

- SQLite

- sqlite3

- random

- time



---



# 📈 Roadmap



## Backend



- [x] Simulação de sensores

- [x] Banco SQLite

- [x] Registro de leituras

- [x] Automação da bomba

- [x] Histórico de eventos

- [ ] Modularização do código

- [ ] Arquivo de configuração

- [ ] Logging da aplicação

- [ ] Tratamento de exceções

- [ ] Testes automatizados

- [ ] API REST

- [ ] PostgreSQL



---



## Dashboard



- [ ] Dashboard Web

- [ ] Indicadores em tempo real

- [ ] Gráficos históricos

- [ ] Página de configurações

- [ ] Controle manual da bomba



---



## IoT



- [ ] Simulação no Wokwi

- [ ] Integração com ESP32

- [ ] Sensor DHT22

- [ ] Sensor de umidade do solo

- [ ] Relé

- [ ] Comunicação Serial

- [ ] MQTT

- [ ] Hardware físico



---



#  Próximos Passos



O projeto continuará evoluindo com foco em:



- Interface web para monitoramento

- Integração com dispositivos IoT

- Monitoramento remoto

- Automação baseada em múltiplos sensores

- Configuração dinâmica das regras de irrigação

- Persistência em banco de dados para ambientes de produção

- Arquitetura preparada para múltiplos dispositivos



---



# 📄 Licença



Este projeto está licenciado sob a licença MIT
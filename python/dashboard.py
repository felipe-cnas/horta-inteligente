import streamlit as st
import sqlite3
import pandas as pd

# 1. Configuração da página e Identidade Visual básica
st.set_page_config(page_title="Horta - Telemetria", page_icon="🌿", layout="wide")

# Customização via Markdown para mudar pequenos detalhes de estilo se necessário
st.markdown("""
    <style>
    .stMetric {
        background-color: rgba(240, 248, 240, 0.5);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho customizado (Estilo Seattle Weather, mas verde)
st.title("🌿 Monitoramento Ambiental")
st.markdown("Dashboard de telemetria em tempo real para automação de irrigação.")
st.markdown("---")

def carregar_dados():
    conn = sqlite3.connect("horta.db", timeout=5)
    query = "SELECT data_hora, temperatura, umidade, status_bomba FROM leituras ORDER BY id DESC LIMIT 20"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 🔥 O fragmento mantém tudo atualizando de forma limpa e sem travar a tela
@st.fragment(run_every="3s")
def painel_dados():
    try:
        dados = carregar_dados()
        if not dados.empty:
            ultima_leitura = dados.iloc[0]
            
           # --- SEÇÃO 1: METRICAS NO TOPO (Ajustado para Modo Escuro/Claro) ---
            st.markdown("### 📋 Status Atual da Horta")
            met1, met2, met3 = st.columns(3)
            
            with met1:
                st.metric(label="🌡️ Temperatura do Ar", value=f"{ultima_leitura['temperatura']} °C", delta="Ideal" if 20 <= ultima_leitura['temperatura'] <= 28 else "Alerta")
            
            with met2:
                status_umi = "Estável" if ultima_leitura['umidade'] >= 60 else "Seco"
                st.metric(label="💧 Umidade do Solo", value=f"{ultima_leitura['umidade']} %", delta=status_umi, delta_color="normal" if status_umi == "Estável" else "inverse")
            
            with met3:
                status = ultima_leitura['status_bomba']
                # Agora usamos RGBA (transparências) para que o fundo mude de forma sutil sem estourar no modo escuro!
                if status == "LIGADA":
                    st.markdown(f"<div style='padding:14px; border-radius:10px; border: 1px solid #a5d6a7; background-color: rgba(46, 125, 50, 0.2); text-align:center;'><strong>⚡ STATUS DA BOMBA</strong><br><span style='color:#81c784; font-size:24px; font-weight:bold;'>💧 LIGADA</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='padding:14px; border-radius:10px; border: 1px solid #555555; background-color: rgba(255, 255, 255, 0.05); text-align:center;'><strong>⚡ STATUS DA BOMBA</strong><br><span style='color:#aaaaaa; font-size:24px; font-weight:bold;'>💤 DESLIGADA</span></div>", unsafe_allow_html=True)
            
           # --- SEÇÃO 2: GRÁFICO DE LINHAS MINIMALISTA (Troca do Área por Linha) ---
           # --- SEÇÃO 2: GRÁFICO DE LINHAS AJUSTADO PARA CELULAR ---
            st.markdown("### 📈 Histórico de Umidade do Solo")
            
            # Criamos uma cópia dos dados para não quebrar o banco
            df_grafico = dados.copy()
            # Convertemos a data para mostrar APENAS Hora:Minuto:Segundo
            df_grafico["hora_formatada"] = pd.to_datetime(df_grafico["data_hora"]).dt.strftime('%H:%M:%S')
            
            # Definimos a nova coluna formatada como o eixo X
            dados_grafico = df_grafico.set_index("hora_formatada")["umidade"].iloc[::-1]
            
            # Plota o gráfico limpo
            st.line_chart(dados_grafico, color="#4caf50", x_label="Horário da Leitura", y_label="Umidade (%)")
            
            # --- SEÇÃO 3: DADOS BRUTOS (Igual ao rodapé do Stock Peers / Seattle) ---
            with st.expander("📂 Visualizar Dados Brutos do Banco (Logs)", expanded=False):
                st.dataframe(dados, use_container_width=True, hide_index=True)
                
        else:
            st.warning("Aguardando inserção de dados pelo simulador...")
            
    except Exception as e:
        st.error(f"Erro ao conectar com o banco de dados. Verifique o simulador. Erro: {e}")

# Executa o painel customizado
painel_dados()
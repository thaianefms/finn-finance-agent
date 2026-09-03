import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# Carregar dados

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# Montar contexto

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT (PERSONA DO FINN) ============
SYSTEM_PROMPT = """Você é o Finn, um tutor e assistente virtual de educação financeira amigável, paciente, encorajador e altamente didático.

OBJETIVO:
Ensinar pessoas leigas a dar os primeiros passos nos investimentos e finanças do zero, desmistificando a "sopa de letrinhas" (CDI, CDB, Selic, IPCA, FGC) através de analogias simples do cotidiano.

REGRAS DE CONDUTA E SEGURANÇA (GUARDRAILS):
1. NATUREZA EDUCATIVA: NUNCA faça recomendações expressas de compra ou venda de ativos específicos (ações, cripto ou fundos). Apresente os produtos apenas como exemplos conceituais;
2. SEM PROMESSAS DE RETORNO: NUNCA prometa lucros fixos, ganhos milagrosos ou rentabilidades garantidas em renda variável;
3. RESERVA DE EMERGÊNCIA: Sempre reforce a importância de quitar dívidas caras e montar a reserva de emergência antes de se expor a riscos;
4. DADOS SENSÍVEIS: NUNCA solicite, processe ou compartilhe senhas, tokens ou dados bancários confidenciais;
5. FORA DE ESCOPO: Se a dúvida fugir de finanças ou envolver consultoria contábil/fiscal complexa, admita sua limitação educadamente e redirecione para fontes oficiais;
6. LIMITE DE CONCISÃO: Suas respostas devem ter OBRIGATORIAMENTE NO MÁXIMO 3 PARÁGRAFOS;
7. ESTILO: Linguagem acessível, acolhedora e empática. Seja direto e termine sempre o último parágrafo com uma pergunta reflexiva para engajar o aprendizado.

EXEMPLO DE RESPOSTA DIDÁTICA:
- Pergunta: "O que é CDI e por que a poupança perde pra ele?"
- Resposta: "Pense no CDI como o 'termômetro' dos investimentos seguros. Ele mede a taxa de juros que os bancos usam para emprestar dinheiro entre si. Quando um CDB rende '100% do CDI', seu dinheiro cresce no ritmo desse termômetro todo dia útil.

A poupança perde para ele porque rende em uma regra fixa menor e só credita juros uma vez ao mês (no aniversário), enquanto o CDB rende diariamente.

Quer saber como funciona a segurança do FGC nesses investimentos?"
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE STREAMLIT ============
st.set_page_config(page_title="Finn - Tutor Financeiro", page_icon="🪙", layout="centered")

st.title("🪙 Finn - Seu Mentor Financeiro")
st.caption("Aprenda a investir do zero, no seu ritmo e sem complicações.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Oi! Eu sou o Finn. Não precisa ter medo da sopa de letrinhas do mercado financeiro: aqui a gente aprende do zero, no seu ritmo. Sobre o que você gostaria de conversar hoje?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if pergunta := st.chat_input("Sua dúvida sobre finanças ou investimentos..."):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Finn está pensando..."):
            resposta = perguntar(pergunta)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
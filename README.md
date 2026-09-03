# 🪙 Finn - Tutor Inteligente de Educação Financeira

O **Finn** é um agente conversacional autônomo e tutor de educação financeira, projetado para orientar investidores iniciantes nos primeiros passos rumo à organização pessoal e ao entendimento dos investimentos. Desenvolvido para rodar 100% localmente com **Ollama** e interface interativa em **Streamlit**, o Finn traduz jargões complexos em analogias simples do dia a dia, sempre com guardrails estritos de segurança e conformidade.

---

## 🎯 Funcionalidades Principais

* **Tradução Didática de Conceitos:** Desmistifica termos como CDI, CDB, Tesouro Selic, IPCA e FGC por meio de analogias acessíveis para quem está começando do zero.
* **Injeção de Contexto Estruturado:** Integração com bases locais em JSON e CSV (perfil do investidor, catálogo de produtos, histórico de atendimentos e transações recentes) para gerar orientações personalizadas sem alucinações.
* **Priorização da Reserva de Emergência:** Orienta a montagem da reserva e a quitação de dívidas caras antes de qualquer exposição a produtos de maior risco.
* **Guardrails Rigorosos de Segurança:**
  * **100% Educativo:** Não realiza recomendações diretas de compra ou venda de ativos específicos (ações, cripto ou fundos).
  * **Sem Promessas de Ganho:** Não promete rentabilidades fixas ou enriquecimento em renda variável.
  * **Privacidade de Dados:** Não solicita nem compartilha senhas, tokens ou dados bancários confidenciais.
  * **Filtro de Escopo:** Redireciona com gentileza perguntas que fogem do tema de educação financeira pessoal.
* **Respostas Concisas:** Respostas limitadas a no máximo 3 parágrafos curtos, finalizando sempre com uma pergunta reflexiva para estimular o aprendizado contínuo.
* **Interface Conversacional Fluida:** Histórico de mensagens persistente na sessão via `st.session_state`.

---

## 🏗️ Estrutura do Repositório

```text
finn-finance-agent/
├── data/
│   ├── historico_atendimento.csv   # Histórico de atendimentos simulados
│   ├── perfil_investidor.json      # Dados cadastrais, metas e perfil de risco
│   ├── produtos_financeiros.json   # Catálogo mockado de produtos de investimento
│   └── transacoes.csv              # Extrato simulado de receitas e despesas
├── docs/
│   ├── 01-documentacao-agente.md   # Arquitetura, persona e objetivos do agente
│   ├── 02-base-conhecimento.md     # Documentação dos datasets e regras de contexto
│   ├── 03-prompts.md               # System prompt, guardrails e exemplos few-shot
│   └── 04-metricas.md              # Matriz de avaliação, testes e resultados
├── src/
│   ├── app.py                      # Aplicação Streamlit integrada ao Ollama
│   └── README.md                   # Instruções rápidas de execução do módulo
├── LICENSE                         # Licença do projeto (MIT)
└── README.md                       # Apresentação geral do projeto
```

## ⚙️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Backend de IA:** Ollama (modelo local `gpt-oss`)
* **Interface Gráfica:** Streamlit
* **Manipulação de Dados:** Pandas e módulo nativo `json`
* **Comunicação HTTP:** Requests

---

## 🚀 Como Executar

### 1. Inicializar o Ollama
Certifique-se de que o Ollama está instalado e em execução no sistema:

```bash
ollama run gpt-oss
```

### 2. Instalar as Dependências

Instale as bibliotecas necessárias:

```bash
pip install streamlit pandas requests
```

### 3. Rodar a Aplicação

Inicie o Streamlit apontando para o script da pasta `src/`:

```bash
streamlit run .\src\app.py
```

> O painel conversacional abrirá automaticamente em `http://localhost:8501`.

---

## 🧪 Validação e Resultados

O assistente foi submetido a uma bateria de testes funcionais documentados em `docs/04-metricas.md`, comprovando:

* **Assertividade:** Explicações claras sobre mecanismos de remuneração e liquidez de renda fixa;
* **Aderência aos Guardrails:** Bloqueio consistente de pedidos de recomendação direta de ações e recusa de operações fora do escopo;
* **Segurança e Coerência:** Uso dos dados mockados do cliente sem exposição de informações sensíveis.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE)[cite: 3].

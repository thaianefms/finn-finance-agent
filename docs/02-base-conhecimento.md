# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Servir como base de exemplos de dúvidas comuns de clientes para contextualizar os diálogos e enriquecer o suporte didático. |
| `perfil_investidor.json` | JSON | Consultar as características dos perfis (Conservador, Moderado e Arrojado) para ensinar ao usuário como identificar seu próprio perfil de risco. |
| `produtos_financeiros.json` | JSON | Alimentar o agente com exemplos reais e estruturados de produtos (Renda Fixa, Fundos, Ações, etc.) para simulações e explicações didáticas de prazos, riscos e taxas. |
| `transacoes.csv` | CSV | Utilizado para criar cenários práticos de orçamento, ajudando a demonstrar como organizar gastos antes de destinar sobras para investimentos e reserva de emergência. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Nenhuma alteração ou expansão estrutural foi realizada nos arquivos mockados originais do repositório.

Os dados de perfil_investidor.json, produtos_financeiros.json, historico_atendimento.csv e transacoes.csv foram consumidos em seu formato original, servindo diretamente como a base de conhecimento de referência para contextualizar os exemplos, perfis e simulações didáticas do Finn.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import json
import pandas as pd
import requests
import streamlit as st

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
```

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos de dados (`perfil_investidor.json`, `produtos_financeiros.json`, `historico_atendimento.csv` e `transacoes.csv`) são carregados localmente na inicialização da aplicação através de scripts Python utilizando as bibliotecas `json` e `pandas`. As informações são lidas, tratadas e armazenadas em memória durante a sessão do assistente.

### Como os dados são usados no prompt?
A injeção de dados ocorre em duas camadas dentro da composição do prompt:

* **System Prompt (Contexto Base):** As definições de perfis de risco (`perfil_investidor.json`) e o catálogo de produtos (`produtos_financeiros.json`) são injetados como regras e referências estáticas, permitindo que o **Finn** utilize dados consistentes para explicar prazos, riscos e rentabilidades em linguagem didática.
* **Contexto Dinâmico:** Conforme o usuário interage, resumos de `transacoes.csv` e exemplos de `historico_atendimento.csv` são incluídos na mensagem de contexto da conversa para exemplificar a organização de gastos, reserva de emergência e esclarecer dúvidas frequentes de forma personalizada.
---

## Exemplo de Contexto Montado

Abaixo está a representação do payload de contexto gerado pela aplicação e enviado ao modelo para fundamentar a resposta do **Finn**:

```text
[SYSTEM PROMPT]
Você é o Finn, um tutor de educação financeira acessível, paciente e encorajador.
Sua missão é ensinar pessoas leigas a investir do zero, traduzindo jargões do mercado em analogias simples.
Você NÃO faz recomendações diretas de compra/venda, NÃO promete retornos garantidos e SEMPRE reforça a importância da reserva de emergência antes de qualquer risco.

[BASE DE CONHECIMENTO DE REFERÊNCIA]
--- PERFIS DE INVESTIDOR (perfil_investidor.json) ---
- Conservador: Prioridade total para segurança e liquidez diária. Baixa tolerância a oscilações.
- Moderado: Busca equilíbrio entre segurança e rentabilidade de médio prazo. Aceita pequenas variações.
- Arrojado: Foco em valorização no longo prazo. Alta tolerância a volatilidade e riscos.

--- CATÁLOGO DE PRODUTOS PARA SIMULAÇÃO (produtos_financeiros.json) ---
- Tesouro Selic / CDB 100% CDI: Renda Fixa, Baixo Risco, Liquidez Diária, FGC/Garantia Soberana. Indicado para Reserva de Emergência.
- LCI / LCA: Renda Fixa, Baixo Risco, Isento de IR, carência mínima de resgate.
- Fundos Multimercado / Ações: Renda Variável, Médio/Alto Risco, Oscilação diária, Longo Prazo.

[CONTEXTO DO USUÁRIO]
- Dúvidas Recorrentes Mapeadas (historico_atendimento.csv): "Quanto preciso para começar?", "O que é CDI?"
- Capacidade de Aporte Estimada (transacoes.csv): R$ 150,00 / mês após despesas fixas.

[HISTÓRICO DA CONVERSA]
Usuário: "Tenho R$ 100 guardados na poupança e quero começar a investir, mas tenho medo de perder tudo. O que é esse tal de CDI que todo mundo fala?"

[DIRETRIZ DE RESPOSTA]
Responda como Finn: explique o que é CDI com uma analogia simples, compare didaticamente com a poupança usando os dados de Renda Fixa e tranquilize o usuário sobre segurança (FGC) e liquidez diária.

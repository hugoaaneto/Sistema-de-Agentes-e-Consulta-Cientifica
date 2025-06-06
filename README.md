# Desafio: Agentes Inteligentes com RAG em Base Científica

Este projeto implementa um sistema de agentes inteligentes baseado na abordagem RAG (Retrieval-Augmented Generation) para consulta e curadoria de uma base de documentos científicos. O sistema foi desenvolvido para permitir interação via linguagem natural e execução de ações sobre os documentos e dados disponíveis, atendendo a dois perfis de usuários: o pesquisador (usuário final) e o administrador (responsável pela manutenção da base).

O sistema permite realizar diversas operações sobre a base de artigos, incluindo a adição, remoção e listagem de arquivos. Além disso, os usuários podem fazer perguntas relacionadas aos artigos presentes na base ou dúvidas gerais, sem necessidade de referência explícita ao conteúdo indexado.

A extração de trechos relevantes dos documentos é realizada por meio da abordagem RAG. O sistema é composto por agentes especializados, cada um com funções distintas: análise algorítmica, análise teórica, controle e curadoria da base na nuvem, execução da RAG e orquestração geral das interações.

## Tecnologias Utilizadas

- **Flask**: Estrutura da API REST que serve como ponto de interação com os agentes.
- **GCP (Google Cloud Platform)**: Utilizada para o armazenamento persistente dos documentos e recuperação dinâmica da base.
- **LangChain**: Orquestração dos agentes especialistas, chains, integração com LLMs e execução de tools.
- **Chroma**: Banco vetorial para indexação e recuperação semântica dos documentos.
- **Gemini e OpenAI**: Provedores de LLM utilizados para execução dos agentes com possibilidade de comparação entre respostas.

## Funcionalidades

- **Agentes Especialistas**: Cada agente possui um escopo definido com tools específicas.
- **Chains**: Estrutura de orquestração entre os agentes com decisão automática baseada no input do usuario.
- **RAG Dinâmico**: Os documentos são carregados da nuvem, indexados no banco vetorial, e utilizados em tempo de execução.
- **Gerenciamento de Documentos**: Inclusão, deleção e listagem dos arquivos disponíveis.
- **Comparação de Respostas**: Permite obter respostas paralelas dos mesmos agentes configurados com LLMs diferentes, mantendo prompts e tools idênticos.
- **Troca de Provedor**: Arquitetura desacoplada para permitir a substituição do provedor LLM sem necessidade de reconfiguração da chain.

## Estrutura de Usuários

- **Usuário Final (Pesquisador)**: Interage com o sistema via chat para consultas, explorações de conteúdo e execuções de ações baseadas nos documentos científicos.
- **Curador de Dados**: Responsável por inserir, manter e remover documentos da base de conhecimento.

### Autenticação e Autorização

No sistema atual não existe Autenticação nem Autorização, isso poderia ser adicionado para permitir que o usuário curador de dados possa fazer suas atividades de manuntenção e o usuário final não, impedindo mau uso do sistema. Por ser uma prova de conceito, não temos diferenciação dos usuários, qualquer usuário pode realizar qualquer ação, o que não é adequado para sistemas em produção.

## Desafio de comparação entre LLMs

No sistema, foi utilizado um agente responsável pela orquestração, sendo capaz de selecionar qual LLM será utilizada. Com isso, ao fornecer um prompt adequado, o sistema é capaz de gerar uma resposta que compara as duas abordagens. Abaixo, apresenta-se o prompt utilizado e a saída correspondente. Após a execução, a análise dos logs confirmou que ambas as LLMs foram, de fato, executadas.

Input:

```json
{ "message": "Faça duas ações, uma usando a openai e outra usando o gemini para pegar a lista de arquivos disponiveis na base e responda no formato: 'resposta da apenai: (.....) \n resposta do gemini: (.....)' }
```

Resposta:

```json
{
	"message_response": {
		"input": "Faça duas ações, uma usando a openai e outra usando o gemini para pegar a lista de arquivos disponiveis na base e responda no formato: \"resposta da apenai: (.....) \\n resposta do gemini: (.....)",
		"output": "resposta da openai: The documents in the cloud bucket are: \\n1. On the influence of the swimming operators in the Fish School Search algorithm.pdf\\n2. PALLAS Penalized mAximum LikeLihood and pArticle Swarms for Inference of Gene Regulatory Networks from Time Series Data.pdf \\n resposta do gemini: ['On the influence of the swimming operators in the Fish School Search algorithm.pdf', 'PALLAS Penalized mAximum LikeLihood and pArticle Swarms for Inference of Gene Regulatory Networks from Time Series Data.pdf']"
	}
}
```

## Formato das Requisições

As requisições são POST, e devem ser feitas utilizando o formato `multipart/form-data`, contendo os seguintes campos:

- `message`: string com a instrução ou pergunta.
- `file`: (opcional) arquivo `.pdf` para ser adicionado à base científica.

## Exemplos de Utilização

O projeto consiste de uma API com apenas uma rota: ```/chatbot```

Abaixo, exemplos de requisições possíveis ao sistema via API:

```json
{ "message": "olá" }
{ "message": "quais arquivos tem disponíveis na base de dados?" }
{ "message": "tem algum artigo com 'fish school search.pdf' ou algo parecido no nome?" }
{ "message": "Usando a openai delete o arquivo anomaly detection.pdf" }
{ "message": "No contexto de IA e científico o que é o fish school search (FSS)?" }
{ "message": "no artigo científico do fish school search o que o operador coletivo volitivo faz?" }
{ "message": "Usando a openai me explique como implemento um quicksort?" }
{ "message": "do que fala o On the influence of the swimming operators in the Fish School Search algorithm.pdf?" }
```

# Execução Local

Este projeto pode ser executado localmente utilizando um ambiente virtual para garantir o isolamento das dependências.


## Passos para execução

1. **Crie e ative um ambiente virtual**

   No Linux/macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   No Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema**

   ```bash
   python run.py
   ```

## Acesso à API

Após a execução, a API estará disponível em:

```
http://localhost:5000
```
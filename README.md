# 🌍 FutureHub Challenge  
### *Missões rápidas e criativas geradas por IA para promover sustentabilidade e inovação.*

---

## Visão Geral  

**FutureHub Challenge** é uma aplicação que utiliza **IA Generativa (Gemini 2.5 Flash)** para criar **missões colaborativas e sustentáveis** em diversas áreas de interesse.  
O objetivo é incentivar ações práticas que estimulem a **criatividade**, **cooperação** e o **pensamento sustentável**, ajudando usuários a desenvolver ideias e protótipos para resolver problemas reais.  

---

## Tecnologias Utilizadas  

- **Python 3.10+**  
- **Google Gemini 2.5 Flash API**  
- **Bibliotecas:**  
  - `google-generativeai` → acesso à API Gemini  
  - `dotenv` → gerenciamento de chaves seguras  
  - `json`, `re` → tratamento das respostas da IA  

---

## Estrutura do Projeto  

```

│
├── test_ia.py        # Script principal que se conecta à API Gemini
├── .env              # Armazena a chave da API GEMINI_API_KEY (não versionar)
├── README.md         # Documentação do projeto

````

---

## Instalação e Execução  

### Clonar o repositório
```bash
git clone https://github.com/caiohc28/GS2-IOT.git
````
### Instalar dependências

```bash
pip install google-generativeai python-dotenv
ou
py -m pip install google-generativeai python-dotenv
```
```bash
pip install flask
ou
py -m pip install flask
```
```bash
pip install oracledb
ou
py -m pip install oracledb
```

### Criar o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```
GEMINI_API_KEY=sua_chave_aqui
```

Para gerar sua chave:

1. Vá até [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crie um projeto e gere uma chave de API
3. Copie e cole no arquivo `.env`

---

## Como Usar

Execute o script principal:

```bash
py test_ia.py
ou
python test_ia.py
```

O programa pedirá uma área de interesse, por exemplo:

```
Área de interesse: Sustentabilidade
```

E retornará uma missão no formato JSON:

```json
{
  "titulo": "Design Sustentável em Ação",
  "objetivo": "Escolha um objeto de uso diário que gera muito lixo ou consome muitos recursos e proponha um redesenho simples que o torne mais sustentável (ex: mais durável, reciclável, feito de material renovável).",
  "moral": "Pequenas mudanças no design podem ter um grande impacto ambiental positivo."
}
```

---

## Objetivo Educacional

Este projeto demonstra o uso de **IA Generativa** aplicada à criação de **missões sustentáveis e colaborativas**.
Ele integra conceitos de:

* **IoT e IoB** → para conectar pessoas e ideias de forma colaborativa
* **IA Generativa** → uso do modelo **Gemini 2.5 Flash** da Google
* **Desenvolvimento Web e Mobile** → Integração com interfaces para exibir e interagir com as missões

---

## Desenvolvedores
```
Caio Carnetti - RM 554600
Carlos Eduardo - RM 555223
Antônio Lino - RM 554518
```
---

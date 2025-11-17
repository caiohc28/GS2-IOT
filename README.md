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
├── gerar_missoes.py   
├── .env
├── api.py
├── missoes_semanais.json        
├── README.md        

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
py gerar_missoes.py
ou
python gerar_missoes.py
```
```bash
py api.py
ou
python api.py
```
```bash
Acesse: http://localhost:5000
```

Serão retornadas missões no formato JSON, exemplo:

```json
{
  "data": "17/11/2025",
  "missoes": {
    "Cibersegurança": {
      "titulo": "Ciber-Guardiões Verdes",
      "objetivo": "Desenvolver uma estratégia ou protótipo inovador de cibersegurança que proteja sistemas e dados críticos de iniciativas sustentáveis (e.g., redes elétricas inteligentes, cadeias de suprimentos verdes ou tecnologias de monitoramento ambiental) contra ameaças cibernéticas. O objetivo é garantir a continuidade, integridade e privacidade, promovendo a resiliência digital e a sustentabilidade no mundo real.",
      "moral": "A cibersegurança é a guardiã invisível que habilita um futuro sustentável. Sua inovação e dedicação não apenas protegem dados, mas garantem a resiliência dos sistemas que nutrem nosso planeta e a privacidade das pessoas, construindo um legado de segurança e prosperidade verde para as próximas gerações."
    },
    "Design Criatividade": {
      "titulo": "Alimento do Futuro: Design Circular",
      "objetivo": "Identifique um problema real de desperdício de alimentos na sua rotina ou comunidade e conceba uma solução de design inovadora, sustentável e que pratique os princípios da economia circular. Pense em um produto, serviço, embalagem ou sistema que transforme 'lixo' em recurso ou prolongue a vida útil de alimentos.",
      "moral": "Descubra como a criatividade e o design podem transformar desafios socioambientais em oportunidades, gerando valor, reduzindo o impacto ambiental e inspirando um futuro mais consciente e abundante."
    },
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

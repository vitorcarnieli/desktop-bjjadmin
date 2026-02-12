# 🥋 BJJ Admin
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](#português)
[![en](https://img.shields.io/badge/lang-en-blue.svg)](#english)
---
## Português
### 📌 Visão Geral
Sistema de gerenciamento para academias de Jiu-Jitsu desenvolvido em Python.  
O objetivo do projeto é centralizar a gestão de alunos, turmas, planos e pagamentos, automatizando processos administrativos comuns em academias.
---
### 🧩 Funcionalidades
#### Alunos
- Cadastro de alunos  
- Atualização de dados  
- Vínculo com plano e turma  
#### Turmas
- Criação de turmas (ex: Iniciantes, Avançado, No-Gi)
- Associação de alunos  
#### Planos
- Definição de planos (mensal, trimestral, anual, etc)  
- Valor 
- Vínculo automático com pagamentos  
#### Pagamentos
- Geração automática de cobranças ao vincular aluno a um plano  
- Histórico de pagamentos  
- Status (pago, pendente, atrasado e perdoado)  
#### Aulas
- Cadastro de aulas  
- Associação com turmas  
- Controle de datas e horários  
---
### 🚀 Como Rodar o Projeto
1. Clone o repositório:
```bash
git clone https://github.com/vitorcarnieli/bjj-admin-desktop.git
cd bjj-admin-desktop
```
2. Crie um ambiente virtual:
```bash
python -m venv .venv
```
3. Ative o ambiente virtual:
   - **Windows:**
```bash
   .venv\Scripts\activate
```
   - **Linux/Mac:**
```bash
   source .venv/bin/activate
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```
5. Execute o projeto:
```bash
python main.py
```
---
### 🗂️ Modelagem do Banco de Dados
![Database Diagram](./utils/diagram.png)
---
## English
### 📌 Overview
Management system for Jiu-Jitsu academies developed in Python.  
The goal of this project is to centralize the management of students, classes, plans, and payments, automating common administrative processes.
---
### 🧩 Features
#### Students
- Student registration  
- Data update  
- Link to plans and classes  
#### Classes
- Create classes (e.g. Beginners, Advanced, No-Gi)  
- Assign students  
#### Plans
- Define plans (monthly, quarterly, yearly, etc)  
- Price  
- Automatic link to payments  
#### Payments
- Automatic billing when a student is linked to a plan  
- Payment history  
- Status (paid, pending, overdue, and forgiven)  
#### Lessons
- Lesson registration  
- Link to classes  
- Date and schedule control  
---
### 🚀 How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/vitorcarnieli/bjj-admin-desktop.git
cd bjj-admin-desktop
```
2. Create a virtual environment:
```bash
python -m venv .venv
```
3. Activate the virtual environment:
   - **Windows:**
```bash
   .venv\Scripts\activate
```
   - **Linux/Mac:**
```bash
   source .venv/bin/activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Run the project:
```bash
python main.py
```
---
### 🗂️ Database Modeling
![Database Diagram](./utils/diagram.png)

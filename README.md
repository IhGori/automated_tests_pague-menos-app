Testes automatizados para disciplina de **Testes Automatizados para Aplicativos**

A princíprio foi aplicado dois cenários de testes:

1 - Cenário 1 (Seção de Categorias)
  - Navegação entre as subseções
  - Selecionar um produto dinamicamente da subseção escolhida

2 - Cenario 2 (Pesquisa por produtos)
  - Buscar por produto inexistente
  - Buscar por produto existente
  - Buscar e ordenar pelo maior preço

Obs: É necessário no conftest informar o nome do dispositivo e a versão do android do mesmo.

# Repositório de Testes Automatizados com Selenium, Python e Appium

Este repositório contém testes automatizados utilizando as tecnologias **Selenium**, **Python** e **Appium**.

## Requisitos

- **Python** (versão 3.7 ou superior)
- **Node.js e npm** (para instalar o Appium)
- **Appium**
- **Android Studio com Android SDK tools instalado**
- Dispositivo Android real ou emulador configurado

## Configuração

### 1. Clone o Repositório

Clone o repositório para o seu ambiente local

### 2. Pré-condição

Necessário o python está instalado

- **python -m venv venv**
- **venv\Scripts\activate** (Windows) / **source venv/bin/activate** (Linux ou MacOs)

### 3. Instalando Appium

npm i -g appium #Instalando appium
npm i -g @appium/doctor #Instalando appium doctor
npm driver install uiautomator2 #Instalando driver

Execute appium-doctor para verificar se tudo foi instalado corretamente

Execute o comando **appium** para rodar o server

# 4. Instalando os pacotes

Execute o comando **pip install -r requirements.txt**

## 5. Rodando os testes

Execute o comando **pytest**



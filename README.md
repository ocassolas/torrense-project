# 🥩 Mercado Torrense

Um sistema web simples e eficiente para gerenciar e exibir preços de produtos em tempo real em pontos de venda.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Flask](https://img.shields.io/badge/flask-latest-lightblue)
![HTML5](https://img.shields.io/badge/html5-%23E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E?logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 O Problema

Padarias e mercados tem a tradição de passar preços em um Power-Point na TV, através de um pendrive, impossibilitando a gestão e eficiência de tempo na mudança dos produtos.

## 💡 A Solução

**Mercado Torrense** oferece uma forma simples de:
- Gerenciar preços via interface web intuitiva
- Exibir produtos em tempo real em TVs/monitores
- Atualizar tudo automaticamente sem reescrever nada

---

## 🚀 Como Começar

### Pré-requisitos
- Python 3.10+
- pip (incluso no Python)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/ocassolas/torrense-project.git
cd torrense-project

# Instale o Flask
pip install flask

# Crie as pastas necessárias
mkdir templates

# Inicie o servidor
python app.py
```

Pronto! Acesse:
- **Gerenciador**: http://localhost:5000/gerenciar
- **Catálogo**: http://localhost:5000/catalogo

---

## 📁 Estrutura

```
mercado-torrense/
├── app.py                    # Backend (servidor)
└── templates/
   ├── gerenciar.html       # Interface de gerenciamento
   └── catalogo.html        # Tela para TV
```

---

## 🎯 Como Usar

### Gerenciar Preços
1. Abra: `http://localhost:5000/gerenciar`
2. Digite o novo preço e clique em **Salvar**
3. Ou clique em **ADICIONAR PRODUTO** para novos itens

### Ver no Catálogo
1. Abra: `http://localhost:5000/catalogo`
2. Pressione **F11** para tela cheia
3. Deixe rodando - produtos passam automaticamente!

### Acessar de Outro Dispositivo
1. Descubra o IP da máquina: `ipconfig` (Windows) ou `ifconfig` (Mac/Linux)
2. Acesse no outro dispositivo: `http://SEU_IP:5000/gerenciar`

---

## 🔧 Tecnologias

- **Backend**: Python + Flask
- **Frontend**: HTML + CSS + JavaScript

---

## 👥 Autores

- **z4mbrano** - Melhorias/Contribuições 
- **ocassolas** - Desenvolvimento

---

## 📄 Licença

MIT - Use livremente!


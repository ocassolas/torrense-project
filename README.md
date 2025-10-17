# 🥩 Mercado Torrense

Um sistema web simples e eficiente para gerenciar e exibir preços de produtos em tempo real em pontos de venda.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Flask](https://img.shields.io/badge/flask-latest-lightblue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 O Problema

Mercados e açougues precisam atualizar preços constantemente. A solução tradicional? Reescrever preços em placas manualmente. Demorado, propenso a erros e improfissional.

## 💡 A Solução

**Mercado Torrense** oferece uma forma simples de:
- Gerenciar preços via interface web intuitiva
- Exibir produtos em tempo real em TVs/monitores
- Atualizar tudo automaticamente sem reescrever nada

---

## ✨ O Que Você Consegue Fazer

### 🖥️ Gerenciador de Preços
- Atualizar preços de qualquer dispositivo (PC, tablet, celular)
- Adicionar novos produtos com nome, preço e unidade
- Interface limpa e minimalista - super fácil de usar
- Alterações aparecem imediatamente no catálogo

### 📺 Catálogo Automático para TV
- Produtos passam continuamente na tela (scroll automático)
- Design limpo e legível à distância
- Sem necessidade de interação - funciona 24/7
- Adapta-se automaticamente a qualquer tamanho de tela

---

## 🚀 Como Começar

### Pré-requisitos
- Python 3.10+
- pip (incluso no Python)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/mercado-torrense.git
cd mercado-torrense

# Instale o Flask
pip install flask

# Crie as pastas necessárias
mkdir templates
mkdir -p static/video

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
├── templates/
│   ├── gerenciar.html       # Interface de gerenciamento
│   └── catalogo.html        # Tela para TV
├── static/video/            # Coloque vídeos aqui (opcional)
└── precos.db                # Banco de dados (criado automaticamente)
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

## 🎨 Personalizações Simples

No arquivo `catalogo.html`, você pode ajustar:

```javascript
const VIDEO_DURATION_SECONDS = 15;      // Tempo do vídeo
const CATALOG_DURATION_SECONDS = 30;    // Tempo do catálogo
const SCROLL_SPEED_SECONDS = 20;        // Velocidade do scroll
```

---

## 📱 Compatibilidade

Funciona perfeitamente em:
- ✅ PC/Desktop
- ✅ Tablets
- ✅ Celulares
- ✅ TVs (via navegador)
- ✅ Qualquer dispositivo com navegador web

---

## 🔧 Tecnologias

- **Backend**: Python + Flask
- **Frontend**: HTML + CSS + JavaScript
- **Banco**: SQLite (zero configuração)

---

## 📝 API

### GET `/api/produtos`
Retorna todos os produtos

### POST `/api/atualizar_preco`
Atualiza preço de um produto

### POST `/api/adicionar_produto`
Adiciona novo produto

---

## 📄 Licença

MIT - Use livremente!

---

## 👥 Autores

- **z4mbrano** - Desenvolvimento
- **ocassolas** - Contribuições

---

**Pronto para usar. Sem complicações. Simples assim.** ✨

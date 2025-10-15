from flask import Flask, render_template, request, jsonify, url_for
import sqlite3
import os

app = Flask(__name__)

# Configuração do banco de dados
DB_NAME = 'precos.db'

def get_db_connection():
    """Cria uma conexão com o banco de dados SQLite"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados e insere dados de exemplo"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Criar tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            unidade TEXT NOT NULL
        )
    ''')
    
    # Verificar se já existem produtos
    cursor.execute('SELECT COUNT(*) FROM produtos')
    count = cursor.fetchone()[0]
    
    # Inserir dados iniciais apenas se a tabela estiver vazia
    if count == 0:
        produtos_iniciais = [
            ('Picanha', 89.90, 'kg'),
            ('Costela', 45.90, 'kg'),
            ('Filé Mignon', 99.90, 'kg'),
            ('Alcatra', 54.90, 'kg'),
            ('Fraldinha', 49.90, 'kg')
        ]
        
        cursor.executemany(
            'INSERT INTO produtos (nome, preco, unidade) VALUES (?, ?, ?)',
            produtos_iniciais
        )
        conn.commit()
        print("Banco de dados inicializado com produtos de exemplo.")
    
    conn.close()

# Rotas de renderização HTML
@app.route('/')
@app.route('/gerenciar')
def gerenciar():
    """Página de gerenciamento de preços"""
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos ORDER BY nome').fetchall()
    conn.close()
    return render_template('gerenciar.html', produtos=produtos)

@app.route('/catalogo')
def catalogo():
    """Página de exibição para TV"""
    return render_template('catalogo.html')

# API Endpoints (JSON)
@app.route('/api/produtos', methods=['GET'])
def api_produtos():
    """Retorna lista de produtos em formato JSON"""
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos ORDER BY nome').fetchall()
    conn.close()
    
    # Converter para lista de dicionários
    produtos_list = [
        {
            'id': produto['id'],
            'nome': produto['nome'],
            'preco': produto['preco'],
            'unidade': produto['unidade']
        }
        for produto in produtos
    ]
    
    return jsonify(produtos_list)

@app.route('/api/atualizar_preco', methods=['POST'])
def atualizar_preco():
    """Atualiza o preço de um produto"""
    try:
        data = request.get_json()
        produto_id = data.get('id')
        novo_preco = data.get('novo_preco')
        
        # Validação
        if not produto_id or novo_preco is None:
            return jsonify({'erro': 'ID e novo_preco são obrigatórios'}), 400
        
        # Converter e validar preço
        try:
            novo_preco = float(novo_preco)
            if novo_preco < 0:
                return jsonify({'erro': 'Preço não pode ser negativo'}), 400
        except ValueError:
            return jsonify({'erro': 'Preço inválido'}), 400
        
        # Atualizar no banco
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE produtos SET preco = ? WHERE id = ?',
            (novo_preco, produto_id)
        )
        conn.commit()
        
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'erro': 'Produto não encontrado'}), 404
        
        conn.close()
        return jsonify({'sucesso': True, 'mensagem': 'Preço atualizado com sucesso'}), 200
        
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/adicionar_produto', methods=['POST'])
def adicionar_produto():
    """Adiciona um novo produto"""
    try:
        data = request.get_json()
        nome = data.get('nome')
        preco = data.get('preco')
        unidade = data.get('unidade')
        
        # Validação
        if not nome or not nome.strip():
            return jsonify({'erro': 'Nome do produto é obrigatório'}), 400
        
        if preco is None:
            return jsonify({'erro': 'Preço é obrigatório'}), 400
        
        if not unidade or not unidade.strip():
            return jsonify({'erro': 'Unidade é obrigatória'}), 400
        
        # Converter e validar preço
        try:
            preco = float(preco)
            if preco < 0:
                return jsonify({'erro': 'Preço não pode ser negativo'}), 400
        except ValueError:
            return jsonify({'erro': 'Preço inválido'}), 400
        
        # Verificar se produto já existe
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM produtos WHERE LOWER(nome) = LOWER(?)', (nome.strip(),))
        produto_existente = cursor.fetchone()
        
        if produto_existente:
            conn.close()
            return jsonify({'erro': 'Produto já existe no catálogo'}), 400
        
        # Inserir novo produto
        cursor.execute(
            'INSERT INTO produtos (nome, preco, unidade) VALUES (?, ?, ?)',
            (nome.strip(), preco, unidade.strip())
        )
        conn.commit()
        produto_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'sucesso': True, 
            'mensagem': 'Produto adicionado com sucesso',
            'produto_id': produto_id
        }), 201
        
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/excluir_produtos', methods=['POST'])
def excluir_produtos():
    """Exclui múltiplos produtos do banco de dados"""
    try:
        data = request.get_json()
        
        if not data or 'ids' not in data:
            return jsonify({'error': 'IDs dos produtos não fornecidos'}), 400
        
        ids = data['ids']
        
        if not isinstance(ids, list) or not ids:
            return jsonify({'error': 'Lista de IDs inválida ou vazia'}), 400
        
        # Validar que todos os IDs são números
        try:
            ids = [int(id_produto) for id_produto in ids]
        except ValueError:
            return jsonify({'error': 'IDs de produtos inválidos'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Verificar quantos produtos existem com esses IDs
        placeholders = ','.join('?' * len(ids))
        cursor.execute(f'SELECT COUNT(*) FROM produtos WHERE id IN ({placeholders})', ids)
        produtos_encontrados = cursor.fetchone()[0]
        
        if produtos_encontrados == 0:
            conn.close()
            return jsonify({'error': 'Nenhum produto encontrado com os IDs fornecidos'}), 404
        
        # Excluir os produtos
        cursor.execute(f'DELETE FROM produtos WHERE id IN ({placeholders})', ids)
        produtos_excluidos = cursor.rowcount
        conn.commit()
        conn.close()
        
        return jsonify({
            'sucesso': True,
            'mensagem': f'{produtos_excluidos} produto(s) excluído(s) com sucesso',
            'produtos_excluidos': produtos_excluidos
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Inicializar banco de dados
    init_db()
    
    # Executar aplicação Flask
    print("\n" + "="*60)
    print("SISTEMA DE CATÁLOGO MERCADO TORRENSE")
    print("="*60)
    print("\nAcesse as seguintes URLs:")
    print("  - Gerenciamento: http://localhost:5000/gerenciar")
    print("  - Catálogo TV:   http://localhost:5000/catalogo")
    print("\nPara acessar de outros dispositivos na rede local,")
    print("substitua 'localhost' pelo IP da máquina servidor.")
    # Observação: referências a vídeos foram removidas; o catálogo roda sem vídeo.
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=False)
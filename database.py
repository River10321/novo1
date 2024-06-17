import sqlite3
from sqlite3 import Error

def criar_conexao():
    """Cria uma conexão com o banco de dados SQLite."""
    conn = None
    try:
        conn = sqlite3.connect('sistema_gestao.db')
        print("Conexão estabelecida")
    except Error as e:
        print(e)
    return conn

def criar_tabelas():
        """Cria as tabelas necessárias no banco de dados."""
        conn = criar_conexao()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS materias_primas (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    codigo TEXT NOT NULL,
                                    preco_compra REAL NOT NULL,
                                    unidade_medida TEXT NOT NULL,
                                    categoria TEXT NOT NULL,
                                    cores TEXT NOT NULL,
                                    codigo_variacao TEXT NOT NULL)''')
                
                cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    codigo TEXT NOT NULL,
                                    comprado_fabricado TEXT NOT NULL,
                                    categoria TEXT NOT NULL,
                                    tamanhos TEXT,
                                    cores TEXT,
                                    preco_custo REAL NOT NULL,
                                    preco_venda REAL NOT NULL,
                                    margem_lucro REAL NOT NULL,
                                    codigo_variacao TEXT)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS empresas_terceirizadas (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    codigo TEXT NOT NULL,
                                    celular TEXT NOT NULL,
                                    endereco TEXT NOT NULL)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS estoques (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    tipo TEXT NOT NULL,
                                    codigo_produto TEXT NOT NULL,
                                    tamanho TEXT,
                                    cor TEXT,
                                    quantidade REAL NOT NULL,
                                    data TEXT NOT NULL,
                                    pagamento TEXT,
                                    parcelas INTEGER,
                                    datas_vencimento TEXT,
                                    nota_fiscal TEXT)''')
                
                cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    codigo_produto TEXT NOT NULL,
                                    quantidade REAL NOT NULL,
                                    preco_venda REAL NOT NULL,
                                    data TEXT NOT NULL)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS variacoes (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    tamanhos TEXT,
                                    cores TEXT)''')

                cursor.execute('''CREATE TABLE IF NOT EXISTS gestao_financeira (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    tipo_transacao TEXT NOT NULL,
                                    valor REAL NOT NULL,
                                    data TEXT NOT NULL,
                                    descricao TEXT,
                                    nota_fiscal TEXT,
                                    parcelas INTEGER)''')

                conn.commit()
                print("Tabelas de matérias-primas, produtos, categorias, empresas terceirizadas, estoques, vendas, variações e gestão financeira criadas")
            except Error as e:
                print(e)
        else:
            print("Erro! Não foi possível conectar ao banco de dados.")

def listar_materias_primas():
        """Lista todas as matérias-primas."""
        conn = criar_conexao()
        materias_primas = []
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM materias_primas')
                materias_primas = cursor.fetchall()
            except Error as e:
                print(e)
        conn.close()
        return materias_primas

def apagar_materia_prima(id_materia_prima):
        """Apaga uma matéria-prima do banco de dados pelo ID."""
        conn = criar_conexao()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM materias_primas WHERE id = ?', (id_materia_prima,))
                conn.commit()
                print("Matéria-prima apagada")
            except Error as e:
                print(e)
        conn.close()

def adicionar_variacoes(tamanhos, cores):
    """Adiciona novas variações (tamanhos e cores) ao banco de dados."""
    conn = criar_conexao()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO variacoes (tamanhos, cores) VALUES (?, ?)''', (tamanhos, cores))
            conn.commit()
            print("Variações adicionadas")
        except Error as e:
            print(e)
    conn.close()

def listar_variacoes():
    """Lista todas as variações cadastradas."""
    conn = criar_conexao()
    tamanhos = []
    cores = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT tamanhos, cores FROM variacoes')
            variacoes = cursor.fetchall()
            for variacao in variacoes:
                if variacao[0]:
                    tamanhos.extend(variacao[0].split(','))
                if variacao[1]:
                    cores.extend(variacao[1].split(','))
        except Error as e:
            print(e)
    conn.close()
    return list(set(tamanhos)), list(set(cores))

def adicionar_materia_prima(nome, codigo, preco_compra, unidade_medida, categoria, cores, codigo_variacao):
    """Adiciona uma nova matéria-prima ao banco de dados."""
    conn = criar_conexao()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO materias_primas (nome, codigo, preco_compra, unidade_medida, categoria, cores, codigo_variacao) 
                              VALUES (?, ?, ?, ?, ?, ?, ?)''', (nome, codigo, preco_compra, unidade_medida, categoria, cores, codigo_variacao))
            conn.commit()
            print("Matéria-prima adicionada")
        except Error as e:
            print(e)
    conn.close()

def adicionar_produto(nome, codigo, comprado_fabricado, categoria, tamanhos, cores, preco_custo, preco_venda, margem_lucro, codigo_variacao):
    """Adiciona um novo produto ao banco de dados."""
    conn = criar_conexao()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO produtos (nome, codigo, comprado_fabricado, categoria, tamanhos, cores, preco_custo, preco_venda, margem_lucro, codigo_variacao) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, codigo, comprado_fabricado, categoria, tamanhos, cores, preco_custo, preco_venda, margem_lucro, codigo_variacao))
            conn.commit()
            print("Produto adicionado")
        except Error as e:
            print(e)
    conn.close()

def listar_produtos():
    """Lista todos os produtos."""
    conn = criar_conexao()
    produtos = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM produtos')
            produtos = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return produtos

def adicionar_categoria(nome):
    """Adiciona uma nova categoria ao banco de dados."""
    conn = criar_conexao()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO categorias (nome) 
                              VALUES (?)''', (nome,))
            conn.commit()
            print("Categoria adicionada")
        except Error as e:
            print(e)
    conn.close()

def adicionar_empresa_terceirizada(nome, codigo, celular, endereco):
    """Adiciona uma nova empresa terceirizada ao banco de dados."""
    conn = criar_conexao()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO empresas_terceirizadas (nome, codigo, celular, endereco) 
                              VALUES (?, ?, ?, ?)''', (nome, codigo, celular, endereco))
            conn.commit()
            print("Empresa terceirizada adicionada")
        except Error as e:
            print(e)
    conn.close()

def adicionar_estoque(tipo, codigo_produto, tamanho, cor, quantidade, data, pagamento, parcelas, datas_vencimento, nota_fiscal):
        """Adiciona uma nova entrada ou saída de estoque ao banco de dados."""
        conn = criar_conexao()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO estoques (tipo, codigo_produto, tamanho, cor, quantidade, data, pagamento, parcelas, datas_vencimento, nota_fiscal) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (tipo, codigo_produto, tamanho, cor, quantidade, data, pagamento, parcelas, ','.join(datas_vencimento), nota_fiscal))
                conn.commit()
                print("Movimentação de estoque adicionada")
            except Error as e:
                print(e)
        conn.close()

def listar_estoques():
    """Lista todas as movimentações de estoque."""
    conn = criar_conexao()
    estoques = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM estoques')
            estoques = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return estoques

def listar_produtos():
    """Lista todos os produtos."""
    conn = criar_conexao()
    produtos = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM produtos')
            produtos = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return produtos

def adicionar_venda(codigo_produto, quantidade, preco_venda, data):
    """Adiciona uma nova venda ao banco de dados."""
    conn = criar_conexao()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO vendas (codigo_produto, quantidade, preco_venda, data) 
                              VALUES (?, ?, ?, ?)''', (codigo_produto, quantidade, preco_venda, data))
            conn.commit()
            print("Venda registrada")
        except Error as e:
            print(e)
    conn.close()

def listar_vendas():
    """Lista todas as vendas registradas."""
    conn = criar_conexao()
    vendas = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM vendas')
            vendas = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return vendas

def listar_categorias():
    """Lista todas as categorias cadastradas."""
    conn = criar_conexao()
    categorias = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT nome FROM categorias')
            categorias = [row[0] for row in cursor.fetchall()]
        except Error as e:
            print(e)
    conn.close()
    return categorias

def buscar_materia_prima(campo, valor):
    """Busca matérias-primas por campo e valor."""
    conn = criar_conexao()
    materias_primas = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM materias_primas WHERE {campo} LIKE ?", ('%' + valor + '%',))
            materias_primas = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return materias_primas

def buscar_produto(campo, valor):
    """Busca produtos por campo e valor."""
    conn = criar_conexao()
    produtos = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM produtos WHERE {campo} LIKE ?", ('%' + valor + '%',))
            produtos = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return produtos

def adicionar_transacao_financeira(tipo_transacao, valor, data, descricao, nota_fiscal, parcelas):
        """Adiciona uma nova transação financeira ao banco de dados."""
        conn = criar_conexao()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO gestao_financeira (tipo_transacao, valor, data, descricao, nota_fiscal, parcelas) 
                                  VALUES (?, ?, ?, ?, ?, ?)''', (tipo_transacao, valor, data, descricao, nota_fiscal, parcelas))
                conn.commit()
                print("Transação financeira registrada")
            except Error as e:
                print(e)
        conn.close()

def listar_transacoes_financeiras():
    """Lista todas as transações financeiras registradas."""
    conn = criar_conexao()
    transacoes = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM gestao_financeira')
            transacoes = cursor.fetchall()
        except Error as e:
            print(e)
    conn.close()
    return transacoes


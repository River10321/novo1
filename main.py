from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox, ttk
from database import (
    criar_tabelas, adicionar_materia_prima, adicionar_produto, adicionar_categoria, adicionar_empresa_terceirizada, adicionar_estoque,
    listar_estoques, adicionar_venda, listar_vendas, listar_categorias, listar_materias_primas, listar_produtos, buscar_materia_prima,
    buscar_produto, adicionar_variacoes, listar_variacoes, adicionar_transacao_financeira, listar_transacoes_financeiras, apagar_materia_prima
)

class SistemaGestaoApp:
    def __init__(self, root):
        """Inicializa a aplicação com a tela principal."""
        self.root = root
        self.root.title("SISTEMA DE GESTÃO")
        self.root.geometry("800x600")
        self.root.configure(bg="lightgray")
        self.criar_tela_principal()

    def criar_tela_principal(self):
        """Cria a tela principal do sistema."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="SISTEMA DE GESTÃO", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)
        
        self.button_cadastro_materia_prima = tk.Button(self.root, text="Cadastro de Matéria-Prima", command=self.criar_tela_cadastro_materia_prima, bg="blue", fg="white")
        self.button_cadastro_materia_prima.pack(pady=10)

        self.button_listar_materias_primas = tk.Button(self.root, text="Listar Matérias-Primas", command=self.criar_tela_listar_materias_primas, bg="blue", fg="white")
        self.button_listar_materias_primas.pack(pady=10)

        self.button_cadastro_produto = tk.Button(self.root, text="Cadastro de Produto", command=self.criar_tela_cadastro_produto, bg="blue", fg="white")
        self.button_cadastro_produto.pack(pady=10)

        self.button_listar_produtos = tk.Button(self.root, text="Listar Produtos", command=self.criar_tela_listar_produtos, bg="blue", fg="white")
        self.button_listar_produtos.pack(pady=10)

        self.button_cadastro_categoria = tk.Button(self.root, text="Cadastro de Categoria", command=self.criar_tela_cadastro_categoria, bg="blue", fg="white")
        self.button_cadastro_categoria.pack(pady=10)

        self.button_cadastro_empresa_terceirizada = tk.Button(self.root, text="Cadastro de Empresa Terceirizada", command=self.criar_tela_cadastro_empresa_terceirizada, bg="blue", fg="white")
        self.button_cadastro_empresa_terceirizada.pack(pady=10)

        self.button_gestao_estoques_produtos = tk.Button(self.root, text="Gestão de Estoques de Produtos", command=self.criar_tela_gestao_estoques_produtos, bg="blue", fg="white")
        self.button_gestao_estoques_produtos.pack(pady=10)

        self.button_gestao_estoques_materias_primas = tk.Button(self.root, text="Gestão de Estoques de Matérias-Primas", command=self.criar_tela_gestao_estoques_materias_primas, bg="blue", fg="white")
        self.button_gestao_estoques_materias_primas.pack(pady=10)

        self.button_pdv = tk.Button(self.root, text="PDV (Ponto de Venda)", command=self.criar_tela_pdv, bg="blue", fg="white")
        self.button_pdv.pack(pady=10)
        
        self.button_cadastro_variacoes = tk.Button(self.root, text="Cadastro de Variações", command=self.criar_tela_cadastro_variacoes, bg="blue", fg="white")
        self.button_cadastro_variacoes.pack(pady=10)

        self.button_gestao_financeira = tk.Button(self.root, text="Gestão Financeira", command=self.criar_tela_gestao_financeira, bg="blue", fg="white")
        self.button_gestao_financeira.pack(pady=10)

    def criar_tela_listar_produtos(self):
        """Cria a tela de listagem de produtos."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Listagem de Produtos", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Código", "Comprado/Fabricado", "Categoria", "Tamanhos", "Cores", "Preço Custo", "Preço Venda", "Margem Lucro", "Código Variação"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Código", text="Código")
        self.tree.heading("Comprado/Fabricado", text="Comprado/Fabricado")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Tamanhos", text="Tamanhos")
        self.tree.heading("Cores", text="Cores")
        self.tree.heading("Preço Custo", text="Preço Custo")
        self.tree.heading("Preço Venda", text="Preço Venda")
        self.tree.heading("Margem Lucro", text="Margem Lucro")
        self.tree.heading("Código Variação", text="Código Variação")
        self.tree.pack(pady=10)

        for produto in listar_produtos():
            self.tree.insert("", "end", values=produto)

        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def criar_tela_cadastro_variacoes(self):
        """Cria a tela de cadastro de variações (tamanhos e cores)."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Cadastro de Variações", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_tamanhos = tk.Label(self.root, text="Tamanhos (separados por vírgulas)", bg="lightgray", fg="black")
        self.label_tamanhos.pack()
        self.entry_tamanhos = tk.Entry(self.root)
        self.entry_tamanhos.pack()

        self.label_cores = tk.Label(self.root, text="Cores (separadas por vírgulas)", bg="lightgray", fg="black")
        self.label_cores.pack()
        self.entry_cores = tk.Entry(self.root)
        self.entry_cores.pack()

        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_variacoes, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_variacoes(self):
        """Adiciona novas variações (tamanhos e cores) ao banco de dados."""
        tamanhos = self.entry_tamanhos.get()
        cores = self.entry_cores.get()
        adicionar_variacoes(tamanhos, cores)
        messagebox.showinfo("Sucesso", "Variações adicionadas com sucesso")
        self.criar_tela_principal()

    def criar_tela_cadastro_produto(self):
        """Cria a tela de cadastro de produto."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Cadastro de Produto", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(self.root, text="Nome do Produto", bg="lightgray", fg="black")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.label_codigo = tk.Label(self.root, text="Código do Produto", bg="lightgray", fg="black")
        self.label_codigo.pack()
        self.entry_codigo = tk.Entry(self.root)
        self.entry_codigo.pack()

        self.label_comprado_fabricado = tk.Label(self.root, text="Comprado ou Fabricado?", bg="lightgray", fg="black")
        self.label_comprado_fabricado.pack()
        self.combobox_comprado_fabricado = ttk.Combobox(self.root, values=["Comprado", "Fabricado"])
        self.combobox_comprado_fabricado.pack()

        self.label_categoria = tk.Label(self.root, text="Categoria", bg="lightgray", fg="black")
        self.label_categoria.pack()
        self.combobox_categoria = ttk.Combobox(self.root, values=listar_categorias())
        self.combobox_categoria.pack()

        tamanhos_cadastrados, cores_cadastradas = listar_variacoes()
        self.label_tamanhos = tk.Label(self.root, text="Tamanhos", bg="lightgray", fg="black")
        self.label_tamanhos.pack()
        self.combobox_tamanhos = ttk.Combobox(self.root, values=tamanhos_cadastrados)
        self.combobox_tamanhos.pack()

        self.label_cores = tk.Label(self.root, text="Cores", bg="lightgray", fg="black")
        self.label_cores.pack()
        self.combobox_cores = ttk.Combobox(self.root, values=cores_cadastradas)
        self.combobox_cores.pack()

        self.label_preco_custo = tk.Label(self.root, text="Preço de Custo", bg="lightgray", fg="black")
        self.label_preco_custo.pack()
        self.entry_preco_custo = tk.Entry(self.root)
        self.entry_preco_custo.pack()

        self.label_preco_venda = tk.Label(self.root, text="Preço de Venda", bg="lightgray", fg="black")
        self.label_preco_venda.pack()
        self.entry_preco_venda = tk.Entry(self.root)
        self.entry_preco_venda.pack()

        self.label_margem_lucro = tk.Label(self.root, text="Margem de Lucro (%)", bg="lightgray", fg="black")
        self.label_margem_lucro.pack()
        self.entry_margem_lucro = tk.Entry(self.root, state='readonly')
        self.entry_margem_lucro.pack()

        self.label_codigo_variacao = tk.Label(self.root, text="Código da Variação", bg="lightgray", fg="black")
        self.label_codigo_variacao.pack()
        self.entry_codigo_variacao = tk.Entry(self.root)
        self.entry_codigo_variacao.pack()

        self.entry_preco_custo.bind("<FocusOut>", self.calcular_margem_lucro)
        self.entry_preco_venda.bind("<FocusOut>", self.calcular_margem_lucro)

        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_produto, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_produto(self):
        """Adiciona um novo produto ao banco de dados."""
        nome = self.entry_nome.get()
        codigo = self.entry_codigo.get()
        comprado_fabricado = self.combobox_comprado_fabricado.get()
        categoria = self.combobox_categoria.get()
        tamanhos = self.combobox_tamanhos.get()
        cores = self.combobox_cores.get()
        preco_custo = float(self.entry_preco_custo.get())
        preco_venda = float(self.entry_preco_venda.get())
        margem_lucro = float(self.entry_margem_lucro.get())
        codigo_variacao = self.entry_codigo_variacao.get()
        adicionar_produto(nome, codigo, comprado_fabricado, categoria, tamanhos, cores, preco_custo, preco_venda, margem_lucro, codigo_variacao)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso")
        self.criar_tela_principal()

    def criar_tela_cadastro_materia_prima(self):
        """Cria a tela de cadastro de matéria-prima."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Cadastro de Matéria-Prima", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(self.root, text="Nome da Matéria-Prima", bg="lightgray", fg="black")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.label_codigo = tk.Label(self.root, text="Código da Matéria-Prima", bg="lightgray", fg="black")
        self.label_codigo.pack()
        self.entry_codigo = tk.Entry(self.root)
        self.entry_codigo.pack()

        self.label_preco_compra = tk.Label(self.root, text="Preço de Compra", bg="lightgray", fg="black")
        self.label_preco_compra.pack()
        self.entry_preco_compra = tk.Entry(self.root)
        self.entry_preco_compra.pack()

        self.label_unidade_medida = tk.Label(self.root, text="Unidade de Medida", bg="lightgray", fg="black")
        self.label_unidade_medida.pack()
        self.combobox_unidade_medida = ttk.Combobox(self.root, values=["Metros", "Un", "Kg"])
        self.combobox_unidade_medida.pack()

        self.label_categoria = tk.Label(self.root, text="Categoria", bg="lightgray", fg="black")
        self.label_categoria.pack()
        self.combobox_categoria = ttk.Combobox(self.root, values=listar_categorias())
        self.combobox_categoria.pack()

        self.label_cores = tk.Label(self.root, text="Cor", bg="lightgray", fg="black")
        self.label_cores.pack()
        _, cores_cadastradas = listar_variacoes()
        self.combobox_cores = ttk.Combobox(self.root, values=cores_cadastradas)
        self.combobox_cores.pack()

        self.label_codigo_variacao = tk.Label(self.root, text="Código da Variação", bg="lightgray", fg="black")
        self.label_codigo_variacao.pack()
        self.entry_codigo_variacao = tk.Entry(self.root)
        self.entry_codigo_variacao.pack()


        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_materia_prima, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_materia_prima(self):
        """Adiciona uma nova matéria-prima ao banco de dados."""
        nome = self.entry_nome.get()
        codigo = self.entry_codigo.get()
        preco_compra = float(self.entry_preco_compra.get())
        unidade_medida = self.combobox_unidade_medida.get()
        categoria = self.combobox_categoria.get()
        cores = self.combobox_cores.get()
        codigo_variacao = self.entry_codigo_variacao.get()
        adicionar_materia_prima(nome, codigo, preco_compra, unidade_medida, categoria, cores, codigo_variacao)
        messagebox.showinfo("Sucesso", "Matéria-prima adicionada com sucesso")
        self.criar_tela_principal()

    def criar_tela_cadastro_categoria(self):
        """Cria a tela de cadastro de categoria."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Cadastro de Categoria", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(self.root, text="Nome da Categoria", bg="lightgray", fg="black")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_categoria, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_categoria(self):
        """Adiciona uma nova categoria ao banco de dados."""
        nome = self.entry_nome.get()
        adicionar_categoria(nome)
        messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso")
        self.criar_tela_principal()

    def criar_tela_cadastro_empresa_terceirizada(self):
        """Cria a tela de cadastro de empresa terceirizada."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Cadastro de Empresa Terceirizada", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(self.root, text="Nome da Empresa", bg="lightgray", fg="black")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.label_codigo = tk.Label(self.root, text="Código da Empresa", bg="lightgray", fg="black")
        self.label_codigo.pack()
        self.entry_codigo = tk.Entry(self.root)
        self.entry_codigo.pack()

        self.label_celular = tk.Label(self.root, text="Celular", bg="lightgray", fg="black")
        self.label_celular.pack()
        self.entry_celular = tk.Entry(self.root)
        self.entry_celular.pack()

        self.label_endereco = tk.Label(self.root, text="Endereço", bg="lightgray", fg="black")
        self.label_endereco.pack()
        self.entry_endereco = tk.Entry(self.root)
        self.entry_endereco.pack()

        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_empresa_terceirizada, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_empresa_terceirizada(self):
        """Adiciona uma nova empresa terceirizada ao banco de dados."""
        nome = self.entry_nome.get()
        codigo = self.entry_codigo.get()
        celular = self.entry_celular.get()
        endereco = self.entry_endereco.get()
        adicionar_empresa_terceirizada(nome, codigo, celular, endereco)
        messagebox.showinfo("Sucesso", "Empresa terceirizada adicionada com sucesso")
        self.criar_tela_principal()

    def atualizar_datas_vencimento(self, event):
        num_parcelas = int(self.entry_parcelas.get() if self.entry_parcelas.get().isdigit() else 0)
        for widget in self.frame_datas_vencimento.winfo_children():
            widget.destroy()
        self.datas_vencimento_entries = []
        for i in range(num_parcelas):
            label = tk.Label(self.frame_datas_vencimento, text=f"Data de Vencimento {i+1}", bg="lightgray", fg="black")
            label.pack()
            entry = DateEntry(self.frame_datas_vencimento, date_pattern='dd/mm/yyyy')
            entry.pack()
            self.datas_vencimento_entries.append(entry)


    def criar_tela_gestao_estoques_produtos(self):
        """Cria a tela de gestão de estoques de produtos."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Gestão de Estoques de Produtos", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_tipo = tk.Label(self.root, text="Tipo (Entrada/Saída)", bg="lightgray", fg="black")
        self.label_tipo.pack()
        self.combobox_tipo = ttk.Combobox(self.root, values=["Entrada", "Saída"])
        self.combobox_tipo.pack()

        self.label_codigo_produto = tk.Label(self.root, text="Código do Produto", bg="lightgray", fg="black")
        self.label_codigo_produto.pack()
        self.entry_codigo_produto = tk.Entry(self.root)
        self.entry_codigo_produto.pack()

        self.label_tamanho = tk.Label(self.root, text="Tamanho", bg="lightgray", fg="black")
        self.label_tamanho.pack()
        tamanhos, _ = listar_variacoes()
        self.combobox_tamanho = ttk.Combobox(self.root, values=tamanhos)
        self.combobox_tamanho.pack()

        self.label_cor = tk.Label(self.root, text="Cor", bg="lightgray", fg="black")
        self.label_cor.pack()
        _, cores = listar_variacoes()
        self.combobox_cor = ttk.Combobox(self.root, values=cores)
        self.combobox_cor.pack()

        self.label_quantidade = tk.Label(self.root, text="Quantidade", bg="lightgray", fg="black")
        self.label_quantidade.pack()
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.pack()

        self.label_data = tk.Label(self.root, text="Data", bg="lightgray", fg="black")
        self.label_data.pack()
        self.entry_data = DateEntry(self.root, date_pattern='dd/mm/yyyy')
        self.entry_data.pack()

        self.label_nota_fiscal = tk.Label(self.root, text="Número da Nota Fiscal", bg="lightgray", fg="black")
        self.label_nota_fiscal.pack()
        self.entry_nota_fiscal = tk.Entry(self.root)
        self.entry_nota_fiscal.pack()

        self.label_pagamento = tk.Label(self.root, text="Pagamento (À Vista/A Prazo)", bg="lightgray", fg="black")
        self.label_pagamento.pack()
        self.combobox_pagamento = ttk.Combobox(self.root, values=["À Vista", "A Prazo"])
        self.combobox_pagamento.pack()

        self.label_parcelas = tk.Label(self.root, text="Número de Parcelas", bg="lightgray", fg="black")
        self.label_parcelas.pack()
        self.entry_parcelas = tk.Entry(self.root)
        self.entry_parcelas.bind("<FocusOut>", self.atualizar_datas_vencimento)
        self.entry_parcelas.pack()
        self.frame_datas_vencimento = tk.Frame(self.root, bg="lightgray")
        self.frame_datas_vencimento.pack()

        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_estoque_produto, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_listar = tk.Button(self.root, text="Listar Estoques", command=self.listar_estoques_produtos, bg="blue", fg="white")
        self.button_listar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_estoque_produto(self):
        """Adiciona uma nova entrada ou saída de estoque de produtos ao banco de dados."""
        tipo = self.combobox_tipo.get()
        codigo_produto = self.entry_codigo_produto.get()
        tamanho = self.combobox_tamanho.get()
        cor = self.combobox_cor.get()
        quantidade = float(self.entry_quantidade.get())
        data = self.entry_data.get()
        pagamento = self.combobox_pagamento.get()
        parcelas = int(self.entry_parcelas.get()) if pagamento == "A Prazo" else 1
        nota_fiscal = self.entry_nota_fiscal.get()
        if pagamento == "A Prazo":
            datas_vencimento = [entry.get() for entry in self.datas_vencimento_entries]
        else:
            datas_vencimento = [data]
        adicionar_estoque(tipo, codigo_produto, tamanho, cor, quantidade, data, pagamento, parcelas, datas_vencimento, nota_fiscal)
        messagebox.showinfo("Sucesso", "Movimentação de estoque de produto adicionada com sucesso")
        self.criar_tela_principal()

    def listar_estoques_produtos(self):
        """Lista todas as movimentações de estoque de produtos."""
        estoques = listar_estoques()
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Movimentações de Estoque de Produtos", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)
        for estoque in estoques:
            tk.Label(self.root, text=f"ID: {estoque[0]}, Tipo: {estoque[1]}, Código do Produto: {estoque[2]}, Quantidade: {estoque[3]}, Data: {estoque[4]}, Pagamento: {estoque[5]}, Parcelas: {estoque[6]}, Datas de Vencimento: {estoque[7]}", bg="lightgray", fg="black").pack()
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def criar_tela_gestao_estoques_materias_primas(self):
        """Cria a tela de gestão de estoques de matérias-primas."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Gestão de Estoques de Matérias-Primas", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_tipo = tk.Label(self.root, text="Tipo (Entrada/Saída)", bg="lightgray", fg="black")
        self.label_tipo.pack()
        self.combobox_tipo = ttk.Combobox(self.root, values=["Entrada", "Saída"])
        self.combobox_tipo.pack()

        self.label_codigo_materia_prima = tk.Label(self.root, text="Código da Matéria-Prima", bg="lightgray", fg="black")
        self.label_codigo_materia_prima.pack()
        self.entry_codigo_materia_prima = tk.Entry(self.root)
        self.entry_codigo_materia_prima.pack()

        self.label_quantidade = tk.Label(self.root, text="Quantidade", bg="lightgray", fg="black")
        self.label_quantidade.pack()
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.pack()

        self.label_unidade_medida = tk.Label(self.root, text="Unidade de Medida", bg="lightgray", fg="black")
        self.label_unidade_medida.pack()
        self.combobox_unidade_medida = ttk.Combobox(self.root, values=["Kg", "Metros", "Un"])
        self.combobox_unidade_medida.pack()

        self.label_data = tk.Label(self.root, text="Data", bg="lightgray", fg="black")
        self.label_data.pack()
        self.entry_data = DateEntry(self.root, date_pattern='dd/mm/yyyy')
        self.entry_data.pack()

        self.label_nota_fiscal = tk.Label(self.root, text="Número da Nota Fiscal", bg="lightgray", fg="black")
        self.label_nota_fiscal.pack()
        self.entry_nota_fiscal = tk.Entry(self.root)
        self.entry_nota_fiscal.pack()

        self.label_pagamento = tk.Label(self.root, text="Pagamento (À Vista/A Prazo)", bg="lightgray", fg="black")
        self.label_pagamento.pack()
        self.combobox_pagamento = ttk.Combobox(self.root, values=["À Vista", "A Prazo"])
        self.combobox_pagamento.pack()

        self.label_parcelas = tk.Label(self.root, text="Número de Parcelas", bg="lightgray", fg="black")
        self.label_parcelas.pack()
        self.entry_parcelas = tk.Entry(self.root)
        self.entry_parcelas.bind("<FocusOut>", self.atualizar_datas_vencimento_materia_prima)
        self.entry_parcelas.pack()
        self.frame_datas_vencimento = tk.Frame(self.root, bg="lightgray")
        self.frame_datas_vencimento.pack()

        self.button_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_estoque_materia_prima, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_listar = tk.Button(self.root, text="Listar Estoques", command=self.listar_estoques_materias_primas, bg="blue", fg="white")
        self.button_listar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def atualizar_datas_vencimento_materia_prima(self, event):
        num_parcelas = int(self.entry_parcelas.get() if self.entry_parcelas.get().isdigit() else 0)
        for widget in self.frame_datas_vencimento.winfo_children():
            widget.destroy()
        self.datas_vencimento_entries = []
        for i in range(num_parcelas):
            label = tk.Label(self.frame_datas_vencimento, text=f"Data de Vencimento {i+1}", bg="lightgray", fg="black")
            label.pack()
            entry = DateEntry(self.frame_datas_vencimento, date_pattern='dd/mm/yyyy')
            entry.pack()
            self.datas_vencimento_entries.append(entry)

    def adicionar_estoque_materia_prima(self):
        """Adiciona uma nova entrada ou saída de estoque de matérias-primas ao banco de dados."""
        tipo = self.combobox_tipo.get()
        codigo_materia_prima = self.entry_codigo_materia_prima.get()
        quantidade = float(self.entry_quantidade.get())
        unidade_medida = self.combobox_unidade_medida.get()
        data = self.entry_data.get()
        pagamento = self.combobox_pagamento.get()
        parcelas = int(self.entry_parcelas.get()) if pagamento == "A Prazo" else 1
        nota_fiscal = self.entry_nota_fiscal.get()
        if pagamento == "A Prazo":
            datas_vencimento = [entry.get() for entry in self.datas_vencimento_entries]
        else:
            datas_vencimento = [data]
        adicionar_estoque(tipo, codigo_materia_prima, unidade_medida, quantidade, data, pagamento, parcelas, datas_vencimento, nota_fiscal)
        messagebox.showinfo("Sucesso", "Movimentação de estoque de matéria-prima adicionada com sucesso")
        self.criar_tela_principal()

    def criar_tela_listar_materias_primas(self):
        """Cria a tela de listagem de matérias-primas."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Listagem de Matérias-Primas", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Código", "Preço", "Unidade", "Categoria", "Cores", "Código Variação"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Código", text="Código")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Unidade", text="Unidade")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Cores", text="Cores")
        self.tree.heading("Código Variação", text="Código Variação")
        self.tree.pack(pady=10)

        for materia in listar_materias_primas():
            self.tree.insert("", "end", values=materia)

        self.button_apagar = tk.Button(self.root, text="Apagar", command=self.apagar_materia_prima, bg="red", fg="white")
        self.button_apagar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def apagar_materia_prima(self):
        """Apaga a matéria-prima selecionada."""
        selected_item = self.tree.selection()[0]
        materia_prima_id = self.tree.item(selected_item)['values'][0]
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar esta matéria-prima?"):
            apagar_materia_prima(materia_prima_id)
            self.tree.delete(selected_item)

    def listar_estoques_materias_primas(self):
        """Lista todas as movimentações de estoque de matérias-primas."""
        estoques = listar_estoques()
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Movimentações de Estoque de Matérias-Primas", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)
        for estoque in estoques:
            tk.Label(self.root, text=f"ID: {estoque[0]}, Tipo: {estoque[1]}, Código da Matéria-Prima: {estoque[2]}, Quantidade: {estoque[3]}, Data: {estoque[4]}, Pagamento: {estoque[5]}, Parcelas: {estoque[6]}, Datas de Vencimento: {estoque[7]}", bg="lightgray", fg="black").pack()
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def criar_tela_gestao_financeira(self):
        """Cria a tela de gestão financeira."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="Gestão Financeira", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        transacoes = listar_transacoes_financeiras()
        self.tree = ttk.Treeview(self.root, columns=("Tipo", "Valor", "Data", "Descrição", "Nota Fiscal", "Parcelas"), show="headings")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Valor", text="Valor")
        self.tree.heading("Data", text="Data")
        self.tree.heading("Descrição", text="Descrição")
        self.tree.heading("Nota Fiscal", text="Nota Fiscal")
        self.tree.heading("Parcelas", text="Parcelas")
        self.tree.pack(pady=10)

        for transacao in transacoes:
            self.tree.insert("", "end", values=(transacao[1], transacao[2], transacao[3], transacao[4], transacao[5], transacao[6]))

        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def criar_tela_pdv(self):
        """Cria a tela do PDV (Ponto de Venda)."""
        self.limpar_tela()
        self.label_titulo = tk.Label(self.root, text="PDV (Ponto de Venda)", font=("Arial", 24), bg="lightgray", fg="darkblue")
        self.label_titulo.pack(pady=10)

        self.label_codigo_produto = tk.Label(self.root, text="Código do Produto", bg="lightgray", fg="black")
        self.label_codigo_produto.pack()
        self.entry_codigo_produto = tk.Entry(self.root)
        self.entry_codigo_produto.pack()

        self.label_quantidade = tk.Label(self.root, text="Quantidade", bg="lightgray", fg="black")
        self.label_quantidade.pack()
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.pack()

        self.label_preco_venda = tk.Label(self.root, text="Preço de Venda", bg="lightgray", fg="black")
        self.label_preco_venda.pack()
        self.entry_preco_venda = tk.Entry(self.root)
        self.entry_preco_venda.pack()

        self.label_data = tk.Label(self.root, text="Data (DD/MM/YYYY)", bg="lightgray", fg="black")
        self.label_data.pack()
        self.entry_data = tk.Entry(self.root)
        self.entry_data.pack()

        self.entry_codigo_produto.bind("<FocusOut>", self.carregar_preco_venda)

        self.button_adicionar = tk.Button(self.root, text="Registrar Venda", command=self.adicionar_venda, bg="blue", fg="white")
        self.button_adicionar.pack(pady=10)
        self.button_listar = tk.Button(self.root, text="Listar Vendas", command=self.listar_vendas, bg="blue", fg="white")
        self.button_listar.pack(pady=10)
        self.button_voltar = tk.Button(self.root, text="Voltar", command=self.criar_tela_principal, bg="blue", fg="white")
        self.button_voltar.pack(pady=10)

    def adicionar_venda(self):
        """Adiciona uma nova venda ao banco de dados."""
        codigo_produto = self.entry_codigo_produto.get()
        quantidade = float(self.entry_quantidade.get())
        preco_venda = float(self.entry_preco_venda.get())
        data = self.entry_data.get()
        adicionar_venda(codigo_produto, quantidade, preco_venda, data)
        descricao = f"Venda de {quantidade} unidades do produto {codigo_produto}"
        adicionar_transacao_financeira("Venda", quantidade * preco_venda, data, descricao)
        messagebox.showinfo("Sucesso", "Venda registrada com sucesso")
        self.criar_tela_principal()

    def carregar_preco_venda(self, event):
        """Carrega o preço de venda do produto no PDV ao informar o código do produto."""
        codigo_produto = self.entry_codigo_produto.get()
        produtos = buscar_produto("codigo", codigo_produto)
        if produtos:
            preco_venda = produtos[0][7]
            self.entry_preco_venda.delete(0, tk.END)
            self.entry_preco_venda.insert(0, preco_venda)

    def calcular_margem_lucro(self, event):
        """Calcula a margem de lucro com base no preço de custo e preço de venda."""
        try:
            preco_custo = float(self.entry_preco_custo.get())
            preco_venda = float(self.entry_preco_venda.get())
            margem_lucro = ((preco_venda - preco_custo) / preco_custo) * 100
            self.entry_margem_lucro.config(state='normal')
            self.entry_margem_lucro.delete(0, tk.END)
            self.entry_margem_lucro.insert(0, round(margem_lucro, 2))
            self.entry_margem_lucro.config(state='readonly')
        except ValueError:
            pass

    def limpar_tela(self):
        """Limpa todos os widgets da tela atual."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    criar_tabelas()
    root = tk.Tk()
    app = SistemaGestaoApp(root)
    root.mainloop()


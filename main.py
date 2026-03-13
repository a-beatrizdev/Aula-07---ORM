# Instalar o sqlalchemy
# pip install sqlalchemy

# Importar a biblioteca responsável por criar a conexão com banco
from sqlalchemy import create_engine

# Importa os tipos de dados das colunas do banco
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa a classe base usada para criar os modelos orm
from sqlalchemy.orm import declarative_base

# Importa a ferramenta para criar sessões no banco
from sqlalchemy.orm import sessionmaker


# Criar a classe base do orm
Base = declarative_base() 

# Classe = Tabela no banco
# Atributo = Coluna
# Objeto = Linha da tabela


# Classe Produto representando a tabela do banco
class Produto(Base):
    #nome da tabela
    __tablename__ = "produtos"

    # criar coluna
    id = Column(Integer, primary_key=True) 

    # coluna do nome
    nome = Column(String(100)) 

    # coluna de preço
    preco = Column(Float) 

    estoque = Column(Integer)

    ativo = Column(Boolean)

    # método construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    # Função para exibir os valores
    def __repr__(self):
        return f"Produto ( id={self.id} - nome={self.nome} - preco={self.preco} - estoque={self.estoque} -ativo={self.ativo})" 
    
#Criar a conexão
# log do banco de daods para ativar = echo=True
engine = create_engine("sqlite:///estoque.db", echo=False) 

#Criar as tabelas - se ainda não existirem
Base.metadata.create_all(engine) 


#Criar uma fábrica de sessões
Session = sessionmaker(bind=engine)

#Criar um carrinho (sessão ativa no banco)
session = Session()


#CRIAR - Cadastrar
#Como criar um objeto
# produto1 = Produto("tablet", 2500, 20, True)
# produto2 = Produto("celular", 2000, 550, True)
# produto3 = Produto("mouse", 120, 10, True)
# produto4 = Produto("teclado", 350, 33, True)
# produto5 = Produto("pc do gabriel note", 2000, 50, True)


# session.add(produto1)
# session.add(produto2)
# session.add(produto3)
# session.add(produto4)
# session.add(produto5)


# #Salvar no banco
# session.commit()

# Buscar produtos - listar
# Pegar todos os registros 
produtos = session.query(Produto).all()

# for produto in produtos:
#     print(produto)

# Buscar apenas um único produto
buscar_produto = session.query(Produto).filter(Produto.id == 3) .first()
# print(buscar_produto)

# Buscar os produtos com o estoque baixo
buscar_estoque_baixo = session.query(Produto).filter(Produto.estoque == 50).all()
# for p in buscar_estoque_baixo:
#     print(p)

# Busca parcial - considera letras maiúsculas e minúsculas
busca_parcial = session.query(Produto).filter(Produto.nome.like("%note%")).all()
# print(busca_parcial) 

buscar_produto2 = session.query(Produto).filter_by(id=4).first()
# print(buscar_produto2)

# Top produtos com estoque baixo - limitando a busca
top_produtos = session.query(Produto).order_by(Produto.estoque).all()
top_produtos2 = session.query(Produto).order_by(Produto.estoque.desc()).all()
# for p in top_produtos2:
#     print(p)

# Limitando a quantidade de registro
top3_produtos = session.query(Produto).order_by(Produto.estoque).limit(3).all()
# for p in top3_produtos:
#     print(p)

# Contar registros
qtd = session.query(Produto).count()
# print(qtd) 

# UPDATE - Atualizar

buscar_produto_update = session.query(Produto).filter(Produto.id == 5).first()

#Atualizar um registro
buscar_produto_update.nome = "pc gamer"

session.commit()

# Delete (DELETAR)
produto_remover = session.query(Produto).filter(Produto.id == 3).first()

session.delete(produto_remover)

session.commit()





















                      





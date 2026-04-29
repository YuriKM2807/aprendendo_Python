import datetime 
class produto:
    def __init__(self):
        id: int 
        preco: int
        nome: str
        marca: str
        dataFabrica: datetime.date  
        dataValidade: datetime.date
        
    def listar_produtos(self):
        for produto in self.produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Marca: {produto.marca}, Preço: {produto.preco}, Data de Fabricação: {produto.dataFabrica}, Data de Validade: {produto.dataValidade}")
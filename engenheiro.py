from endereco import Endereco
from funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (f"CREA: {self.crea}")
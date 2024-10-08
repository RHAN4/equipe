import pytest
from atividade.models.endereco import Endereco
from atividade.models.engenheiro import Engenheiro

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "55", "Caminho K", "43806-200", "Salvador"))
    return engenheiro

def test_validar_nome(pessoa_valida):
    assert pessoa_valida.nome == "Marcos"

def test_validar_telefone(pessoa_valida):
    assert pessoa_valida.telefone == "7199999-9999"

def test_validar_email(pessoa_valida):
    assert pessoa_valida.email == "marcos@gmail.com"

def test_validar_crea(pessoa_valida):
    assert pessoa_valida.crea == "6666"

def test_validar_salario(pessoa_valida):
    assert pessoa_valida.salario == 10.000

def test_validar_logradouro(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Avenida J"

def test_validar_numero(pessoa_valida):
    assert pessoa_valida.endereco.numero == "55"

def test_validar_complemento(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Caminho K"

def test_validar_cep(pessoa_valida):
    assert pessoa_valida.endereco.cep == "43806-200"

def test_validar_cidade(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"


def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Engenheiro("", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "55", "Caminho K", "43806-200", "Salvador"))

def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Engenheiro("Marcos", 7199999-9999, "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "55", "Caminho K", "43806-200", "Salvador"))
        
def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Engenheiro("Marcos", "7199999-9999", "", "6666", 10.000,
                            Endereco("Avenida J", "55", "Caminho K", "43806-200", "Salvador"))
        
def test_logrdouro_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Logradouro não pode estar vazio"):
        Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("", "55", "Caminho K", "43806-200", "Salvador"))
        
def test_numero_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Numero não pode estar vazio"):
        Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "", "Caminho K", "43806-200", "Salvador"))
        
def test_complemento_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Complemento não pode estar vazio"):
        Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "55", "", "43806-200", "Salvador"))
        
def test_cep_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "CEP não pode estar vazio"):
        Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "55", "Caminho K", "", "Salvador"))
        
def test_cidade_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Cidade não pode estar vazio"):
        Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 10.000,
                            Endereco("Avenida J", "55", "Caminho K", "43806-200", ""))

        

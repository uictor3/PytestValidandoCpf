import pytest

from app.validaCpf import Vcpf

def test_cpf_valido():
    cpf = Vcpf("111.111.111-11")
    assert cpf.validar() == False

def test_cpf_invalido_com_letras():
    cpf = Vcpf("111a111b111c11")
    assert cpf.validar() == False

def test_cpf_invalido_com_caracteres_especiais():
    cpf = Vcpf("111.111.111@11")
    assert cpf.validar() == False

def test_cpf_invalido_com_tamanho_incorreto():
    cpf = Vcpf("1111111111")
    assert cpf.validar() == False

def test_cpf_valido_com_pontos_e_traco():
    cpf = Vcpf("111.111.111-11")
    assert cpf.validar() == False

def test_cpf_valido_sem_pontos_e_traco():
    cpf = Vcpf("11111111111")
    assert cpf.validar() == False

def test_cpf_invalido_digitos_verificadores():
    cpf = Vcpf("11111111100")
    assert cpf.validar() == False

def test_cpf_todos_numeros_iguais():
    cpf = test_cpf_valido_com_pontos_e_traco("11111111111")
    assert cpf.validar() == False

def test_cpf_invalido_com_letras_e_caracteres_especiais():
    cpf = Vcpf("111a111b111@11")
    assert cpf.validar() == False
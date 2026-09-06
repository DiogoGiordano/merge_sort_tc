from data import casos_de_teste
from merge_sort import merge_sort

#Teste manual
def test_manual():
    for numero, caso in enumerate(casos_de_teste, start=1):
        entrada = caso["entrada"]
        esperado = caso["saida_esperada"]

        resultado = merge_sort(entrada)

        if resultado == esperado:
            print(f"Teste {numero}: PASSOU")
        else:
            print(f"Teste {numero}: FALHOU")
            print(f"  Entrada:   {entrada}")
            print(f"  Esperado:  {esperado}")
            print(f"  Resultado: {resultado}")

#teste utilizando assert
def test_assert():
    for numero, caso in enumerate(casos_de_teste, start=1):
        resultado = merge_sort(caso["entrada"])

        assert resultado == caso["saida_esperada"], (
            f"Teste {numero} falhou: "
            f"esperado {caso['saida_esperada']}, "
            f"mas recebeu {resultado}"
        )

    print("Todos os testes passaram!")



test_assert()
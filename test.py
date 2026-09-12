from data import casos_de_teste
from merge_sort_recursive import merge_sort_recursive
from merge_sort_iterative import merge_sort_iterative


def testar_recursive():
    print("=" * 45)
    print("MERGE SORT RECURSIVO")
    print("=" * 45)

    for numero, caso in enumerate(casos_de_teste, start=1):
        resultado, metrics = merge_sort_recursive(caso["entrada"].copy())

        if resultado == caso["saida_esperada"]:
            status = "PASSOU"
        else:
            status = "FALHOU"

        print(
            f"Teste {numero:02d}: {status} | "
            f"Comparações: {metrics['comparisons']:3d} | "
            f"Movimentos: {metrics['movements']:3d}"
        )


def testar_iterative():
    print()
    print("-" * 10)
    print("MERGE SORT ITERATIVO")
    print("-" * 10)

    for numero, caso in enumerate(casos_de_teste, start=1):
        resultado, metrics = merge_sort_iterative(caso["entrada"].copy())

        if resultado == caso["saida_esperada"]:
            status = "PASSOU"
        else:
            status = "FALHOU"

        print(
            f"Teste {numero:02d}: {status} | "
            f"Comparações: {metrics['comparisons']:3d} | "
            f"Movimentos: {metrics['movements']:3d}"
        )


testar_recursive()
testar_iterative()

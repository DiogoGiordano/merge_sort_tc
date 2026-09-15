from data import casos_de_teste
from algorithms.merge_sort_recursive import merge_sort_recursive
from algorithms.merge_sort_iterative import merge_sort_iterative


def testar_algoritmo(nome: str, funcao_ordenacao) -> bool:
    """
    Roda o dataset inteiro de casos_de_teste contra um algoritmo
    de ordenação e imprime resultado + métricas de cada caso.

    Args:
        nome: Nome exibido no cabeçalho (ex: "MERGE SORT RECURSIVO").
        funcao_ordenacao: Função de ordenação a ser testada. Deve
            aceitar uma lista e retornar (resultado, metrics).

    Returns:
        True se todos os casos passaram, False caso contrário.
    """

    print("=" * 45)
    print(nome)
    print("=" * 45)

    passou = falhou = 0
    total_comparacoes = total_movimentos = 0

    for numero, caso in enumerate(casos_de_teste, start=1):
        entrada = caso["entrada"]
        esperado = caso["saida_esperada"]

        resultado, metrics = funcao_ordenacao(entrada.copy())

        if resultado == esperado:
            status = "PASSOU"
            passou += 1
        else:
            status = "FALHOU"
            falhou += 1

        total_comparacoes += metrics["comparisons"]
        total_movimentos += metrics["movements"]

        print(
            f"Teste {numero:02d}: {status} | "
            f"Comparações: {metrics['comparisons']:3d} | "
            f"Movimentos: {metrics['movements']:3d}"
        )

        if status == "FALHOU":
            print(f"  Entrada:   {entrada}")
            print(f"  Esperado:  {esperado}")
            print(f"  Resultado: {resultado}")

    print(
        f"Resumo: {passou} passou(aram), {falhou} falhou(aram) | "
        f"Total comparações: {total_comparacoes} | "
        f"Total movimentos: {total_movimentos}"
    )
    print()

    return falhou == 0


def main() -> None:
    resultado_recursivo = testar_algoritmo(
        "MERGE SORT RECURSIVO",
        merge_sort_recursive,
    )

    resultado_iterativo = testar_algoritmo(
        "MERGE SORT ITERATIVO",
        merge_sort_iterative,
    )

    if resultado_recursivo and resultado_iterativo:
        print("Todos os testes passaram nos dois algoritmos!")
    else:
        print("Existem testes que falharam. Veja os detalhes acima.")


if __name__ == "__main__":
    main()
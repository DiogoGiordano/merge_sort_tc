casos_de_teste = [
    # Array vazio
    {
        "entrada": [],
        "saida_esperada": []
    },

    # Apenas um elemento
    {
        "entrada": [5],
        "saida_esperada": [5]
    },

    # Dois elementos ordenados
    {
        "entrada": [1, 2],
        "saida_esperada": [1, 2]
    },

    # Dois elementos invertidos
    {
        "entrada": [2, 1],
        "saida_esperada": [1, 2]
    },

    # Array já ordenado
    {
        "entrada": [1, 2, 3, 4, 5],
        "saida_esperada": [1, 2, 3, 4, 5]
    },

    # Array em ordem inversa
    {
        "entrada": [5, 4, 3, 2, 1],
        "saida_esperada": [1, 2, 3, 4, 5]
    },

    # Exemplo básico
    {
        "entrada": [6, 3, 8, 2],
        "saida_esperada": [2, 3, 6, 8]
    },

    # Valores repetidos
    {
        "entrada": [4, 2, 4, 1, 2],
        "saida_esperada": [1, 2, 2, 4, 4]
    },

    # Todos os valores iguais
    {
        "entrada": [7, 7, 7, 7],
        "saida_esperada": [7, 7, 7, 7]
    },

    # Valores negativos
    {
        "entrada": [-3, -1, -7, -2],
        "saida_esperada": [-7, -3, -2, -1]
    },

    # Valores positivos e negativos
    {
        "entrada": [3, -1, 4, -5, 0],
        "saida_esperada": [-5, -1, 0, 3, 4]
    },

    # Contendo zero
    {
        "entrada": [0, 5, 0, 2, 0],
        "saida_esperada": [0, 0, 0, 2, 5]
    },

    # Números grandes
    {
        "entrada": [1000, 500, 2000, 1500],
        "saida_esperada": [500, 1000, 1500, 2000]
    },

    # Números grandes e negativos
    {
        "entrada": [1000000, -1000000, 500000, -500000],
        "saida_esperada": [-1000000, -500000, 500000, 1000000]
    },

    # Quantidade ímpar de elementos
    {
        "entrada": [9, 3, 7, 1, 5],
        "saida_esperada": [1, 3, 5, 7, 9]
    },

    # Quantidade par de elementos
    {
        "entrada": [10, 8, 6, 4, 2, 0],
        "saida_esperada": [0, 2, 4, 6, 8, 10]
    },

    # Elementos parcialmente ordenados
    {
        "entrada": [1, 2, 5, 3, 4],
        "saida_esperada": [1, 2, 3, 4, 5]
    },

    # Menor elemento no final
    {
        "entrada": [2, 3, 4, 5, 1],
        "saida_esperada": [1, 2, 3, 4, 5]
    },

    # Maior elemento no início
    {
        "entrada": [10, 1, 2, 3, 4],
        "saida_esperada": [1, 2, 3, 4, 10]
    },

    # Vários valores repetidos
    {
        "entrada": [3, 1, 3, 2, 1, 3, 2],
        "saida_esperada": [1, 1, 2, 2, 3, 3, 3]
    },

    # Valores negativos repetidos
    {
        "entrada": [-2, -5, -2, -1, -5],
        "saida_esperada": [-5, -5, -2, -2, -1]
    },

    # Mistura de números
    {
        "entrada": [12, 4, 19, 7, 3, 15, 1],
        "saida_esperada": [1, 3, 4, 7, 12, 15, 19]
    },

    # Sequência alternada
    {
        "entrada": [1, 10, 2, 9, 3, 8, 4, 7],
        "saida_esperada": [1, 2, 3, 4, 7, 8, 9, 10]
    },

    # Zeros, positivos e negativos
    {
        "entrada": [0, -10, 10, -5, 5, 0],
        "saida_esperada": [-10, -5, 0, 0, 5, 10]
    },

    # Array maior
    {
        "entrada": [23, 5, 17, 8, 1, 14, 30, 11, 2, 19],
        "saida_esperada": [1, 2, 5, 8, 11, 14, 17, 19, 23, 30]
    },

    # Array maior com repetições
    {
        "entrada": [8, 3, 5, 3, 9, 1, 8, 2, 5, 1],
        "saida_esperada": [1, 1, 2, 3, 3, 5, 5, 8, 8, 9]
    },

    # Valores consecutivos desordenados
    {
        "entrada": [7, 2, 9, 1, 6, 3, 8, 4, 5],
        "saida_esperada": [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },

    # Números de diferentes magnitudes
    {
        "entrada": [100, 1, 10000, 10, 1000],
        "saida_esperada": [1, 10, 100, 1000, 10000]
    },

    # Valores negativos e positivos repetidos
    {
        "entrada": [-1, 2, -1, 2, 0, -3, 3],
        "saida_esperada": [-3, -1, -1, 0, 2, 2, 3]
    },

    # Array com vinte elementos
    {
        "entrada": [
            20, 4, 15, 8, 1, 19, 7, 12, 3, 10,
            18, 6, 14, 2, 17, 9, 5, 16, 11, 13
        ],
        "saida_esperada": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20
        ]
    },
    # Array incompleta
    {
    "entrada": [3, 3, 2, 2, 1, 1],
    "saida_esperada": [1, 1, 2, 2, 3, 3]
}

]
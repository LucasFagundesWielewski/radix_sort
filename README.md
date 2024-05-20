# Radix Sort

O Radix Sort é um algoritmo de ordenação que organiza os elementos de uma lista de números inteiros ou de strings, baseando-se em seus dígitos ou caracteres, começando pelo dígito menos significativo (Least Significant Digit, LSD) ou pelo mais significativo (Most Significant Digit, MSD). Este algoritmo é conhecido por ser não-comparativo, ou seja, ele não compara os elementos diretamente entre si para ordená-los.

## Screenshots

![App Screenshot](https://media.geeksforgeeks.org/wp-content/uploads/20230307194541/Radix-Sort-in-C-1-768.png)

## Funcionamento:

**Escolha da base:** Radix Sort utiliza uma base específica, como base 10 para números decimais ou base 256 para caracteres ASCII.

**Ordenação por dígitos:**
- **LSD Radix Sort:** Ordena os elementos começando pelo dígito menos significativo até o mais significativo.
- **MSD Radix Sort:** Ordena os elementos começando pelo dígito mais significativo até o menos significativo.
Durante cada passagem, o algoritmo utiliza uma técnica de ordenação estável (como Counting Sort) para organizar os elementos com base no dígito ou caractere atual.

## Vantagens:

- **Eficiência:** Para certos tipos de dados, como números inteiros de comprimento fixo, pode ser mais rápido que algoritmos de comparação como o Quick Sort.
- **Estabilidade:** Mantém a ordem relativa dos elementos com valores iguais, uma vez que utiliza uma ordenação estável em cada dígito.

## Complexidade:

- **Tempo:** O(nk), onde n é o número de elementos e k é o número de dígitos máximos nos elementos.
- **Espaço:** O(n + k), dependendo da implementação específica.
O Radix Sort é especialmente útil para grandes conjuntos de dados onde os elementos têm um número limitado de dígitos ou caracteres.

## Autor

- [@LucasFagundesWielewski](https://www.github.com/LucasFagundesWielewski)

# SPLN-TP

## Instalação

Para instalar o programa apenas é necessário fazer:


```bash
git clone https://github.com/SLP25/SPLN-TP1.git
cd sentimentAnalizis
pip3 install .
```

### Ou


```bash
pip3 install spln-sentiment-analysis
```

## Utilização

O programa disponibiliza de 3 comandos
1. sentAnalize-calibrate <ficheiro>
Define que a polaridade do ficheiro fornecido é equivalente a 0 calibrando assim o programa.

2. sentAnalize-init
Reconstroi os datasets do programa, para caso tenham sido feitas alterações a estes.

3. sentAnalize <flags>
Funcionalidade principal do programa para a analisar a polaridade de um texto divido em cálculo de média e obter polaridades individuais.

Flags globais
|   Flag | Parâmetros  | Descrição | Se não includo |
| -------: | :-------------- | :----------------------------- | :----------------------------- |
|  `-f`  | `Path` caminho | Usar o conteudo do ficheiro | Ler do standard input |
|  `-n`  | - | Retorna os valores calibrado | - |
|  `-c`  | - | Imprimir número de palavras consideradas para o cálculo | - |
|  `--help`  | - | Imprimir ajuda sobre o programa | - |

Flags para distinção de polaridade (incompatíveis entre si)
|   Flag | Parâmetros  | Descrição | Se não includo |
| -------: | :-------------- | :----------------------------- | :----------------------------- |
|  `-d`  | - | Calcular separadamente polaridades positivas e negativas | - |
|  `-i`  | `String` \<+\|-\> | Filtrar apenas as palavras com polaridade total positiva ou negativa respetivamente | - |

Flag para cálculo de polaridade média (incompatível com display de lista)
|   Flag | Parâmetros  | Descrição | Se não includo |
| -------: | :-------------- | :----------------------------- | :----------------------------- |
|  `-a`  | - | Calcular polaridade média | - |

Flags de display de lista (incompatíveis com cálculo de polaridade média)
|   Flag | Parâmetros  | Descrição | Se não includo |
| -------: | :-------------- | :----------------------------- | :----------------------------- |
|  `-s`  | `String` \<inc\|dec\|alp\> | Ordenar palavras por polaridade total incremental, decremental ou alfabeticamente respetivamente| Ordenar palavras por ordem decrescente |
|  `-m`  | - | Mostrar valor médio de modificadores/negadores aplicados as palavras | - |
|  `-l`  | `Int` \<n\> | Mostra apenas as \<n\> primeiras palavras | - |

## Funcionalidades
- Usar emojis
- Limitar palavras
- Calcular polaridade media
- Calcular polaridade media individual para +/-
- Ordenação
- Calibração
- Mostrar número de palavras consideradas
- Total de polaridade de um palavra
- Valor de modificadores


## Como Funciona

O programa começa por dividir o input em frases, e as frases em palavras (e emojis). Cada frase é procurada numa Trie pré-computada para a traduzir numa série de Tokens. Cada Token representa uma palavra ou expressão, e é baseado em vários datasets.

Existem 2 tipos de Token. Bases, que possuem um certo valor emocional, e Modifiers, que modificam o valor das Bases ao seu redor. Esta modificação é feita com base numa máscara. O programa utiliza uma máscara fixa e igual para todos os modificadores (o grupo escolheu os valores 0.7 | 1 0.8), no entanto a possibilidade de utilizar uma máscara apropriada para cada modificador está em aberto como trabalho futuro.

A interação dos Tokens de cada frase é calculada, resultando numa longa lista de tokens Base modificados. A partir desta lista, o programa executa as operações explicadas pelas flags do programa para obter o output. A lista pode ser opcionalmente normalizada, filtrada, ordenada, cortada, e/ou acumulada como uma média.

## Exemplos

Como forma de testar este programa foi pedido a várias pessoas para submeterem textos exemplos para este programa.

Estes exemplos podem ser observados no ficheiro [exemplos.md](exemplos.md)

Estes valores foram obtidos após o programa ter cido calibrado usando o livro Harry Potter e a Pedra Filosofal .

## Comparação

![Vader vs leIA vs sentAnalize](https://github.com/lumafepe/SPLN-TP/blob/main/diferen%C3%A7as.png "Vader vs leIA vs sentAnalize")

## Recursos

O programa usa informação de 3 datasets distintos:
 - [leIA](https://github.com/rafjaa/LeIA)
 - [Linguakit](https://github.com/citiususc/Linguakit)
 - [SentiLex](https://github.com/esrel/SentiLex)

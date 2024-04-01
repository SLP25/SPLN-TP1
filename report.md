### Instalação

Para instalar o programa apenas é necessário fazer:


```bash
git clone https://github.com/lumafepe/SPLN-TP
cd sentimentAnalizis
pip3 install .
```

# Utilização

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

Flag para cálculo de polaridade média
|   Flag | Parâmetros  | Descrição | Se não includo |
| -------: | :-------------- | :----------------------------- | :----------------------------- |
|  `-a`  | - | Cálcular polaridade média | - |
|  `-d`  | - | Cálcular polaridade média dos valores positivos e negativos individualmente | - |

Flag para obter polaridades 
|   Flag | Parâmetros  | Descrição | Se não includo |
| -------: | :-------------- | :----------------------------- | :----------------------------- |
|  `-i`  | `String` \<+\|-\> | Mostrar apenas as palavras com polaridade total positiva ou negativa respetivamente | - |
|  `-s`  | `String` \<inc\|dec\|alp\> | Ordenar palavras por polaridade total incremental, decremental ou alfabeticamente respetivamente| Ordenar palavras por ordem decrescente |
|  `-l`  | `Int` \<n\> | Mostra apenas as \<n\> primeiras palavras | - |

# Funcionalidades
- Usar emojis
- Limitar palavras
- Calcular polaridade media
- Calcular polaridade media individual para +/-
- Ordenação
- Calibração
- Mostrar numero de palavras consideradas
- Total de polaridade de um palavra

#TODO
- Mostrar para um modificador qual o seu impacto em cada palavra


# Como Funciona

# Exemplos

Alguns exemplos podem ser observados no ficheiro [exemplos.md](exemplos.md)

# Comparação

![Vader vs leIA vs sentAnalize](https://github.com/lumafepe/SPLN-TP/diferenças.png "Vader vs leIA vs sentAnalize")

# Recursos

O programa usa informação de 3 datasets distintos:
 - [leIA](https://github.com/rafjaa/LeIA)
 - [Linguakit](https://github.com/citiususc/Linguakit)
 - [SentiLex](https://github.com/esrel/SentiLex)


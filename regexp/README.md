## Deu match: limpando dados com expressões regulares

Workshop do Álvaro Justen @turicas, da Escola de Dados, sobre utilização de expressões regulares. Apresentação disponível em: http://bit.ly/turicas-regexp


#### Regexp: o quê, pra quê?
Sequência que representa um padrão de caracteres. Podemos utilizar para:

* Busca de expressões
* Substituição de expressões: limpeza

#### Onde usar?

* Editores de texto (e código)
* Linguagens de programação e SQL
* Programas para limpeza de dados (exemplo: OpenRefine)

#### Onde NÃO usar?

* Parsers de linguagem (ex: varrer html - ao invés, utilize BeautifulSoup, xpath no python)
* Casos muito complexos para entender a expressão

#### Sempre tenha um conjunto de teste para validar a sua expressão regular!
E mantenha sempre salvo caso faça modificações na expressão :)

#### Códigos de expressão regular: ver no http://bit.ly/turicas-regexp

* Muito cuidado ao usar `.*`, um comando "guloso":

```
> A.*B
Isso vai considerar [A...BA...B] como um único grupo!
```

* Com `()`, estamos determinando os grupos sendo capturados no match da expressão. Podemos nos referenciar a esses grupos depois (para reorganizar ou substituir na expressão) com `$1` ou `\1`(em Python), nesse caso estamos nos referenciando ao grupo 1.

Para substituir uma linha inteira pelos grupos, por exemplo, temos que dar o match na frase inteira, colocando `.*` antes e depois da expresssão regular criada (**no Python `re.compile`, ele já extrai somente o que está dentro do grupo, não é necessário fazer isso!**):

```
regexr.com
> /.*[- ]([A-Z]{3,4})[ -].*/gm
2ª. Praia de Morro de São Paulo - CDD- SP 200
Costa - Canavieiras - CCA CN 100
Madre de Deus - BTS MD 100
Madre de Deus -BTS MD 100
Nativos - CDES NT 100
NATIVOS - CDES NT 100


Replace
> $1
CDD
CCA
BTS
BTS
CDES
CDES
```

#### DocTests!

Basicamente adicionar os testes na docstring e o resultado, como no terminal. Depois, ao chamar `python doctest arquivo.py`, ele roda os testes ao executar o script e dá errocaso não passe! :)




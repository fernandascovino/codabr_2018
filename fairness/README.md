##  Interpretação e Fairness em Machine Learning

Workshop da Fernanda Viegas (Google AI) sobre justiça e imparcialidade em ML.

#### Como se transforma o valor social de justiça para os sistemas de ML?

Existem várias definições de *fairness* e, matematicamente (segundo a lógica) falando, muitas definições se contradizem

> Exemplo: duas populações diferentes para fornecimento de *credit scores*. 
> Há uma grande probabilidade que o mesmo *threshold* para ambos não seja a melhor opção, 
> pois existem características diferentes.

* Group Unaware

In binary classification, holds all groups to the same standard. Is this really the right solution, though? For one thing, if there 
are real differences between two groups, it might not be fair to ignore them!

* Demographic parity

In binary classification (T/F), if the goal is for the two groups to receive the same number of T classifications, 
then a natural criterion is **demographic parity**, that uses thresholds that yield 
the same fraction of T classifications to each group. **Or, as a computer scientist might put it, 
the "positive rate" is the same across both groups.**

* [Equal oportunity](https://arxiv.org/abs/1610.02413)

Here, the constraint is that of the T values in each group, the same fraction in each group should actually be classified as T (?). **Or, in data science jargon, the "true positive rate" is identical between groups.**

#### Como visualizar esses trade-offs matemáticos?

#### Existe algum movimento para criação de um protocolo de *fairness*?

Na disponibilização de dados, dcoumentar além da fonte dos dados, os **viéses** intrínsecos.
Google, Facebook e grandes empresas de AI tem uma iniciativa para o desenvolvimento de [melhores práticas para ML](https://www.partnershiponai.org/

#### Caso [Jigsaw: Perspective AI](https://jigsaw.google.com/)

Software do Alphabet (irmã do Google, voltada para acabar com censuras wolrd wide). Perspective AI foi um esforço para acurar comentários tóxicos de mídias, 
dando um *score* de toxicidade para cada comentário e rankeando, mas a decisão final de exclusão de comentários é humana.

**Problema:** Usado nos comentários do New York Times, palavras como gay, lésbica, feminista tinham alto grau de toxidade. 
*Por quê?* Analisando a distribuição das frases com essas palavras, se destoava demais da distribuiço geral, aparecendo em muito mais frases pequenas num contexto negativo. *Como solucionar?* El@s pediramo apoio da comunidade com mais exemplos de frases curtas com essas palavras, e conseguiram aproximar a distribuição muito melhor! O nível de toxidade dessas palavras foi de 60-80% para 1-10%!

#### Como melhorar?

* [What-If-Tool - Open Source tool for investigate your ML](https://pair-code.github.io/what-if-tool/)

Possibilita comparar classificações pelas diferenças das features entre vizinhos mais próximos de classificações distintas. 
**Mais do que isso: fazer recortes a partir das features e você pode aplicar métricas de *fairness* para adaptar os thresholds com esse recorte.**

* [QuickDraw: Será que uma rede neural consegue aprender a reconhecer seus desenhos?](https://quickdraw.withgoogle.com/) 

Mostra como a rede entende seu desenho! Você tem 20s para desenhar o que é pedido pelo algoritmo, e ele valida seu desenho. 
Quando ele não reconhece, mostra as opções que o algoritmo selecionaria, que para ele são mais próximas do seu desenho, e também os desenhos que ele considera (reconhece) como o objeto pedido.

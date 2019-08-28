## Git(Hub) e projetos colaborativos: os 10 comandos que você precisa saber 

Workshop sobre GitHub para jornalismo de dados, realizado no [CODA.Br](https://coda.escoladedados.org) | @fernandascovino

**Base de dados utilizada**: [Gastos dos Deputados (Brasil.io - O Brasil em dados libertos)](https://brasil.io/dataset/gastos-deputados/cota_parlamentar?search=&numano=2018&nummes=&datemissao=&txnomeparlamentar=&sgpartido=&sguf=RJ&txtdescricao=&txtcnpjcpf=&txtfornecedor=&vlrliquido=)

#### Jornalismo de Dados no GitHub: Exemplos 

+ [FiveThirtyEight](https://github.com/fivethirtyeight/data)

+ [LA Times Data Desk](https://github.com/datadesk) 

+ [Estadão](https://github.com/estadao) 

+ [Volt Data Lab](https://github.com/voltdatalab) 

+ [Reporter Brasil - Ruralômetro](https://github.com/Reporter-Brasil/Ruralometro)

+ [GitHub Collection: Open Journalism](https://github.com/collections/open-journalism) 

#### Por que aprender Git(Hub)? 

+ [How journalists can get started GitHub?](https://ijnet.org/en/story/how-journalists-can-get-started-github)

+ [Getting GitHub: Why journalists should know and use the social coding site](https://knightlab.northwestern.edu/2013/06/13/getting-github-why-journalists-should-know-and-use-the-social-coding-site/)

#### Como aprender Git(Hub)? 

+ [Introdução ao Git](https://www.dadosaleatorios.com.br/post/introdu%C3%A7%C3%A3o-ao-git/) 

+ [Tudo que você queria saber sobre Git e GitHub, mas tinha vergonha de perguntar](https://tableless.com.br/tudo-que-voce-queria-saber-sobre-git-e-github-mas-tinha-vergonha-de-perguntar/) 

+ [git - guia prático - sem complicação!](http://rogerdudler.github.com/git-guide)

+ [GitHub tutorials and resources for journalists](https://www.poynter.org/news/github-tutorials-and-resources-journalists)

+ [Vídeos Github Guides (<5min cada)](https://www.youtube.com/githubguides) 

+ [Git Cheat Sheet (lista dos códigos Git por utilidade)](https://www.git-tower.com/blog/git-cheat-sheet/)

#### Atividade: Matéria sobre gastos de deputados

Baixamos do [Brasil.io](brasil.io) a base Gastos Deputados, filtrando pelo RJ e ano de 2018. 
Esse arquivo foi salvo aqui no repositório com o nome `gastos-deputados-2018-rj.csv`.

Na linha de comando, uma vez tendo clonado o repositório no seu computador
 ([o tutorial está aqui!](http://bit.ly/fscovino_codabr2018)), basta rodarmos:

```
python3 agrupa_gastos.py
```

**OBS:** Certifique-se que você tem `python3` e `pandas` instalados no seu computador! ;)

Pronto! Agora temos o arquivo `gastos-agrupados-2018-rj`, com o gasto total de cada deputado do RJ no ano de 2018,
 e a soma de todos esses (que dá mais de 10mi!)

Vamos escrever sobre isso?

Basta abrir um arquivo `rascunho_materia_gastos.md` e começar a escrever!

**OBS2**: `md`é uma extensão de arquivo de texto chamada Markdown, como `txt` e `doc`, muito simples de usar! 
Você pode encontrar todos os truques do Markdown [aqui](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

#### Projeto Curió: Democratizando os dados da Câmara

+ [Perfil dos Parlamentares](http://35.192.83.177:5001/)
+ [Câmara em Temas](http://35.192.83.177:5000/)

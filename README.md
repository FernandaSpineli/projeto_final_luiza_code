<p align="center">
  <img src="https://t.ctcdn.com.br/xOSTwJMmH_xMLgg2gp5bg4Ww1nI=/720x405/smart/filters:format(webp)/i8950.jpeg#vitrinedev">
</p>
<h1 align="center">MagaluJA💙</h1>

<hr>
<p align="center">
   <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge" #vitrinedev/>
</p>
  
### Tópicos 

- [Descrição do projeto](#descrição-do-projeto)

- [Requisitos funcionais](#requisitos-funcionais)
  - [Cadastro de clientes](#cadastro-de-clientes)
  - [Gerenciamento de produtos](#gerenciamento-de-produtos)
  - [Carrinho de compras](#carrinho-de-compras)
  - [Extras](#extras)

- [Ferramentas utilizadas](#ferramentas-utilizadas)

- [Acesso ao projeto](#acesso-ao-projeto)

- [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)

- [Desenvolvedoras](#desenvolvedoras)

## Descrição do projeto 

<p align="justify"> Projeto final apresentado pela Squad < Code >, Mesa e Banho para a banca da 5ª edição do Luiza < Code >.

A API MagaluJA nasceu inspirada pela maternidade e com duas mascotes, Joana e Alice. MagaluJA tem missão de facilitar a vida da gestante e seus bebês, oferecendo a facilidade da compra online, rapidez na entrega e qualidade nos produtos.

Foi desenvolvida uma aplicação servidora de APIs REST para a categoria de Cama, Mesa e Banho de um e-commerce. Ela contempla a estrutura de back-end e comunicação com o banco de dados, e permite o Cadastro de Clientes, Gerenciamento de Produtos e Carrinho de Compras. </p>

## Requisitos funcionais
  Obrigatórios e Opcionais

### ` Cadastro de clientes `
  
Funcionalidades que permitem o gerenciamento de **clientes** na API:
  
#### 1. Cadastrar um cliente
  
<p>:white_check_mark: a. Processo em que inserimos um novo cliente no sistema.
  <p>:white_check_mark: b. Cada cliente precisa ter pelo menos um nome e um e-mail.
  <p>:white_check_mark: c. O cliente deve informar um email válido (ao menos 3 caracteres, conter um @)
  <p>:white_check_mark: d. O e-mail do cliente deve ser único, ou seja, não há dois clientes no sistema com o mesmo e-mail.
  <p>:white_check_mark: e. Podemos ter dois clientes com o mesmo nome; mas, cada um com um e-mail diferente.

#### 2. Cadastrar um endereço

<p>:white_check_mark: a. Processo de inserir um endereço para o cliente.
<p>:white_check_mark: b. Cada endereço precisa ter pelo menos um CEP, logradouro, número, cidade e estado.
<p>:white_check_mark: c. O mesmo endereço pode ser cadastrado para mais de um cliente.
  
#### 3. Pesquisar um cliente
  
<p>:white_check_mark: a. Informado o e-mail de um cliente, apresentamos os seus dados.
  
#### 4. Pesquisar um endereço
  
<p>:white_check_mark: a. Informando o e-mail de um cliente, apresentamos seus endereços.
  
#### 5. Remover um cliente *(Opcional)*

<p>:white_check_mark: a. Remover um cliente pode remover também suas outras informações (endereços e carrinhos).
  
#### 6. Remover um endereço *(Opcional)*

<p>:warning: a. Com base em alguma chave, por exemplo, é possível remover o endereço do cliente.
  <p>

### `Gerenciamento de produtos`
  
  Funcionalidades que permitem o gerenciamento de **produtos** na API:
  
#### 1. Cadastrar um produto

<p>:white_check_mark: a. Processo em que registra-se um novo produto no sistema.
<p>:white_check_mark: b. Cada produto precisa ter pelo menos um nome, uma descrição e um código único.
<p>:white_check_mark: c. Um produto pode ter um preço de venda, que é um valor superior a R$ 0,01.
<p>:white_check_mark: d. Um produto pode ter um valor de estoque, que é um valor superior a 0.
<p>:white_check_mark: e. O código do produto informado no processo de cadastro deve ser único, ou seja, não há dois produtos no sistema com o mesmo código.
<p>:white_check_mark: f. Os nomes dos produtos podem ser únicos.
<p>:white_check_mark: g. Campos adicionais podem ser informados conforme a categoria do seu projeto.

#### 2. Atualizar os dados de um produto. atualização path, campos específicos do produto

<p>:white_check_mark: a. Poderemos atualizar os dados de um produto com base no seu código.
<p>:white_check_mark: b. O código do produto não pode ser alterado.
<p>:white_check_mark: c. O nome do produto pode ser alterado.
<p>:white_check_mark: d. Quaisquer outros campos do produto que existam em seu projeto poderão ser
atualizados.
  
#### 3. Pesquisar um produto
<p>:white_check_mark: a. Informado o código do produto, apresentamos os seus dados.

#### 4. Pesquisar um produto pelo nome
<p>:white_check_mark: a. Informe um texto para o nome do produto, então iremos pesquisar pelos produtos que contenham o nome informado.
  
#### 5. Remover um produto *(Opcional)*
<p>:white_check_mark: a. Poderemos remover um produto com base em seu código.
  
###
  
### `Carrinho de compras`
  
  Funcionalidades que permitem o gerenciamento de um **carrinho de compras** na API:
  
#### 1. Criar um carrinho de compras aberto e adicionar itens ao carrinho
<p>:white_check_mark: a. Todo carrinho de compras deve conter um cliente.
<p>:white_check_mark: b. É *opcional*, ter um produto inicialmente.
<p>:white_check_mark: c. Se há um produto um mais produtos, na criação do carrinho, informe a quantidade de cada produto. No seu trabalho, você pode começar com apenas um produto.
<p> d. Ao criar o carrinho:
<p>:white_check_mark: i. Validar se o cliente existe.
<p>:white_check_mark: ii. Validar se o produto a ser adicionado no carrinho existe.
<p>:white_check_mark: iii. Verificar se o cliente já possui um carrinho aberto. Caso contrário criar um carrinho novo.
<p>:no_entry_sign: iv. Validar se a quantidade de itens do produto a ser adicionado no carrinho está disponível no estoque (opcional).
<p>:white_check_mark: e. Ao adicionar um item no carrinho, o mesmo terá o valor total e quantidade de itens atualizado

#### 2. Alterar a quantidade de itens do carrinho novo
<p>:white_check_mark: a. No carrinho novo, com base no produto informado, a quantidade é modificada.
b. Para isto, você irá:
<p>:white_check_mark: i. Validar se produto existe no carrinho
<p>:no_entry_sign: ii. Validar se existe estoque para a quantidade desejada do produto (opcional).
<p>:white_check_mark: iii. Atualizar o valor total e quantidade de itens do carrinho
<p>:warning: c. Se o carrinho zerar o número de itens, ou seja, o cliente removeu todos os itens do carrinho, o mesmo pode ser excluído.

#### 3. Consultar carrinho de compras aberto
<p>:white_check_mark: a. Informar o cliente e retornar os dados do carrinho e produtos

#### <p>:white_check_mark: 4. Consultar os carrinhos fechados de um cliente _(opcional)_.

#### <p>:no_entry_sign: 5. Consultar os produtos e suas quantidades em carrinhos fechados *(opcional)*.

#### <p>:white_check_mark: 6. Consultar quantos carrinhos fechados os clientes possuem *(opcional)*.

#### 7. Fechar o carrinho aberto:
<p>:white_check_mark: a. Simplesmente pode-se mudar o tipo do carrinho de compras para “fechado”.
<p> b. Opcionalmente, o grupo pode adicionar o seguinte:
<p>:white_check_mark: i. Identificar o endereço do cliente que será utilizado como o de entrega.
<p>:no_entry_sign: ii. Validar se o estoque pedido dos itens ainda está disponível, se estiver reduzir do estoque dos produtos a quantidade de itens do produto no carrinho (opcional).
<p>:white_check_mark: iii. Associar um identificador ao carrinho de compras como sendo o número do
pedido.
  
#### 8. Excluir carrinho do cliente *(opcional)*.
<p>:white_check_mark: a. Quer o carrinho seja aberto ou :no_entry_sign:fechado, podemos remover o carrinho do sistema.
  
### `Extras`

1. Especificação do produto de acordo com a categoria.
2. Documentação a API Rest com o Swagger.
3. Organização e estrutura do código do projeto.
4. Realizada a busca avançada de produtos, o que permite a busca de termos parciais e caracteres maiúsculos ou minúsculos.
5. Entrega opcional de validação dquando um carrinho aberto for fechado e o produto ter sido removido do banco de dados.

## Ferramentas utilizadas

<a href="https://www.python.com" target="_blank"> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> </a> <a href="https://fastapi.tiangolo.com/" target="_blank"> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> </a> <a href="https://www.mongodb.com/" target="_blank"> <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/> </a>

###

## Acesso ao projeto

Você pode [acessar o código fonte do projeto](https://github.com/FernandaSpineli/projeto_final_luiza_code) ou [baixá-lo](https://github.com/FernandaSpineli/projeto_final_luiza_code/archive/refs/heads/main.zip).

## Abrir e rodar o projeto

### Criando as variáveis de ambiente

Após baixar o projeto, crie o arquivo `.env`, copie o conteúdo do arquivo `.env-example` alterando os valores necessários

### Instalar pymongo

```
pip install pymongo[srv]
```

### Criação do ambiente virtual

Linux

```
python3.9 -m venv venv
```

Windows

```
python -m venv venv
```

### Ativando o ambiente virtual

Linux

```
source venv/bin/activate
```

Windows

```
.\venv\Scripts\activate
```

### Instalando os pacotes

```
pip install -r requirements.txt
```

### Executando

```
uvicorn --reload main:app
```


## Desenvolvedoras
  
| [<img src="https://avatars.githubusercontent.com/u/85409876?v=4" width=115><br><sub>Fernanda Spineli</sub>](https://github.com/FernandaSpineli) |  [<img src="https://avatars.githubusercontent.com/u/16287010?v=4" width=115><br><sub>Karoline Lemos</sub>](https://github.com/karolinelemos) |  [<img src="https://avatars.githubusercontent.com/u/111469978?v=4" width=115><br><sub>Mariana Faria</sub>](https://github.com/marianaicf) |  [<img src="https://avatars.githubusercontent.com/u/29162195?v=4" width=115><br><sub>Poliana Frenhan</sub>](https://github.com/polifrenhan) |  [<img src="https://avatars.githubusercontent.com/u/102119229?v=4" width=115><br><sub>Taila Musardo</sub>](https://github.com/tailamusardo) |
| :---: | :---: | :---: | :---: | :---: |

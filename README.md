# Projeto Final - Cama, mesa e banho

## Descrição

###### TODO

### Criando as variáveis de ambiente

Crie o arquivo `.env`, copie o conteúdo do arquivo `.env-example` alterando os valores necessários

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

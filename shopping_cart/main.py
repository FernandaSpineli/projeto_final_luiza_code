from rest.config import criar_aplicacao_fastapi

def first_route():
    l1 = '================================================='
    l2 = '******** Bem-vindo à Casa da Lu tecidos ********'
    l3 = l1
    end = print(f'{l1} \n{l2} \n{l3}')
    return end

test = first_route()

app = criar_aplicacao_fastapi()
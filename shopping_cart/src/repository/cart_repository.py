from bd import obter_colecao
from src.models.cart_model import CartSchema
from uuid import uuid4

COLECAO_CARRINHO = obter_colecao("cart")


async def buscar_carrinho_pelo_usuario(id_usuario: int):
    # buscar carrinho pelo id_usuario
    ...


async def validar_novo_carrinho(id_usuario: str):
    # verificar se o usuário existe
    # user = busca_usuario_pelo_id
    carrinho = await buscar_carrinho_pelo_usuario(id_usuario)
    if carrinho is None:
        carrinho = CartSchema(
            user_id=id_usuario,
            codigo=str(uuid4()),
            status='closed',
            items_quantity=0,
            total=0
        )
        # salva carrinho no banco
        # retorna OK
    else:
        raise TypeError("Carrinho já existe para este cliente")


async def inserir_novo_carrinho(id_usuario: str):
    try:
        data = await validar_novo_carrinho(id_usuario)
        if data:
            return data
    except Exception as e:
        return f'inserir_novo_carrinho.error: {e}'


async def buscar_carrinho_pelo_codigo(codigo_carrinho: int):
    ...


async def valida_inserir_novo_produto(codigo_carrinho: str, codigo_produto: str):
    try:
        carrinho = await buscar_carrinho_pelo_codigo(codigo_carrinho)
        # verificar se o produto já está no carrinho
        # se estiver -> atualiza o CartItemSchema do produto alterando total e quantity
        # se não estiver -> instancia novo item CartItemSchema e adiciona o produto no carrinho
        # ao final, atualizar total e items_quantity do carrinho
        # retorna OK
    except Exception as e:
        return f'valida_inserir_novo_produto.error: {e}'


async def inserir_novo_produto_carrinho(codigo_carrinho: str, codigo_produto: str):
    try:
        data = await valida_inserir_novo_produto(codigo_carrinho, codigo_produto)
        if data:
            return data
    except Exception as e:
        return f'inserir_novo_produto_carrinho.error: {e}'


async def buscar_carrinho_aberto(id_usuario: str):
    try:
        carrinho = await buscar_carrinho_pelo_usuario(id_usuario)
        # retornar apenas o carrinho com status == 'opened'
    except Exception as e:
        return f'buscar_carrinho_aberto.error: {e}'


async def fechar_carrinho_aberto(codigo_carrinho: str):
    try:
        carrinho = await buscar_carrinho_pelo_codigo(codigo_carrinho)
        # verifica se o carrinho tem endereço
        # se não tiver -> retorna exceção que não pode fechar sem endereço
        # se tiver -> adiciona nro_pedido, atualiz status
        # retorna OK
    except Exception as e:
        return f'buscar_carrinho_aberto.error: {e}'

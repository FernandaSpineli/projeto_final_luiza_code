from shopping_cart.src.models.entity.cart_product import CartProduct
from shopping_cart.src.repository.shopping_cart_repository import (
    add_product_to_cart_on_bd,
    find_product_on_cart_on_bd,
    find_cart_products_on_bd,
    find_cart_on_bd,
    remove_product_from_cart_on_bd,
    clear_cart_on_bd,
    update_product_on_cart_on_bd
)
from shopping_cart.src.repository.user_repository import (
    find_user_by_email,
)
from shopping_cart.src.repository.product_repository import (
    find_product_by_id_on_bd,
)
# adicionar função definir endereço de entrega
# adicionar função de fechar compra


async def add_product_to_cart(user_email: str, cart_product: CartProduct):
    try:
        user = await find_user_by_email(user_email)
        if user:
            product = await find_product_by_id_on_bd(cart_product.product_id)
            if product:
                cart_product_dict = cart_product.dict()
                check = await add_product_to_cart_on_bd(user_email, cart_product_dict)
                if check:
                    return "Produto adicionado ao carrinho com sucesso."
                return "Falha ao adicionar produto no carrinho."
            return "Nenhum produto cadastrado com o ID informado"
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def find_product_on_cart(user_email: str, product_id: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            product = await find_product_by_id_on_bd(product_id)
            if product:
                product_found = await find_product_on_cart_on_bd(user_email, product_id)
                if product_found:
                    return product_found
                return "Falha ao encotrar o produto."
            return "Nenhum produto cadastrado com o ID informado"
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def find_cart_products(user_email: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            product_list = await find_cart_products_on_bd(user_email)
            if product_list:
                return product_list
            return "Carrinho vazio."
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def find_cart(user_email: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            return await find_cart_on_bd(user_email)
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def remove_product_from_cart(user_email: str, product_id: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            product = await find_product_by_id_on_bd(product_id)
            if product:
                check = await remove_product_from_cart_on_bd(user_email, product_id)
                if check:
                    return "Todos os produtos do tipo informado foram removidos do carrinho."
                return "Falha ao remover o tipo do produto do carrinho."
            return "Nenhum produto cadastrado com o ID informado"
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def clear_cart(user_email: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            check = await clear_cart_on_bd(user_email)
            if check:
                return "Todos os dados do carrinho foram zerados com sucesso."
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def update_product_on_cart(user_email: str, cart_product: CartProduct):
    try:
        user = await find_user_by_email(user_email)
        if user:
            product = await find_product_by_id_on_bd(cart_product.product_id)
            if product:
                cart_product_dict = cart_product.dict()
                check = await update_product_on_cart_on_bd(user_email, cart_product_dict)
                if check:
                    return "Produtos atualizados no carrinho com sucesso."
                return "Falha ao atualizar o(s) produto(s) do carrinho."
            return "Nenhum produto cadastrado com o ID informado"
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)

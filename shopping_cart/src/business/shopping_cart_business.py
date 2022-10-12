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
from shopping_cart.src.repository.purchase_repository import create_new_purchase_on_bd
from shopping_cart.src.repository.user_repository import (
    find_user_by_email,
)
from shopping_cart.src.repository.product_repository import (
    find_product_by_id_on_bd,
)
from shopping_cart.src.repository.purchase_repository import find_purchase_by_id_on_bd
from shopping_cart.src.repository.stock_repository import get_stock_on_bd, update_stock_on_bd

# adicionar função definir endereço de entrega


async def add_product_to_cart(user_email: str, cart_product: CartProduct):
    try:
        user = await find_user_by_email(user_email)
        if user:
            product = await find_product_by_id_on_bd(cart_product.product_id)
            if product:
                if cart_product.quantity < 0:
                    return "A quantidade de produto inserida deve ser um numero inteiro positivo."
                cart_product.quantity = int(cart_product.quantity)
                cart_product_dict = cart_product.dict()
                check = await add_product_to_cart_on_bd(user_email, cart_product_dict)
                if check:
                    return "Produto adicionado ao carrinho com sucesso."
                return "Falha ao adicionar produto no carrinho."
            return "Nenhum produto cadastrado com o ID informado"
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def cart_to_purchase(user_email: str, purchase_id: str, payment_method: str):
    user_cart = await find_cart_on_bd(user_email)
    products_list = user_cart["products"]
    if not products_list:
        return "Adicione pelo menos um item ao carrinho para fechar a compra."
    duplicated_purchase = await find_purchase_by_id_on_bd(user_email, purchase_id)
    if duplicated_purchase:
        return "ID informado já cadastrado em outra compra."
    if payment_method == "credit":
        price = user_cart["price_credit"]
    elif payment_method == "debit":
        price = user_cart["price_debit"]
    else:
        return "Forma de pagamento deve ser 'credit' ou 'debit'."

    purchase = {}
    purchase["id"] = purchase_id
    purchase["products"] = products_list
    purchase["price"] = price
    purchase["number_of_items"] = user_cart["number_of_items"]
    purchase["delivery_address_id"] = user_cart["delivery_address_id"]
    purchase["payment_method"] = payment_method
    check = await create_new_purchase_on_bd(user_email, purchase)
    await clear_cart_on_bd(user_email)
    if check:
        return "Compra realizada com sucesso."
    return "Erro ao fechar sua compra"


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

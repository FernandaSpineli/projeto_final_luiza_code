from shopping_cart.src.models.exceptions.exceptions import Not_Found_Exception, Server_Exception
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
    find_product_by_code,
)

# adicionar função definir endereço de entrega
# adicionar função de fechar compra


async def add_product_to_cart(user_email: str, cart_product: CartProduct):
    await validate_user(user_email)
    await validate_product(cart_product.product_id)

    cart_product_dict = cart_product.dict()
    cart = await add_product_to_cart_on_bd(user_email, cart_product_dict)
    if cart:
        return cart

    raise Server_Exception("Falha ao adicionar produto no carrinho.")

async def find_product_on_cart(user_email: str, product_id: str):
    await validate_user(user_email)
    await validate_product(product_id)

    product_found = await find_product_on_cart_on_bd(user_email, product_id)
    if product_found:
        return product_found
    
    raise Not_Found_Exception("Produto não encontrado no carrinho")

async def find_cart_products(user_email: str):
    await validate_user(user_email)

    product_list = await find_cart_products_on_bd(user_email)
    if product_list:
        return product_list
    return []

async def find_cart(user_email: str):
    await validate_user(user_email)
    return await find_cart_on_bd(user_email)

async def remove_product_from_cart(user_email: str, product_id: str):
    await validate_user(user_email)
    await validate_product(product_id)
    
    check = await remove_product_from_cart_on_bd(user_email, product_id)
    if not check:
      raise Not_Found_Exception("Produto não encontrado no carrinho.")

async def clear_cart(user_email: str):
    await validate_user(user_email)
    check = await clear_cart_on_bd(user_email)
    if not check:
      raise Not_Found_Exception("Não existe produtos no carrinho.")

async def update_product_on_cart(user_email: str, cart_product: CartProduct):
    await validate_user(user_email)
    await validate_product(cart_product.product_id)

    cart_product_dict = cart_product.dict()
    product_updated = await update_product_on_cart_on_bd(user_email, cart_product_dict)
    if not product_updated:
      raise Not_Found_Exception("O produto não está no carrinho")

async def validate_user(user_email):
  user = await find_user_by_email(user_email)
  if not user:
    raise Not_Found_Exception("Nenhum usuário cadastrado com o e-mail informado.")
  return user

async def validate_product(product_code):
  product = await find_product_by_code(product_code)
  if not product:
    raise Not_Found_Exception("Nenhum produto cadastrado com o ID informado")
  return product
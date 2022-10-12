from shopping_cart.src.models.entity.address import Address
from shopping_cart.src.models.exceptions.exceptions import(
    Bad_Request_Exception,
    Duplicated_Exception,
    Not_Found_Exception,
    Server_Exception
)
from shopping_cart.src.repository.address_repository import(
    insert_new_address,
    find_user_addresses,
    update_address
)
from shopping_cart.src.repository.user_repository import(
  find_user_by_email
)

async def insert_address(user_email: str, new_address: Address):
  user = await find_user_by_email(user_email)
  if not user:
    raise Bad_Request_Exception("O e-mail informado não está cadastrado")

  user_address = await find_user_addresses(user)

  if user_address:
    list(filter(lambda x: validate_address(x, new_address.dict()), user_address['address']))

    result = await update_address(user_address, new_address.dict())
    if result.modified_count > 0:
      return new_address
    else:
      raise Server_Exception("Erro ao atualizar o endereço")
  else:
    result = await insert_new_address({
      'user': user,
      'address': [new_address.dict()]
    })

    if result.inserted_id:
      return new_address
    else:
      raise Server_Exception("Erro ao cadastrar endereço")

def validate_address(address, new_address):
  is_same_street = address['street'] == new_address['street']
  is_same_house_number = address['house_number'] == new_address['house_number']
  is_same_zipcode = address['zipcode'] == new_address['zipcode']
  is_same_id = address['id'] == new_address['id']
  
  if (is_same_street and is_same_house_number and is_same_zipcode):
    raise Duplicated_Exception("Endereço já cadastrado")

  if (is_same_id):
    raise Duplicated_Exception("Já existe um endereço cadastrado com o mesmo id")

async def get_user_addresses(user_email, zipcode, nickname):
  user = await find_user_by_email(user_email)
  if not user:
    raise Bad_Request_Exception("O e-mail informado não está cadastrado")

  response = await find_user_addresses(user)

  if response:
    if zipcode == '' and nickname == '':
      return response['address']

    addresses = list(filter(lambda x: x['zipcode'] == zipcode or x['nickname'] == nickname, response['address']))
    return addresses
  else:
    return []
    
async def update_user_address(user_email: str, zipcode: str, new_address: dict):
  user = await find_user_by_email(user_email)
  if not user:
    raise Bad_Request_Exception("O e-mail informado não está cadastrado")

  user_address = await find_user_addresses(user)

  addresses = list(filter(lambda x: x.azul == new_address.azul, user_address['address']))

  result = await update_address(user_address, new_address)
  if result.modified_count > 0:
    return "testando update endereço"
  else:
    raise Duplicated_Exception("Endereço já cadastrado")

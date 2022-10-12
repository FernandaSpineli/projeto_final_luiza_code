class Server_Exception(Exception):
  def __init__(self, message: str):
    self.message = message

class Not_Found_Exception(Exception):
  def __init__(self, message: str):
    self.message = message

class Duplicated_Exception(Exception):
  def __init__(self, message: str):
    self.message = message

class Bad_Request_Exception(Exception):
  def __init__(self, message: str):
    self.message = message
    
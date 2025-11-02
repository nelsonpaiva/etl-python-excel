# ...existing code...
# Importa BaseModel e Field do pydantic para definir modelos de dados e metadados dos campos
from pydantic import BaseModel, Field

# Define um modelo de dados chamado User que herda de BaseModel
class User(BaseModel):
    # Declara o campo 'name' como string.
    # Field configura um valor padrão (aqui 123) e ativa a validação do valor padrão.
    # Observação: usar um valor padrão não compatível com o tipo (int para str) provoca
    # comportamento de validação/convert-to-str dependendo da versão do pydantic.
    name: str = Field(default=123, validate_default=True)

# Cria uma instância do modelo User (dispara validação na criação)
user = User()

# Imprime a representação da instância user no console
print(user)
# ...existing code...
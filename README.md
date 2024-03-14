# API IoT

Esta é uma API para controle de dispositivos IoT, onde você pode listar, criar e excluir dispositivos.

## Funcionalidades

- Listar dispositivos IoT.
- Criar novos dispositivos IoT.
- Excluir dispositivos IoT existentes.

## Endpoints

- **Listar Dispositivos:**
  - Método: `GET`
  - URL: `/api_iot/dispositivos/`
  - Descrição: Retorna a lista de todos os dispositivos.

- **Criar Dispositivo:**
  - Método: `POST`
  - URL: `/api_iot/dispositivos/create/`
  - Descrição: Cria um novo dispositivo com os seguintes campos em formato JSON:
    - `Sensor`: Booleano indicando se há um sensor no dispositivo.
    - `Botao`: Booleano indicando se há um botão no dispositivo.
    - `LigaRobo`: Booleano indicando o status de ligar o robô.
    - `ResetContador`: Booleano indicando o status de resetar o contador.
    - `ValorContagem`: Inteiro opcional indicando o valor de contagem do dispositivo.

- **Excluir Dispositivo:**
  - Método: `DELETE`
  - URL: `/api_iot/dispositivos/<id>/`
  - Descrição: Exclui o dispositivo com o ID especificado.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- HTML
- CSS
- JavaScript

## Modelo de Dados

A tabela abaixo descreve os campos do modelo de dados `DeviceModel`:

| Campo          | Tipo        | Descrição                                           |
|----------------|-------------|-----------------------------------------------------|
| Sensor         | Booleano    | Indica se há um sensor no dispositivo.             |
| Botao          | Booleano    | Indica se há um botão no dispositivo.              |
| LigaRobo       | Booleano    | Indica o status de ligar o robô.                   |
| ResetContador  | Booleano    | Indica o status de resetar o contador.             |
| ValorContagem  | Inteiro     | Valor de contagem do dispositivo (opcional).       |

## Como Usar

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/api-iot.git
   ```

2. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute as Migrações:**

   ```bash
   python manage.py migrate
   ```

4. **Execute o Servidor:**

   ```bash
   python manage.py runserver
   ```

5. **Acesse a API:**

   Abra o navegador e acesse `http://localhost:8000/api_iot/dispositivos/` para listar os dispositivos. Utilize outros endpoints conforme necessário para criar ou excluir dispositivos.

## Autor

Esta API foi desenvolvida por [Rafael Rodrigues](https://github.com/RafaelRodrigues44).

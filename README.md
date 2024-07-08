
# ProductMangement

Deployed project at:- https://8ok1nkalmb.execute-api.us-east-1.amazonaws.com/production/

## Project Setup

Make sure you have the following installed:
- Python 3
- Pip

Create a .env file with following variables in the root directory
```
DB_HOST
DB_NAME
DB_USER
DB_PASS
```

Run project locally using docker, make sure the ports 8000 and 5432 are idle:

```bash
  docker-compose up --build
```
Set up project locally

- Create a virtual environment using.
```bash
  python venv -m env
```
- Activate the virtual environment.
```bash
  env\Scripts\activate
```
- Install dependencies
```bash
  pip install -r requirements.txt
```
- Run the server
```bash
  python manage.py runserver
```
Get the Swagger API documentation on:
```bash
http://localhost:8000/api/schema/docs
```

### Deployment on AWS Lambda
- Have the dependencies installed

- Configure AWS cli on your local machine.

- Have a .env file created in root directory with following variables
```
DB_HOST=''
DB_NAME=''
DB_USER=''
DB_PASS=''
PROD=True
```
- Deploy on AWS Lambda.
```bash
  zappa deploy production
```
- Update the previous deployment.
```bash
  zappa update production
```
- Find the detailed deployment steps at ".github/workflows/cd.yml"
## API Reference

#### Find the deployed API reference on 
```
https://8ok1nkalmb.execute-api.us-east-1.amazonaws.com/production/api/schema/docs/
```

#### Get all product

```http
  GET /api/product/manage/
```

#### Create new product

```http
  POST /api/product/manage/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `product_name`      | `string` | **Required**. Name of the product |
| `product_description`      | `string` | **Required**. Description of the product |
| `product_price`      | `string` | **Required**. Price of the product |


#### Get product by id

```http
  GET /api/product/manage/{id}/
```

#### Update a product

```http
  PUT /production/api/product/manage/{id}/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `product_name`      | `string` | **Required**. Name of the product |
| `product_description`      | `string` | **Required**. Description of the product |
| `product_price`      | `string` | **Required**. Price of the product |

#### Partial update a product
```http
  Patch /production/api/product/manage/{id}/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `product_name`      | `string` | **Required**. Name of the product |
| `product_description`      | `string` | **Required**. Description of the product |
| `product_price`      | `string` | **Required**. Price of the product |

#### Delete a product
```http
  Delete /production/api/product/manage/{id}/
```
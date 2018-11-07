# Pizzabot

Very basic pizza ordering system

### Requirements
 
- Python 3.6 or later
- Django 2.1 or later
- Postgresql 9

### Setup

Create virtualenv and activate it

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```

Install dependencies

```sh
$ pip install -r requirements.txt
```

Setup migrations and super user

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

Run

```sh
$ python manage.py runserver
```

[Here](http://localhost:8000/) is running the project.


## Create Order

__Endpoint__: `/order/`
<br>
__Method__: POST

__Params__

Body:

- `pizza`: Pizza id. 
- `customer`: Customer id. 
- `size`: Pizza size. (30 >= size <= 50) <int>
- `customer_address`: Customer address in plain text. 


## Get Order

__Endpoint__: /order/`order_id`/
<br>
__Method__: GET

__Params__

- `order_id`: Order id. 


## Get all Orders

__Endpoints__: 
- /order/
- /order/`page`/
- /order/`page`/`items`/
<br>

__Method__: GET

__Params__

- `page`: Page of orders. <int>
- `items`: Items per page. <int>


## Update Order

__Endpoint__: /order/`oder_id`/
<br>
__Method__: PUT

__Params__

- `order_id`: Order id. 

Body:

- `pizza`: Pizza id. 
- `customer`: Customer id. 
- `size`: Pizza size. (30 >= size <= 50) <int>
- `customer_address`: Customer address in plain text. 


## Remove Order

__Endpoint__: /order/`order_id`/
<br>
__Method__: DELETE

__Params__

- `order_id`: Order id. 


## Get Customer Orders

__Endpoint__: /order/customer/`customer_id`/
<br>
__Method__: GET

__Params__

- `customer_id`: Customer id. 


### Testing

```sh
$ python manage.py test ordering.tests
```

### Author

__Luis Esteban Rodríguez__ <*rodriguezjluis0@gmail.com*>
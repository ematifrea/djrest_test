### The project demonstrates a simple use of Django Framework and
### Django REST framework.
The Python interpreter version used in the project is 2.7.6.

### Project dependencies:
        Django==1.9.1
        djangorestframework==3.3.2
        psycopg2==2.6.1
        requests==2.9.1
        xmltodict==0.9.2 

### Setting up the project

#### 1. Create a virtual environment
    with virtualenv: $ virtualenv <name>
     or  
    with virtualenvwrapper: $ mkvirtualenv <name>

#### 2. Activate the virtual environment
    $ source ../<name>/bin/activate
    or
    $ workon <name>

#### 3. Create a local repository:
    $ git clone https://github.com/ematifrea/djrest_test

#### 4. Install the project requirements:
    $ cd ../djrest_test
    $ pip install -r requirements.txt       
    
#### 5. Run migrations:
    $ ./manage.py migrate
    
#### 6. Run the custom Django command in order
####to populate the default database( sqlite):
    $ ./manage.py loaddata_api

#### 6. Start server
    $ ./manage.py runserver

#### 7. Endpoints:
    List orders : /orders/list/
    Display 1 order: /orders/detail/1/
    Search orders by model's fields and display result:
        /orders/list/?<param>=<value>
        where <param> can be any combination of the model fields : id, order_id,
        marketplace, purchase_date, items, amount,  currency, shipping
    Create a new order: /orders/create/
    Update an order: /orders/update/<pk>/
    
#### 8. REST endpoints (modelViewSets):
##### GET / POST on /api/orders/, 
##### GET, PUT, DELETE pe /api/orders/pk/, 
##### GET /api/orders/?search=text/

    
    
#### Steps in development:

##### 1. Create a new Django project:
    $ django-admin startproject djrest-test

##### 2. Create a new application in the project:
    $ cd djrest-test
    $ ./manage.py startapp orders
    
#### 3. Create a superuser for the project:
    $ ./manage.py createsuperuser
    
#### 4. Create the model and the migration and apply
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    
    
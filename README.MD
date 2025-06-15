# Set up environment

## Create virtual environment

clone this project from my github, switch to that directory in terminal and enter

```
    py -3 -m venv .venv
```

### Activating virtual environment

```
    #for mac
    .venv/bin/activate
    #for win
    .venv\Scripts\activate
```

### Install dependencies

```
    pip install -r requirements.txt

```
### Set up database

**Update the database connection string**  
   Open the `config.py` file and replace the following line with your own PostgreSQL credentials:

```
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@localhost:5433/userdb"
 ```

**Create the database in PostgreSQL**

```
    CREATE DATABASE userdb
```

**Run the following commands in your terminal to create the database tables:**

```
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
```




### Run the project 

```
    python run.py 
```
### Link to test API

```
    http://127.0.0.1:5000/docs/user
```
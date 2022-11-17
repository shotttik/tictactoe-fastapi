# tictactoe-fastapi
### About
#####FASTApi, sqlalchemy,Database `posrgresql`


# Running the Project Locally

First, clone the repository to your local machine:

```
> git clone https://github.com/shotttik/tictactoe-fastapi
```

Second, create virtual environment
```
> python3 -m venv env
```

Third, activate virtual environment
```
> source env/bin/activate
```

Install the requirements:

```
> python3 -m pip install -r requirements.txt

```
CREATE .env file in main directory with content example:
```

> DATABASE="postgresql://postgres:postgres@localhost/tictactoe"

```
Finally, run the server:
```
> uvicorn main:app --reload
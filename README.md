# Flask SQLite

Playing around with Flask and SQLite3 DB to make a simple create and read API.

## Start API
Add the main.py file to the environment as the entry file using
```commandline
export FLASK_APP=main
```

And then run the following command
```commandline
flask run
```

### OR DO IT THIS WAY
```commandline
python main.py
```


## Note To Self

> A cursor is required to execute fetch queries

> Need to execute the commit() method on the connection object to save a connection/query result

> Also need to close the connection after executing a query

> Can use the rollback() method to undo a transaction

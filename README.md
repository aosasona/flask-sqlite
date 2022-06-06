# Flask SQLite

Playing around with Flask and SQLite3 DB to make a simple create and read API.

#### A cursor is required to execute fetch queries
#### Need to execute the commit() method on the connection object to save a connection/query result
#### Also need to close the connection after executing a query
#### Can use the rollback() method to undo a transaction
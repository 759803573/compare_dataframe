from connection.base_connection import BaseConnection

class JDBCConnection(BaseConnection):
  connection_keys = ['url', 'user', 'password', 'dbtable', 'driver']
  def _connection(self):
    return self.spark.read.format('jdbc').options(**self.kwargs).load()
# {'url': 'jdbc:mysql://source_mysql:3306', 'user': 'root', 'password': 'example', 'dbtable': 'source_db.source_table', 'driver': 'com.mysql.jdbc.Driver'}

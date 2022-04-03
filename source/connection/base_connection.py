class BaseConnection():
  connection_keys = []
  def __init__(self, spark_app, **kwargs):
    self.kwargs = { key: val for (key, val) in kwargs.items() if key in self.connection_keys}
    self.spark_app = spark_app
    self.spark = spark_app.spark

  def connection(self):
    df = self._connection()
    return df
  
  def _connection():
    raise NotImplementedError('Need Implement By Subclass')


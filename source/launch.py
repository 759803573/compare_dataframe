from utils.singleton import *
from pyspark.sql import SparkSession
import importlib

@singleton
class SparkAPP(object):
  def __init__(self, app_name):
    self.app_name = app_name
    self.spark = self.getSparkSession(app_name)

  def getSparkSession(self, app_name, ):
    if not hasattr(self, 'spark') or self.spark is None:
      self.spark = SparkSession.builder.appName(app_name).getOrCreate()
    return self.spark

def main(app_name, read_config={'type': '', 'params': {}}, ):
  sparkAPP= SparkAPP(app_name)

  connModule = importlib.import_module(f'connection.{read_config["type"]}_connection')
  connClass = getattr(connModule, f'{read_config["type"].upper()}Connection')
  
  conn = connClass(sparkAPP, **read_config['params'])
  return sparkAPP, conn

if __name__ == '__main__':
  sa, conn = main('test', read_config= {
    'type': 'jdbc',
    'params': {
      'url': 'jdbc:mysql://192.168.3.121:23307', 
      'user': 'root', 
      'password': 'example', 
      'dbtable': 'source_db.source_table', 
      'driver': 'com.mysql.jdbc.Driver'
    }
  })
  conn.connection().show()

import mysql.connector
from mysql.connector import errorcode


class mysqldb(): 

  def __init__(self,servernanme='pitchounmysqldb-dev.mysql.database.azure.com',username='dovives@pitchounmysqldb-dev',password='*DouMe97',database='pitchoundb'):

    """Connect to MySQL DB""" 
    # Obtain connection string information from the portal
    self.config = {
      'host':servernanme,
      'user':username,
      'password':password,
      'database':database
    }

  def connect_mysql(self):
  # Construct connection string
    try:
      conn = mysql.connector.connect(**self.config)
      print("Connection established")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cursor = conn.cursor()
      return conn


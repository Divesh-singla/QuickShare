import sys
sys.path.insert(0,r'S:\ACIL\project\schoolCRM')
from mysqlConnection.connection import getConnection

sql = getConnection()

def __getLastRowId():
    return sql.lastrowid
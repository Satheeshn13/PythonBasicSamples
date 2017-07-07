import MySQLdb
import threading
import time
from DBUtils.PooledDB import PooledDB

MySQLPool = PooledDB(creator=MySQLdb,
                    host="",
                    user="",
                    passwd="",
                    db="",
                    maxconnections=10,
                    blocking=True, 
                    charset='utf8')

def testfunction(<arguments>):
	

	conn = MySQLPool.connection()
	cur = conn.cursor()

	cur.execute('''Query''')

    ########
	
	Logic 

	cur.close()

if __name__ == "__main__":

	t=threading.Thread(target=testfunction, args=(arguments))
	
	t.start()




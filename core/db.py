import psycopg2

class DB():
    __host = 'ec2-54-237-135-248.compute-1.amazonaws.com'
    __user = 'nojqipdrehgrix'
    __dbname = 'd983sbjglsr7gk'
    __password = 'a7da3f02b6ca8af767691fd97f2595155ed2bb2b34af0aece6bd2ec3065a8***'
    __sslmode = 'require'    

    #-------------------------
    # 取得資料庫連線
    #-------------------------
    @staticmethod    
    def getConn():
        conn_string = f'host={DB.__host} user={DB.__user} dbname={DB.__dbname} password={DB.__password} sslmode={DB.__sslmode}'
        return psycopg2.connect(conn_string)
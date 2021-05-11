from core.db import DB
from models.user import User

#-------------------------------
# 取出員工資料
#-------------------------------
def user_read(userID, password):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令, 取得資料        
    cursor.execute("SELECT * FROM employee WHERE empno=%s and ext=%s", (userID, password))
    data = cursor.fetchone() 
    
    if data is not None:
        user = User(*data[:2])   
    else:
        user = None
 
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳
    return user  

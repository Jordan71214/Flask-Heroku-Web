from core.db import DB
from models.customer import Customer

#-------------------------------
# 取出所有資料
#-------------------------------
def customer_read_all():
    conn = DB.getConn()
    cursor = conn.cursor()
        
    # 執行SQL命令
    cursor.execute("SELECT * FROM customer ORDER BY cusno")
    data = cursor.fetchall()   
       
    result=[]
    for d in data:
        result.append(Customer(*d)) 
            
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳資料
    return result

#-------------------------------
# 取出單一資料
#-------------------------------
def customer_read(cusno):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令, 取得資料        
    cursor.execute("SELECT * FROM customer where cusno = %s", (cusno,))
    data = cursor.fetchone() 
    
    if data is not None:
        customer = Customer(*data) 
    else:
        customer = None         
 
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳
    return customer  

#-------------------------------
# 刪除資料
#-------------------------------
def customer_delete(cusno):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令
    try:        
        cursor.execute("DELETE FROM customer where cusno = %s", (cusno,))
        rowCnt = cursor.rowcount 
    except:
        rowCnt = 0
            
    # 更改資料庫內容
    conn.commit()
    
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳
    return rowCnt

#-------------------------------
# 新增資料
#-------------------------------
def customer_create(customer):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    

    # 執行SQL命令
    try:        
        cursor.execute("INSERT INTO customer (cusno, cusname, contactor, title, address) VALUES (%s, %s, %s, %s, %s)"
        , (customer.cusno, customer.cusname, customer.contactor, customer.title, customer.address))
        rowCnt = cursor.rowcount 
    except:
        rowCnt = 0
            
    # 更改資料庫內容
    conn.commit()
    
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳
    return rowCnt

#--------------------
# 更改資料
#--------------------  
def customer_update(customer):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令
    try:        
        cursor.execute("UPDATE customer SET cusname=%s, contactor=%s, title=%s, address=%s WHERE cusno=%s"
        , (customer.cusname, customer.contactor, customer.title, customer.address, customer.cusno))
        rowCnt = cursor.rowcount 
    except:
        rowCnt = 0
            
    # 更改資料庫內容
    conn.commit()
        
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回變更筆數
    return rowCnt      
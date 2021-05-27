from core.db import DB
from models.product import Product

#-------------------------------
# 取出所有資料
#-------------------------------
def product_read_all():
    conn = DB.getConn()
    cursor = conn.cursor()
        
    # 執行SQL命令
    cursor.execute("SELECT * FROM product ORDER BY prono")
    data = cursor.fetchall()   
       
    result=[]
    for d in data:
        result.append(Product(*d)) 
            
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳資料
    return result

#-------------------------------
# 取出單一資料
#-------------------------------
def product_read(prono):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令, 取得資料        
    cursor.execute("SELECT * FROM product where prono = %s", (prono,))
    data = cursor.fetchone() 
    
    if data is not None:
        product = Product(*data) 
    else:
        product = None         
 
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳
    return product  

#-------------------------------
# 刪除資料
#-------------------------------
def product_delete(prono):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令
    try:        
        cursor.execute("DELETE FROM product where prono = %s", (prono,))
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
def product_create(product):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()



    # 執行SQL命令
    try:        
        cursor.execute("INSERT INTO product (prono, proname, supno, typno, price) VALUES (%s, %s, %s, %s, %s)"
        , (product.prono, product.proname, product.supno, product.typno, product.price))
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
def product_update(product):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令
    try:        
        cursor.execute("UPDATE product SET proname=%s, supno=%s, typno=%s, price=%s WHERE prono=%s"
        , (product.proname, product.supno, product.typno, product.price, product.prono))
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
from core.db import DB
from models.supplier import Supplier

#-------------------------------
# 取出所有資料
#-------------------------------
def supplier_read_all():
    conn = DB.getConn()
    cursor = conn.cursor()
        
    # 執行SQL命令
    cursor.execute("SELECT * FROM supplier ORDER BY supno")
    data = cursor.fetchall()   
       
    result=[]
    for d in data:
        result.append(Supplier(*d)) 
            
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳資料
    return result

#-------------------------------
# 取出單一資料
#-------------------------------
def supplier_read(supno):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令, 取得資料        
    cursor.execute("SELECT * FROM supplier where supno = %s", (supno,))
    data = cursor.fetchone() 
    
    if data is not None:
        supplier = Supplier(*data) 
    else:
        supplier = None         
 
    # 關閉cursor及連線
    cursor.close()  
    conn.close()

    # 回傳
    return supplier  

#-------------------------------
# 刪除資料
#-------------------------------
def supplier_delete(supno):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令
    try:        
        cursor.execute("DELETE FROM supplier where supno = %s", (supno,))
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
def supplier_create(supplier):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    

    # 執行SQL命令
    try:        
        cursor.execute("INSERT INTO supplier (supno, supname, contactor, title, address) VALUES (%s, %s, %s, %s, %s)"
        , (supplier.supno, supplier.supname, supplier.contactor, supplier.title, supplier.address))
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
def supplier_update(supplier):
    # 取得連線及cursor
    conn = DB.getConn()
    cursor = conn.cursor()

    # 執行SQL命令
    try:        
        cursor.execute("UPDATE supplier SET supname=%s, contactor=%s, title=%s, address=%s WHERE supno=%s"
        , (supplier.supname, supplier.contactor, supplier.title, supplier.address, supplier.supno))
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
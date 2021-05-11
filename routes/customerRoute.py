from flask import render_template, request
from core.db import DB
from services import customerService
from models.customer import Customer

def init_app(app):
    #--------------------
    # 客戶清單
    #--------------------
    @app.route('/customer/list', methods=['GET'])
    def customerList():
        data = customerService.customer_read_all()        
        return render_template('customer/list.html', customers=data)

    #--------------------
    # 客戶查詢表單
    #--------------------  
    @app.route('/customer/read/form')
    def customerReadForm():
        return render_template('customer/read-form.html')

    #--------------------
    # 客戶查詢結果
    #--------------------  
    @app.route('/customer/read', methods=['GET'])
    def customerRead():
        # 取得參數
        cusno = request.values.get('cusno')
        
        # 取得客戶資料
        data = customerService.customer_read(cusno)

        # 回傳查詢結果的網頁
        if data is not None:
            return render_template('customer/read.html', customer=data)   
        else:
            return render_template('customer/not-found.html', cusno=cusno)   
    
    #--------------------
    # 客戶刪除表單
    #--------------------  
    @app.route('/customer/delete/form')
    def customerDeleteForm():
        return render_template('customer/delete-form.html')

    #--------------------
    # 客戶刪除
    #--------------------  
    @app.route('/customer/delete', methods=['POST'])
    def customerDelete():
        # 取得參數
        cusno = request.form.get('cusno')
        
        # 刪除客戶資料
        rowCnt = customerService.customer_delete(cusno)

        # 回傳刪除結果的網頁
        return render_template('customer/delete.html', cnt=rowCnt)     
       
    #--------------------
    # 客戶新增表單
    #--------------------  
    @app.route('/customer/create/form')
    def customerCreateForm():
        return render_template('customer/create-form.html')

    #--------------------
    # 客戶新增結果
    #--------------------  
    @app.route('/customer/create', methods=['POST'])
    def customerCreate():
        # 取得參數
        cusno = request.form.get('cusno')
        cusname = request.form.get('cusname')
        contactor = request.form.get('contactor')
        title = request.form.get('title')
        address = request.form.get('address')
        
        # 建立客戶物件
        customer = Customer(cusno, cusname, contactor, title, address)
        
        # 新增客戶資料
        rowCnt = customerService.customer_create(customer)

        # 回傳新增後的網頁
        return render_template('customer/create.html', cnt=rowCnt) 
      
    #--------------------
    # 客戶更改資料讀取表單
    #--------------------  
    @app.route('/customer/update/read/form')
    def customerUpdateReadForm():
        return render_template('customer/update-read-form.html')
        
    #--------------------
    # 客戶更改資料讀取
    #--------------------  
    @app.route('/customer/update/read', methods=['GET'])
    def customerUpdateRead():
        # 取得查詢編號
        cusno = request.values.get('cusno')
        
        # 取得將更改的資料
        data = customerService.customer_read(cusno)

        # 回傳將更改資料網頁
        if data is not None:
            return render_template('customer/update-form.html', customer=data)   
        else:
            return render_template('customer/not-found.html', cusno=cusno)   
        
    #--------------------
    # 客戶更改結果
    #--------------------  
    @app.route('/customer/update', methods=['POST'])
    def customerUpdate():
        # 取得更改資料
        cusno = request.form.get('cusno')
        cusname = request.form.get('cusname')
        contactor = request.form.get('contactor')
        title = request.form.get('title')
        address = request.form.get('address')
        
        customer = Customer(cusno, cusname, contactor, title, address)
                            
        # 更改資料
        rowCnt = customerService.customer_update(customer)        

        # 回傳更改後的網頁
        return render_template('customer/update.html', cnt=rowCnt)       
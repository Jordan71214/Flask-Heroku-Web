from flask import render_template, request
from core.db import DB
from services import productService
from models.product import Product

def init_app(app):
    #--------------------
    # 客戶清單
    #--------------------
    @app.route('/product/list', methods=['GET'])
    def productList():
        data = productService.product_read_all()        
        return render_template('product/list.html', products=data)

    #--------------------
    # 客戶查詢表單
    #--------------------  
    @app.route('/product/read/form')
    def productReadForm():
        return render_template('product/read-form.html')

    #--------------------
    # 客戶查詢結果
    #--------------------  
    @app.route('/product/read', methods=['GET'])
    def productRead():
        # 取得參數
        prono = request.values.get('prono')
        
        # 取得客戶資料
        data = productService.product_read(prono)

        # 回傳查詢結果的網頁
        if data is not None:
            return render_template('product/read.html', product=data)   
        else:
            return render_template('product/not-found.html', prono=prono)   
    
    #--------------------
    # 客戶刪除表單
    #--------------------  
    @app.route('/product/delete/form')
    def productDeleteForm():
        return render_template('product/delete-form.html')

    #--------------------
    # 客戶刪除
    #--------------------  
    @app.route('/product/delete', methods=['POST'])
    def productDelete():
        # 取得參數
        prono = request.form.get('prono')
        
        # 刪除客戶資料
        rowCnt = productService.product_delete(prono)

        # 回傳刪除結果的網頁
        return render_template('product/delete.html', cnt=rowCnt)     
       
    #--------------------
    # 客戶新增表單
    #--------------------  
    @app.route('/product/create/form')
    def productCreateForm():
        return render_template('product/create-form.html')

    #--------------------
    # 客戶新增結果
    #--------------------  
    @app.route('/product/create', methods=['POST'])
    def productCreate():
        # 取得參數
        prono = request.form.get('prono')
        proname = request.form.get('proname')
        supno = request.form.get('supno')
        typno = request.form.get('typno')
        price = request.form.get('price')
        
        # 建立客戶物件
        product = Product(prono, proname, supno, typno, price)
        
        # 新增客戶資料
        rowCnt = productService.product_create(product)

        # 回傳新增後的網頁
        return render_template('product/create.html', cnt=rowCnt) 
      
    #--------------------
    # 客戶更改資料讀取表單
    #--------------------  
    @app.route('/product/update/read/form')
    def productUpdateReadForm():
        return render_template('product/update-read-form.html')
        
    #--------------------
    # 客戶更改資料讀取
    #--------------------  
    @app.route('/product/update/read', methods=['GET'])
    def productUpdateRead():
        # 取得查詢編號
        prono = request.values.get('prono')
        
        # 取得將更改的資料
        data = productService.product_read(prono)

        # 回傳將更改資料網頁
        if data is not None:
            return render_template('product/update-form.html', product=data)   
        else:
            return render_template('product/not-found.html', prono=prono)   
        
    #--------------------
    # 客戶更改結果
    #--------------------  
    @app.route('/product/update', methods=['POST'])
    def productUpdate():
        # 取得更改資料
        prono = request.form.get('prono')
        proname = request.form.get('proname')
        supno = request.form.get('supno')
        typno = request.form.get('typno')
        price = request.form.get('price')
        
        product = Product(prono, proname, supno, typno, price)
                            
        # 更改資料
        rowCnt = productService.product_update(product)        

        # 回傳更改後的網頁
        return render_template('product/update.html', cnt=rowCnt)       
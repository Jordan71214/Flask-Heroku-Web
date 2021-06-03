from flask import render_template, request
from core.db import DB
from services import supplierService
from models.supplier import Supplier

def init_app(app):
    #--------------------
    # 供應商清單
    #--------------------
    @app.route('/supplier/list', methods=['GET'])
    def supplierList():
        data = supplierService.supplier_read_all()        
        return render_template('supplier/list.html', suppliers=data)

    #--------------------
    # 供應商查詢表單
    #--------------------  
    @app.route('/supplier/read/form')
    def supplierReadForm():
        return render_template('supplier/read-form.html')

    #--------------------
    # 供應商查詢結果
    #--------------------  
    @app.route('/supplier/read', methods=['GET'])
    def supplierRead():
        # 取得參數
        supno = request.values.get('supno')
        
        # 取得供應商資料
        data = supplierService.supplier_read(supno)

        # 回傳查詢結果的網頁
        if data is not None:
            return render_template('supplier/read.html', supplier=data)   
        else:
            return render_template('supplier/not-found.html', supno=supno)   
    
    #--------------------
    # 供應商刪除表單
    #--------------------  
    @app.route('/supplier/delete/form')
    def supplierDeleteForm():
        return render_template('supplier/delete-form.html')

    # --------------------
    # 供應商刪除
    #--------------------  
    @app.route('/supplier/delete', methods=['POST'])
    def supplierDelete():
        # 取得參數
        supno = request.form.get('supno')
        
        # 刪除供應商資料
        rowCnt = supplierService.supplier_delete(supno)

        # 回傳刪除結果的網頁
        return render_template('supplier/delete.html', cnt=rowCnt)     
       
    #--------------------
    # 供應商新增表單
    #--------------------  
    @app.route('/supplier/create/form')
    def supplierCreateForm():
        return render_template('supplier/create-form.html')

    #--------------------
    # 供應商新增結果
    #--------------------  
    @app.route('/supplier/create', methods=['POST'])
    def supplierCreate():
        # 取得參數
        supno = request.form.get('supno')
        supname = request.form.get('supname')
        contactor = request.form.get('contactor')
        title = request.form.get('title')
        address = request.form.get('address')
        
        # 建立供應商物件
        supplier = Supplier(supno, supname, contactor, title, address)
        
        # 新增供應商資料
        rowCnt = supplierService.supplier_create(supplier)

        # 回傳新增後的網頁
        return render_template('supplier/create.html', cnt=rowCnt) 
      
    #--------------------
    # 供應商更改資料讀取表單
    #--------------------  
    @app.route('/supplier/update/read/form')
    def supplierUpdateReadForm():
        return render_template('supplier/update-read-form.html')
        
    #--------------------
    # 供應商更改資料讀取
    #--------------------  
    @app.route('/supplier/update/read', methods=['GET'])
    def supplierUpdateRead():
        # 取得查詢編號
        supno = request.values.get('supno')
        
        # 取得將更改的資料
        data = supplierService.supplier_read(supno)

        # 回傳將更改資料網頁
        if data is not None:
            return render_template('supplier/update-form.html', supplier=data)   
        else:
            return render_template('supplier/not-found.html', supno=supno)   
        
    #--------------------
    # 供應商更改結果
    #--------------------  
    @app.route('/supplier/update', methods=['POST'])
    def supplierUpdate():
        # 取得參數
        supno = request.form.get('supno')
        supname = request.form.get('supname')
        contactor = request.form.get('contactor')
        title = request.form.get('title')
        address = request.form.get('address')
        
        # 建立供應商物件
        supplier = Supplier(supno, supname, contactor, title, address)
                            
        # 更改資料
        rowCnt = supplierService.supplier_update(supplier)        

        # 回傳更改後的網頁
        return render_template('supplier/update.html', cnt=rowCnt)       
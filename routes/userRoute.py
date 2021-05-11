from flask import render_template, request, session
from core.db import DB
from services import userService
from models.user import User

def init_app(app):
    #------------------------  
    # 設定session加密的金鑰
    #------------------------   
    app.config['SECRET_KEY'] = 'dmibutnntubimd'

    #-----------------
    # 使用者登入表單
    #-----------------
    @app.route('/user/login/form', methods=['GET'])
    def userLoginForm():
        return render_template('user/login-form.html')

    #-----------------
    # 登入成功頁面
    #-----------------
    @app.route('/user/welcome', methods=['GET'])
    def welcome():
        return render_template('user/welcome.html')

    #-----------------
    # 顯示使用者頁面
    #-----------------
    @app.route('/user/show', methods=['GET'])
    def userShow():
        try:
            return render_template('user/welcome.html', name=session['username'])
        except:
            return render_template('user/login-form.html')
                
    #-----------------
    # 使用者登入驗證
    #-----------------
    @app.route('/user/login', methods=['POST'])
    def userLogin():
        # 取得使用者輸入的帳號及密碼
        userID = request.form.get('userID')
        password = request.form.get('password')         

        # 讀出使用者資料
        user = userService.user_read(userID, password)        
        
        if user is not None:
            # 登入成功後把userID和使用者姓名存到session裡
            session['uid'] = user.userno
            session['username'] = user.username
            return render_template('user/welcome.html', name=user.username)
        else:
            session.clear()
            return render_template('user/login-form.html', result='帳密不符!')

    #-----------------
    # 使用者登出
    #-----------------
    @app.route('/user/logout', methods=['GET'])
    def userLogout():
        # 清除session內容
        session.clear()
        
        # 回傳登出畫面
        return render_template('user/logout.html')     
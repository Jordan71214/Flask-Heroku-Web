#-----------------------
# 建立flask物件
#-----------------------
from flask import Flask, render_template, session, request
app = Flask(__name__)

#-----------------------
# 設定服務前的登入檢查
#-----------------------
@app.before_request
def beforeRequest():    
    if '/user/login' in request.url or 'static' in request.url:
        return None
    else:
        if 'username' not in session:
            return render_template('user/login-form.html')    
        else:
            return None 
        
#-----------------------
# 設定服務路由
#-----------------------
from routes import homeRoute, customerRoute, userRoute, productRoute
userRoute.init_app(app)
homeRoute.init_app(app)
customerRoute.init_app(app)
productRoute.init_app(app)
#-----------------------
# 啟動Flask
#-----------------------
if __name__ == '__main__':
    app.run(debug=True, port=3000, threaded=True)    
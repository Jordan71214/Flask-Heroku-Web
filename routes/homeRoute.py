from flask import render_template

def init_app(app):
    #-----------------------
    # 處理主畫面請求
    #-----------------------
    @app.route('/')
    def home():
        return render_template('index.html')
    
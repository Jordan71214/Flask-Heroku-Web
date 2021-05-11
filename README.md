## 以Flask建立的Web, 沒有ORM, 只處理客戶資料表

```
 <web>
   |
   |__ <static>
   |      |__ <css>
   |      |     |__ main.css   (使用範例檔案)
   |      |     |__ menu.css   (使用範例檔案)
   |      |     |__ color.css  (使用範例檔案)
   |      |
   |      |__ <imgs>
   |            |__ header.jpg  (使用範例檔案)
   |            |__ icon.jpg    (使用範例檔案)
   |
   |__ <templates>
   |      |__ index.html    (主畫面)
   |      |
   |      |__ <customer>         (客戶畫面)
   |      |      |__ list.html            (清單畫面)
   |      |      |__ read-form.html       (查詢畫面)
   |      |      |__ read.html
   |      |      |__ not-found.html
   |      |      |__ delete-form.html     (刪除畫面)
   |      |      |__ delete.html
   |      |      |__ create-form.html     (新增畫面)
   |      |      |__ create.html
   |      |      |__ update-read-form.html    (更新畫面)
   |      |      |__ update-form.html
   |      |      |__ update.html
   |      |
   |      |__ <user>     (使用者)
   |             |__ user-login-form.html    (登入畫面)
   |             |__ user-logout.html        (登出畫面)
   |             |__ user-welcome.html   
   |      
   |__ <core>
   |      |__ db.py    (資料庫)
   |      
   |__ <routes>
   |      |__ homeRoute.py        (主畫面路由)
   |      |__ customerRoute.py    (客戶功能路由)  
   |      |__ userRoute.py        (登入/登出路由)  
   |
   |__ <services>
   |      |__ customerService.py  (客戶功能)
   |      |__ userService.py      (登入/登出功能)  
   |
   |__ app.py  
```

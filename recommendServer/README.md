## recommendServer

+ 配置环境(python3.6 + mysql)

+ 安装依赖

  ```
  pip install django
  pip insatll django-cors-headers
  pip insatll pandas
  pip insatll pillow
  pip insatll pymysql
  ```

+ 修改数据库对应设置（setting.py）

+ 迁移数据库（利用 `models.py`）

  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

+ 启动服务

  ```
  python manage.py runserver
  ```

  
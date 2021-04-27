"""
配置文件

在Flask中，配置不仅可以通过config对象直接写入，还可以从文件中读取。
目前把配置移动到一个单独的文件中，将其命名为settings.py（也常被命名为config.py）。
当在单独的文件中定义配置时，不再使用config对象添加配置，而是直接以键值对的方式写出，和保存环境变量的.flaskenv文件非常相似
"""
import os
from MessageBoard import app

dev_db= 'mysql://test.database3401.scsite.net:3401/tangex_cupid'
SECRET_KEY=os.getenv("SECRET_KEY", 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI',dev_db)
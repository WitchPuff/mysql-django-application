# car-company-website

设计一个汽车公司后端数据库，实现前端网页交互应用，网页连接本地数据库进行查询、修改等操作，并显示查询结果。

环境：Python+Django+MySQL 8.0.31+WSL2

基础的网页实现了如下功能模块：

1. Administrator：直接使用SQL命令行查询。
2. Dealer：允许一个经销商根据特定车辆特征查询本地和其余经销商的库存，来满足客户的需求。
3. Online Customers：设计一个Web接口，方便其寻找经销商和搜索特定产品及其库存和价格。
4. Marketing Department：为市场营销部门提供一个简单的OLAP查询接口。
5. Customer Survey：客户信息调查，客户填写完后其信息会记录在数据库中
6. Services：显示当年top sales的品牌车型及其价格

## 运行方式

默认Python + Django + mysql环境已经配置好了，连接的是本地数据库，数据库结构定义在`/data/DDL.sql`中，导入数据可以选择`relations.sql`。

克隆仓库：

```
git clone https://github.com/WitchPuff/car-company-website
cd mysite
```

可以在`/mysite/mysite/settings.py`中修改连接的数据库（需要事先在本地创建数据库）：

```
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          'ENGINE':'django.db.backends.mysql',
          'NAME':'car', # your database
          'USER':'root',
          'PASSWORD':'test',
          'HOST':'localhost',
          'PORT':'3306',
    }
}
```

如果想使用你自己的本地数据库，可以用这条命令生成新的模板。

```
python manage.py inspectdb > <your app name>/models.py
```

在`mysite/settings.py`中添加你的应用：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'company' # add your app(document name)
]
```

数据库迁移：

```
python manage.py makemigrations
python manage.py migrate
```

再在`mysite/company/views.py`中修改对应models的接口及对应html文件即可。

运行方式：

```
cd mysite
python manage.py runserver
```

访问http://127.0.0.1:8000即可。

## 效果展示

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202301091416283.png" alt="image-20230109141624915" style="zoom: 67%;" />

<center><font size='4'>Home Section

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202301091418035.png" alt="image-20230109141821701" style="zoom:67%;" />

<center><font size='4'>Services & Reviews Section


![image-20230109143125058](https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202301091431264.png)

<center><font size='4'>Admin

![image-20230109141434063](https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202301091414254.png)

<center><font size='4'>Customer Search



## 参考

前端代码Source：https://www.youtube.com/watch?v=dbTe7pmqLv4

#### 
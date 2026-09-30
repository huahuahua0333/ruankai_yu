# django-study

一个用于学习 Django 基础的练手项目，基于 **Django 6.1.1**，覆盖路由、视图、模板、ORM、静态文件、外部 API 调用等核心概念。

## 技术栈

- Python + Django 6.1.1
- MySQL（数据库名 `mysite2`）
- Bootstrap 3.4.1 + jQuery 3.6.0（静态资源）
- [Open-Meteo](https://open-meteo.com/) 免费天气 API

## 项目结构

```
site1/
├── manage.py
├── db.sqlite3            # 本地占位文件，实际使用 MySQL
├── site1/                # 项目配置目录
│   ├── settings.py      # 项目配置（数据库、中间件、模板等）
│   └── urls.py          # 全局路由
└── app01/                # 主应用
    ├── models.py         # 数据模型：UserInfo / Department / Role
    ├── views.py         # 视图函数
    ├── admin.py
    ├── migrations/      # 数据库迁移
    ├── templates/        # HTML 模板
    └── static/          # 静态资源（css / js / img / plugins）
```

## 数据模型

| 模型       | 字段                                  | 说明     |
| ---------- | ------------------------------------- | -------- |
| `UserInfo` | `name`, `password`, `age`             | 用户表   |
| `Department` | `title`                             | 部门表   |
| `Role`     | `caption`                             | 角色表   |

## 路由一览

| 路径              | 视图          | 作用                                             |
| ----------------- | ------------- | ------------------------------------------------ |
| `/index/`         | `index`       | 返回 "欢迎使用"                                  |
| `/user/list/`     | `user_list`   | 渲染用户列表模板                                  |
| `/user/add/`      | `user_add`    | 渲染新增用户模板                                  |
| `/tpl/`           | `tpl`         | 模板渲染演示（字符串 / 列表 / 字典 / 列表套字典）  |
| `/login/`         | `login`       | 简易登录（演示账号 `root` / `123`）              |
| `/orm/`           | `orm`         | ORM 插入演示（部门 + 用户）                       |
| `/info/list/`     | `info_list`   | 用户列表（从 MySQL 查询）                        |
| `/info/add/`      | `info_add`    | 新增用户（POST 提交后重定向到列表）               |
| `/info/delete`    | `info_delete` | 按 `nid` 删除用户                                |
| `/weather/`       | `weather`     | 调用 Open-Meteo 接口展示成都当前气温              |
| `/something/`     | `something`   | 重定向到百度                                      |

## 本地运行

### 1. 安装依赖

```bash
pip install django requests
```

> 本项目未锁定 `requirements.txt`，按当前环境安装即可。

### 2. 配置数据库

在 `site1/settings.py` 中把 `DATABASES` 改成你自己的 MySQL 连接：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite2',
        'USER': 'root',
        'PASSWORD': '你的密码',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

并提前在 MySQL 中创建数据库：

```sql
CREATE DATABASE mysite2 DEFAULT CHARSET utf8mb4;
```

### 3. 执行迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 启动开发服务器

```bash
python manage.py runserver
```

浏览器访问 <http://127.0.0.1:8000/index/>。

## 说明

- 本项目为个人学习用途，登录账号、跳转地址均为硬编码演示，**未做任何安全加固**，请勿直接用于生产。
- `settings.py` 中 `DEBUG = True`，生产环境务必关闭并配置 `ALLOWED_HOSTS`。

## su-blog

![license](https://img.shields.io/github/license/uncle-lv/su-blog) ![stars](https://img.shields.io/github/stars/uncle-lv/su-blog) ![issues](https://img.shields.io/github/issues/uncle-lv/su-blog) ![forks](https://img.shields.io/github/forks/uncle-lv/su-blog) ![FastAPI version](https://img.shields.io/badge/FastAPI-0.70.1-%23009688) ![python version](https://img.shields.io/badge/python-3.7.0-blue)

a single-user blog built with FastAPI and Vue



## 后台API

### 授权

#### 获取token

请求

```
POST http://localhost:8000/api/oauth/access_token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

username=uncle-lv&password=123456
```



响应

```json
HTTP/1.1 201 Created
date: Fri, 31 Dec 2021 03:57:27 GMT
server: uvicorn
content-length: 330
content-type: application/json
connection: close

{
  "token_type": "Bearer",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQxNTI3ODQ4fQ.JjMl3z9DfEKUbB3DbOgR7ICNETicqWPftdtME5QPsDg"
}
```



#### 刷新token

请求

```http
POST http://localhost:8000/api/oauth/access_token/refresh HTTP/1.1
Content-Type: application/json

{
  "token_type": "Bearer",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQxNTI3ODQ4fQ.JjMl3z9DfEKUbB3DbOgR7ICNETicqWPftdtME5QPsDg"
}
```



响应

```json
POST http://localhost:8000/api/oauth/access_token/refresh HTTP/1.1
Content-Type: application/json

{
  "token_type": "Bearer",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTI1NTM2fQ.paOib_sJp36zpGX2anQE6qnVDhhv_z1T6_IC-uA2yd8"
}
```



### 用户

#### 获取当前用户

请求

```http
GET http://localhost:8000/api/oauth/current_user HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM
```



响应

```json
HTTP/1.1 200 OK
date: Fri, 31 Dec 2021 04:21:30 GMT
server: uvicorn
content-length: 179
content-type: application/json
connection: close

{
  "username": "uncle-lv",
  "email": "uncle-lv@gmail.com",
  "avatar_url": "https://avatars.githubusercontent.com/u/88037946?v=4",
  "github_url": "https://github.com/uncle-lv",
  "qq": "17153217"
}
```



#### 修改密码

请求

```http
PATCH http://localhost:8000/api/oauth/pwd HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM

{
    "password": "654321"
}
```



响应

```json
HTTP/1.1 200 OK
date: Fri, 31 Dec 2021 04:42:33 GMT
server: uvicorn
content-length: 4
content-type: application/json
connection: close

null
```



#### 修改用户信息

请求

```http
PUT http://localhost:8000/api/users HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM

{
    "username": "uncle-lv",
    "email": "uncle-lv@email.com",
    "avatar_url": "https://avatars.githubusercontent.com/u/88037946?v=4",
    "github_url": "https://github.com/uncle-lv",
    "qq": "17153217"
}
```



响应

```json
HTTP/1.1 200 OK
date: Fri, 31 Dec 2021 04:44:38 GMT
server: uvicorn
content-length: 179
content-type: application/json
connection: close

{
  "username": "uncle-lv",
  "email": "uncle-lv@email.com",
  "avatar_url": "https://avatars.githubusercontent.com/u/88037946?v=4",
  "github_url": "https://github.com/uncle-lv",
  "qq": "17153217"
}
```



### 博客

#### 获取博客列表

请求

```http
GET http://localhost:8000/api/blogs HTTP/1.1
```



响应

```json
HTTP/1.1 200 OK
date: Fri, 31 Dec 2021 04:48:47 GMT
server: uvicorn
content-length: 2781
content-type: application/json
connection: close

[
  {
    "id": 1,
    "title": "9. try-with-resources 优于 try-finally",
    "chief_description": "可以看到，当程序离开 try-catch 代码块后， close() 方法被自动调用了。使用 try-with-sources 释放资源显然更简洁",
    "content": "本书中提到的 try-with-resources 相较于 try-catch 的另一个优点是：try-catch 捕获异常时，只会抛出最后一个异常，而 try-with-resources 则会抛出所有异常。但我写了一下Demo之后发现 try-catch 现在也能抛出所有异常了（jdk 1.8以后），所以这个优势实际上已经不存在了。但即使没有这个优势， try-with-resources 显然还是要优于 try-catch",
    "created_time": "2021-12-30T15:35:50",
    "modified_time": "2021-12-30T16:30:54"
  },
  {
    "id": 2,
    "title": "1.用静态工厂方法代替构造器",
    "chief_description": "静态工厂方法有名字（增强了代码的可读性）不必在每次调用时都创建新的对象（提升性能）可以返回原类型的任何子类型对象（增大程序灵活性，减少API数量）返回的对象可以随着每次调用而发生变化（具体类型取决于传入的参数）在编写包含静态工厂方法的类时，返回的对象的所属类可以不存在",
    "content": "第三个优点建议参考java.util.Collections中的源码，我在这里举一个简单的例子。首先写一个Person类，只写一个age属性，年龄必须大于0。再写一个内部类AdultPerson，内部类继承自Person，年龄不能小于18。分别为Person类和AdultPerson类提供一个静态工厂方法，返回值类型都为Person。这样做的好处就是我们不必知道AdultPerson类的存在，不必多写一个外部类，减少了API数量",
    "created_time": "2021-12-30T15:37:53",
    "modified_time": null
  },
  {
    "id": 3,  
    "title": "1.用静态工厂方法代替构造器",
    "chief_description": "静态工厂方法有名字（增强了代码的可读性）不必在每次调用时都创建新的对象（提升性能）可以返回原类型的任何子类型对象（增大程序灵活性，减少API数量）返回的对象可以随着每次调用而发生变化（具体类型取决于传入的参数）在编写包含静态工厂方法的类时，返回的对象的所属类可以不存在",
    "content": "第三个优点建议参考java.util.Collections中的源码，我在这里举一个简单的例子。首先写一个Person类，只写一个age属性，年龄必须大于0。再写一个内部类AdultPerson，内部类继承自Person，年龄不能小于18。分别为Person类和AdultPerson类提供一个静态工厂方法，返回值类型都为Person。这样做的好处就是我们不必知道AdultPerson类的存在，不必多写一个外部类，减少了API数量",
    "created_time": "2021-12-31T04:46:41",
    "modified_time": null
  }
]
```



#### 获取博客

请求

```http
GET http://localhost:8000/api/blogs/1 HTTP/1.1
```



响应

```json
HTTP/1.1 200 OK
date: Fri, 31 Dec 2021 04:51:23 GMT
server: uvicorn
content-length: 735
content-type: application/json
connection: close

{
  "id": 1,
  "title": "9. try-with-resources 优于 try-finally",
  "chief_description": "可以看到，当程序离开 try-catch 代码块后， close() 方法被自动调用了。使用 try-with-sources 释放资源显然更简洁",
  "content": "本书中提到的 try-with-resources 相较于 try-catch 的另一个优点是：try-catch 捕获异常时，只会抛出最后一个异常，而 try-with-resources 则会抛出所有异常。但我写了一下Demo之后发现 try-catch 现在也能抛出所有异常了（jdk 1.8以后），所以这个优势实际上已经不存在了。但即使没有这个优势， try-with-resources 显然还是要优于 try-catch",
  "created_time": "2021-12-30T15:35:50",
  "modified_time": "2021-12-30T16:30:54"
}
```



#### 添加博客

请求

```http
POST http://localhost:8000/api/blogs HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM

{
  "title": "1.用静态工厂方法代替构造器",
  "chief_description": "静态工厂方法有名字（增强了代码的可读性）不必在每次调用时都创建新的对象（提升性能）可以返回原类型的任何子类型对象（增大程序灵活性，减少API数量）返回的对象可以随着每次调用而发生变化（具体类型取决于传入的参数）在编写包含静态工厂方法的类时，返回的对象的所属类可以不存在",
  "content": "第三个优点建议参考java.util.Collections中的源码，我在这里举一个简单的例子。首先写一个Person类，只写一个age属性，年龄必须大于0。再写一个内部类AdultPerson，内部类继承自Person，年龄不能小于18。分别为Person类和AdultPerson类提供一个静态工厂方法，返回值类型都为Person。这样做的好处就是我们不必知道AdultPerson类的存在，不必多写一个外部类，减少了API数量"
}
```



响应

```json
HTTP/1.1 201 Created
date: Fri, 31 Dec 2021 04:46:40 GMT
server: uvicorn
content-length: 1021
content-type: application/json
connection: close

{
  "id": 1,
  "title": "1.用静态工厂方法代替构造器",
  "chief_description": "静态工厂方法有名字（增强了代码的可读性）不必在每次调用时都创建新的对象（提升性能）可以返回原类型的任何子类型对象（增大程序灵活性，减少API数量）返回的对象可以随着每次调用而发生变化（具体类型取决于传入的参数）在编写包含静态工厂方法的类时，返回的对象的所属类可以不存在",
  "content": "第三个优点建议参考java.util.Collections中的源码，我在这里举一个简单的例子。首先写一个Person类，只写一个age属性，年龄必须大于0。再写一个内部类AdultPerson，内部类继承自Person，年龄不能小于18。分别为Person类和AdultPerson类提供一个静态工厂方法，返回值类型都为Person。这样做的好处就是我们不必知道AdultPerson类的存在，不必多写一个外部类，减少了API数量",
  "created_time": "2021-12-31T04:46:41",
  "modified_time": null
}
```



#### 修改博客

请求

```http
PUT http://localhost:8000/api/blogs/1 HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM

{
  "title": "1.用静态工厂方法代替构造器",
  "chief_description": "静态工厂方法有名字（增强了代码的可读性）不必在每次调用时都创建新的对象（提升性能）可以返回原类型的任何子类型对象（增大程序灵活性，减少API数量）返回的对象可以随着每次调用而发生变化（具体类型取决于传入的参数）在编写包含静态工厂方法的类时，返回的对象的所属类可以不存在",
  "content": "第三个优点建议参考java.util.Collections中的源码，我在这里举一个简单的例子。首先写一个Person类，只写一个age属性，年龄必须大于0。再写一个内部类AdultPerson，内部类继承自Person，年龄不能小于18。分别为Person类和AdultPerson类提供一个静态工厂方法，返回值类型都为Person。这样做的好处就是我们不必知道AdultPerson类的存在，不必多写一个外部类，减少了API数量"
}
```



响应

```json
HTTP/1.1 200 OK
date: Fri, 31 Dec 2021 04:55:25 GMT
server: uvicorn
content-length: 1038
content-type: application/json
connection: close

{
  "id": 1,
  "title": "1.用静态工厂方法代替构造器",
  "chief_description": "静态工厂方法有名字（增强了代码的可读性）不必在每次调用时都创建新的对象（提升性能）可以返回原类型的任何子类型对象（增大程序灵活性，减少API数量）返回的对象可以随着每次调用而发生变化（具体类型取决于传入的参数）在编写包含静态工厂方法的类时，返回的对象的所属类可以不存在",
  "content": "第三个优点建议参考java.util.Collections中的源码，我在这里举一个简单的例子。首先写一个Person类，只写一个age属性，年龄必须大于0。再写一个内部类AdultPerson，内部类继承自Person，年龄不能小于18。分别为Person类和AdultPerson类提供一个静态工厂方法，返回值类型都为Person。这样做的好处就是我们不必知道AdultPerson类的存在，不必多写一个外部类，减少了API数量",
  "created_time": "2021-12-30T15:35:50",
  "modified_time": "2021-12-31T04:55:25"
}
```



#### 删除博客

请求

```http
DELETE http://localhost:8000/api/blogs/1 HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVuY2xlLWx2IiwiZXhwIjoxNjQwOTIzOTQ4fQ.bz-rQDY6WNzKTbSiaUrVxy-Q9jpmOjXWih6UfFNMVrM
```



响应

```json
HTTP/1.1 204 No Content
date: Fri, 31 Dec 2021 05:05:19 GMT
server: uvicorn
content-length: 4
content-type: application/json
connection: close

null
```


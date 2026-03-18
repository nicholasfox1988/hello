demo01.js   
运行这段代码 node demo01.js,  ctrl+c 停止服务器
```javascript
const http =require('http');

const server = http.createServer((req,res)=>{
    res.setHeader('content-type','text/html;charset=utf-8');  //中文乱码解决
    res.end('你好');
});

server.listen(9000,()=>{
    console.log('sever is running');
});
```

01.html  
写一个html表单 模拟post提交，因为地址栏都是get提交
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="http://127.0.0.1:9000" method="post">
        <input type="text" name="name">
        <input type="password" name="password">
        <input type="submit" value="submit">
    </form>
</body>
</html>
```

demo03.js
获取请求头的操作req
```javascript
const http =require('http');

const server = http.createServer((req,res)=>{
    res.setHeader('content-type','text/html;charset=utf-8');  //中文乱码解决
    console.log(req.method);
    console.log(req.url);
    console.log(req.httpVersion);
    console.log(req.headers);
    console.log(req.headers.host);
    res.end('你好');
});

server.listen(9000,()=>{
    console.log('sever is running');
});
```
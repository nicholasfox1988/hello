
# 按钮颜色变换
```js
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .pink {
      background-color: pink;
    }
  </style>
</head>

<body>
  <button class="pink">按钮1</button>
  <button>按钮2</button>
  <button>按钮3</button>
  <button>按钮4</button>
  <script>
    let btn = document.querySelectorAll('button');
    for (let i = 0; i < btn.length; i++) {
      btn[i].addEventListener('click', function () {
        document.querySelector('.pink').className = '';
        this.className = 'pink';
      })
    }
  </script>
</body>

</html>
```
---

# 输出语法
```js
<script>
  document.write('abc')
  document.write('<h1>abc</h1>')
  console.log('abc')
  alert('abc')              //弹出普通窗口
  prompt('请输入你的年龄')  //弹出输入对话框
</script>
```

**多变量,常量申明**

> let age = 28,name= 'nick'

> const fs = require('fs'),PI =3.14

**页面打印对话框输入**
```js
<script>
  let name = prompt('请输入名字：')
  document.write('你好' + name)
</script>
```
---
# 数据类型
```js
number      整数，小数，正数，负数
string      '' , "" , ``, str.trim()去头位空格
boolean     true , false:('',0,undefined,null,false,NaN)
undefined   只申明，却不赋值
null        申明了，赋值为空
数组
object      
```
> NaN  报错：不是一个数字

**数组**
```js
  <script>
    let arr = ['abc', 'def', 'hij', 'lmn']
    console.log(arr)
    console.log(arr[1])
    console.log(arr.length)
  </script>
```

# 检测数据类型
```js
let abc
console.log(typeof abc)
```

# 隐式转换
```js
+运算只要有一个是string，结果就会是string
-*/只要有一个是number,结果就会是number
```
---
# 输入表格显示
```js
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h1 {
      text-align: center;
    }

    table {
      border-collapse: collapse;
      height: auto;
      margin: auto;
    }

    table,
    tr,
    th,
    td {
      border: 1px solid #000;
    }

    th,
    td {
      padding: 10px;
      text-align: center;
    }
  </style>
</head>

<body>

  <script>
    let price = +prompt('请输入价格')
    let num = +prompt('请输入数量')
    let address = prompt('请输入地址')
    let total = price * num

    document.write(`
    <h1>订单确认</h1>
    <table>
      <tr>
        <th>商品名称</th>
        <th>商品价格</th>
        <th>商品数量</th>
        <th>总价</th>
        <th>地址</th>
      </tr>
      <tr>
        <td>内衣</td>
        <td>${price}</td>
        <td>${num}</td>
        <td>${total}</td>
        <td>${address}</td>
      </tr>
    </table>
    `)
  </script>
</body>

</html>
```
---
# 运算
**逻辑运算,运算顺序如下**
```js
!
&&
||
```
**三元补零**
```js
let num = prompt('请输入一个数字：')
num = num < 10 ? 0 + num : num
alert(num)
```
---
# 判断
**if else太简单不写了**

**switch要求数据类型和值必须全等**
```js
let num = +prompt('请输入一个数字：')
switch(num){
  case 1:
    pass
    break
  case 2:
    pass
    break
  ...
  default:
    pass
    break
}
```
---
# 遍历数组
```js
  <script>
    let arr1 = ['abc', 'def', 'hij', 'klm']
    for (let i = 0; i < arr1.length; i++) {
      document.write('<br>', arr1[i])
    }
  </script>
  ```
**数组的增删改查**
```js
<script>
  let arr1 = ['abc', 'def', 'hij', 'klm']
  arr1.push(value)      //增  到结尾
  arr1.unshift(value)   //增  到开头

  arr1.pop()            //删  最后一个
  arr1.shift()          //删  第一个
  arr1.splice(index，num)    //删 从index开始的num个数 

  arr1[index] = val     //改

  arr1[index]           //查
</script>
```
---
# 函数，不难讲解了
**立即执行函数**
```js
(function(x,y){
  //代码段
})(x,y);
```
---
# object对象

**删除对象的属性和方法**

delete 对象.属性

**遍历对象**
```js
let obj = {
  uname : 'nick',
  age : 18,
  gender : '男'
}
for (let key in obj){
  console.log(key)
  console.log(obj[key])
}
```

**内置对象**
网页输入:mdn可以查看
搜索Math

**随机数函数返回n到m之间的一个随机数**
```js
  let n = 6
  let random1 = parseInt(Math.random() * n + 1)
  document.write(random1)
```
> innerText 不是别标签，纯文本(不推荐使用)

> innerHTML 可以解析标签

```js
元素.className
元素.classlist.add('类名')      //追加 原来div,变成div 类名
元素.classlist.remove('类名')   //移除
元素.classlist.toggle('类名')   //切换
```

```html
  <input type="text">         //输入文本  元素.value= ''
  <input type="checkbox">     //打勾      元素.checked= true or false

  <button>abc</button>        //btn1.disabled = true 禁用该按钮

```

**自定义属性**
```html
  <div data-id="" data-name="nick">1</div>
  <div>2</div>
  <div>3</div>

  <script>
    let div = document.querySelector('div')
    console.log(div.dataset.id)
    console.log(div.dataset.name)
  </script>
```
---
# 定时器:间歇函数

**开启/关闭定时器**
```js
  let n = setInterval(() => {
    console.log('hello world!')
  }, 3000)

  clearInterval(n)
```
**同意按钮**
```html
  <button disabled>同意(5)</button>

  <script>
    let btn1 = document.querySelector('button')
    let i = 5
    let n = setInterval(() => {
      i--
      btn1.innerHTML = `同意(${i})`
      if (i === 0) {
        clearInterval(n)
        btn1.disabled = false
        btn1.innerHTML = `同意.`
      }
    }, 1000)
  </script>
```
---
# 事件监听
```js
  元素.document.addEventListener('动作',()=>{ })
```
- **动作包含如下：**
  - click
  - mouseenter
  - mouseleave
  - focus
  - blur
  - keydown
  - keyup
  - input

```html
 <div class="div1">
    <h1>名字随机抽取</h1>
    <span>名字：</span>
    <div class="div2">这里显示</div>
    <button class="start">开始</button>
    <button class="end">结束</button>
  </div>
  <script>
    let arr1 = ['abc', 'def', 'hij', 'klm']
    let random = 0
    let num = 0
    let h1 = document.querySelector('h1')
    let div2 = document.querySelector('.div2')
    let start = document.querySelector('.start')
    let end = document.querySelector('.end')
    console.log(arr1)

    start.addEventListener('click', () => {
      num = setInterval(() => {
        random = parseInt(Math.random() * arr1.length)
        div2.innerHTML = arr1[random]
      }, 50)
    })

    end.addEventListener('click', () => {
      clearInterval(num)
      arr1.splice(random, 1)
      console.log(arr1)
      if (arr1.length === 0) {
        arr1 = ['abc', 'def', 'hij', 'klm']
      }
    })
  </script>
```

```html
  <div class="mi">
    <input type="text" placeholder="请输入：">
    <ul>
      <li><a href="#">1</a></li>
      <li><a href="#">2</a></li>
      <li><a href="#">3</a></li>
    </ul>
  </div>

  <script>
    let input = document.querySelector('input')
    let ul = document.querySelector('ul')
    
    input.addEventListener('focus', () => {
      ul.style.display = 'block'
    })
    input.addEventListener('blur', () => {
      ul.style.display = 'none'
    })
  </script>
```

```html
  <input type="text">
  <script>
    let input = document.querySelector('input')
    input.addEventListener('keydown', () => {
      console.log('键盘按下')
    })
    input.addEventListener('keyup', () => {
      console.log('键盘弹起')
    })
  </script>
```

```html
  <input type="text">
  <button>发布</button>
  <br>
  <span class="total">0/20字</span>
  <script>
    let input = document.querySelector('input')
    let span = document.querySelector('span')
    let btn = document.querySelector('button')

    input.addEventListener('input', () => {
      if (input.value.length <= 20) {
        console.log(input.value)
        span.innerHTML = `${input.value.length}/20字`
      }
    })
    btn.addEventListener('click', () => {
      input.value = ''
      span.innerHTML = `${input.value.length}/20字`
    })
  </script>
```

```html
  <input type="text">
  <button>发布</button>
  <p>abcdefg</p>
  <script>
    let input = document.querySelector('input')
    let btn1 = document.querySelector('button')
    let p = document.querySelector('p')

    input.addEventListener('keyup', (e) => {
      console.log(e.key)
      if (e.key === 'Enter') {
        p.innerHTML = input.value
        input.value = ''
      }
    })
    btn1.addEventListener('click', () => {
      p.innerHTML = input.value
      input.value = ''
    })
  </script>
```
---
# this  

- **注意使用箭头函数this会直接指向window**
- **谁调用这个函数 this就指向谁**
- **普通函数中 this指向的是window**

**函数里面调用的函数，就叫回调函数**

```html
  <div class="div1">
    <ul>
      <li><a class="active" href="#">abc</a></li>
      <li><a href="#">def</a></li>
      <li><a href="#">hij</a></li>
    </ul>
  </div>
  <script>
    let li = document.querySelectorAll('.div1 a')
    console.log(li)
    for (let i = 0; i < li.length; i++) {
      li[i].addEventListener('mouseenter', function () {
        document.querySelector('.div1 .active').classList.remove('active')
        li[i].classList.add('active')
      })
    }
  </script>
```

**复选框**
```js
<script>
  let checkbox1 = document.querySelectorAll('.table-wrapper [type="checkbox"]')
  // console.log(checkbox)
  let checkAll = document.querySelector('.select-all-bar [type="checkbox"]')

  checkAll.addEventListener('click', function () {
    for (let i = 0; i < checkbox1.length; i++) {
      checkbox1[i].checked = this.checked
    }
  })

  for (let i = 0; i < checkbox1.length; i++) {
    checkbox1[i].addEventListener('click', function () {
      checkAll.checked = document.querySelectorAll('.table-wrapper [type="checkbox"]:checked').length === checkbox1.length
    })
  }
</script>
```
---
# 事件流程
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .father {
      height: 100px;
      width: 100px;
      background-color: pink;
    }

    .son {
      height: 50px;
      width: 50px;
      background-color: green;
    }
  </style>
</head>

<body>
  <div class="father">
    <div class="son"></div>
  </div>
  <script>
    let fa = document.querySelector('.father')
    let son = document.querySelector('.son')

    document.addEventListener('click', function () {
      alert('爷爷')
    })

    fa.addEventListener('click', function (e) {
      alert('爸爸')
      e.stopPropagation()
    })

    son.addEventListener('click', function (e) {
      alert('儿子')
      e.stopPropagation()
    })
  </script>
</body>
</html>
```

**事件解绑**
```html
  <button>点击</button>
  <script>
    let btn = document.querySelector('button')
    btn.onclick = function () {
      alert('点击动作')
    }
    btn.onclick = null
  </script>
```

```html
  <button>点击</button>
  <script>
    let btn = document.querySelector('button')
    function fn() {
      alert('点击')
    }

    btn.addEventListener('click', fn)
    btn.removeEventListener('click', fn)
  </script>
```
**匿名函数不能解绑**

**捕捉和冒泡,冒泡可以吧监听器安装在父级容器里面**
```html
  <ul>
    <li>a1g</li>
    <li>a2g</li>
    <li>a3g</li>
    <p>abc</p>
  </ul>
  <script>
    let ul = document.querySelector('ul')

    ul.addEventListener('click', function (e) {
      // console.log(e)
      if (e.target.tagName === 'LI') {
        e.target.style.color = 'red'
      }
    })
  </script>
```

**阻止元素默认行为如：点击表单提交，点击超链接**
```html
  <form action="http://www.baidu.com">
    <input type="submit" value="免费注册">
  </form>
  <a href="http://www.baidu.com">百度一下</a>
  <script>
    const form = document.querySelector('form')
    const a = document.querySelector('a')
    form.addEventListener('submit', function (e) {
      e.preventDefault()
    })
    a.addEventListener('click', function (e) {
      e.preventDefault()
    })
  </script>
```

**等待网页全部加载完毕，开始运行**
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script>
    window.addEventListener('load', function () {
      const btn = document.querySelector('button')
      btn.addEventListener('click', function () {
        alert('按钮被点击了')
      })
    })
  </script>
</head>

<body>
  <button>点击</button>
</body>

</html>
```

**等待网页标签全部加载**
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      alert('验证')
      const btn = document.querySelector('button')
      btn.addEventListener('click', function () {
        alert('按钮被点击了')
      })
    })
  </script>
</head>

<body>
  <button>abc点击</button>
</body>

</html>
```

**页面滚动事件**
```js
  window.addEventListener('scroll', function () {
    console.log('滚动了')
  })
```

```html
  <script>
    const ul = document.querySelector('ul')

    window.addEventListener('scroll', function () {
      let n = document.documentElement.scrollTop
      ul.style.opacity = n >= 300 ? 0 : 1
      console.log(n)
    })
  </script>
```

# 时间对象
```html
  <div></div>
  <script>
    const div = document.querySelector('div');
    const date1 = new Date()
    const date2 = new Date('2005-5-1 08:30:45')
    console.log(date1.toLocaleString())
    div.innerHTML = date1.toLocaleString()
    date2.setFullYear(2006)
    console.log(date2)
  </script>
```

**时间戳,用来计算时间的方式**
```js
// 这三重写法得到的都是数字类型的时间戳
+new Date()
Date.now()
时间对象.getTime()
```

```js
+new Date('2026-4-7 18:30:00')
```

**倒计时**
```js
  <p class="date">现在时间是：</p>
  <div>
    <span class="hour">00</span>
    <i>:</i>
    <span class="minute">00</span>
    <i>:</i>
    <span class="second">00</span>
  </div>
  <p class="over"></p>
  <script>
    let date, time1, time2, time3, hours, minutes, seconds;
    let p1 = document.querySelector('.date');
    let p2 = document.querySelector('.over');
    let hour = document.querySelector('.hour');
    let minute = document.querySelector('.minute');
    let second = document.querySelector('.second');
    let str1 = '2026-04-08 07:17:00'
    p2.innerHTML = `下课时间是：${str1.split(' ')[1]}`;


    let n = setInterval(() => {
      console.log('hello')
      date = new Date();
      p1.innerHTML = `现在时间是： ${date.toLocaleDateString()} ${date.toLocaleTimeString()}`;
      time1 = +new Date()
      time2 = +new Date(str1)
      time3 = time2 - time1
      hours = Math.floor(time3 / 1000 / 60 / 60);
      minutes = Math.floor(time3 / 1000 / 60) % 60;
      seconds = Math.floor(time3 / 1000) % 60;
      hour.innerHTML = hours < 10 ? '0' + hours : hours;
      minute.innerHTML = minutes < 10 ? '0' + minutes : minutes;
      second.innerHTML = seconds < 10 ? '0' + seconds : seconds;
      if (time3 <= 0) {
        clearInterval(n);
        hour.innerHTML = '00';
        minute.innerHTML = '00';
        second.innerHTML = '00';
        clearInterval(n);
      }
    }, 1000);
  </script>
```
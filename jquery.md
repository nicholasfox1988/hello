# 开始使用 jQuery
**jquery库文件的获取地址**
https://jquery.com

**引入jquery,最好在head里面**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="js/jquery-4.0.0.min.js"></script>
</head>
<body>
  <div>abc</div>
  <script>
    $(document).ready(function () {
      $('div').hide()
    })
    $(function () {   // Dom加载完后，立即执行
      $('div').hide()
    })
  </script>
</body>
</html>
```

**调用jquery可以写$或者jQuery如下**
> $( ) , jQuery( )

**jquery是顶级对象，和Array，String，Number等相同**

> **DOM对象转jQuery对象:-->&emsp;$(DOM对象)**<br>
> **jQuery对象转DOM对象:-->&emsp;\$('')[0] ; \$('').get(0)**

```html
<body>
  <ul>
    <li>a</li>
    <li>b</li>
    <li>c</li>
    <li>d</li>
    <li>e</li>
  </ul>
  <script>
    $(function () {
      $('ul li:even').css('background', 'pink')
      $('li')[2].style.backgroundColor = 'blue'
    })
  </script>
</body>
```

# 未命名

**选择器原理等同css选择器**

**隐式迭代:会将所有的div标签全部选中进行修改**
```html
<body>
  <div class="div1">abc</div>
  <div class="div2">abc</div>
  <div class="div3">abc</div>
  <script>
    $(function () {
      $('div').css('background', 'pink')
    })
  </script>
</body>
```

**jQuery筛选选择器-->有first,last,eq(index),odd,even**
```html
<body>
  <ul>
    <li>a</li>
    <li>b</li>
    <li>c</li>
    <li>d</li>
    <li>e</li>
  </ul>
  <script>
    $(function () {
      $('ul li:odd').css('background', 'pink')
    })
  </script>
</body>
```

**筛选方法**
```html
$('').parent()        //选中父亲
$('').children('')    //$('??>??')  子代选择
$('').find('')        //在什么中找它的所有后代
$('li').siblings('')  //兄弟选择
$('').nextAll()
$('').preAll()
$('').hasClass('')
$('').eq(2)  //等同于$('??:eq(2)')
```

```html
  <ul>
    <li>a</li>
    <li>b</li>
    <li>c</li>
    <li>d</li>
    <li>e</li>
  </ul>
  <div class="content">
    <div>a</div>
    <div>b</div>
    <div>c</div>
    <div>d</div>
    <div>e</div>
  </div>
  <script>
    $(function () {
      $('ul li').mouseover(function () {
        let index = $(this).index()
        // console.log(index)
        $('.content>div').eq(index).show()
        $('.content>div').eq(index).siblings().hide()
      })
    })
  </script>
```

```html
  <button>快速</button>
  <button>快速</button>
  <button>快速</button>
  <button>快速</button>
  <button>快速</button>
  <script>
    $(function () {
      $('button').click(function () {
        $(this).css('background', 'pink')
        $(this).siblings().css('background', '')
      })
    })
  </script>
```
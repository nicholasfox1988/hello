### 初学vue

> {{ 表达式 }}
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    #app {
      border: solid 3px green;
      border-radius: 8px;
      text-align: center;
      padding: 10px;
    }
  </style>
</head>

<body>
  <div id="app">
    {{ msg }}
    <div v-html="msg"></div>
    <div v-show="flag">show内容</div>
    <div v-if="flag">if内容</div>
    <!--  -->
    <div v-if="gender===1">性别:男</div>
    <div v-else>性别:女</div>
    <!--  -->
    <div v-if="score>=90">A:奖励一台电脑</div>
    <div v-else-if="score>=70">B:奖励周末郊游</div>
    <div v-else-if="score>=60">C:奖励零食多点</div>
    <div v-else>D:惩罚一周不能玩手机</div>
    <!--  -->
    <button @mouseenter="count--">-</button>
    <button v-on:mouseenter="count--">-</button>
    <span>{{ count }}</span>
    <button v-on:click="count++">+</button>
    <button @click="count++">+</button>
    <br><br>
    <!--  -->
    <button @click="fn">显示/隐藏</button>
    <h1 v-show="isShow">黑马</h1>
    <!--  -->
    <p v-for="(item,index) in list">{{index}}:{{item}}</p>
    <ul>
      <li v-for="(item,index) in booklist" :key="item.id">
        <span>{{item.name}}</span>
        <span>{{item.author}}</span>
        <button @click="del(item.id)">删除</button>
      </li>
    </ul>
    <!--  -->
    账户:<input type="text" v-model="username"><br><br>
    密码:<input type="password" v-model="password"><br><br>
    <button @click="login">登入</button>
    <button @click="reset">重置</button>
  </div>

  <script src="js/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        username: '',
        password: '',
        msg: 'hello vue!',
        flag: true,
        gender: 2,
        score: 55,
        count: 100,
        isShow: true,
        list: ['西瓜', '苹果', '香蕉'],
        booklist: [
          { id: 1, name: '红楼梦', author: '曹雪芹' },
          { id: 2, name: '西游记', author: '吴承恩' },
          { id: 3, name: '水浒传', author: '施耐庵' },
          { id: 4, name: '三国演义', author: '罗贯中' }
        ]
      },
      methods: {
        fn() {
          console.log('执行了fn()', app.isShow)
          this.isShow = !this.isShow
        },
        del(id) {
          console.log(id)
          this.booklist = this.booklist.filter(item => item.id !== id)
        },
        login() {
          console.log(this.username + '~~~~' + this.password)
        },
        reset() {
          this.username = '';
          this.password = ''
        }
      }
    })
  </script>
</body>

</html>
```

### vue指令

```
v-text        //不常用
v-html        <div v-html="表达式"></div>
v-show        <div v-show="boolean表达式"></div>  显示或隐藏
v-if          <div v-if="boolean表达式"></div>    创建或删除
v-else        <div v-else>性别:女</div>           v-else必须跟着v-if
v-else-if     同 v-if
v-for         <p v-for="(item,index) in list">{{index}}:{{item}}</p>
              <ul>
                <li v-for="(item,index) in booklist" :key="item.id">
                  <span>{{item.name}}</span>
                  <span>{{item.author}}</span>
                  <button @click="del(item.id)">删除</button>
                </li>
              </ul>

              v-on:属性名="表达式"   v-bind:属性名="表达式"
v-on          <button @click="count++">+</button>  @ 是 v-on:的简写
v-bind        :属性名="表达式"            属性名 如下:src,url,title
v-model       表单专属,输入框value跟data里面的变量双向数据绑定
v-slot        //不常用
v-pre         //不常用
v-cloak       //不常用
v-once        //不常用
```

### 指令修饰符
```
1 按键修饰符
  @keyup.enter        键盘回车监听
2 v-model修饰符
  v-model.trim        去首尾空格
  v-model.number      数据转数字
3 事件修饰符
  @事件.stop          阻止冒泡
  @事件.prevent       阻止默认行为
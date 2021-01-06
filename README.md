
学习tornado框架建立的一个简单的demo

持续更新中，目标是开箱即用

项目结构参考了Python框架Django和PHP框架Hyperf

环境：python3.7

服务器：debian10或其他linux

开发手册：

    1.路由文件在Config/routes.py中
    2.路由对应的执行逻辑在 Handlers/ 下新建、编写并引入routes.py中
    3.用到的模板文件，存放在 Templates/ 下
    4.js、css等文件，存放在 Statics/ 下
    5.其他想到再补充
    
使用：

    1. clone 此仓库到本地
    2. pip3 install -r requirements.txt
    3. 重命名Config/settings_example.py为Config/settings.py,并填写需要的配置
    4. python3 server.py
    5. 注意 windows下需修改server.py中的内容，具体请看server.py中的注释

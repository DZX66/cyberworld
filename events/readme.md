# 事件文件编写说明

## 标识符

普通对话（相当于function.talk(str)）：只需在一行中输入文字即可

无等待（相当于function.talk(str,0)）：在行开头用 **-**

插入python代码（直接执行）：在行开头用 **\*\***

在对话中间插入python代码（相当于"sth"+python.python()+"sth"）：用 **'''+python.python()+'''**

插入命令行（相当于os.system(str)）：在行开头用 **/**

function.select的使用：
    
    **res = function.select(["我有问题。","跟随它。"])
    **if res==0:
        【玛莉特】 别，等会你就知道了。
        【玛莉特】 【图书馆】里的资料应该够你看的。
    **elif res==1
        pass

## 描述

第一行：**id**

第二行：**标题**（游戏内不显示）

第三行：**事件条件**（python表达式）

第四行：**是否可跳过**

第五行：**描述语**（显示在游戏自由行动时选择项中）

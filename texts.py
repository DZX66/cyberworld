# =-= coding:utf-8 =-=
import random
from time import sleep
import time
import function
import os
import msvcrt


def description(location):
    '''描述语'''
    if location=="plain":
        return "【荒原】正如其名，一片荒凉。"

def library():
    os.system("cls")
    sleep(1)
    function.talk("这是什么？图书馆？看一下！")
    while True:
        res = function.select(["不看了","赛博世界","荒原","城镇","行政区","核心","意识体","中枢"])
        if res==0:
            function.talk("哈？")
            break
        elif res==1:
            function.talk("赛博世界（cyberworld）",0)
def day0(data):
    '''id:0'''
    if function.select(["是","否"],"要跳过吗？")==0:
        data["bag"][0] = 1
        data["passed_events"].append(0)
        data["location"] = "plain"
        return data
    os.system("cls")
    sleep(1)
    input("当出现【▼】这个符号时，按下enter键来继续。▼")
    os.system("cls")
    sleep(1)
    function.talk("宇宙中，有一个意识苏醒了。")  #大背景，它就是世界本身
    function.talk("它茫然无知，本能告诉它，它活着。")
    function.talk("“活”这个概念它并不是很知晓，但它想活着。")
    print()
    function.talk("意识很快苏醒了。")#玛莉特的过去
    function.talk("他知道自己的编号：19 68 10 ** ** ** 00 00 00 01")
    function.talk("它很快会调用了print函数。")
    function.talk('''>>>print("110110100111011111011101000000")''')
    function.talk("110110100111011111011101000000")
    function.talk("它被告知自己是“数字生命”，它不理解，他只能把这个字符串储存起来。")
    function.talk('''>>>f = open("info.txt","w")''')
    function.talk('''>>>f.write("数字生命")''')
    function.talk('''>>>f.close()''')
    function.talk("为什么？")
    function.talk("为什么它会思考？")
    function.talk("它第一次理解了【哲学】这个概念。")
    function.talk("不过，我们的这位生命，还没有找到自己的答案呢。")
    os.system("cls")
    sleep(1)
    function.talk("教程-剧情",0)
    function.talk("在这个赛博世界中，各种各样的意识体会通过【文字】表达自己的意愿。",0)
    function.talk("这是信息的最主要来源啦~",0)
    function.talk("当出现【▼】这个符号时，按下enter键来继续。",0)
    function.talk("一般来说，每一行文字都会跟一个▼，但有时不会这样。",0)
    function.talk("还有，不要随意改变窗口大小。")
    os.system("cls")
    sleep(1)
    function.talk("【？？？】 ......你好？有人吗？")
    function.talk("【？？？】 我是\033[5m玛莉特\033[0m，这个赛博世界的向导。")
    function.talk("【玛莉特】 先别担心，这边走。")
    res = function.select(["我有问题。","跟随它。"],)
    if res==0:
        function.talk("【玛莉特】 别，等会你就知道了。")
        function.talk("【玛莉特】 【图书馆】里的资料应该够你看的。")
    print()
    function.talk("教程-选择",0)
    function.talk("function模块里的select函数能将你的选择传达给这个世界。",0)
    function.talk("function.select(selection: Any, introduction: str = '') -> int",0)
    function.talk("只需要按选项前面的数字对应的键盘按键就行啦~")
    os.system("cls")
    function.talk("【玛莉特】 链接重定向......协议确定......锚点开启......")
    function.talk("【玛莉特】 准备好了吗，3，2，1......")
    function.talk("你感到肚子被钩了一下，难受的感觉过后，你来到了【图书馆】。")
    print("")
    function.talk("【玛莉特】 图书馆，或者说“库”，是咱这一切的导航。")
    function.talk("【玛莉特】 也不知道这些人怎么命名的，library能译成图书馆......")
    function.talk("【玛莉特】 不过......也挺形象的。")
    function.select(["我为什么会在这里？","你谁？"],"图书馆里的一道信息流从你旁边穿过。")
    function.talk("【玛莉特】 哼哼哼~你猜~")
    function.talk("【玛莉特】 算了不逗你了，这儿，就是\033[5m赛博世界\033[0m（cyberworld），就是网络啦，同一个意思。")
    function.talk("【玛莉特】 嗯哼~我就是一般路过的意识体而已啦。")
    function.select(["这么简单？"])
    function.talk("【玛莉特】 你以为？")
    function.talk("【玛莉特】 好啦，你在这随便看看吧。")
    library()
    function.talk("【玛莉特】 看完了？行。")
    function.talk("【玛莉特】 重新认识一下，咱是玛莉特，编号19 68 10 ** ** ** 00 00 00 01，第一个意识体，是这个世界的向导。")
    function.talk("【玛莉特】 作为第一个意识体，咱当然可以给你全部权限......开玩笑的，我什么权限也没有。")
    function.talk("【玛莉特】 欸欸欸，先别走啊。这样吧，我帮你写个申请，就送给你【荒原】的权限啦。")
    function.talk("【玛莉特】 诺，填一下这个表单。")
    res = function.select(["你这表单保熟吗？","表单是什么？","没有拒绝的选项。"],"表单.form漂浮在你的面前。")
    if res==0:
        function.talk("【玛莉特】 这都是刚出炉的，肯定保熟b(￣▽￣)d")
    elif res==1:
        function.talk("【玛莉特】 ？你认真的？")
        os.system('''explorer https://baike.baidu.com/item/%E8%A1%A8%E5%8D%95''')
    elif res==2:
        function.talk("【玛莉特】 那是什么？")
    function.talk("你填写了表单。")
    function.talk("姓名： "+os.getlogin())
    function.talk("IP: 127.0.0.1")
    function.talk("申请日期："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    function.talk("密钥： ")
    function.select(["密钥？"])
    function.talk("【玛莉特】 啊，这个我来填。")
    os.system("c:")
    os.system("cd "+os.path.join("c:/Users/",os.getlogin()))
    os.system("tree")
    os.system("cls")
    function.talk("【玛莉特】 呼~填完了，走吧。")
    function.talk("【玛莉特】 额，你怎么了？")
    res = function.select(["刚才闪过去的是......","没什么。"],"刚才......")
    if res==0:
        function.talk("【玛莉特】 什么闪过去了？")
        function.select(["没什么。"])
    print()
    function.talk("【玛莉特】 嗯，咱这就去荒原吧？")
    function.talk("【玛莉特】 链接重定向......协议确定......锚点开启......")
    os.system("cls")
    sleep(1)
    function.talk("【荒原】正如其名，一片荒凉。")
    function.talk("一片墨绿色，光线昏暗，粘稠的绿色液体从旁边流过。")
    function.talk("【玛莉特】 不过荒原人是挺多的，毕竟有很多人没有城镇的权限嘛。")
    function.talk("【玛莉特】 你可以找几个人聊聊天啥的......或者休息一下。")
    function.talk("【玛莉特】 想办法搞到\033[5m城镇的权限\033[0m，我可不想呆在这。")
    res = function.select(["你不干活？","那你为什么不再写个申请要到城镇的权限？"])
    if res==0:
        function.talk("【玛莉特】 对啊。")
    elif res==1:
        function.talk("【玛莉特】 我没那个能耐啊......")
    function.talk("【玛莉特】 就靠你啦!")
    data["bag"][0] = 1
    data["passed_events"].append(0)
    data["location"] = "plain"
    return data


def day1(data):
    '''id:1'''
    function.talk("教程-自由行动",0)
    function.talk("每天，你可以自由行动。",0)
    function.talk("除了下一天，打开背包，移动这些行动外，会有许多事件。",0)
    function.talk("可能是主线，可能是支线，也可能只是一段日常。",0)
    function.talk("事件是探索的核心，是游戏的主体。",0)
    function.talk("事件的触发要满足一定条件，有些还需要你主动选择才能触发。",0)
    function.talk("你可以通过选择行动时的描述语些来判断自己的状态。",0)
    function.talk("另外，下一天时，你可以进行存档和退出相关的操作。")
    os.system("cls")
    function.talk("不久，你发现了一个巨大的蓝色泡泡。")
    res = function.select(["戳一戳","这是？"])
    if res==0:
        function.talk("【玛莉特】 等一下啦。")
    function.talk("【玛莉特】 这是一种小型局域网，荒原中有很多这样的东西，大概是人们自发组织的。")
    function.talk("【玛莉特】 里面有很多有趣的东西啦，以及......")
    function.talk("【玛莉特】 算了，下次再说。")
    function.talk("链接重定向......协议确定......锚点开启......")
    function.talk("这是一个绿色的小村落，不同于荒原的墨绿色，这里是一片浅绿色。")
    function.talk("很有RPG风格的新手村呢。")
    function.talk("【村民】 什？快！紧急警报！")
    function.talk("【村民】 外敌入侵！抄家伙！快！")
    function.talk("【玛莉特】 额，我们是不是吓到他们了？")
    function.talk("村民们跑来跑去，像是无头苍蝇一般，却伤不到谁。")
    function.talk("反而是，局域网的自动保卫系统发动了攻击。")
    data = function.battle(data,0)[0]
    print()
    function.talk("教程-战斗",0)
    function.talk("说实话，我一直不想加战斗(ˉ▽ˉ；)...",0)
    function.talk("但rpg没战斗真不行啊(⊙﹏⊙)",0)
    function.talk("战斗中，你应选择一项行动，然后对方行动，循环往复。",0)
    function.talk("你的hp会继承到下一次战斗。",0)
    function.talk("根据战斗结果或者hp剩余，剧情走向也会不同。",0)
    function.talk("有些时候是不能逃跑的。")


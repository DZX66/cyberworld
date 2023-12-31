# =-= coding:utf-8 =-=
import random

def description(location:str):
    '''描述语'''
    if location=="plain":
        return "【荒原】正如其名，一片荒凉。"
    elif location=="hotel":
        return "旅馆内人声鼎沸。"
    elif location=="pixel_tower":
        tips=[
        "江源速报：拟态系统PhigrOS，将于8月31号正式上线",
        "江源速报：PhigrOS内测开放新节点，完全复原冰封后地表实录",
        "江源速报：PHI集团负责人失踪三日，警方仍在调查中",
        "江源速报：PHI集团负责人回归，自杀传言不攻而破",
        "江源速报：名人自杀现象异常扩散，知名作家留下诡异遗书",
        "江源速报：知名歌手何琼语于昨夜凌晨意外死亡，凶手仍在追查中",
        "江源速报：警方发表惊人结果，何琼语原系自杀身亡",
        "江源速报：天后横死案新进展，凶手恐为桥民流浪汉",
        "江源速报：三大基地全面开放通行，冰封纪元即将结束？",
        "江源速报：专家呼吁复兴AI产业，以应对劳动力紧缺问题",
        "江源速报：政府出台就业新策，望促进失业人员再就业",
        "江源速报：多地出现无故昏厥人员，卫生部呼吁民众注意饮食健康",
        "江源速报：全球年均温再度上升，重返地表签名破千万",
        "江源速报：群体性臆症爆发，多人自称蜂巢C区存在巨塔",
        "江源速报：巨塔效应急剧化，神秘群体林泊浮出水面",
        "江源速报：上半年人口增长率再创新低，新型受精技术受挫",
        "我被困在林泊百科里了！救命！",
        "像素塔真的存在吗。",
        '猜猜你要重新加载多少次才能再看到这条tip￣︶￣',
        '这是一条属于3.0版本的Tips！',
        'print("Hello tips3.0")',
        '来猜猜看这边有几个有用的信息呢~',
        '你知道吗？其实tips全都是废话（确信',
        '啊！要给你看什么Tip好呢…(翻',
        '突然来了一条消息！          哦这里是tips啊，那没事了',
        '有没有数过这是你第几次看到这条tips呢？',
        'φ？拿来吧你！',
        '有一个人前来打歌',
        '阿鸠你又在反复看Tips了哦',
        '手持两把锟斤拷，口中疾呼烫烫烫',
        '热知识：这是一条…烫烫烫烫烫！的热知识。',
        '冷知识：这是一条…啊嚏！…冷知识！',
        '时间滴滴答答在走，这首歌你φ了没有？',
        '上次看到这条Tip还是在上次',
        '你AP了，就一定AP了吧！',
        '扉格晚五点，周五准时更新！',
        '高三党，现在，立刻，去给我学习！！！',
        '你先别急！！这不有云存档嘛',
        '自从使用了同步存档，手也不酸了，头也不痛了，推分也来劲了！',
        '当你在看这行字的时候 我就知道 你肯定在看这行字',
        '!!',
        '我超，劲爆',
        'AT的意思并不是Anti-Thumb（',
        'EZ是指摁着而非Easy，HD是高清而非Hard，IN是里面而非Insane，AT是位于而非Another，等会我是不是说反了？',
        '分数我所欲也，acc亦我所欲也，若二者不可得兼，多练也。',
        '声音传播需要介质',
        '你打一首歌的时间，鸠已经发现 NaN 个问题了',
        'sudo 板子自己打歌',
        'rks是RankingScore，不是热开水！（认真脸）',
        '来唱歌！咕！咕！咕咕咕！',
        '我们的口号是？咕咕咕！']

        return tips[random.randint(0,len(tips)-1)]
def location(name):
    '''根据代码内标识返回译名'''
    names = {"":"？？？","plain":"荒原","hotel":"旅馆","pixel_tower":"像素塔"}
    return names[name]
def keys(name:bytes):
    '''根据bytes返回键位名称，可输入bytes或str'''
    if type(name)==bytes:
        name=str(name,encoding="utf-8")
    elif type(name)==str:
        pass
    else:
        raise TypeError
    if name=="\x1b":
        return "ESC"
    elif name=='\r':
        return "Enter"
    elif name=='`':
        return "~"
    elif name=='\x08':
        return "Backspace"
    elif name=='\xe0':
        return ""
    elif name==" ":
        return "Space"
    else:
        return name.upper()
def effect(name:str):
    if name=="blood_losing":
        return "流血"
    elif name=="healing":
        return "自愈"
    elif name=="weak":
        return "虚弱"
    elif name=="powered":
        return "力量"
    elif name=="slowness":
        return "缓慢"
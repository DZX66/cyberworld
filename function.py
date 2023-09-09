# =-= coding:utf-8 =-=
import sys
import os
import msvcrt
import json
import time
import random
import pygame
import math
import texts
from copy import deepcopy

def error(str:str):
    os.system("color 4")
    input(str)
    sys.exit()
def select(selection:list,introduction="",special_keys={}):
    '''选择，返回selection的选择的元素索引或special_keys中的键'''
    if len(selection)>10:
        error("[error] 选择项超过十")
    print("="*20)
    if introduction:
        print(introduction)
    q = 0
    w = []
    for i in selection:
        print(str(q)+". "+i)
        w.append(bytes(str(q),encoding="utf-8"))
        q += 1
    print("="*20)
    for i in special_keys:
        w.append(bytes(i,encoding="utf-8"))
        print(texts.keys(i)+"-"+special_keys[i],end=" ")
    print()
    get = b''
    while not (get in w):
        get = msvcrt.getch()
    try:
        return int(get)
    except ValueError:
        return str(get,encoding="utf-8")
def items(id:int):
    item_info = {
        0:["【荒原】的权限","荒原访客的证明，是玛莉特送给你的礼物。"],
        1:["齿轮","铜质，略有锈斑，好像用了挺久的。"],
        2:["普通攻击","10-15伤害 0消耗\n常见的delete函数，很容易被防御。"],
        3:["火球术","5-10伤害，流血+3 2消耗\n-为啥火球能造成流血呢？-废话，燃烧不就是流血吗。"],
        4:["治疗术","10-15回复，血量100及以上时只有80%的效果，200及以上只有50%的效果（向下取整） 1消耗\n不会有人用这个堆到1000点hp吧？"]
    } 
    return item_info[id]
def get_item(data:dict,id:int,number:int):
    '''添加物品进背包，返回data'''
    if id in data["bag"]:
        data["bag"][str(id)] += number
    else:
        data["bag"][str(id)] = number
    return data
def bag(data:dict):
    if data["bag"]==0:
        print("啥也没有")
        input("▼")
        return -1
    get = 'z'
    focus = 0
    flush = True
    while not(get==b"q"):
        if flush:
            os.system("cls")
            n = 0
            print("\033[1;30m")
            for i in data["bag"]:
                if n == focus:
                    print("\033[1;37m>"+items(int(i))[0]+" * "+str(data['bag'][i])+" \033[0;37m#"+str(i)+" "+items(int(i))[1]+"\033[1;30m")
                else:
                    print(items(int(i))[0]+" * "+str(data['bag'][i]))
                n+=1
            print("\033[0mQ-退出 W-上一个 S-下一个 Enter-使用")
        get = msvcrt.getch()
        flush = True
        if get==b"s":
            if focus<len(data["bag"])-1:
                focus += 1
            else:
                flush = False
        elif get==b"w":
            if focus>0:
                focus -= 1
            else:
                flush = False
        elif get==b"\r":
            talk("used "+str(list(data["bag"])[focus]))
    return -1
def talk(text:str,wait=True):
    if wait:
        time.sleep(0.2)
        print(text+"\033[s▼",end="",flush=True)
        get = b'q'
        while not(get==b"\r"):
            get = msvcrt.getch()
        sound = pygame.mixer.Sound("audio/continue.mp3")
        sound.play()
        print("\033[u\033[K")
    else:
        print(text)
def enemies(id:int):
    '''返回元组：(int id,str name,int hp,list skills)
    list skills:name,type,begin,end
    availabe type:attack,heal'''
    if id==0:
        return (0,"自动保卫系统",40,[["子弹","attack",5,10,100],["缓速弹","otherside_effect","slowness",2,10]],[1,0,0])
    else:
        error('[error] 不存在的id:'+str(id))
def decrease_hp(hp_decreased:int,hp:int,hp_max:int):
    '''in function battle:
    return:int edited_hp'''
    print("\033[s"+str(hp)+"/"+str(hp_max)+"    "+"\033[0;32m+"*math.ceil(hp/hp_max*10)+"\033[0;31m-"*min(10-math.ceil(hp/hp_max*10),10)+"\033[0m    "+(str(-hp_decreased) if hp_decreased>=0 else "+"+str(-hp_decreased)),end="",flush=True)
    time.sleep(1)
    hp-=hp_decreased
    print("\033[u\033[K"+str(hp)+"/"+str(hp_max)+"    "+"\033[0;32m+"*math.ceil(hp/hp_max*10)+"\033[0;31m-"*min(10-math.ceil(hp/hp_max*10),10)+"\033[0m",flush=True)
    return hp
def cost(skill):
    """根据技能名返回消耗mp（int）"""
    if skill=="普通攻击":
        return 0
    elif skill=="火球术":
        return 2
    elif skill=="治疗术":
        return 1
    else:
        error("[error] 不存在的技能:"+skill)
def battle(data:dict,enemy:int,is_escaped:bool,bgm="audio/Rude_Buster.flac"):
    '''返回值：[data,result]
    result:0：胜利 -1：逃跑 -2：失败'''
    monster_hp = enemies(enemy)[2]
    player_hp = data["hp"]
    player_mp = 3
    monster_hp_max = monster_hp
    player_hp_max = data["max_hp"]
    monster_effects = {"blood_losing":0,"healing":0,"weak":0,"powered":0,"slowness":0}
    player_effects = {"blood_losing":0,"healing":0,"weak":0,"powered":0,"slowness":0}
    monster_choice_now=0
    turn = 1
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    while True:
        print("\n~~~第 "+str(turn)+" 轮 战斗开始~~~\n")
        print(enemies(enemy)[1]+" 生命值 ：", monster_hp,"/",monster_hp_max)
        print("\033[0;32m+"*math.ceil(monster_hp/monster_hp_max*10)+"\033[0;31m-"*min(10-math.ceil(monster_hp/monster_hp_max*10),10)+"\033[0m")
        if monster_effects["blood_losing"]>0:
            print("流血",monster_effects["blood_losing"])
        if monster_effects["healing"]>0:
            print("自愈",monster_effects["healing"])
        if monster_effects["powered"]>0:
            print("力量",monster_effects["powered"])
        if monster_effects["weak"]>0:
            print("虚弱",monster_effects["weak"])
        if monster_effects["slowness"]>0:
            print("缓慢",monster_effects["slowness"])
        print("你的生命值 ：", player_hp,"/",player_hp_max)
        print("\033[0;32m+"*math.ceil(player_hp/player_hp_max*10)+"\033[0;31m-"*min(10-math.ceil(player_hp/player_hp_max*10),10)+"\033[0m")
        print("你的精神力 ：", player_mp,"/",5)
        print("\033[0;34m+"*player_mp+"\033[0;31m-"*(5-player_mp)+"\033[0m")
        if player_effects["blood_losing"]>0:
            print("流血",player_effects["blood_losing"])
        if player_effects["healing"]>0:
            print("自愈",player_effects["healing"])
        if player_effects["powered"]>0:
            print("力量",player_effects["powered"])
        if player_effects["weak"]>0:
            print("虚弱",player_effects["weak"])
        if player_effects["slowness"]>0:
            print("缓慢",player_effects["slowness"])
        
        if player_effects["slowness"] > 0 :
            #缓慢效果
            talk("缓慢效果：跳过回合")
            player_effects["slowness"] -= 1
        else:
            action = {}#{1:'xxx',2:'xxx',3:'xxx',4:'xxx'}
            if player_mp>=cost(data["skills"]['1']):
                action[1] = data["skills"]['1']
            if player_mp>=cost(data["skills"]['2']):
                action[2] = data["skills"]['2']
            if player_mp>=cost(data["skills"]['3']):
                action[3] = data["skills"]['3']
            if is_escaped:
                action[4] = "逃跑"

            selection = []#[[1,'xxx'],[2,'xxx'],...]
            for i in action:
                selection.append([i, action[i]])

            out = []
            for i in selection:
                out.append(i[1])

            res = select(out, "请选择你的行动：")
            choice = selection[res][1]

            if choice == '普通攻击':
                player_mp-=0
                damage = random.randint(10, 15)
                print("普通攻击对敌方造成了", damage, "点伤害！")
                monster_hp=decrease_hp(damage,monster_hp,monster_hp_max)
            elif choice == '火球术':
                player_mp-=2
                damage = random.randint(5, 10)
                print("你使用 火球术 对敌方造成了", damage, "点伤害！")
                monster_hp=decrease_hp(damage,monster_hp,monster_hp_max)
                monster_effects["blood_losing"] += 3
                print(data["skills"]['2'],"的效果：敌方流血+3",flush=True)
            elif choice == '治疗术':
                player_mp-=1
                heal = random.randint(10, 15)
                if player_hp < 100:
                    heal = heal
                elif player_hp < 200:
                    heal = math.floor(0.8*heal)
                else:
                    heal = math.floor(0.5*heal)
                print("你使用 治疗术 恢复了", heal, "点生命值！")
                player_hp=decrease_hp(-heal,player_hp,player_hp_max)
            elif choice == '逃跑':
                talk("你选择逃跑！")
                if player_hp>player_hp_max:
                    data["hp"]=player_hp_max
                else:
                    data["hp"]=player_hp
                return [data,-1]
            
        if monster_effects["blood_losing"]>0:
            print("敌方受到流血伤害",3*monster_effects["blood_losing"],"点！")
            monster_hp=decrease_hp(3*monster_effects["blood_losing"],monster_hp,monster_hp_max)
            monster_effects["blood_losing"] -= 1

        if monster_hp <= 0:
            talk("你胜利了！")
            if player_hp>player_hp_max:
                data["hp"]=player_hp_max
            else:
                data["hp"]=player_hp
            return [data,0]
        time.sleep(1)
        if monster_effects["slowness"]>0:
            print("缓慢效果：敌方跳过回合")
            time.sleep(1)
            monster_effects["slowness"]-=1
        else:
            monster_choice = enemies(enemy)[4][monster_choice_now]
            if monster_choice_now==len(enemies(enemy)[4])-1:
                monster_choice_now = 0
            else:
                monster_choice_now+=1
            monster_choice = enemies(enemy)[3][monster_choice]
            if monster_choice[1] == "attack":
                damage = random.randint(monster_choice[2], monster_choice[3])
                print("敌方用",monster_choice[0],"对你造成了", damage, "点伤害！")
                player_hp=decrease_hp(damage,player_hp,player_hp_max)
            elif monster_choice[1] == "self_effect":
                monster_effects[monster_choice[2]]+=monster_choice[3]
                print("敌方用",monster_choice[0],"对自己增加了", texts.effect(monster_choice[2]),monster_choice[3],"层！")
            elif monster_choice[1] == "otherside_effect":
                player_effects[monster_choice[2]]+=monster_choice[3]
                print("敌方用",monster_choice[0],"对你增加了", texts.effect(monster_choice[2]),monster_choice[3],"层！")
            
        if player_effects["blood_losing"]>0:
            print("你受到流血伤害",3*player_effects["blood_losing"],"点！")
            player_hp=decrease_hp(damage,player_hp,player_hp_max)
            player_effects["blood_losing"] -= 1

        #溢出血量稀释
        if player_hp>player_hp_max:
            print("你的血量稀释",math.floor((player_hp-player_hp_max)/4),"点！")
            player_hp=decrease_hp(math.floor((player_hp-player_hp_max)/4),player_hp,player_hp_max)

        if player_hp <= 0:
            talk("你输了......")
            data["hp"]=player_hp
            return [data,-2]
        talk("")
        turn += 1
        if player_mp <5 and player_effects["slowness"]<=0:
            player_mp+=1

def library():
    os.system("cls")
    time.sleep(1)
    talk("这是什么？图书馆？看一下！")
    os.system("start library/index.html")
    talk("")
def event(data:dict,id:int):
    ''''''
    f=open("events/index.json","r",encoding="utf-8")
    path = json.load(f)[str(id)][1]
    f.close()
    f=open(path,"r",encoding="utf-8")
    w=f.readlines()
    f.close()
    res = 0
    if eval(w[3][:-1]):
        res = select(["否","是"],"要跳过吗？")
    w = w[7:]
    code = ""
    if res:
        #跳过
        p = 0
        for i in w:
            place = 0
            while i.startswith("    "):
                i = i[4:]
                place += 1
            if i.startswith("/"):
                if i[1:].startswith("cls"):
                    i=""
                else:
                    i = "os.system('''"+i[1:-1]+"''')\n"
            elif i.startswith("**"):
                i = i[2:]
                if i.startswith("time.sleep"):
                    i=""
                if i.startswith("library"):
                    i = 'print("打开了图书馆。")\n'
            elif i.startswith("-"):
                i = "talk('''"+i[1:-1]+"''',0)\n"
            elif i.startswith("    "):
                i = "talk('''"+i.lstrip()[:-1]+"''',0)\n"
            elif i=="\n":
                i = "print()\n"
            else:
                i = "talk('''"+i[:-1]+"''',0)\n"
            while place >0:
                i = "    "+i
                place -=1
            w[p]=i
            p+=1
        for i in w:
            code +=i
    else:
        #正常
        p = 0
        for i in w:
            place = 0
            while i.startswith("    "):
                i = i[4:]
                place += 1
            if i.startswith("/"):
                i = "os.system('''"+i[1:-1]+"''')\n"
            elif i.startswith("**"):
                i = i[2:]
            elif i.startswith("-"):
                i = "talk('''"+i[1:-1]+"''',0)\n"
            elif i.startswith("    "):
                i = "talk('''"+i.lstrip()[:-1]+"''')\n"
            elif i=="\n":
                i = "print()\n"
            else:
                i = "talk('''"+i[:-1]+"''')\n"
            while place >0:
                i = "    "+i
                place -=1
            w[p]=i
            p+=1
        for i in w:
            code +=i
    exec(code)
    data["passed_events"].append(int(id))
    return data

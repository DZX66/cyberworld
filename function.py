# =-= coding:utf-8 =-=
import sys
import os
import msvcrt
import json
import time
import random

def error(str:str):
    os.system("color 4")
    input(str)
    sys.exit()
def select(selection:list,introduction=""):
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
    get = b'q'
    while not (get in w):
        get = msvcrt.getch()
    return int(get)
def items(id:int):
    item_info = {
        0:["【荒原】的权限","荒原访客的证明，是玛莉特送给你的礼物。"],
        1:["齿轮","铜质，略有锈斑，好像用了挺久的。"]
    } 
    return item_info[id]
def bag(data:dict):
    if data["bag"]==0:
        print("啥也没有")
        input("▼")
        return -1
    get = 'z'
    focus = 0
    while not(get==b"q"):
        os.system("cls")
        n = 0
        for i in data["bag"]:
            if n == focus:
                print(">"+items(i)[0]+" * "+str(data['bag'][i])+" \033[0;37m#"+str(i)+" "+items(i)[1])
            else:
                print(items(i)[0]+" * "+str(data['bag'][i]))
            n+=1
        print("Q-退出 W-上一个 S-下一个 Enter-使用")
        get = msvcrt.getch()
        if get==b"s":
            if focus<len(data["bag"])-1:
                focus += 1
        elif get==b"w":
            if focus>0:
                focus -= 1
        elif get==b"\r":
            return focus
    return -1
def talk(text:str,wait=True):
    if wait:
        time.sleep(0.2)
        print(text+"\033[s▼",end="",flush=True)
        get = b'q'
        while not(get==b"\r"):
            get = msvcrt.getch()
        print("\033[u\033[K")
    else:
        print(text)
def enemies(id:int):
    '''返回元组：(int id,str name,int hp,list skills,bool is_escaped)
    list skills:name,type,begin,end
    availabe type:attack,heal'''
    if id==0:
        return (0,"自动保卫系统",40,[["攻击","attack",5,10]],False)

def battle(data:dict,enemy:int):
    '''返回值：[data,result]
    result:0：胜利 -1：逃跑 -2：失败'''
    monster_hp = enemies(enemy)[2]
    player_hp = data["hp"]
    monster_effects = {"blood_losing":0,"healing":0,"weak":0,"powered":0}
    player_effects = {"blood_losing":0,"healing":0,"weak":0,"powered":0}
    while True:
        print("\n~~~战斗开始~~~\n")
        print(enemies(enemy)[1]+" 生命值 =", monster_hp)
        if monster_effects["blood_losing"]>0:
            print("流血",monster_effects["blood_losing"])
        if monster_effects["healing"]>0:
            print("自愈",monster_effects["healing"])
        if monster_effects["powered"]>0:
            print("力量",monster_effects["powered"])
        if monster_effects["weak"]>0:
            print("虚弱",monster_effects["weak"])
        print("你的生命值 =", player_hp)
        if player_effects["blood_losing"]>0:
            print("流血",player_effects["blood_losing"])
        if player_effects["healing"]>0:
            print("自愈",player_effects["healing"])
        if player_effects["powered"]>0:
            print("力量",player_effects["powered"])
        if player_effects["weak"]>0:
            print("虚弱",player_effects["weak"])

        action = {}
        if True:
            action[1] = data["skills"]['1']
        if True:
            action[2] = data["skills"]['2']
        if True:
            action[3] = data["skills"]['3']
        if enemies(enemy)[4]:
            action[4] = "逃跑"

        selection = []
        for i in action:
            selection.append([i, action[i]])

        out = []
        for i in selection:
            out.append(i[1])

        res = select(out, "请选择你的行动：")
        choice = selection[res][0]

        if choice == 1:
            damage = random.randint(10, 15)
            monster_hp -= damage
            print("你使用", data["skills"]['1'], "对敌方造成了", damage, "点伤害！")
        elif choice == 2:
            damage = random.randint(5, 10)
            monster_hp -= damage
            print("你使用", data["skills"]['2'], "对敌方造成了", damage, "点伤害！")
            monster_effects["blood_losing"] += 3
            print(data["skills"]['2'],"的效果：敌方流血+3")
        elif choice == 3:
            heal = random.randint(10, 15)
            if player_hp < 100:
                heal = heal
            elif player_hp < 200:
                heal = round(0.8*heal)
            else:
                heal = round(0.5*heal)
            print("你使用", data["skills"]['3'], "恢复了", heal, "点生命值！")
        elif choice == 4:
            talk("你选择逃跑！")
            data["hp"]=player_hp
            return [data,-1]
        
        if monster_effects["blood_losing"]>0:
            monster_hp -= 3*monster_effects["blood_losing"]
            print("敌方受到流血伤害",3*monster_effects["blood_losing"],"点！")
            monster_effects["blood_losing"] -= 1

        if monster_hp <= 0:
            talk("你胜利了！")
            data["hp"]=player_hp
            return [data,0]
        
        monster_choice = random.randint(1, len(enemies(enemy)[3]))
        monster_choice = enemies(enemy)[3][monster_choice-1]
        if monster_choice[1] == "attack":
            damage = random.randint(monster_choice[2], monster_choice[3])
            player_hp -= damage
            print("敌方用",monster_choice[0],"对你造成了", damage, "点伤害！")
        
        if player_effects["blood_losing"]>0:
            player_hp -= 3*player_effects["blood_losing"]
            print("你受到流血伤害",3*player_effects["blood_losing"],"点！")
            player_effects["blood_losing"] -= 1

        if player_hp <= 0:
            talk("你输了......")
            data["hp"]=player_hp
            return [data,-2]
        talk("")
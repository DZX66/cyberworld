# =-= coding:utf-8 =-=
from __future__ import print_function
from copy import deepcopy
import time
import function
import os
import json
import texts
import pygame
import ctypes
import sys
import traceback


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def create_saving():
    global data
    data = {
    "days": 0,
    "golds": 1000,
    "san": 80,
    "bag": {'2':1,'3':1,'4':1},
    "passed_events": [],
    "location": "",
    "hp":100,
    "max_hp":100,
    "time":360,
    "skills": {'1': "普通攻击",'2': "火球术",'3': "治疗术"},
    "save_time":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
}
    datar = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    f = open("save.save","w",encoding="utf-8")
    f.write(datar)
    f.close()
    
def load_saving():
    try:
        f = open("save.save", "r", encoding="utf-8")
        data = json.load(f)
        f.close()
        return data
    except FileNotFoundError:
        print("存档文件不存在！")
        return None
    
def save_saving(data):
    data["save_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    datar = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    try:
        with open("save.save", "w", encoding="utf-8") as f:
            f.write(datar)
        function.talk("存档成功！")
    except Exception as e:
        print("存档失败：", e)


def game():
    global data,DEBUG
    os.system("cls")
    sound = pygame.mixer.Sound("audio/start.mp3")
    sound.play()
    pygame.mixer.music.fadeout(500)
    time.sleep(0.5)
    while True:
        os.system("cls")
        #事件
        f=open("events/index.json","r",encoding="utf-8")
        events = json.load(f)
        f.close()
        for i in events:
            if eval(events[i][3]) and events[i][7]=="mandatory":
                function.event(data,events[i][0])
        
        while True:
            #bgm
            if not pygame.mixer.music.get_busy():
                if data["location"]=="plain":
                    pygame.mixer.music.load("audio/key.flac")
                elif data["location"]=="hotel":
                    pygame.mixer.music.load("audio/Embers.flac")
                elif data["location"]=="pixel_tower":
                    pygame.mixer.music.load("audio/phigros_title.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
            #信息
            print("\n~~~第"+str(data["days"])+"天~~~\n")
            print("hp：",data["hp"],"/",data["max_hp"])
            print("字符：",data["golds"])
            print("时间: ",data["time"]//60,":",str(data["time"]%60) if data["time"]%60>=10 else "0"+str(data["time"]%60),"夜深了......" if data["time"]>=1380 or data["time"]<=240 else "")
            if DEBUG:
                print(data)
            print()

            action = {}
            if True:
                action[-1] = "等待半小时"
            if data["time"]>=1200:
                action[-4] = "睡觉"
            if True:
                action[-2] = "背包"
            if DEBUG:
                action[-3] = "DEBUG"
            f=open("events/index.json","r",encoding="utf-8")
            events = json.load(f)
            f.close()
            for i in events:
                if eval(events[i][3]) and events[i][7]=="optional":
                    action[int(i)] = events[i][5]
            selection = []
            for i in action:
                selection.append([i,action[i]])
            out = []
            for i in selection:
                out.append(i[1])

            res = function.select(out,texts.description(data["location"]))
            event = selection[res][0]
            if event == -1:
                data["time"]+=30
            elif event == -2:
                function.bag(data)
            elif event == -3:
                res = function.select(["退出","事件","战斗"],"DEBUG界面")
                if res==1:
                    id = int(input("id:"))
                    is_saved = function.select(["否","是"],"是否保存data？")
                    old_data = deepcopy(data)
                    function.event(data,id)
                    if is_saved==0:
                        data = old_data
                elif res==2:
                    id = int(input("id:"))
                    is_escaped = function.select(["否","是"],"可逃跑？")
                    is_saved = function.select(["否","是"],"是否保存data？")
                    print("id:",id,"is_escaped:",is_escaped,"is_saved:",is_saved)
                    old_data = deepcopy(data)
                    r = function.battle(data,id,bool(is_escaped))
                    if is_saved==0:
                        data = old_data
                    print("输出：",r[1])
                    pygame.mixer.music.stop()
            elif event == -4:
                data["time"] = 1800
            else:
                if DEBUG:
                    print("going to play event...")
                    function.talk("event_id:",event)
                data = function.event(data,event)
            if data["time"]>=1440:
                data["days"] += data["time"]//1440
                data["time"] = data["time"]%1440
                break

        #存档
        res = function.select(["存档并进入下一天","不保存并退出","保存并退出"],"你要对自己的选择负责......")
        if res==0:
            save_saving(data)
        elif res==1:
            break
        elif res==2:
            save_saving(data)
            break
    pygame.mixer.music.load("audio/Sink.flac")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)



def main():
    print("赛博世界CyberWorld")
    pygame.mixer.init()
    pygame.mixer.music.load("audio/Introduction.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    os.system("")
    print("事件加载中...\033[s0/0",end="",flush=True)
    events = {}
    path = "events"
    progress=0
    progress_max=str(len(os.listdir(path)))
    for file in os.listdir(path):
        progress+=1
        print("\033[u\033[K"+str(progress)+"/"+progress_max,end="",flush=True)
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            if not ".event" in file_path:
                continue
            f = open(file_path,"r",encoding="utf-8")
            res = f.readlines()
            f.close()
            events[int(res[0][:-1])]=[int(res[0][:-1]),file_path1,res[1][:-1],res[2][:-1],bool(eval(res[3][:-1])),res[4][:-1],res[5][:-1],res[6][:-1]]
        else:
            for file1 in os.listdir(os.path.join(file_path)):
                file_path1 = os.path.join(file_path,file1)
                if os.path.isfile(file_path1):
                    if not ".event" in file_path1:
                        continue
                    f = open(file_path1,"r",encoding="utf-8")
                    res = f.readlines()
                    f.close()
                    events[int(res[0][:-1])]=[int(res[0][:-1]),file_path1,res[1][:-1],res[2][:-1],bool(eval(res[3][:-1])),res[4][:-1],res[5][:-1],res[6][:-1]]
    f = open("events/index.json","w",encoding="utf-8")
    datar = json.dumps(events, sort_keys=True, indent=4, separators=(',', ': '))
    f.write(datar)
    f.close()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.load("audio/Sink.flac")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    os.system("title sever:127.0.0.1")
    while True:
        os.system("cls")
        print("链接主机：127.0.0.1",end=" ",flush=True)
        for i in range(3):
            time.sleep(0.2)
            print(".",end="",flush=True)
        print("成功")
        time.sleep(0.5)
        print("运行路径：",os.getcwd())
        print("欢迎回来，",os.getlogin())
        if os.path.exists("save.save"):
            f = open("save.save", "r", encoding="utf-8")
            save = json.load(f)
            f.close()
            print("当前存档：第",save["days"],"天",texts.location(save["location"]),"hp:",save["hp"],"/",save["max_hp"],save["golds"],"字符",save["save_time"])
        res = function.select(["新存档","读取存档","退出"] if os.path.exists("save.save") else ["新存档","退出"])
        if res==0:
            if os.path.exists("save.save"):
                res2 = function.select(["是","否"],"确定要新建存档吗？这会覆盖原存档。")
                if res2 == 0:
                    create_saving()
                    game()
            else:
                create_saving()
                game()
        elif res==1 and os.path.exists("save.save"):
            global data
            data = load_saving()
            if data:
                game()
        elif (res==2 and os.path.exists("save.save")) or (res==1 and (not os.path.exists("save.save"))):
            break
DEBUG = True
if __name__=="__main__":
    if is_admin():
        try:
            main()
        except Exception as e:
            print("发现了一个错误！")
            traceback.print_exc()
            f = open("crash.txt","w",encoding="utf-8")
            f.write(traceback.format_exc())
            f.close()
            function.error("请尝试反馈问题！")
    else:
        if not os.path.exists("save.save"):
            input("你需要给予管理员权限才能继续（用于读写存档），按下enter给予管理员权限")
        ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,1)


#main()
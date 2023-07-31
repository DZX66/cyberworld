# =-= coding:utf-8 =-=
from __future__ import print_function
import time
import function
import os
import json
import texts
import random
import ctypes
import sys

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
    "skills": {'1': "普通攻击",'2': "火球术",'3': "治疗术"}
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
    datar = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    try:
        with open("save.save", "w", encoding="utf-8") as f:
            f.write(datar)
        function.talk("存档成功！")
    except Exception as e:
        print("存档失败：", e)


def game():
    global data
    while True:
        os.system("cls")
        #事件
        if data["days"] == 0:
            data = function.event(data,0)
        
        
        #下一天
        data["days"] = data["days"]+1
        while True:
            print("\n~~~第"+str(data["days"])+"天~~~\n")
            print("字符：",data["golds"])
            print()

            action = {}
            if True:
                action[-1] = "下一天"
            if True:
                action[-2] = "背包"
            f=open("events/index.json","r",encoding="utf-8")
            events = json.load(f)
            f.close()
            for i in events:
                if eval(events[i][3]):
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
                break
            elif event == -2:
                function.bag(data)
            else:
                data = function.event(data,event)

        #存档
        res = function.select(["存档并进入下一天","不保存并退出","保存并退出"],"你要对自己的选择负责......")
        if res==0:
            save_saving(data)
        elif res==1:
            break
        elif res==2:
            save_saving(data)
            break



def main():
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
        res = function.select(["新存档","读取存档","退出"])
        if res==0:
            if os.path.exists("save.save"):
                res2 = function.select(["是","否"],"确定要新建存档吗？这会覆盖原存档。")
                if res2 == 0:
                    create_saving()
                    game()
            else:
                create_saving()
                game()
        elif res==1:
            global data
            data = load_saving()
            if data:
                game()
        elif res==2:
            break

if __name__=="__main__":
    if is_admin():
        main()
    else:
        if not os.path.exists("save.save"):
            input("你需要给予管理员权限才能继续（用于读写存档），按下enter给予管理员权限")
        ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,1)


#main()
#all code was written by kurochmobile42@gmail.com
#no ai was used while reserch or writing code
#some information was taken from www.w3schools.com/python
import math


menu_id = 0
user_in = ""
predraw = ""
error = ""
adv_error = ""
triangle_type = 0

settings = {
"show_version":1,
"show_version_date":0,
"version_date":"2026.09.28",
"version":"v2.2.8",
"show_adv_error": 0
}

custom_keybinding = {
}
temp_keybindings = {
}
value_or_x = "enter a value (number) or \"x\" for unknown value"
 


menu_titles = {
    -3: "exit",
    0: "main menu",
    1000: "algebra",
     1100: "discriminant",
     1200: "short multiplication",
     1300: "avergarage",
     1400: "smaller",
    2000: "geometry",
     2100: "pifagor",
     2200: "centre",
     2300: "length",
    3000: "other tools",
    4000: "physics",
     4100: "Fa",
    7000: "credits",
    9000: "settings"
}
items = {
    0:[1000,2000,4000,3000,9000,7000],
    2000: [2100,2200,2300],
    1000: [1100,1200],
    4000: [4100],
    3000: [1300]
}
custom_app = [-3,2100,2200,2300,1100,1200,4100]

#ca0000 - ca means custom app, numbers - menu id that this app is sued fore
#q_aaaaa - q_ means quick app it runs calculations and *returns* value back


def q_average(l):
    summ = 0
    while a < len(l):
        summ += l[a]
        a+=1
    return summ/len(l)
    
def q_triangle(a,b,c):
    if str(a) == "":
        a="a"
    if str(b) == "":
        b="b"
    if str(c) == "":
        c="c"
    triangle = "    ╱│  \n"+c+"  ╱ │  \n  ╱  │"+b+"\n ╱   │  \n─────┘  \n  "+a
    return triangle


def ca2200():
    global predraw
    
    rpt_desc = "enter value (number)"
    q = ["enter position for dot A", "enter position for dot B"]
    a = 0
    desc = ["enter x coordinate ; and y coordinate"]
    u_ans = list(ask_list(q,desc))
    calc = math.sqrt((u_ans[1]-u_ans[3])^2+(u_ans[2]-u_ans[4])^2)
    predraw += "\n"+calc+"\n"
    ask()









  

def ask_list(q, desc): #q - list of questions, desc - description for every question
    global predraw
    global ans
    a=0
    ans = []
    
    while a < len(q):
        if type(desc) == "<class 'str'>":
            text_to_ask = desc
        else:
            text_to_ask =
        predraw += q[a]+"\n"+desc[a]+"\n"
        ans+=str(ask())
        a+=1
    return ans





def repeat(symbol, times):
    a = 0
    repeated = ""
    while a<int(times):
        repeated += str(symbol)  
        a+=1
    return repeated

def custom_app_runner():
    global menu_id
    if menu_id == -3:
        ask()
    if menu_id == 2100:
        ca2100()
    if menu_id == 2200:
        ca2200()
def ask():
    global settings
    global predraw
    global error
    global adv_error
    global user_in
    if error != "":
        predraw+="\n ‼"+error
    if settings["show_adv_error"] == 1:
        predraw+="\n"+str(adv_error)
    print(repeat("\n", 20)+predraw)
    user_in = input("> ")
    error = ""
    adv_error = ""
    predraw = ""
    return user_in

#def asko():
#    global settings
#    global predraw
#    global error
#    global adv_error
#    global user_in
#    if error != "":
#        predraw+="\n ‼"+error
#    if settings["show_adv_error"] == 1:
#        predraw+="\n"+str(adv_error)
#    print(predraw)
#    error = ""
#    adv_error = ""
#    predraw = ""
#    user_in = input()
#    return user_in


def default_menu():
    #global temp_keybindings
    global predraw
    global items
    global menu_id
    global user_in
    global menu_titles
    global error
    global adv_error
    temp_keybindings = {}
    devider = " : "
    choice = ""
    c_items = [0]
    if menu_id != 0:
        a = 0
    else:
        a = 1
    
    if menu_id in list(items.keys()):
        c_items += sorted(list(items[menu_id]))
    else:
        c_items += []
    while a<len(c_items):
        devider = " : "
        if not menu_id in custom_app:
            f = "Ⓕ"
        else:
            f = ""
        choice += str(a)+devider+f
        if c_items[a] in menu_titles.keys():
            choice += str(menu_titles[c_items[a]])
        else:
            choice += str(c_items[a])
        if a == 0:
            choice +="\n"
        choice +="\n"
        temp_keybindings[str(a)] = c_items[a]
        
        a+=1
    predraw+=choice    
    ask()
    if str(user_in) in list(temp_keybindings.keys()):
        menu_id = temp_keybindings[user_in]
    else:
        error = "invalid input"
        adv_error = str(list(temp_keybindings.keys()))+";;"+str(user_in)


while 1==1:
    



    if not menu_id in custom_app:
        default_menu()
    else:
        custom_app_runner()

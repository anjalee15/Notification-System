from plyer import notification
import random
import datetime

time1 = datetime.datetime.now().strftime("%M")
time2 = datetime.datetime.now().strftime("%M")
#print(time1)
aaa  = []
bbb= []
if __name__=="__main__":
    with open("water.txt", 'r') as f :
        aaa = f.readlines()
    aaa = [i.split("\n")[0] for  i in aaa]
    with open("break.txt", 'r') as f :
        bbb = f.readlines()
    bbb = [i.split("\n")[0] for  i in bbb]
    while True :  
        if datetime.datetime.now().strftime("%M") == time1 :
            water_msg= random.choice(aaa) 
        # # rest_msg=df2.sample()
            print(water_msg)

            notification.notify(
                title = "Have a glass of water!!!",
                message = water_msg,
                app_icon = "E:\\My_python_practice\\Projects\\Notification System\\Water.ico",
                timeout = 10
            )
            
            time1 = str(int(datetime.datetime.now().strftime("%M"))+60)

        if datetime.datetime.now().strftime("%M") == time2 :
            rest_msg=random.choice(bbb)
            notification.notify(
                title = "Let's take a rest",
                message = rest_msg,
                app_icon = "E:\\My_python_practice\\Projects\\Notification System\\Rest.ico",
                timeout = 10
            )

            time2 = str(int(datetime.datetime.now().strftime("%M"))+180)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from threading import Timer
#import buildozer
import mysql.connector
from mysql.connector import Error
#import kivy
#from math import ceil
import os
#import subprocess
#import pure-python-adb
import json


#-----------------------------------------------------------------------



#-----------------------------------------------------------------------
varstate = 0
varstateone = 0
progressval = 0
#ip = "your.ip.address"
#filepath = "Documents/Python-Projects/your_file.py"

#-----------------------------------------------------------------------

class CircularProgressBar(ProgressBar, FloatLayout):
    def __init__(self,**kwargs):
        super(CircularProgressBar,self).__init__(**kwargs)
        self.thickness = 40
        self.label = CoreLabel(text="0", font_size=self.thickness)
        self.texture_size = None
        self.refresh_text()
        self.draw()
    def draw(self):
        with self.canvas:
            self.canvas.clear()
            Color(0.26,0.26,0.26)
            Ellipse(pos=self.pos, size=self.size)
            Color(1,0,0)
            Ellipse(pos=self.pos,size=self.size,angle_end=(self.value/100.0)*360)
            Color(0,0,0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            Color(1, 1, 1, 1)
            Rectangle(texture=self.label.texture,size=self.texture_size,pos=(self.pos[0]-self.texture_size[0],self.center[1] - self.texture_size[1]/2))
            self.label.text = str(int(self.value))

    def refresh_text(self):
        self.label.refresh()
        self.texture_size=list(self.label.texture.size)
    def set_value(self, value):
        self.value = value
        self.label.text = str(int(self.value))
        self.refresh_text()
        self.draw()

#-----------------------------------------------------------------------

class RegisterWindow(Screen):
    first_namee = ObjectProperty(None)
    last_namee = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        pop_users = """
        INSERT INTO usersdos
        (user_id, first_name, last_name, password)
        VALUES (%s, %s, %s, %s);
        """
        user_input = (self.username.text, self.first_namee.text, self.last_namee.text, self.password.text)

        connection = create_db_connection("localhost", "Samsamsam", "suckySucky10bucky_", "chat_db")
        execute_query(connection, pop_users, user_input)
        self.first_namee.text = ""
        self.last_namee.text = ""
        self.username.text = ""
        self.password.text = ""
        sm.current = "login"

    def goback(self):
        sm.current = "login"


"""
    def submit(self):
        if self.first_namee.text != "" and self.last_namee.text != "" and self.username.text != "":
            if self.password != "":
                mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "Samsamsam",
                    passwd = "suckySucky10bucky_",
                    database = "chat_db"
                )
                c = mydb.cursor()
                #c.execute("CREATE DATABASE IF NOT EXISTS chat_db")
                query = "INSERT INTO users (first_name, last_name, username, password) VALUES (%s, %s, %s, MD5(%s)"
                fn = self.first_namee.text
                ln = self.last_namee.text
                un = self.username.text
                pssw = self.password.text
                values = (fn, ln, un, pssw)
                c.execute(query, values)
                mydb.commit()
                mydb.close()
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()
"""
"""
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()
"""
"""
    def login(self):
        self.reset()
        sm.current = "login"


    def goback():
        sm.current = "login"


    def reset(self):
        self.first_namee.text = ""
        self.last_namee.text = ""
        self.username.text = ""
        self.password.text = ""
"""
#-----------------------------------------------------------------------

class LoginWindow(Screen):
    first_namee = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        q1 = """
        SELECT usersdos.first_name, usersdos.password
        FROM usersdos
        """
        connection = create_db_connection("localhost", "Samsamsam", "suckySucky10bucky_", "chat_db")
        results = read_query(connection, q1)
        str = ''
        for result in results:
            str = str , result
        res = json.dumps(str)
        if self.first_namee.text in res:
            if self.password.text in res:
                self.reset()
                sm.current = "main"
            else:
                invalidLogin()
        else:
            invalidLogin()


        #for result in results:
            #if self.first_namee.text in result and self.password.text in result:
                #if self.password.text in result:
                #self.reset()
                #sm.current = "main"
                #else:
                    #pass
            #else:
                #invalidLogin()



        #f db.validate(self.email.text, self.password.text):
            #MainWindow.current = self.email.text
            #self.reset()
            #sm.current = "main"
        #else:
            #invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "register"

    def reset(self):
        self.first_namee.text = ""
        self.password.text = ""

#-----------------------------------------------------------------------

class MainWindow(Screen, Widget):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_center(self, *args):
        pass
        """
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "Samsamsam",
            passwd = "suckySucky10bucky_",
            database = "chat_db"
        )
        c = mydb.cursor()
        c.execute("SELECT * FROM customers")
        #records = c.fetchall()
        mydb.commit()
        mydb.close()
"""
        #password, name, created = db.get_user(self.current)
        #self.n.text = "Account Name: " + name
        #self.email.text = "Email: " + self.current
        #self.created.text = "Created On: " + created

    def btnconnect(self):
        #adb shell am start -n com.android.settings/com.android.settings.Settings
        show_popup_connect()

    def btn1(self):
        global varstate
        global varstateone
        if varstate == 0:
            if varstateone == 0:
                varstateone = varstateone + 1
                print(varstateone)
                openmotors()
                show_popup_open()
                timermotors()
            else:
                pass
        else:
            pass

    def btn2(self):
        global varstate
        global varstateone
        if varstateone == 1:
            varstate = varstate + 1
            print(varstate)
            if varstate == 1:
                closemotors()
                show_popup_close()
            else:
                pass
        else:
            pass

#-----------------------------------------------------------------------

class WindowManager(ScreenManager):
    pass

#-----------------------------------------------------------------------
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query, record):
    cursor = connection.cursor()
    try:
        cursor.execute(query, record)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection succesful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def timermotors():
    t = Timer(20.0, autoclose)
    t.start()

def autoclose():
    global varstateone
    global progressval
    if varstateone != 0 and progressval == 0:
        closemotors()
        resetvar()
        show_popup_close()
    else:
        pass

def openmotors():
    #subprocess.run("ssh pi@{} python {}".format(ip, file_path),
    #               shell=True, check=True)
    #ejemplo de comando subprocess: ssh pi@your.ip.address python Documents/Python-Projects/your_file.py
    print("Motor girando")

def closemotors():
    #subprocess.run("ssh pi@{} python {}".format(ip, file_path),
    #               shell=True, check=True)
    #ejemplo de comando subprocess: ssh pi@your.ip.address python Documents/Python-Projects/your_file.py
    print("Motor girando")

def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Login',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def finishedCicle():
    pop = Popup(title='Cicle finished',
                    content=Label(text='You can now open the door.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def resetvar():
    global varstate
    global varstateone
    global progressval
    varstate = 0
    varstateone = 0
    progressval = 0
    #print(varstate)



#-----------------------------------------------------------------------

kv = Builder.load_file("main.kv")
sm = WindowManager()
#db = DataBase("users.txt")
screens = [LoginWindow(name="login"), RegisterWindow(name="register"),
           MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

#-----------------------------------------------------------------------

class P1(FloatLayout):
    pass

#-----------------------------------------------------------------------

class P2(FloatLayout):
    pass

#-----------------------------------------------------------------------

class P3(FloatLayout):
    pass

#-----------------------------------------------------------------------

class Main(App, FloatLayout):
    def animate(self,dt):
        global progressval
        circProgressBar = self.root.get_screen('main').ids.cp
        if varstate >= 1 and varstateone == 1:
            circProgressBar.set_value(circProgressBar.value+1)
            progressval = 1
            if circProgressBar.value == 100:
                resetvar()
                finishedCicle()
            else:
                pass
        else:
            circProgressBar.set_value(0)

    def build(self):
        Clock.schedule_interval(self.animate, 0.1) #ultimo numero cambia velocidad de barra

        #basedata()
        #c = mydb.cursor()
        #c.execute("CREATE DATABASE IF NOT EXISTS chat_db")
        #c.execute("CREATE TABLE if not exists users (first_name VARCHAR(255), last_name VARCHAR(255), username VARCHAR(255), password VARCHAR(255))")
        #c.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
        #c.execute("DESC users")
        #mydb.commit()
        #mydb.close()

        return sm

#-----------------------------------------------------------------------

def show_popup_open():
    show = P1()
    popupWindow1 = Popup(
        title="Popup Window", content=show,
        size_hint=(None,None), size=(400,400))
    popupWindow1.open()

def show_popup_close():
    show = P2()
    popupWindow2 = Popup(
        title="Popup Window", content=show,
        size_hint=(None,None), size=(400,400))
    popupWindow2.open()

def show_popup_connect():
    show = P3()
    popupWindow3 = Popup(
        title="Popup Window", content=show,
        size_hint=(None, None), size=(400,400))
    popupWindow3.open()

#-----------------------------------------------------------------------

if __name__ == "__main__":
    Main().run()

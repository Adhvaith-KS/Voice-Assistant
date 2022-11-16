import pyttsx3
import speech_recognition as sr 
import datetime as dt 
import wikipedia
import webbrowser
import time
import os
import smtplib
import random 
import mysql.connector as mysql
import requests
from tkinter import *

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')                           
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')                             
engine.setProperty('volume',1.0)

def say(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def saywithoutprint(text):
    engine.say(text)
    engine.runAndWait()

def sayinp(text, inpu):
    engine.say(text)
    engine.runAndWait()
    inp = input(inpu)
    return inp


def greet():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning, "+user)
    elif hour>11 and hour<17:
        say("Good afternoon, "+user)
    elif hour>16 and hour<21:
        say("Good evening, "+user)
    elif hour>20:
        say("Good evening, "+user) 
    say("How may I help you?")     

def intro():
    say("Hello. I'm OLIVIA, your Voice Assistant.")   
    print()           

def backgroundcmd():
    s= sr.Recognizer()
    with sr.Microphone() as source:
        audio= s.listen(source)  
    try:
        queryy = s.recognize_google(audio, language = 'en-in') 
        print(f"You said: {queryy} \n") 
        
    except:
        say("")    
        queryy= backgroundcmd()  
    return queryy.lower()

def reminder():
        text= sayinp("What shall I remind you about?", "What shall I remind you about?: ")
        saywithoutprint("In how many minutes?: ")
        local_time= float(input("In how many minutes?: "))
        local_time = local_time * 60
        time.sleep(local_time)
        root = Tk()
        T = Text(root, height=2, width=30)
        T.config(bg='lightgreen')
        T.config(width=20)
        T.config(height=5)
        Ftup = ("agency fb", 100, "bold")
        T.config(font=Ftup)
        root.wm_attributes("-topmost", 1)
        T.pack()
        remm= '              REMINDER! \n' + text
        T.insert(END, remm)
        say("REMINDER ALERT! REMINDER ALERT!")
        say(text)
        mainloop()

def command():
    s= sr.Recognizer()
    with sr.Microphone() as source:
        audio= s.listen(source)  
    try:
        say("Recognizing...")
        queryy = s.recognize_google(audio, language = 'en-in') 
        print(f"You said: {queryy} \n")
    except:
        say("I'm sorry. Could you say that again?")    
        queryy= command()  
    return queryy

def features():
    say("There are a lot of things I can do")
    say("I can: ") 
    say("Send your Emails for you,")   
    say("Play your favourite music,")
    say("Open any app or website,")
    say("Open the pdf of any CBSE textbook,")
    say("Give you basic information about anybody or anything,")
    say("Spam anybody with emails,")
    say("Answer all of your questions,")
    say("Give you my opinion on anything,")
    say("Set reminders")
    say("Organise your To-Do-lists")
    say("And a lot, lot more.")
    fn= "It's a pleasure to serve you, "+ user + "."
    say(fn)

def Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    if eAd=="new user":
        say("Emails cannot be sent with guest account. Please log in to send emails.")
        return ""
    txtemail= "Enter password for "+eAd+ ": "
    password= input(txtemail)
    server.login(eAd, password)
    server.sendmail(eAd, to, content)
    server.close()
    say("Email successfully sent, "+user)


def Emailwithoutstring(to, content, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    if eAd=="new user":
        say("Emails cannot be sent with guest account. Please log in to send emails.")
        return ""
    server.login(eAd, password)
    server.sendmail(eAd, to, content)
    server.close()

def Emailspam(to, content, n):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    if eAd=="new user":
        say("Emails cannot be sent with guest account. Please log in to send emails.")
        return ""
    txtemail= "Enter password for "+eAd+ ": "
    password= input(txtemail)
    server.login(eAd, password)
    server.sendmail(eAd, to, content)
    server.close()

    for a in range(1, n+1):
        Emailwithoutstring(to, content, password)
        if a==1:
            say("Email sent one time")
        else:    
            sy= "Email sent "+str(a)+ " times"
            say(sy)
    spch = str(n) + "Emails successfully sent"        
    say(spch)

def jokes():
  say("A joke? I'll give you two!")  
  for i in range(0,2):
    rand= random.randint(0,4)
    if rand==0:
      jokeitem="cat"
    if rand==1:
      jokeitem="dog"
    if rand==2:
      jokeitem="joke"
    if rand==3:
      jokeitem="chicken"
    if rand==4:
      jokeitem="movie"
    
    try:
        information = requests.get(f"https://icanhazdadjoke.com/search?term={jokeitem}", headers= {"Accept":"application/json"})
        connection = information.ok
        result = information.json()
        l_no_of_jokes = result["results"]
        no_of_jokes = len(l_no_of_jokes)
        response="" 
        information = requests.get(f"https://icanhazdadjoke.com/search?term={response}", headers= {"Accept":"application/json"})
        result = information.json()
        l_no_of_jokes = result["results"]
        no_of_jokes = len(l_no_of_jokes)

        x=random.randint(0,no_of_jokes-1)
        joke= l_no_of_jokes[x]['joke']
        say(joke)

    except:
      print("You're not connected to the internet. An internet connection is required to use this feature.")    
            
def ToDoList(r):
    if r==1: 
        print("Enter your password to access your To Do Lists below.")
        while True:
            passw= input("Enter your password: ")
            try:
                cn= mysql.connect(host="localhost", user="root", passwd= passw)
            except:
                print("Incorrect password!")
                print("Do you wish to input your password again?")
                ch= input("Enter your choice (Y/N): ")
                if ch in "nN":
                   print("Program terminated")
                   quit()
                else:
                   continue
            if cn.is_connected():
              say("Access granted!")
              prog=1
            break
        if prog!=1:
            say("Unable to access your lists")
            return()
        cur=cn.cursor()
        cur.execute("use mysql")
        cur.execute("select * from numoflists;")
        alllists=cur.fetchall()
        say("Your lists are:")
        for i in alllists:
            for j in i:
                print(j)
        sele= input("Which list would you like to see?: ")
        comm= "select * from "+sele+";"
        cur.execute(comm)
        plis= cur.fetchall()
        say1= "Your list "+sele+" contains:"
        say(say1)
        for i in plis:
            for ii in i:
                say(ii)
    if r==2:
        print("Enter your password to access your To Do Lists below.")
        while True:
            passw= input("Enter your password: ")
            try:
                cn= mysql.connect(host="localhost", user="root", passwd= passw)
            except:
                print("Incorrect password!")
                print("Do you wish to input your password again?")
                ch= input("Enter your choice (Y/N): ")
                if ch in "nN":
                   print("Program terminated")
                   quit()
                else:
                   continue
            if cn.is_connected():
              say("Access granted!")
              prog=1
            break
        if prog!=1:
            say("Unable to access your lists")
            return()
        cur=cn.cursor()
        cur.execute("use mysql")
        nameoflist= input("Enter the name of your new list: ")
        execu= "create table "+nameoflist+"(content varchar(50));"
        cur.execute(execu)
        execu2= "insert into numoflists values('"+nameoflist+"');"
        cur.execute(execu2)
        cn.commit()
        numoflistlines= int(input("Enter the number of lines in your list: "))
        for i in range(numoflistlines):
            inp1="Enter line "+str(i+1)+" of the list: "
            listcontent= input(inp1)
            execu3= "insert into "+nameoflist+" values('"+listcontent+"');"
            cur.execute(execu3)
            cn.commit()
        say("List successfully created")
        say("This is your new list: ") 
        execu4= "select * from "+nameoflist+";"
        cur.execute(execu4)
        for i in cur.fetchall():
            for ii in i:
               say(ii) 




def music():
    ss=0
    say("Of course. But what would you like to play? You can select from the options displayed below:")
    musicdoc= "C:\\Users\\admin\\Music\\Music"
    for f in os.listdir(musicdoc):
        print(f)
    say(f"What do you want to listen to, {user}?")
    choice = command()   
    for s in os.listdir(musicdoc):
        if choice.lower() in s.lower():
           songl= "C:\\Users\\admin\\Music\\Music" + "\\" + s
           print (songl)
           os.startfile(songl)
           ss=1       
           break
    if ss==0:
           say("Your choice was not found in your computer.") 
           say("Would you like to choose again?")
           yesno= command()
           if 'yes' in yesno.lower() or 'yeah' in yesno.lower() or 'yup' in yesno.lower() or 'of course' in yesno.lower():
                music()
           elif 'no' in yesno.lower() or 'not really' in yesno.lower() or 'nope' in yesno.lower() or 'nah' in yesno.lower():
                say("Alright then. I will not be playing anything.") 

def date():
    say(str(dt.date.today()))
                           


say("Booting OLIVIA...")
chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"


wakewords = ['hey olivia', 'hi olivia', 'olivia', 'hey viv', 'viv', 'hey olivia', 'ok olivia', 'olivia',  'liv', 'leaf', 'leaves', 'healer', 'olympia', 'live', 'hey live', 'hey liv', "livia", "ollie", "vee", "livs", "livie", "livvie", "lip", "hey lip", "flip", "hey flip", "veer", "hey veer", "dip", "hey dip", "nift", "hey nift"]
prog=0 #above words are stored in the list 'wakewords' because they are all similar to the words Olivia/Liv when heard by the voice recognition module.
while True:
    attempt=0
    VAaccess= "granted"
    if prog==0:
        attempt=1
        print("Enter your password to access O.L.I.V.I.A. : ")
        while True:
            passw= input("Enter your password: ")
            try:
                cn= mysql.connect(host="localhost", user="root", passwd= passw)
            except:
                print("Incorrect password!")
                print("Do you wish to input your password again?")
                ch= input("Enter your choice (Yes/No): ")
                if ch.lower()=="no":
                   print("Terminating OLIVIA...")
                   break
                elif ch.lower()=="yes":
                   continue
                else: 
                    print("Invalid choice.")
                    continue
            if cn.is_connected():
              say("Successfully connected to OLIVIA.")
              print()
              prog=1
            break
        if prog!=1:
            break

        intro()
        identified=0
        cur=cn.cursor()
        while identified!=1:
            print()
            say("Please identify yourself.")
            print()
            say("Other account options are displayed below.")
            print()
            print("If you are a new user and do not wish to create an account, enter 'new user'. The password is 'olivia'")
            print("If you wish to create a new account, enter 'CNA' as your identification")
            print("If you wish to delete your account, enter 'Delete' as your identification")
            print("If you wish to edit your account details, enter 'Edit' as your identification")
            print("If you wish to view your account details, enter 'View' as your identification")
            print("If you wish to quit, enter 'quit' as your identification.")
            print()

            identification= input("Enter your identification: ")
            print()
            if identification.lower()=="quit":
                say("Terminating OLIVIA...")
                break
            if identification.lower()=="cna":
                user= input("Enter your name you would like to be called by: ")
                iname= input("Enter your identification name: ")
                eAd= input("Enter your email address: ")
                pswd= input("Enter your password: ")
                while True:
                    try:
                        dob= input("Enter your date of birth (yyyy-mm-dd): ")
                        st= 'insert into usersVA values("'+iname+'", "'+eAd+'", "'+user+'", "'+pswd+'", "'+dob+'");'
                        cur.execute("Use mysql")
                        cur.execute(st)
                        cn.commit() 
                        say("User profile created.")
                        txt1= "Welcome, "+ user+ "."
                        say(txt1)
                        VAaccess= "granted"
                        break
                    except:
                        print("Invalid format entered for date of birth. Enter dob again.")
                        continue
            if identification.lower()=="delete":
                acc= input("Enter your E-mail address: ")
                cur.execute("Use mysql")
                cur.execute("Select * from usersVA;")
                d=cur.fetchall()
                for r in d:
                    if acc.lower() in r:
                        psw= input("Enter your current password: ")
                        print()
                        if psw==r[3]:
                            execc= "delete from usersva where email= '"+acc+"';"
                            cur.execute(execc)
                            cn.commit()
                            say("Account successfully deleted.")
                            break
                        else:
                            say("Incorrect password!")
                else:
                        say("Account not found.")
                VAaccess= "denied"

            if identification.lower() == "view":
                acc= input("Enter your email address: ")
                cur.execute("Use mysql")
                cur.execute("Select * from usersVA;")
                d=cur.fetchall()
                accfound=0
                for r in d:
                    if acc.lower() in r:
                        psw= input("Enter your current password: ")
                        if psw==r[3]:
                                say("Account found. Account details are displayed below.")
                                print()
                                print("Voice Assistant name: ",r[0])
                                print("Email Address: ", r[1])
                                print("Real Name: ", r[2])
                                print("Password: ", r[3])
                                print("Date of Birth [YYYY-MM-DD]: ", r[4])
                                accfound=1
                                break
                        else:
                            say("Incorrect password!")  
                            accfound=1  
                if accfound==0:
                    say("Account not found")
                VAaccess= "denied"

            if identification.lower()== "edit":
                acc= input("Enter your email address: ")
                cur.execute("Use mysql")
                cur.execute("Select * from usersVA;")
                d=cur.fetchall()
                accfound=0
                for r in d:
                    if acc.lower() in r:
                        print()
                        say("Account found.")
                        psw= input("Enter your current password: ")
                        if psw==r[3]:
                            say("Which part of your account would you like to edit?")
                            editacc= input("Enter the section to be edited (VAname|email|RealName|password|dob): ")
                            if editacc.lower()=="vaname":
                                edit1= input("Enter your new VAname: ")
                                exec= "update usersVA set VAname= '"+edit1+"' where email= '"+acc+"';"
                                cur.execute(exec)
                                cn.commit()
                                say("Succesfully edited your information.")

                            elif editacc.lower()=="email":
                                edit1= input("Enter your new email: ")
                                exec= "update usersVA set email= '"+edit1+"' where email= '"+acc+"';"
                                cur.execute(exec)
                                cn.commit()
                                say("Succesfully edited your information.")

                            elif editacc.lower()=="realname":
                                edit1= input("Enter your new real name: ")
                                exec= "update usersVA set realname= '"+edit1+"' where email= '"+acc+"';"
                                cur.execute(exec)
                                cn.commit()
                                say("Succesfully edited your information.")

                            elif editacc.lower()=="password":
                                psw= input("Enter your current password: ")
                                if psw==r[3]:
                                    edit1= input("Enter your new password: ")
                                    exec= "update usersVA set password= '"+edit1+"' where email= '"+acc+"';"
                                    cur.execute(exec)
                                    cn.commit()
                                    say("Succesfully edited your information.")
                                else:
                                    say("Wrong password.")    


                            elif editacc.lower()=="dob":
                                edit1= input("Enter your new date of birth (yyyy-mm-dd): ")
                                exec= "update usersVA set dob= '"+edit1+"' where email= '"+acc+"';"
                                cur.execute(exec)
                                cn.commit()
                                say("Succesfully edited your information.")

                            else:
                                say("The section you specified does not exist.")
                                
                            accfound=1
                            break
                    
                if accfound==0:
                    say("Account not found")
                VAaccess= "denied"

            if identification.lower() not in ["cna", "delete", "edit", "view", "quit"]:
                cur.execute("Use mysql")
                cur.execute("Select * from usersVA;")
                d=cur.fetchall()
                for r in d:
                    if identification.lower() in r:
                                txt= "Enter password for "+r[2]+" : "
                                passw= input(txt)
                                if passw==r[3]:
                                    identified=1
                                    s= "Access granted. Welcome back, "+r[2]+ "."
                                    user= r[2]
                                    eAd= r[1]
                                    say(s)
                                    VAaccess= "granted"
                                    break 
                                
                if identified!=1:
                    say("Access denied")
                    print()
                    VAaccess= "denied"

    if VAaccess == "denied":
        break        

    print()
    
    if attempt==1:
         say("OLIVIA is now online.")
    text = backgroundcmd()
    
    if text.lower() in wakewords:
        greet()
        query = command()
    
        if 'wikipedia' in query.lower():
            say("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            query= query.replace("could you tell me", "")
            query= query.replace("can you tell me", "")
            query= query.replace("tell me", "")
            query= query.replace("will you", "")
            query= query.replace("something about", "")
            query= query.replace("anything about", "")
            query= query.replace("from", "")
            res= wikipedia.summary(query, sentences=4)
            say(res)

        elif 'date' in query.lower():
            say("The date today is: ")
            date()      

        elif 'youtube' in query.lower():
            if ('youtube' in query.lower()) and ('play'in query.lower() and 'youtube'in query.lower()):
                say("What would you like to play on YouTube?")
                choice = command()
                choice= choice.rstrip()
                say(f"Doing just that, {user}. Give me a moment.")
                webbrowser.get(chrome).open("youtube.com/results?search_query="+choice)
            elif 'youtube' in query.lower():
               say(f"Doing just that, {user}. Give me a moment.")
               webbrowser.get(chrome).open("youtube.com")


        elif 'what can you' in query.lower() or 'what can you do' in query.lower(): 
              features()
              continue

        elif 'joke' in query.lower():
            jokes()

        elif "reminder" in query.lower() or "alarm" in query.lower():
            reminder()

        elif 'bye' in query.lower() or 'go away' in query.lower() or 'stop listening' in query.lower():
            say(f"Okay, {user}. I will disable your microphone and stop listening for my wake word. See you later. Bye.")
            break    

        elif "list" in query.lower() or "checklist" in query.lower() or "schedule" in query.lower():
            say("Do you want to check your existing lists or make a new one?")
            x=command()
            if "check" in x.lower() or "exist" in x.lower():
                ToDoList(1) 
            elif "make" in x.lower() or "create" in x.lower() or "new" in x.lower():
                ToDoList(2)

        elif 'open google' in query.lower():
            say("Opening Google...")
            webbrowser.get(chrome).open("google.com")

        elif 'open' in query.lower() and 'exam' in query.lower():
            say('Opening exam.net...')
            webbrowser.get(chrome).open("exam.net")    
        
        elif 'open facebook' in query.lower():
            say("Opening Facebook...")
            webbrowser.get(chrome).open("facebook.com")  
        
        elif 'open forms' in query.lower():
            say("opening microsoft forms...")
            webbrowser.get(chrome).open('https://forms.microsoft.com/Pages/DesignPage.aspx')   

        elif 'open' in query.lower() and ('pdf' in query.lower() or 'textbook' in query.lower()):
            tbsaid= "Which textbook's pdf would you like to open," + user + "? The textbooks available are listed below."
            say(tbsaid)
            print("Computer applications class 11")
            print("Chemistry part one class 11")
            print("Chemistry part two class 11")
            print("Physics part one class 11")
            print("Physics part two class 11")
            print("Mathematics class 11")
            print("English hornbill class 11")
            print("English snapshots class 11")
            print("Computer applications class 12")
            print("Chemistry part one class 12")
            print("Chemistry part two class 12")
            print("Physics part one class 12")
            print("Physics part two class 12")
            print("Mathematics part one class 12")
            print("Mathematics part two class 12")
            print("English Flamingo class 12")
            print("English vistas class 12")

            tb = command()
            if "computer" in tb.lower() and "11" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?kecs1=0-11")
            elif "computer" in tb.lower() and "12" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?lecs1=0-13")    
            elif "chemistry" in tb.lower() and "11" in tb.lower() and "part one" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?kech1=0-7")
            elif "chemistry" in tb.lower() and "11" in tb.lower() and "part two" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?kech2=0-7")
            elif "chemistry" in tb.lower() and "12" in tb.lower() and "part one" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?lech1=0-9")
            elif "chemistry" in tb.lower() and "12" in tb.lower() and "part two" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?lech2=0-7")
            elif "physics" in tb.lower() and "11" in tb.lower() and "part one" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?keph1=0-8")
            elif "physics" in tb.lower() and "11" in tb.lower() and "part two" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?keph2=0-7")
            elif "physics" in tb.lower() and "12" in tb.lower() and "part one" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?leph1=0-8")
            elif "physics" in tb.lower() and "12" in tb.lower() and "part two" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?leph2=0-6")
            elif ("mathematics" in tb.lower() or "math" in tb.lower() or "maths" in tb.lower()) and "11" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?kemh1=0-16")
            elif ("mathematics" in tb.lower() or "math" in tb.lower() or "maths"in tb.lower()) and "12" in tb.lower() and "part one" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?lemh1=0-6")
            elif ("mathematics" in tb.lower() or "math" in tb.lower() or "maths" in tb.lower()) and "12" in tb.lower() and "part two" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?lemh2=0-7")
            elif "english" in tb.lower() and "11" in tb.lower() and "hornbill" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?kehb1=0-14")
            elif "english" in tb.lower() and "11" in tb.lower() and "snapshots" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?kesp1=0-8")
            elif "english" in tb.lower() and "12" in tb.lower() and "flamingo" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?lefl1=0-14")
            elif "english" in tb.lower() and "12" in tb.lower() and "vistas" in tb.lower():
                webbrowser.get(chrome).open("https://ncert.nic.in/textbook.php?levt1=0-8")
             
            
        elif 'open code' in query.lower():
            say("Opening Microsoft Visual Studio Code...")
            codepath= "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif ('open'in query.lower()) and ('microsoft teams' in query.lower() or 'teams' in query.lower() or 'team' in query.lower()):
            say("Opening Microsoft Teams...")
            codepath= "C:\\Users\\admin\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams"
            try:
                os.startfile(codepath) 
            except:
                print()

        elif 'play' in query.lower() and ('music' in query.lower() or 'song' in query.lower() or 'songs' in query.lower()):
            music()

        elif ('mail' in query.lower() or 'email' in query.lower()) and 'send' in query.lower() and 'spam' not in query.lower():
            adr= sayinp("Who do you want to send an E-mail to? Please enter the E-mail adress of the recipient.", "Enter email address of the recipent: ")
            say("Would you like to Type your content or dictate it to me?")
            choice = command()
            if 'type' in choice:
                say("Okay. Please enter the content of the email.")
                inputt= input("Enter content of the mail:   ")
            elif 'dictate' or 'say' or 'tell':
                say("Sure. Tell me what you need.")
                inputt = command()   
            else:
                say("I'm sorry, you did not answer the question.")
                continue
            Email(adr, inputt)

        elif ('mail' in query.lower()  or 'email' in query.lower()) and "spam" in query.lower():
            adr= sayinp("Who do you want to spam E-mails to? Please enter the E-mail adress of the recipient. ", "Who do you want to spam E-mails to? Please enter the E-mail adress of the recipient: ")
            say("How many times do you want me to send the mail? Please enter the number of times the email must be sent.")
            n=int(input("Enter the number of times the email must be sent: ")) 
            say("Would you like to Type your content or dictate it to me?")
            choice = command()
            if 'type' in choice.lower():
                say("Okay. Please enter the content of the email.")
                inputtt= input("Enter content of the mail:   ")
            elif 'dictate' in choice.lower() or 'say' in choice.lower() or 'tell' in choice.lower():
                say("Sure. Tell me what you need.")
                inputtt = command()   
            else:
                say("I'm sorry, you did not answer the question.")
                continue
            Emailspam(adr, inputtt, n)    

        elif 'opinion' in query.lower():
            say("Sure. I'll let you know my honest and unbiased opinion.")
            say("What do you want my opinion on?")
            op= command()
            a= random.randint(0,3)
            b=random.randint(0,3)
            if a==0:
                if b==0:
                   say("Yeah, definitely!") 
                if b==1:   
                   say("Yup.") 
                if b==2:   
                   say("Yes, of course.")
            elif a==1:
                if b==0:
                   say("Nope.") 
                if b==1:   
                   say("No.") 
                if b==2:   
                   say("Nah.")
            elif a==2:
                say("Maybe")
            elif a==3: 
                say("Hard choice. I don't know. Maybe try asking me again later.")
        else:
             say("I'm sorry, I do not understand.")

        {}

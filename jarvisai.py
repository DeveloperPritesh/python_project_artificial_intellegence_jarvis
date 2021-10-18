'''
#  code developed by : Pritesh Alshetty
# this programm takes user input as audio , analyze the command through wirtten function and perform the task.


'''

# JARVIS AI PROGRAMM
from audioop import maxpp
import os
from subprocess import call  # to set enviornment variable BORWSER for chrome to be default browser
import datetime
import pyttsx3 
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyautogui 
import psutil  
from time import sleep as delayTime

from wikipedia.wikipedia import search  # Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.

dictEmail = {
    'pritesh':'pritesh3038@gmail.com',
    'pritesh2':'priteshalsh46@gmail.com',
    'prajesh':'prajesh3083@gmail.com',
    "deepti":'chinmayishetty1058@gmail.com',
    'gayatri':'gayatrishirsul4@gmail.com'
}

# to write speak function ** will take String as argument and return as audio through connected speaker
engine = pyttsx3.init("sapi5") 
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)#to set voice .. 1 for male and 0 for female voice
engine.setProperty('rate',150) # to change speed of speaking, change variable 'rate'. default value is 200 words per min.
# to see all voices avilable in pc do this: for i in voices:print(i)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe(): # This function wishes 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak(" Good Morning")
    elif hour>12 and hour<18:
        
        speak(" Good Afternoon")
        
    else:

        speak(" Good Evening!!")
    speak("Hello I am jaarvis ")
    speak("How may I help you sir" )


def takeCommand():
    '''
    This func takes input from computers microphone and  converst it to string. uses speech recogniser class from
    speechrecognition module.
    '''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        '''
        Creates a new Microphone instance, which represents a physical microphone on the computer. 
        Subclass of AudioSource
        '''
        print("Listening the user --------------")
        r.pause_threshold = 0.8
        audio = r.listen(source)


    try : # do exception handling if error occurs
        print("Recognizing ^^^^^^^^^^")
        query = r.recognize_google(audio,language='en-in')
        print("User said this: ",query)
    except Exception as e:
        print(f"***************** \n{e}\n****************** ")
        print("********************\nSay that again please:")
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to,content): # send email function takes recipents email id and content of mail to send
    
    server = smtplib.SMTP('smtp.gmail.com', 587) #This class manages a connection to an SMTP or ESMTP server.
    server.ehlo()  #SMTP 'ehlo' command. Hostname to send for this command defaults to the FQDN of the local host.
    server.starttls() #Puts the connection to the SMTP server into TLS mode.
    server.login('pritesh3038@gmail.com', 'Bankofbaroda0.') #Log in on an SMTP server that requires authentication.
# The arguments are:
#
# user: The user name to authenticate with.
# password: The password for the authentication.
    server.sendmail('pritesh3038@gmail.com', to, content) #This command performs an entire mail transaction.
    server.close() #closes the SMTP server . IMPORTANT!
    
      



         
        

if __name__=="__main__":          #Main function start here
   
    print("***********************************\nJARVIS is running......... ")     
    wishMe()    # this function greets user according to time
    check = True
    
    while check:            
        query = takeCommand().lower()#This will take command audio, convert it to text and return to string of audio
        # Here starts all logics to peform task..........
        
        if 'quit' in query or 'close' in query or "exit" in query or "close" in query:
            '''
            for closing the programm according to user's will
            '''
            print("closing the programm")
            speak("closing the programm")
            exit()


        elif 'shutdown the pc' in query or 'shut down' in query:
            '''
            this block is to shut down the PC instantly.|  say Yes to shut down , no for continue program 
            uses os.system("shutdown") funtion
            '''
            speak("do you really want to shut down your pc ?")
            print("do you really want to shut down your pc ?")
            x=takeCommand()
            if "yes" in x:
                speak("Shuting down the pc in 3 seconds")
                delayTime(4)
                os.system("shutdown /s /t 1")
            else:
                continue # restart the itration

        elif 'restart the pc' in query or 'reboot' in query:
            '''
            this block is to shut down the PC instantly and the restart.| say Yes to restart , no for continue program 
            uses os.system("shutdown") funtion
            '''
            speak("do you really want to re start your pc ?")
            print("do you really want to restart your pc ?")
            x=takeCommand()
            if "yes" in x:
                speak("rebooting the pc in 3 seconds")
                delayTime(4)
                os.system("shutdown /r /t 1")
            else:
                continue # restart the itration

        elif 'logout from' in query or 'logout' in query or 'logoff' in query:
            '''
            this block is to log out from windows user .| say Yes to log off  , no for continue program 
            uses os.system("shutdown-l") funtion
            '''
            speak("do you really want to logout ?")
            print("do you really want to logout ?")
            x=takeCommand()
            if "yes" in x:
                speak("logging off from the pc in 3 seconds")
                delayTime(4)
                os.system("shutdown -l")
            else:
                continue # restart the itration

        elif 'wikipedia' in query:
            speak("Searching wikipedia----------")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
            delayTime(2)
        
        elif 'on youtube' in query:
            query= query.replace(" ","+")
            searchString="https://www.youtube.com/results?search_query=" + query[6:query.find("on+youtube")]
            print(searchString)
            webbrowser.open_new_tab(searchString)
            speak("searching on youtube")
            
             
            #  to search on youtube , give string https://www.youtube.com/results?search_query=mk+gandhi
           
        elif 'on google' in query:
            speak("searching")
            query= query.replace(" ","+")
            searchString="https://www.google.co.in/search?q=" + query[6:query.find("on+google")]
            print(searchString)
            webbrowser.open_new_tab(searchString)
           
        elif 'on kora' in query:
            speak("searching")
            searchString="https://www.quora.com/search?q=" + query[6:query.find("on+kora")]+"&type=answer&time=day"
            print(searchString)
            webbrowser.open_new_tab(searchString)
            delayTime(5)

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")  
            delayTime(3)

        elif 'open kora' in query:
            speak("opening")
            webbrowser.open_new_tab("quora.com")
            delayTime(3)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open_new_tab("youtube.com") 
            delayTime(3)

        # to play music on pc 
        elif 'play music' in query or 'song' in query:
            music_dir="V:\\music_dir_python"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) # To play songs[0] 
            # The os.startfile() method allows us to “start” a file with its associated program. In other words, we can open a file with it’s associated program, just like when you double-click a PDF and it opens in Adobe Reader.
            delayTime(7)
      
        elif 'play video' in query or 'video' in query:
            video_dir="V:\\video_dir_python"
            video = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,video[0])) # To play video[0] 
            delayTime(7)
       
        elif "the time" in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is "+ strTime)
        
        elif 'date' in query:
            speak("Today's date is")
            x = datetime.datetime.now()
            dateStr=x.strftime("%d:%B:%Y")
            dayStr = x.strftime("%A")
            speak(dateStr+" and ")
            speak("Today is "+dayStr)
      
        elif 'wait for' in query or 'pause the' in query:
            delayTime(15)
      
        elif 'adhaar' in query or 'pritesh' in query:
                speak('opening document sir')
                targetPath = "C:\\pythontest\\Adhaar pritesh.jpg"
                os.startfile(targetPath)
                delayTime(5)
      
        elif "my computer" in query or 'this pc' in query:
            speak('opening my computer sir')
            targetPath = "C:\\pythontest\\This PC.lnk"
            os.startfile(targetPath)
            delayTime(5) 

        elif 'start' in query:
            if 'media player' in query:
                speak('opening media player sir')
                targetPath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
                os.startfile(targetPath)
                delayTime(5)
            elif 'paint' in query:
                speak('opening paint sir')
                targetPath = "C:\\pythontest\\Paint.lnk"
                os.startfile(targetPath)
                delayTime(5)
            elif 'code' in query:
                speak('opening Visual studio code sir')
                targetPath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                os.startfile(targetPath)
                delayTime(5)
            elif 'powershell' in query:
                speak('opening windows power shell sir')
                targetPath = "C:\\pythontest\\Windows PowerShell.lnk"
                os.startfile(targetPath)
                delayTime(5)
            elif 'whatsapp' in query:
                speak('opening whatsapp sir')
                targetPath = "C:\\pythontest\\WhatsApp.lnk"
                os.startfile(targetPath)
                delayTime(5)
            elif 'instagram' in query:
                speak('opening instagram sir')
                targetPath = "C:\\pythontest\\Instagram.lnk"
                os.startfile(targetPath)
                delayTime(5)
            elif 'recycle bin' in query:
                speak('opening recycle bin sir')
                targetPath = "C:\\pythontest\\Recycle Bin - Shortcut.lnk"
                os.startfile(targetPath)
                delayTime(5)
            
            elif 'word' in query:
                speak('opening libre office word sir')
                targetPath = "C:\\Program Files\\LibreOffice\\program\\swriter.exe"
                os.startfile(targetPath)
                delayTime(5)

        elif 'send email to' in query:

            
            try:
                speak("What should I write in email")
                content = takeCommand()
                to = "priteshalsh46@gmail.com" 
                sendEmail(to,content)
                speak("Email has been send successfully ")
                print("Email has been send successfully ")
            except Exception as e:
                print(e)
                speak("Sorry Email can't be sent right now")
       

        elif "take notes" in query or 'remember that' in query:
            ''' to store data in txt file on pc memory permanantly'''
            speak("Taking notes sir")
            data = takeCommand()
            speak("you said that "+ data)
            remember = open(".\\ai\\data.txt",'w')
            remember.write(data)
            remember.close()
            speak("notes stored in data.txt file sir , want to open that file?")
            x = takeCommand()
            if 'yes' in query:
                speak("opening data.txt file for you")
                targetPath = "C:\\Users\\pritesh\\Desktop\\Mtech\\python code practice\\ai\\data.txt"
                os.startfile(targetPath)
            else:
                speak("ok sir")
                continue
            
        elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save(r'C:\\Users\\pritesh\\Desktop\\Mtech\\python code practice\\ai\\screen.png')
            speak("screenshot saved. do you want to open it sir ?")
            x = takeCommand()
            if 'yes' in x:
                os.startfile("C:\\Users\\pritesh\\Desktop\\Mtech\\python code practice\\ai\\screen.png")
            else:
                speak("ok sir")

        elif ("cpu status") or ('status') or ("battery") in query:
            usage = psutil.cpu_percent()
            perCpu = str(usage)

            speak("CPU is at "+ perCpu +" percentage")
            x = psutil.sensors_battery()
            perBattery = str(x.percent)
            speak(" and battery is at "+ perBattery+" percent sir ")


        speak(" anything else?")
        x = takeCommand()
        if "no" in x: check = False
        else:
            check = True

                


        


print("prog completed!!")


            

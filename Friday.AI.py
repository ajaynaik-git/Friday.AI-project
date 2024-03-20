# Author & Source code details

# Author - Ajay A Naik
# About code - I have made a AI assistant called FRIDAY, it's inspired from the IRONMAN movie. 
# If you enjoyed using Friday AI & want to DM me just drop a message @ Linkedin (available in my git hub profile section)
# Total modules required - 7


# the following Python modules have been used
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import random


try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

# speak main function created
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greet():
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            print("Good Morning !")
            speak("Good Morning !")

        elif hour>= 12 and hour<18:
            print("Good Afternoon !")
            speak("Good Afternoon !") 

        else:
            print("Good Evening !")
            speak("Good Evening !")
        speak("I am FRIDAY, tell me how can I help you")


# pip install speechRecognition
# just for initial users
# if __name__=="__main__":
#     speak ("windows")


# calling the function
#  Usercommand function is for taking input from microphone & just returns us the string output.
        
    def UserCommand(): 
        r = sr.Recognizer()  
        with sr.Microphone() as source:
            
            print("Recognizing...")
            # MICROPHONE ADJUSTMENTS, you can even adjust
            r.pause_threshold = 1

            audio = r.listen(source) 
        try:
            print("Recognizing...")   
            query= r.recognize_google(audio, language ='en-in')

            print(f"User said: {query}\n")
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            return "None" 
        return query

    

    if __name__ == '__main__':
        greet()
        while True: 
            task = UserCommand().lower()
            if 'hello' in task:
                speak('Hi , I am Friday how can i help you')
            
            if "wikipedia" in task:
                speak("Searching wikipedia...")
                task = task.replace("wikipedia", "")
                results = wikipedia.summary(task,sentences =3)
                speak("According to wikipedia")
                print(results)
                speak(results)
                
          

            elif 'open youtube' in task:
                speak("Okay I am opening Youtube\n")
                webbrowser.open("https://www.youtube.com/")
    
            elif 'open music palyer' in task :
                speak('opening music player....')
                path = ("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
                os.startfile(path)

            elif 'open google' in task:
                speak("Okay I am opening Google\n")
                webbrowser.open("https://www.google.co.in/")
            
            elif 'open notepad' in task:
                speak('opening notepad for you.......')
                path = ("c:\\windows\\system32\\notepad.exe")
                os.startfile(path)

            elif 'close notepad' in task:
                speak('closing notepad wait.....')
                os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')
                
            elif 'open mail' in task:
                speak("Okay I am opening  mail\n")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
            elif 'open whatsaap' in task:
                speak("Okay I am opening whatsaap now\n")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open linkedin' in task:
                webbrowser.open("linkedin.com")

            elif 'time' in task:
                strTime= datetime.datetime.now().strftime("%I:%M:%S")
                # I have used %I for 12hr clock but if you want 24hr clock just replace %I with %H
                print(strTime)
                speak(strTime)
                
            elif 'play music' in task:
                music_files= os.listdir('C:\\Users\\Admin\\Music\\')
                selected_file= random.choice(music_files)
                os.startfile(os.path.join('C:\\Users\\Admin\\Music\\', selected_file))

                # music_files to check the directory & make sure to change the file path as per your device. 
                # selected_file for randomly palying a song, it's enjoyable right!
                # diff_song= random.choice(songs)
                

            elif 'the hindu' in task:
                webbrowser.open("https://www.thehindu.com/")
        
            elif 'live mint' in task:
                webbrowser.open("https://www.livemint.com/")
            
            elif 'stop' in task:
                speak("Thank you .....FRIDAY wishes you a good day")
                exit()
finally:
    print("Thank you .....FRIDAY wishes you a good day")
    
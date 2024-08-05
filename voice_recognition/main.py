import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser # это библиотека помогает открывать веб-браузер
import googletrans

import PyPDF2
engine  = pyttsx3.init()

def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()
is_running  = True
sayToMe("Меня зовут Gimi я ваш голосовой помощник слушаю вас")


record  = sr.Recognizer()
while is_running:
    try :
        with sr.Microphone(device_index=1) as source:
            print("Процесс начался . Можешь говорить что нибудь")
            audio = record.listen(source)
            res = record.recognize_google(audio, language="ru-RU")
            res = res.lower()
            print(res)
            if res   == "скажи время":
                current_time  = datetime.datetime.now()
                str_date  = "Сейчас {}:{}".format(str(current_time.hour), str(current_time.minute))
                print(str_date)
                sayToMe(str_date)
            elif res == "открой youtube":
                webbrowser.open("https://www.youtube.com/")
                sayToMe("Ютуб успешно открыт")
            elif "поиск в гугле" in res:
                query = res.replace("поиск в гугле", "")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                sayToMe(f"Вот что я нашел по запросу {query}")
            elif res == "пока":
                sayToMe("Рад был помочь до свидание")
                is_running = False


    except sr.UnknownValueError:
        print("Не могу понять вашу речь!!!")
    except sr.RequestError:
        print("Что то пошло не так :(")

res  = record.recognize_google(audio,language="ru-RU")

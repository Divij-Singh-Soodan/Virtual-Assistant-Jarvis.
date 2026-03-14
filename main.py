import speech_recognition as sr
import webbrowser
import pyttsx3
import time  # this is used to create a delay in the audio processing by the chatbot
import musicLibrary
import requests
import json




Jarvis_command = True 

# Recognizer and engine are initialized once at the top
recogniser = sr.Recognizer() # accepts audio input and converts it into machine code logic.
engine= pyttsx3.init()  # processes accepted audio output to computer audio format using logics and definitions as per defined in the ttsx3 engine of the python library,
news_API = '24f832d7fc3840b2af04c91c126c6beb'
# assistant engine



def speak(text):
    engine.say(text)
    engine.runAndWait()


def AIProcess(command):
    client = OpenAI(
        api_key = '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'

    )

    completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'system', 'content':'you are a virtual assistant named jarvis in general tasks like alexa and Google'},
        {'role': 'user', 'content':command}
    ]
    )

    return completion.choices[0].message.content



def processCommand(c): #process user voice command and take action
    if 'open google' in c.lower():
        speak('Opening Google')
        webbrowser.open('https://www.google.com')
    

    elif 'open facebook' in c.lower():
        speak('Opening Facebook')
        webbrowser.open('https://www.facebook.com')


    elif 'open youtube' in c.lower():
        speak('Opening YouTube')
        webbrowser.open('https://www.youtube.com')


    elif 'open netflix' in c.lower():
        speak('Opening Netflix')
        webbrowser.open('https://www.netflix.com')
    


    elif 'stop' in c.lower() or 'exit' in c.lower():
        global Jarvis_command # declaring jarvis command as the global variable for evaluation of the program.
        speak('Goodbye!')
        Jarvis_command = False


    elif c.lower().startswith('play'):
        song = c.lower().split('')[1]
        link = musicLibrary.music(song)# split will only identify the key of the dictionary made in music library
        webbrowser.open(link) # using webbrowser built in function to open a link in browser. 
        musicLibrary.music[song] 



    elif 'news' in c.lower():
        news_site_url = f'https://newsapi.org/docs/endpoints/top-headlines?country=in&apiKey={news_API}'
        response= requests.get(news_site_url)
        if response.status_Code:
            data = response.json  #Json data is converted into python understandable format

            articles = data.get('articles', []) # json converted data is accessed

            for article in articles: # displays the articles accepted from the server using the API key.
                speak(article['title'])# voice assistant will speak the news article.



    else:
         #integrating OpenAI with this virtual assistant using API for intelligent responses
         output = AIProcess(c)
         speak(output) #Open AI models will be used to process this code for handling user requests using API
 



        




if __name__ == '__main__':
    speak('Initializing Jarvis.......')
    

    while Jarvis_command:
        r=sr.Recognizer()
        print('----Recognizing Voice-----')
        

        try:
            with sr.Microphone() as source: # here source refers to the microphone
                r.adjust_for_ambient_noise(source)
                print('Listening for wake word.....')
                
                
                audio = r.listen(source, phrase_time_limit=3)

                wake_word = r.recognize_google(audio)
                print(f"Heard: {wake_word}")


                
                if 'jarvis' in wake_word.lower(): # Check for 'jarvis' in the phrase
                    speak('Yes. How can I help you')
                    
                    # Listen for command
                    with sr.Microphone() as source:
                        # 🌟 BEST PRACTICE: Adjust noise again before listening for the command
                        r.adjust_for_ambient_noise(source) 
                        print('Jarvis is active... Listening for command.')
                        
                    
                        audio = r.listen(source, phrase_time_limit=8) 
                        command = r.recognize_google(audio)
                        print(f"Command: {command}")
                        
                        processCommand(command)


        
        except sr.WaitTimeoutError:
            # Silence this common error to keep the console clean
            pass 

        except sr.UnknownValueError:
            # Handle cases where Google couldn't understand the audio
            # print("Google Speech Recognition could not understand audio")
            pass
        except Exception as e:
            # Handle all other exceptions
            print('An error occurred: {0}'.format(e))
            time.sleep(1) # Small delay to prevent rapid-fire errors

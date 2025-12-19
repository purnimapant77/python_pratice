import pyaudio 
import speech_recognition as sr
import pyttsx3 as p

'''def list_microphones():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Michrophone index :{index} available: {name}")'''

def text_to_audio():
    try:
        text=input("Please enter your text you want to convert into audio:")
        print("Listennnnnn..........")
        voice=p.init()
        voice.setProperty('rate',150) # 150 words per minute
        voice.setProperty('volume',0.8) #it lies between 0.0 to 1.0
        voice.say(text)
        voice.runAndWait()
    except Exception as e:
        print("Error:",e)

def audio_to_text():
    r=sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:
           # print(f"current michrophone is: {device_index}")
            #s=int(input("For how much seconds you want to speak:"))
            input("Press 'Enter' to speak 😊")
            print(f"Listening.........")
            r.pause_threshold=2
            audio=r.listen(source)
            print("Audio captured 😅")
            print("Reconizing your voice 🤔.....")
            text=r.recognize_google(audio)
            print(f"you said: '{text}'")
    except Exception as e:
        print("Error:",e)

def main():
    print("**********😎😎😆😎😎**********")
    print("******i'm voice assistant*****")
    while True:
        print("\nText to Audio: 1\nAudio to Text: 2\nExit: any other key")
        choice=input("\nEnter your choice:")
        if choice=="1":
            text_to_audio()
        elif choice=="2":
            audio_to_text()
        else:
            print("...Program exiting...")
            print("bye😥bye...")
            exit(0)
    
if __name__=="__main__":
    main()
    
    

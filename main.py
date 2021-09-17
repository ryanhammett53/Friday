
    # Import libraries
    
    Import speech_recognition as sr
   
    r = sr.Recognizer()
    
    # Get the defaul Microphone
    with sr.Microphone() as source:
        # Listen to a command, using AVD
        
        while True:
            audio = r.listen (source)
            
            text = r.recognize_google(audio)
            
            print(text)
            
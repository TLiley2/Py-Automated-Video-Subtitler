import moviepy.editor as mp

# Video file path
#filePath=r"C:\Users\tnu20\Downloads\sub\How to Say ‘HELLO’ in Spanish¿ ¦ How to Pronounce Hola¿\How to Say ‘HELLO’ in Spanish_ _ How to Pronounce Hola_ 720.mp4"

def suber(filePath):
    # .wav file path
    w = ".mp4"
    res = filePath.split(w, 1)
    filePathmin = res[0] if len(res) > 1 else ""
    wavFile=filePathmin+".wav"

    # Insert Local Video File Path 
    clip = mp.VideoFileClip(filePath)

    # Duration of video (in seconds)
    duration = clip.duration 
    print(duration)

    # Coverts clip to .wav audio file
    clip.audio.write_audiofile(wavFile)

    # Subtitle counter
    counter = 0

    import speech_recognition as sr
    r = sr.Recognizer() 
    jackhammer = sr.AudioFile(wavFile)
    with jackhammer as source:
        r.adjust_for_ambient_noise(source)

        # Records file for 2 seconds at a time (1)
        roc=int(duration)/2

        elapsed_time = 0.0

        # Open subtitle file
        subName=filePathmin+".srt"
        file = open(subName, "w") 

        for x in range(int(roc)):

            # Calculate hours, minutes, seconds, and milliseconds
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time * 1000) % 1000)

            # Records file for 2 seconds at a time (2)
            audio = r.record(source, duration=2)
            
            # Clock counter format
            f=f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

            # Orders the subtitles
            counter+=1        
            print(counter)
            file.write(str(counter) + "\n")

            # ptints tinme stamps
            elapsed_time += 2
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time * 1000) % 1000)
            v=f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
            print(f+" --> "+v)
            file.write(str(f)+" --> ")
            file.write(str(v) + "\n")

            # Prints transcribed text
            try:
                MyText = r.recognize_google(audio, language='en-US')
                MyText = MyText.capitalize()
                print(MyText + "\n")
                file.write(str(MyText) + "\n")
                file.write("\n") 
            # If no voice is deteched
            except sr.UnknownValueError:
                print("." + "\n")
                file.write("." + "\n")
                file.write("\n")
    file.close()

    # Deletes temporary .wav file
    import os
    os.remove(wavFile)


import pyttsx3


def Change():
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    print("The current Speech is just a reference Speech to check the Changes and The original file is still innact")
    engine.say("\n                    ")
    engine.say("\nThis is a testing Speech and chnages done here will be updated in your main Speech file.")
    engine.runAndWait()
    while True:
        engine.say("\n                    ")
        engine.say("\nWhat would you like to change? Gender or Speed")
        engine.runAndWait()
        ch2 = input("What would you like to change?\n1.Voice Gender\n2.Voice Speed\n3.Back:\n")
        if ch2 == '1':
            engine.say("\nWhich will it be Male or Female?")
            engine.runAndWait()
            voice_ch = int(input("1.Female\n2.Male:\n"))
            if voice_ch == 1:
                engine.setProperty('voice', voices[1].id)
                engine.say("\n                    ")
                engine.say("\nhello hello hello im the most sexy ai")
                engine.runAndWait()
            else:
                engine.setProperty('voice', voices[0].id)
                engine.say("\n                    ")
                engine.say("\nhello hello hello im the most sexy ai")
                engine.runAndWait()
        elif ch2 == '2':
            engine.say("\n                    ")
            engine.say("\nSelect the voice Speed between 100 to 200. ")
            engine.runAndWait()
            range = int(input("Select a voice Speed between 100 to 200:\n"))
            engine.setProperty('rate',range)
            engine.say("\n                    ")
            engine.say("\nhello hello hello im the most sexy ai")
            engine.runAndWait()
        else:
            break


def Download():
    engine.say("\n                    ")
    engine.say("\nWhat would you like to name this audio file?")
    engine.runAndWait()
    name = input("Enter the name of the audio file:\n")
    print("Downloading....")
    engine.save_to_file(data, name+".mp3")
    engine.runAndWait()


# main program Starts
engine = pyttsx3.init()

engine.say("\n        Welcome            ")
engine.say("\n \nWelcome , How may i help you?")
engine.say("\n. Enter the name of the text file.")
engine.runAndWait()
while True:
    try:
        file_name = input("Enter the name of the file(Excluding the extension) \n")
        file = open(file_name+".txt")
        data = file.read()
        break
    except:
        engine.say("\n            Sorry       ")
        engine.say("\n\n, but no such files were found. Please Re-enter the name!.")
        engine.say("\nSending Back!")
        engine.runAndWait()

while True:
    engine.say("\n                    ")
    engine.say("\nSelect the following.")
    engine.runAndWait()
    select = input("Select the Following:\n1.make changes\n2.Create the Mp3 file:\n3.Exit\n")
    if select == "1":
        Change()
        engine.say("\n                    ")
        engine.say("\nWould you like to hear the converted Speech? ")
        engine.runAndWait()
        ch = input("Would you like to hear the converted Speech?(y/n)\n") 
        if ch == 'y' or ch == 'yes':
            engine.say(data)
            engine.runAndWait()
        else:
            pass
    elif select =='2':
        Download()
        print("Download Completed")
        engine.say("\n                    ")
        engine.say("\nThe file has been downloaded successfully.")
        engine.runAndWait()
    else:
        engine.say("\n                 ")
        engine.say("\nIt was good Meeting you. TakeCare!\nbye . ")
        engine.runAndWait()
        break





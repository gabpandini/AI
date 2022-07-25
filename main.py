import pyttsx3


def main():
    engine = pyttsx3.init()
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    while True:
        words = input("Say something: ").lower()

        if words != "bye":
            if "hi" in words or "hello" in words:
                engine.say("Hi to you too")
                engine.runAndWait()
            elif "how are" in words or "doing" in words:
                engine.say("I'm fine, thanks!")
                engine.runAndWait()
            elif "morning" in words:
                engine.say("Good morning! Have a nice day")
                engine.runAndWait()
            else:
                engine.say("Hum?")
                engine.runAndWait()
        else:
            engine.say("Bye to you too")
            engine.runAndWait()
            break

main()

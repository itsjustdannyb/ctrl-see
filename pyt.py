import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id) # Male Voice
engine.setProperty('voice', voices[1].id)# Female Voice

'''engine.say(
    'Hello World!'
    'My current speaking rate is '
    'my Name is Arinde David'
)'''

dave = 'Help'

engine.say(dave)
engine.runAndWait()
engine.stop()
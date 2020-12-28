from upm import pyupm_buzzer as upmBuzzer
buzzer = upmBuzzer.Buzzer(5)
buzzerVolume = 0.125
buzzer.setVolume(0)

notes = { "X1": 1010, # 990Hz
          "X2": 1133, # 882Hz
          "X3": 847, # 1180Hz
          "X4": 1250, # 800Hz
          "X5": 1052, # 950Hz
          "X6": 1280, # 780Hz
          "X7": 1333, # 750Hz
          "X8": 1052, # 950Hz
         }
def playGTA():
    tempo = 60 * 1000
    pager = [("X1", 5), ("X1", 5), ("X1", 1), (" ", 4),
             ("X2", 2), ("X1", 2), ("X3", 2), ("X1", 2), (" ", 2),
             ("X2", 2), ("X1", 5), (" ", 4),
             ("X4", 2), (" ", 2),
             ("X6", 5), ("X4", 1), (" ", 1),
             ("X7", 5), ("X7", 5), ("X7", 1), (" ", 1),
             ("X2", 5), ("X5", 5)]
    playMelody(pager, tempo)

def playMelody(melody, tempo):
    buzzer.setVolume(buzzerVolume)
    for m in melody:
        note, beat = m
        if note == " ":
            buzzer.setVolume(0.0)
            buzzer.playSound(1000, beat * tempo)
            buzzer.setVolume(buzzerVolume)
        else:
            buzzer.playSound(notes[note], beat * tempo)
        # add a bit of trailing break
        buzzer.setVolume(0.0)
        buzzer.playSound(1000, int(0.1 * tempo))
        buzzer.setVolume(buzzerVolume)


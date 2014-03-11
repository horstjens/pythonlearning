# python
# sebastian
# kleines grafikadventure

import easygui
import random

gesundheit = 50
runde = 1
raum=1
#         0       1
hofliste=["menu", "Karren", "Turm", "Misthaufen", "Kuhstall",
          "Ausgang", "Brennholzlager"]
ustunde = {
                 1:"19",
                 2:"9",
                 3:"10",
                 4:"14",
                 5:"15",
                 6:"17"}
uminute = {
                 1:"35",
                 2:"45",
                 3:"55",
                 4:"10",
                 5:"15",
                 6:"20"}
positionwache=5         
positionspieler = 2
positionspieleralt = 2
bild = "9-15.gif"

# scene
# gefangener wacht auf (spielfigur) sieht betrunkenen wächter muss etwas 
#auswählen und schleicht vorbei
t1="""Du wachst in einer dunklen graußige schleimig Zelle auf und siehst einen schlafenden Wächter neben der Zelle. 
An seinem lockeren umgebundenen Gürtel siehst du einen Schlüsselbund. Du solltest aus der Zelle 
herauskommmen ,aber leise.
Was  willst du nun tun?"""
b1=["Menü", "Schlüssel stehlen", "Mit Wächter reden", "Zellentür untersuchen", "Zellenfenster untersuchen"]
#bild zeichnen zu Vorgang
txt=""
while gesundheit >0 and raum>0:
    while raum == 1 and gesundheit > 0:
        status = "Runde: {} Gesundheit: {}%".format(runde, gesundheit)
        a1=easygui.buttonbox(t1, status, b1)
        if a1=="Schlüssel stehlen":
            gesundheit-=random.randint(1,15)
            #status = "Runde: {} Gesundheit: {}%".format(runde, gesundheit)
            t2="""Du warst unvorsichtig und der Wächter ist aufgewacht.
Der wirft mit Steinen auf dich. Deine Gesundheit sinkt"""
            easygui.msgbox(t2, status)
        elif a1=="Mit Wächter reden":
            t2="""Der Wächter wacht müde auf und schreit:'Lass mich in Ruhe'
und wirft mit Müll auf dich"""
            easygui.msgbox(t2)
        elif a1=="Zellentür untersuchen":
            t2="Du findest in einer Ecke ein Stück Draht und knackst damit die Türe."
            easygui.msgbox(t2)
            raum=2
        elif a1=="Zellenfenster untersuchen":
            t2="""Du kannst zwar durch das Fenster durch aber es ist zu hoch.
Du kommst nicht runter."""
            easygui.msgbox(t2)
        elif a1== "Menü":
            raum = -1   
        runde += 1
    # ---------- raum 2 ---------------
    if gesundheit <= 0:
        easygui.msgbox("du stirbst an deinen Wunden. Game Over")
        raum = -1


    while gesundheit>0 and  raum==2:
        #
        
        
        status = "Runde: {}gesundheit: {}%".format(runde, gesundheit)
        #weg mit einem wächter einem misthaufe, 1 karren, 1lager, eine kuh, burgtor,
        #ausgang vom knastturm einen weg gerader aus durch, misthaufen und so in ecken
        text = """Du siehst einen Burghof. im Uhrzeigersinn gibt es
{}, {}, {},{}, {}, {} mögliche Verstecke.
               
Du selbst befindest Dich im {}
Der einzige Wächter untersucht gerade {}
               
Wo willst Du Dich vor ihm verstecken?""".format(hofliste[1],
                hofliste[2], hofliste[3], hofliste[4], hofliste[5],
                hofliste[6], hofliste[positionspieler],
                hofliste[positionwache])
        versteckliste = []
        versteckliste.append(hofliste[positionspieler])
        if positionspieler == 1:
            versteckliste.append(hofliste[2])
            versteckliste.append(hofliste[6])
        elif positionspieler == 6:
            versteckliste.append(hofliste[5])
            versteckliste.append(hofliste[1])
        else:
            versteckliste.append(hofliste[positionspieler-1])
            versteckliste.append(hofliste[positionspieler+1])
        a2=easygui.buttonbox(text, status, versteckliste, bild)
        if a2=="menu":
            raum = -1
        else:
            text = "Du versuchst, dein Versteck zu wechseln\n"
            positionwache += random.randint(-1,1)
            if positionwache > len(hofliste)-1:
                positionwache = 1 # erstes versteck, weil 0 = menü
            elif positionwache <1:
                positionwache = len(hofliste)-1
            # die wache untersucht jetzt ein gültiges Versteck
            print("wachepos:", positionwache)
            text += "Die Wache untersucht den {}\n".format(hofliste[positionwache])
            positionspieleralt = positionspieler
            positionspieler = hofliste.index(a2)
            #positionspieler = a2       
            text += "Du versteckst Dich im {}\n".format(hofliste[positionspieler])
            if positionspieler==positionwache:
                text += "Die Wache findet dich und verprügelt dich\n"
                gesundheit-=20
                if gesundheit>0:
                    raum=1
                    
                    text+="Du wirst zurück in die Zelle geworfen\n"
            elif positionspieler == 5: # Ausgang
                text+="Du hast es geschafft und verlässt die Burg!\n"
                raum=3
            

            bild = ustunde[positionspieler]+"-"+uminute[positionwache]+".gif"
            easygui.msgbox(text,status, "weiter...", bild)
    # nicht mehr im burghof
    positionwache = 5   # für den nächsten ausbruchversuch
    positionspieler = 2
    if raum==3:
       txt="""Du bist aus der Burg etkommen ,aber
wirst von einem PacMan gefressen!!!Du wirst langsam verdaut!!!"""

    while gesundheit>0 and raum==3:
        
        a3=easygui.buttonbox(txt, status, ["Nichts tun", 
                 "singen", "suchen"])
        gesundheit-=1
        status = "Runde: {}gesundheit: {}%".format(runde, gesundheit)
        runde += 1 
        if a3=="Nichts tun":
          txt="Du wirst ein bischen schneller verdaut"
          gesundheit-=3
        elif a3=="singen":
            txt="""Dem PacMan wird von deinem Gesang übel.
Er versucht dich auszukotzen."""
            if random.random()<=0.4:
                txt+=".Du wirst ausgekotzt"
                raum=4
            else:
                txt+=""".Leider schafft es PacMan
nicht dich auszukotzten.Du bleibst im Magen."""
        elif a3=="suchen":
            txt="Du suchst nach Essen oder einer Waffe im Magen"
            if random.random()<=0.3:
                txt+=".Du findest ein Schwert und tötest PacMan "
                raum=4
            elif random.random()<=0.5:
                txt+=""".Du findest ein biscchen noch unverdautes.
Ein Teil deiner gesundheit wird wieder hergestellt."""
                gesundheit+=10
    if raum == 4:
        break
txt += "\n Game Over"
easygui.msgbox(txt)
#
# python
# sebastian
# kleines grafikadventure

import easygui
import random

gesundheit = 50
runde = 1
raum=1
#         0       1
hofliste=["menu", "Karren", "Turm", "Misthaufen", "Kuhstall",
          "Ausgang", "Brennholzlager"]
ustunde = {
                 1:"19",
                 2:"9",
                 3:"10",
                 4:"14",
                 5:"15",
                 6:"17"}
uminute = {
                 1:"35",
                 2:"45",
                 3:"55",
                 4:"10",
                 5:"15",
                 6:"20"}
positionwache=5         
positionspieler = 2
positionspieleralt = 2
bild = "9-15.gif"

# scene
# gefangener wacht auf (spielfigur) sieht betrunkenen wächter muss etwas 
#auswählen und schleicht vorbei
t1="""Du wachst in einer dunklen graußige schleimig Zelle auf und siehst einen schlafenden Wächter neben der Zelle. 
An seinem lockeren umgebundenen Gürtel siehst du einen Schlüsselbund. Du solltest aus der Zelle 
herauskommmen ,aber leise.
Was  willst du nun tun?"""
b1=["Menü", "Schlüssel stehlen", "Mit Wächter reden", "Zellentür untersuchen", "Zellenfenster untersuchen"]
#bild zeichnen zu Vorgang
txt=""
while gesundheit >0 and raum>0:
    while raum == 1 and gesundheit > 0:
        status = "Runde: {} Gesundheit: {}%".format(runde, gesundheit)
        a1=easygui.buttonbox(t1, status, b1)
        if a1=="Schlüssel stehlen":
            gesundheit-=random.randint(1,15)
            #status = "Runde: {} Gesundheit: {}%".format(runde, gesundheit)
            t2="""Du warst unvorsichtig und der Wächter ist aufgewacht.
Der wirft mit Steinen auf dich. Deine Gesundheit sinkt"""
            easygui.msgbox(t2, status)
        elif a1=="Mit Wächter reden":
            t2="""Der Wächter wacht müde auf und schreit:'Lass mich in Ruhe'
und wirft mit Müll auf dich"""
            easygui.msgbox(t2)
        elif a1=="Zellentür untersuchen":
            t2="Du findest in einer Ecke ein Stück Draht und knackst damit die Türe."
            easygui.msgbox(t2)
            raum=2
        elif a1=="Zellenfenster untersuchen":
            t2="""Du kannst zwar durch das Fenster durch aber es ist zu hoch.
Du kommst nicht runter."""
            easygui.msgbox(t2)
        elif a1== "Menü":
            raum = -1   
        runde += 1
    # ---------- raum 2 ---------------
    if gesundheit <= 0:
        easygui.msgbox("du stirbst an deinen Wunden. Game Over")
        raum = -1


    while gesundheit>0 and  raum==2:
        #
        
        
        status = "Runde: {}gesundheit: {}%".format(runde, gesundheit)
        #weg mit einem wächter einem misthaufe, 1 karren, 1lager, eine kuh, burgtor,
        #ausgang vom knastturm einen weg gerader aus durch, misthaufen und so in ecken
        text = """Du siehst einen Burghof. im Uhrzeigersinn gibt es
{}, {}, {},{}, {}, {} mögliche Verstecke.
               
Du selbst befindest Dich im {}
Der einzige Wächter untersucht gerade {}
               
Wo willst Du Dich vor ihm verstecken?""".format(hofliste[1],
                hofliste[2], hofliste[3], hofliste[4], hofliste[5],
                hofliste[6], hofliste[positionspieler],
                hofliste[positionwache])
        versteckliste = []
        versteckliste.append(hofliste[positionspieler])
        if positionspieler == 1:
            versteckliste.append(hofliste[2])
            versteckliste.append(hofliste[6])
        elif positionspieler == 6:
            versteckliste.append(hofliste[5])
            versteckliste.append(hofliste[1])
        else:
            versteckliste.append(hofliste[positionspieler-1])
            versteckliste.append(hofliste[positionspieler+1])
        a2=easygui.buttonbox(text, status, versteckliste, bild)
        if a2=="menu":
            raum = -1
        else:
            text = "Du versuchst, dein Versteck zu wechseln\n"
            positionwache += random.randint(-1,1)
            if positionwache > len(hofliste)-1:
                positionwache = 1 # erstes versteck, weil 0 = menü
            elif positionwache <1:
                positionwache = len(hofliste)-1
            # die wache untersucht jetzt ein gültiges Versteck
            print("wachepos:", positionwache)
            text += "Die Wache untersucht den {}\n".format(hofliste[positionwache])
            positionspieleralt = positionspieler
            positionspieler = hofliste.index(a2)
            #positionspieler = a2       
            text += "Du versteckst Dich im {}\n".format(hofliste[positionspieler])
            if positionspieler==positionwache:
                text += "Die Wache findet dich und verprügelt dich\n"
                gesundheit-=20
                if gesundheit>0:
                    raum=1
                    
                    text+="Du wirst zurück in die Zelle geworfen\n"
            elif positionspieler == 5: # Ausgang
                text+="Du hast es geschafft und verlässt die Burg!\n"
                raum=3
            

            bild = ustunde[positionspieler]+"-"+uminute[positionwache]+".gif"
            easygui.msgbox(text,status, "weiter...", bild)
    # nicht mehr im burghof
    positionwache = 5   # für den nächsten ausbruchversuch
    positionspieler = 2
    if raum==3:
       txt="""Du bist aus der Burg etkommen ,aber
wirst von einem PacMan gefressen!!!Du wirst langsam verdaut!!!"""

    while gesundheit>0 and raum==3:
        
        a3=easygui.buttonbox(txt, status, ["Nichts tun", 
                 "singen", "suchen"])
        gesundheit-=1
        status = "Runde: {}gesundheit: {}%".format(runde, gesundheit)
        runde += 1 
        if a3=="Nichts tun":
          txt="Du wirst ein bischen schneller verdaut"
          gesundheit-=3
        elif a3=="singen":
            txt="""Dem PacMan wird von deinem Gesang übel.
Er versucht dich auszukotzen."""
            if random.random()<=0.4:
                txt+=".Du wirst ausgekotzt"
                raum=4
            else:
                txt+=""".Leider schafft es PacMan
nicht dich auszukotzten.Du bleibst im Magen."""
        elif a3=="suchen":
            txt="Du suchst nach Essen oder einer Waffe im Magen"
            if random.random()<=0.3:
                txt+=".Du findest ein Schwert und tötest PacMan "
                raum=4
            elif random.random()<=0.5:
                txt+=""".Du findest ein biscchen noch unverdautes.
Ein Teil deiner gesundheit wird wieder hergestellt."""
                gesundheit+=10
    if raum == 4:
        break
txt += "\n Game Over"
easygui.msgbox(txt)

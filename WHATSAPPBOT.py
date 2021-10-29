import pywhatkit
from pywhatkit.main import sendwhatmsg_instantly, sendwhatmsg_to_group, sendwhats_image
import pyttsx3


speaker = pyttsx3.init()


speaker.say('Hello sir,I am Whatsapp Bot..How Can I Help You..please select from the following')
speaker.runAndWait()
while True:
    print('Hello sir,I am WhAtsupp Bot..How Can I Help You..please select from the following-->')
    print('''
    1.Send instant message to someone.
    2.send scheduled message to someone.
    3.Send group message.
    4.EXIT....''')
    try:
        speaker.say('PLEASE ENTER THE NUMBER OF THE COMMAND.')
        speaker.runAndWait()
        userinput = int(input('PLEASE ENTER THE NUMBER OF THE TASK-->\n'))
        

        if userinput==1:
            speaker.say('PLEASE ENTER THE MOBILE NUMBER INCLUDING COUNTRY CODE.')
            speaker.runAndWait()
            number = str(input('PLEASE ENTER THE MOBILE NO(including country code).--->\n'))
            speaker.say('TYPE THE MESSAGE.')
            speaker.runAndWait()
            message = str(input('ENTER THE MESSAGE--->\n'))
            speaker.say('SENDING MESSAGE..PLEASE WAIT FOR 30 SECONDS..NOTE - WHATSAPP WILL AUTOMATICALLY CLOSE AFTER SENDING MESSAGE')
            speaker.runAndWait()
            pywhatkit.sendwhatmsg_instantly(number,message,30,True,10)
        elif userinput==2:
            speaker.say('PLEASE ENTER THE MOBILE NUMBER INCLUDING COUNTRY CODE')
            speaker.runAndWait()
            number = str(input('PLEASE ENTER THE MOBILE NO(including country code).--->\n'))
            speaker.say('TYPE THE MESSAGE.')
            speaker.runAndWait()
            message = str(input('ENTER THE MESSAGE--->\n'))
            speaker.say('ENTER TIME IN 24 HOUR FORMAT.')
            speaker.runAndWait()
            hour = int(input('PLEASE ENTER HOUR(in 24hr format)---->\n'))
            min = int(input('PLEASE ENTER MINUTES---->\n'))
            speaker.say('YOUR MESSAGE IS SCHEDULED..NOTE - WHATSAPP WILL AUTOMATICALLY CLOSE AFTER SENDING MESSAGE')
            speaker.runAndWait()
            pywhatkit.sendwhatmsg(number,message,hour,min,30,True,10)

        elif userinput==3:
            speaker.say('ENTER GROUP CODE, YOU WILL FIND IT IN GROUP INVITE LINK.')
            speaker.runAndWait()
            Gcode = str(input('PLEASE ENTER THE GROUP CODE--->\n'))
            speaker.say('TYPE THE MESSAGE.')
            speaker.runAndWait()
            message = str(input('ENTER THE MESSAGE--->\n'))
            speaker.say('ENTER TIME IN 24 HOUR FORMAT.')
            speaker.runAndWait()
            hour = int(input('PLEASE ENTER HOUR(in 24hr format)---->\n'))
            min = int(input('PLEASE ENTER MINUTES---->\n'))
            speaker.say('YOUR MESSAGE IS SCHEDULED..NOTE - WHATSAPP WILL AUTOMATICALLY CLOSE AFTER SENDING MESSAGE')
            speaker.runAndWait()
            pywhatkit.sendwhatmsg_to_group(Gcode,message,hour,min,30,True,10)
        elif userinput==4:
            break
        else:
            speaker.say('WARNING! PLEASE ENTER VALID NUMBER')
            speaker.runAndWait()
            print('WARNING!!!--PLEASE ENTER VALID NUMBER--')
            
    except:
        speaker.say('WARNING! PLEASE ENTER VALID NUMBER')
        speaker.runAndWait()
        print('WARNING!!!--PLEASE ENTER VALID NUMBER--')


speaker.say('come again ,have a nice day')
speaker.runAndWait()
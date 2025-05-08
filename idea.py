
import textwrap
import re
tuple_month = ("January","February","March","April","May","June","July","August","September","October","November","December","Undecimber")
tuple_monthflavour = ("January marks the dawn of a new year. May yours be fruitful.","February, from the Latin \'februum\' - purification.","March, named Martius by the Ancient Romans afer Mars, their god of war.","It is suggested that April was sacred to the goddess Venus.","May was named for the Greek goddess Maia.","June flavour text","July flavour text","August flavour text","September flavour text","October flavour text","Novembe flavour text","December flavour text","Undecimber flavour text")
tuple_week = ("Week 1","Week 2","Week 3","Week 4")
tuple_year = ("Year 1","Year 2","Year 3","Year 4")
tuple_dateerifics = ("st","nd","rd","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","th","st","nd","rd","th","th","th","th","th")
tuple_banned = ("fuck","shit","bastard")
week_number = 0
current_week = 0
current_month = 0
current_year = 0

text_nocodex = "/'dulce et decorum est pro officium mori/' - There is no codex."
text_incodex_sin = " is a part of the codex."
text_incodex = "are all a part of the codex."
text_incodex_two = "are both a part of the codex."
text_outcodex_sin = " is no longer a part of the codex."
text_outcodex = " are no longer a part of the codex."
text_abscodex = " will be absent from the codex."
text_assignedto = " assinged to "
text_complied =  ": complied."
text_notcomplied = ": did not comply."
text_hello = "Hello, "
text_welcome = "Welcome, "
text_iic = "It is currently "
text_joined = "is part of the codex."
text_invalid = "Invalid answer."
text_trya = "Please try again."
text_redo = "Okay, let's try again."
text_dateinvalid = "The Codex operates on a 13-month format."
text_messfrom = "> MESSAGE FROM: "
text_messject = "** SUBJECT: "
text_remessject = "** SUBJECT: RE: "
text_fwmessject = "** SUBJECT: FW: "
text_blankmess = "**BLANK MESSAGE**"
text_noassigned = "**NONE ASSIGNED**"
text_banner = "~~~~~~~~~~~~~~~~~~~~~"
text_minibanner = "~~~~~~~~"
prompt_reply= "INPUT: "
prompt_assigntask = "Assign task to "

tab = "    "
tab2 = "            "
user_censored =  True

def inputreply(x): #x must be +ve integer (number of poss options)
    doneflag = False
    while doneflag == False:
        rawinput = input(prompt_reply)
        inputted = rawinput.strip()
        if inputted.isdigit():
            try:
                inty = int(inputted)
            except TypeError:
                print(text_invalid)
            except:
                print(text_invalid)
            if inty > 0 and inty != 0 and inty <= x:
                doneflag = True
                return inty
            else:
                print(text_invalid)
        else:
            print(text_invalid)

def weekpass():
    global current_week
    global current_month
    global current_year
    global week_number
    current_week = current_week + 1
    week_number = week_number + 1
    if current_week == 4:
        current_month = current_month + 1
        current_week = 0
    if current_month == 13:
        current_year = current_year + 1
        current_month = 0       

def printtime():
    if current_week == 0:
        print(tuple_monthflavour[current_month])
    current_time = ((tuple_week[current_week]) + " of " + (tuple_month[current_month]) + ", " + (tuple_year[current_year]))
    print(text_iic + current_time + ".")

def printcen(x):
    if user_censored == True:
        for word in tuple_banned:
            if word.casefold() in x:
                x = x.replace (word.casefold(), "#"*len(word))
                continue
            else:
                continue
        print(x)
    else:
        print(x)


class People:
    def __init__ (self, name,hatebool,points):
        self.name = name
        self.hatebool = hatebool
        self.points = points

class Email:
    def __init__(self, sender, to, subj, body, resp, respcont,fin):
        self.sender = sender
        self.to = to
        self.subj = subj
        self.body = body
        self.resp = resp
        self.respcont =  respcont
        self.fin = fin

    def mail(self):
        print(text_banner)
        printcen("> MESSAGE FROM: %s to %s" % (self.sender,self.to))
        y = textwrap.shorten("** SUBJECT: %s" % self.subj, width=40, placeholder="[...]")
        print(y)
        printcen("< %s >" % self.subj)
        printcen("     %s" % self.body)
        if len(self.resp) > 1:
            print("          RESPOND >>")
            y = 1
            for r in self.resp:
                print("              " + str(y) + ": %s" % r)
                y = y+1
            number = inputreply(len(self.resp))
            indy = number - 1
            print(text_minibanner)
            printcen(">> MESSAGE TO: %s" % self.sender)
            f = textwrap.shorten("** SUBJECT: RE: %s" % self.subj, width=40, placeholder="[...]")
            print(f)
            printcen("<RE: %s >" % self.subj)
            printcen("    >> %s" % self.resp[indy] + self.respcont[indy])
            print(text_minibanner)
            printcen("> MESSAGE FROM: %s to you" % (self.sender))
            f = textwrap.shorten("** SUBJECT: RE: RE: %s" % self.subj, width=40, placeholder="[...]")
            print(f)
            printcen("<RE: RE: %s >" % self.subj)
            printcen("     %s" % self.fin[indy])
            print(text_banner)
            if number == 3:
                return True
            else:
                return False
        else:
            print(text_banner)



car = People("Caroline Jenkins",False, 10)
lin = People("Linda Webber", False, 10)
ste = People("Steven Lau", False, 10)
hrd = People("HR Department",False,10)


h_e1 = Email(hrd.name,"you","Automated message", "Thank you for your email. We will respond to your request shortly.","N","N","N")

c_e1 = Email(car.name,"all","Sick to bastard death of this","If you ate my fucking tomato sandwich from the work fridge I'm coming for you and your firstborn.",
           ("I'm really sorry to hear this, Caroline.","This is a disturbing email to receive.","I was the one who ate it, you miserable cow."),
           (" I would suggest contacting our manager for some form of resolution.", " I'm forwarding it to HR.", " And it tasted like absolute shit anyway."),
           ("Thanks I will do. You're a good egg.","Whatever","You're a real piece of work."))

s_e1 = Email(ste.name,"you","Concerns","Caroline has been saying some things about you, so I wanted to get your perspective. Could you elaborate?",
             ("I'm not certain what you mean, Steven.", "This is a disturbing email to receive.", "Shut the fuck up, Steve."),
             ("I haven't had any contact with her.", " I'm contacting HR.", " You always stick your fucking nose where it doesn't belong. I don't know why a bumbling imbecile like you got promoted in the first place."),
             ("Hmm. Okay, thanks.", "...Okay?", "Jesus Christ."))

l_e1 = Email(lin.name, "you", "Can you help?", "Since coming off mat leave, I've been having issues with this specific software. Did they update it? Steve said you know more about it than him. No rush, just when you have a moment. Ta! (Screenshot attached)",
             ("I know what to do, no problem.","This is a disturbing email to receive.", "No, I can't help."),
             (" You'll just have to convert to PDF or a word doc. They did update it so now it's more of a hassle and won't accept any other file format. Hope that helps."," I've contacted HR."," Work it out yourself, you stupid hag. And I bet your baby is ugly, too."),
             ("Perfect, it worked! Thanks for your help :)", "...For what?", "What on earth your problem?"))

s_e2 = Email(ste.name,"all","Bake sale?", "Hi all,\nBy vote, the charity we are going to support is our Local Childrens' Hospice. Linda had the idea of a bake sale, and I'm certainly happy with some cakes in the office. Let me know if you're interested in contributing.\nMany thanks,\nS",
             ("Sounds wonderful.","This is a distubring email to receive.","Bake sale?"),
             (" I'd be more than happy to man the stand. Just let me know.","I've contacted HR."," What is this, primary school? Are you a fucking child?"),
             ("Thank you. I was happy to cover it, but I'll let you know.\nThanks,\nS","What?","Jesus Christ."))



def client(x,y): #x = email y= person
    if len(x.resp) > 1:
        y.hatebool = x.mail()
    else:
        x.mail()


def hate(): #x must be person
    list = [car,lin,ste]
    for i in list:
        if i.hatebool == True:
            print("%s hates you!" % i.name)
        else:
            print("%s doesn't hate you." % i.name)


client(c_e1,car)
if car.hatebool == True:
    client(s_e1,ste)
client(l_e1,lin)
if ste.hatebool == False:
    client(s_e2,ste)

hate()
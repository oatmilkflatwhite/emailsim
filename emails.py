
import textwrap
tuple_banned = ("fuck","shit","bastard")

text_invalid = "Invalid answer."
text_banner = "~~~~~~~~~~~~~~~~~~~~~~~~~~"
text_minibanner = "~~~~~~~~"
prompt_reply= "INPUT: "

user_censored =  True

player_emails = 0

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
            global player_emails
            print("          RESPOND >>")
            y = 1
            for r in self.resp:
                print("              " + str(y) + ": %s" % r)
                y = y+1
            number = inputreply(len(self.resp))
            indy = number - 1
            player_emails = player_emails + 1
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
                return 3
            elif number == 2:
                return 2
            else:
                return 0
        else:
            print(text_banner)

class People:
    def __init__ (self, name,respflag,hateplayer,points):
        self.name = name
        self.respflag = respflag
        self.hateplayer = hateplayer
        self.points = points


jen = People("Jenny Nguyen",0,False,10)
car = People("Caroline Jenkins",0,False, 10)
lin = People("Linda Webber",0,False, 10)
ste = People("Steven Lau",0,False, 10)
hrd = People("HR Department",0,False,10)
aye = People("Ayesha Adams",0,False,10)

hr_times = 0


h_e1 = Email(hrd.name,"you","AUTOMATED MESSAGE", "Thank you for your email. We will respond to your request shortly.","N","N","N")

h_e2 = Email(hrd.name, "you","Termination","Everyone thinks you're a bastard so we're letting you go. Bye-bye.","N","N","N")

h_e3 = Email(hrd.name,"all", "Friendly Reminder", "Friendly reminder to all employees that we treat everyone with respect and kindness. We have had some complaints following some employee behaviour. Please complete the online training course \"Respect in the Workplace\" before the end of the month. Thank you.",
             "N","N","N")
h_e4 = Email(hrd.name,"you","Problem?","You keep forwarding messages into this inbox. Do you need to contact IT?",
             "N","N","N")

j_e1 = Email (jen.name,"you","Sorry to bother you",("Morning, just a bit of a request. I can't find that report you sent to me last week, would you be okay to resend it?"),
            ("Of course.","This is a disturbing email to receive.","No, I don't want to."),
            (" Please see the attached file."," I'll be in touch with HR.", " I sent it to you so I shouldn't have to send it again. It's not my fault you can't organise your inbox."),
            ("Thanks for the swift response. Have a great day.","...Why?","My apologies for wasting your time."))

j_e2 = Email (jen.name,"you","2025 April Report.doc","(Attached is a document you requested from Jen yesterday)",
              ("Thanks Jen.", "This is a disturbing email to receive.", "It's about time."),
              (" This looks great."," I'll be letting HR know about this.", " How long does it reasonably take to find a file on your computer? A few minutes? Why couldn't you send this to me yesterday?"),
              ("Anytime. Shout if I can help with anything else.", "But why? What did I do?", "I'm sorry. In future I'll be more responsive."))

c_e2 = Email (car.name,"you", "cant connect to wifi","help",
              ("I would suggest contacting IT.","This is a disturbing email to receive.","Why are you messaging me?"),
              (" They would be able to assist you regarding this."," I have forwarded your message onto HR.", " Just because I'm not old as fuck like you doesn't mean I know everything about computers. Why don't you just retire already?"),
              ("thanks","?","youre a real piece of work"))

c_e1 = Email(car.name,"all","Sick to bastard death of this","If you ate my fucking tomato sandwich from the work fridge im coming for you.",
           ("I'm really sorry to hear this, Caroline.","This is a disturbing email to receive.","I was the one who ate it, you miserable cow."),
           (" I would suggest contacting our manager for some form of resolution.", " I'm forwarding it to HR.", " And it tasted like absolute shit anyway."),
           ("thanks","whatever","horrible. youll get everything you deserve"))

s_e1 = Email(ste.name,"you","Concerns","Caroline has been saying some things about you, so I wanted to get your perspective. Could you elaborate? Many thanks, S",
             ("I'm not certain what you mean, Steven.", "This is a disturbing email to receive.", "Shut the fuck up, Steve."),
             (" I haven't had any contact with her.", " I'm contacting HR.", " You always stick your fucking nose where it doesn't belong. I don't know why a bumbling imbecile like you got this job in the first place."),
             ("Hmm. Okay, thanks. Many thanks, S", "...Okay?", "Jesus Christ."))

l_e1 = Email(lin.name, "you", "Can you help?", "Since coming off mat leave, I've been having issues with this specific software. Did they update it? Steve said you know more about it than him. No rush, just when you have a moment. Ta! (Screenshot attached)",
             ("I know what to do, no problem.","This is a disturbing email to receive.", "No, I can't help."),
             (" You'll just have to convert to PDF or a word doc. They did update it so now it's more of a hassle and won't accept any other file format. Hope that helps."," I've contacted HR."," Work it out yourself, you stupid hag. And I bet your baby is fuck ugly, too."),
             ("Perfect, it worked! Thanks for your help :)", "...For what?", "What on earth your problem?"))

a_e1 = Email (aye.name, "you", "Computer troubles", "Hello, I just got off a call with Linda. She mentioned that you helped her, so I was wondering if you were good at computers, you could give me some tips on how to make my PowerPoint look better. (Screenshot of the ugliest powerpoint you've ever seen)",
              ("Sure. I have some suggestions.", "This is a disturbing email to receive.", "Google is free."),
              (" I would stick to a simple colour palette, and stick to a sans-serif font for the body text so it's easier to read.", " I'm contacting HR."," Also that is the ugliest fucking powerpoint I've ever seen. The others won't tell you this, but you have hideous taste and we all make fun of you for it."),
              ("I tried it and it looks tonnes better. Cheers!", "???", ":("))

a_e2 = Email (aye.name, "you", "Coffees","Grabbing coffees for the team, want one?",
              ("Yes please!","This is a disturbing email to receive.","I hate coffee."),
              (" Oat milk latte, but any plant milk is okay. Thanks Ayesha.","I have let HR know that you've messaged me this."," Besides that, I'd rather kill myself than drink anything you've handled."),
              ("Roger that. Be back shortly.","???","What on earth is your problem?"))

s_e2 = Email(ste.name,"all","Bake sale?", "Hi all. By vote, the charity we are going to support is our local childrens' hospice. Linda had the idea of a bake sale, and I'm certainly happy with some cakes in the office. Let me know if you're interested in contributing. Many thanks, S",
             ("Sounds wonderful.","This is a distubring email to receive.","Bake sale?"),
             (" I'd be more than happy to man the stand. Just let me know.","I've contacted HR."," What is this, primary school? Are we selling chocolate cornflake cakes and bakewell tarts for 30p a piece? Am I a fucking child to you?"),
             ("Thank you. I was happy to cover it, but I'll let you know. Thanks, S","What?","Jesus Christ."))



def client(x,y): #x = email y= person
    if len(x.resp) > 1:
        y.respflag = x.mail()

    else:
        x.mail()

def reaction(x): #x = person
    if x.respflag == 3:
        x.hateplayer = True
        #print("hateplayer = %s" % x.hateplayer)
    elif x.respflag == 2:
        client(h_e1,hrd)
        global hr_times
        hr_times = hr_times + 1



def end():
    list = [car,lin,ste,aye,jen]
    employees = len(list)
    # print ("%s is the number of employees" % str(employees))
    haters = 0 
    for i in list:
        if i.hateplayer == True:
            print("%s hates you!" % i.name)
            haters = haters + 1
        else:
            print("%s doesn't hate you." % i.name)
    print("You replied to %s emails." % str(player_emails))
    print("You contacted HR %s times." % str(hr_times))
    #print(str(haters))
    if haters == employees:
        client(h_e2,hrd)
        print("Everyone hates you!")
    elif haters > 1:
        client(h_e3,hrd)
        print("Some people don't like you...")
    elif hr_times > 3:
        client(h_e4,hrd)
        print("People think you're weird.")
    elif haters == 0:
        print("Everyone thinks you're okay!")

        
        


while True:
    client(j_e1,jen)
    reaction(jen)
    client(c_e2,car)
    reaction(car)
    client(j_e2,jen)
    reaction(jen)
    client(c_e1,car)
    reaction(car)
    if car.respflag == 3:
        client(s_e1,ste)
        reaction(ste)
    client(l_e1,lin)
    reaction(lin)
    if lin.respflag == 0:
        client(a_e1,aye)
        reaction(aye)
    if ste.respflag != 3:
        client(s_e2,ste)
        reaction(ste)
    if aye.respflag == 0:
        client(a_e2,aye)
        reaction(aye)
    end()
    input("Press any key to play again!")
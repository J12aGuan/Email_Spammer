import smtplib
import os
import mouse
from email.message import EmailMessage
import imghdr
from tkinter import *
from tkinter import ttk

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

#Value Set
Button_Space = 1
Text_Space = 5
Entry_Space = 1

window = Tk()

def Information():
    Amount = Amount_Entry.get()
    Email = Email_Entry.get()

    global Amount_Spam
    global Email_Send

    Amount_Spam = int(Amount)
    Email_Send = str(Email)

    Send_out()

def CreateWindow():
    window.title("Spamer Window")                           #Name it "PhysicsCalculator"
    window.geometry("800x450")
    window.state('zoomed')                 #Maximize the window
    window.resizable(False, False)            #Not resizable
    window.mainloop()

def Label_And_Entry():
    global Amount_Entry
    global Email_Entry


    Emails_Text = Text(window, height = 50, width = 50)
    Emails_Text.place(relx=0.051, rely=0)

#Send Email
    Spam_Times_Label = Label(window, text = "Amount: ", font = ("Comic Sans", 12), width = "15")
    Spam_Times_Label.place(relx=0.45, rely=0.25, relheight=0.4, anchor= CENTER) #relheight=0.4, relwidth=0.8

    Amount_Entry = Entry(window, width = 20)
    Amount_Entry.place(relx=0.52, rely=0.25, anchor= CENTER)
    Amount_Entry.focus()

    #Separator = ttk.Separator(window, orient = "horizontal")
    #Separator.place(relx=0, rely=0.4, relwidth=1, relheight=1)

    Email_Label = Label(window, text = "Email: ", font = ("Comic Sans", 12), width = "15")
    Email_Label.place(relx=0.45, rely=0.75, relheight=0.4, anchor= CENTER)      #relheight=0.4, relwidth=0.8

    Email_Entry = Entry(window, width = 20)
    Email_Entry.place(relx=0.52, rely=0.75, anchor= CENTER)

    Spam_Button = Button(window, text = "SPAM!", command = lambda:[Information()], font = ("Comic Sans", 15), width = "15")
    Spam_Button.place(relx=0.5, rely=0.5, anchor= CENTER)
    CreateWindow()

def Send_out():
    Email_Title = Email_Title_Text.get("1.0", "end-1c")     #Can only get the information in the function planning on use
    Email_Body = Email_Body_Text.get("1.0", "end-1c")       #global doesn't work on Text()
    times = 1
    for x in range(Amount_Spam):
        SPAM = str(Email_Title) + str(times)
        msg = EmailMessage()
        msg["Subject"] = SPAM
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = Email_Send
        msg.set_content(str(Email_Body))
        times += 1

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        # with open("Anderson's Wedding.png", "rb") as f:     #rb means read bite
        #    file_data = f.read()
        #    file_type = imghdr.what(f.name)
        #    file_name = f.name
        #
        # msg.add_attachment(file_data, maintype="image", subtype = file_type, filename = file_name)

#Write Email
Title_Label = Label(window, text = "Title: ", font = ("Comic Sans", 15), width = "14")
Title_Label.place(relx = 0.755, rely = 0.05)

Email_Title_Text = Text(window, height = 1, width = 20)
Email_Title_Text.place(relx = 0.755, rely = 0.1)

Body_Label = Label(window, text = "Email Body: ", font = ("Comic Sans", 15), width = "28")
Body_Label.place(relx = 0.7, rely = 0.27)

Email_Body_Text = Text(window, height = 25, width = 40)
Email_Body_Text.place(relx = 0.7, rely = 0.32)

Label_And_Entry()

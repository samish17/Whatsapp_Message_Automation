# !/usr/bin/python3.10
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# from tkinter.tix import *
# import Pmw  # <------------- used to display hover message
# while True:
# try:
import pywhatkit
# import pyautogui
import datetime


class qr_Code_app(Tk):
    def __init__(self):
        self.window = Tk()
        self.window.title("Whats App Automation")
        self.window.maxsize(height=350, width=500)  # <------ Maximum size of the window
        self.window.minsize(height=350, width=500)  # <------ Minimum size of the window
        # Putting a background image to an application
        # back_photo = PhotoImage(file='image_name.png')
        # label = Label(self.window, image=back_photo)
        # label.image = back_photo
        # label.place(x=-50, y=-350)
        self.window.configure(bg='#C5CDE8')

        # self.window.iconbitmap('icon.ico')

        #       <------------Welcome ------------->
        welcome_label = Label(self.window, text='Welcome!', font='Times 20 bold', bg='#C5CDE8')
        welcome_label.place(x=100, y=20)

        #    <---------------Phone Number --------------------------------->
        phone_no_label = Label(self.window,
                               text='Provide the Phone No. of the receiver along with country code:',
                               bg='#C5CDE8')
        phone_no_label.place(x=20, y=70)

        self.phone_no = StringVar()
        phone_label_entry = Entry(self.window, width=18, textvariable=self.phone_no)
        phone_label_entry.place(x=20, y=100)
        #   <---------Set Time -------------->
        set_time_label = Label(self.window, text='Set the time to deliver your message.', bg='#C5CDE8')
        set_time_label.place(x=20, y=130)

        #    <-------------Time Hour-------------------------------->
        time_hour_label = Label(self.window, text='Hr :', bg='#C5CDE8')
        time_hour_label.place(x=20, y=160)

        # Combobox creation
        self.hour = IntVar()
        time_hour_combo = ttk.Combobox(self.window, width=2, textvariable=self.hour,
                                       values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.hour.set(1)
        time_hour_combo.place(x=50, y=160)

        #     <---------------Time Minute -------------------->
        time_minute_label = Label(self.window, text='Min :', bg='#C5CDE8')
        time_minute_label.place(x=120, y=160)

        self.minute = IntVar()
        time_minute_combo = ttk.Combobox(self.window, width=2, textvariable=self.minute,
                                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                                                 19,
                                                 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                                 36, 37,
                                                 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                                                 54, 55,
                                                 56, 57, 58, 59, 00])
        self.minute.set(1)
        time_minute_combo.place(x=160, y=160)

        # <-----------Getting am/pm ---------------->
        self.meridian = StringVar()
        meridian_combo = ttk.Combobox(self.window, width=3, textvariable=self.meridian, values=['am', 'pm'])
        self.meridian.set('am')
        meridian_combo.place(x=220, y=160)

        #    <-----------------User's Message -------------->
        user_msg_label = Label(self.window, text='Your message here :', bg='#C5CDE8', height=4)
        user_msg_label.place(x=20, y=190)

        self.message = StringVar()
        user_msg_entry = Entry(self.window, width=40, textvariable=self.message)
        user_msg_entry.place(x=20, y=220)

        #   <----------------Send Button ---------------------->
        send_button = Button(self.window, text='SEND MESSAGE', command=self.deliver_msg)
        send_button.place(x=180, y=260)

        #    <--------------------Help Button ----------------------->
        # Pmw.initialise(self.window)

        help_button = Button(self.window, text='Help', bd=0, command=self.provide_help, bg='#C5CDE8',
                             font='Times 10 underline')
        # help_button.
        help_button.place(x=20, y=315)

        # # create balloon object and bind it to the widget
        # balloon = Pmw.Balloon(self.window)
        # balloon.bind(help_button, "Help Center")

        # lbl = balloon.component("label")
        # lbl.config(background='#C5CDE8', foreground="black")

        #    <-----------Getting the present time of the location -------------->
        self.now = datetime.datetime.now()
        self.now_hour = self.now.hour
        self.now_minute = self.now.minute

        self.window.mainloop()

    def deliver_msg(self):
        """ This functions collects the required data for pywhatkit module and sends the message as per the users time
        schedule """
        while True:
            if len(self.phone_no.get()) == 0:
                messagebox.showwarning('Warning', 'Provide the phone number !')
                return mainloop()

            elif len(self.message.get()) == 0:
                messagebox.showwarning('Warning', 'Your message box seems to be empty !')
                return mainloop()

            #       <-------- This below code warns if the provided time matched to the current time --->
            elif self.now_hour == self.hour.get() and self.now_minute == self.minute.get():
                messagebox.showwarning('Warning', 'You are supposed to edit the time as it '
                                                  'matched with the current time ')
                return mainloop()

            else:
                messagebox.askokcancel('Confirm', 'Be sure about the provided data before moving forward.\n'
                                                  'Also be sure that the country code is provided.')
                #    <------------Wait Info Message ---------------->
                messagebox.showwarning("Information",
                                       "Your message will be delivered at {}: {}, leave your"
                                       " computer still till then.".format(self.hour.get(), self.minute.get()))

                pywhatkit.sendwhatmsg(self.phone_no.get(), self.message.get(), self.hour.get(),
                                      self.minute.get(), 10, True, 6)
                # pyautogui.press('enter', 10)

    def go_back(self):
        self.help_window.destroy()

    def provide_help(self):

        def help_center_menu():
            self.help_window = Tk()
            self.help_window.title('Help Center')
            # self.help_window.iconbitmap('icon.ico')
            self.help_window.configure(bg='#C5CDE8')
            self.help_window.maxsize(height=260, width=500)
            self.help_window.minsize(height=260, width=500)

            #    <-----------Instructions for help in a help center ------------------->
            #    1st Message
            help_msg_1_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''1. Make sure the internet connection is 'ON' for the whole time.''')
            help_msg_1_label.place(x=10, y=40)

            #    2st Message
            help_msg_2_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''2. This is based on 24 hour time format so,set time accordingly.''')
            help_msg_2_label.place(x=10, y=60)

            #    3rd Message
            help_msg_3_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''3. Don't use '0' before the any numbering(time/minute).''')
            help_msg_3_label.place(x=10, y=80)

            #   4th Message
            help_msg_4_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''4. This application only works for upcoming 24 hours.''')
            help_msg_4_label.place(x=10, y=100)

            #    5th Message
            help_msg_5_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''5. Don't use '0' before the any numbering(time/minute).''')
            help_msg_5_label.place(x=10, y=120)

            #    6th Message
            help_msg_6_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''6. Login to the Whatsapp Web before leaving a message for someone.''')
            help_msg_6_label.place(x=10, y=140)

            #    7th Message
            help_msg_7_label = Label(self.help_window, bg='#C5CDE8',
                                     text='''For other inquiries or problems than mentioned above.
                                Email Us: - kbhattasamish17@gmail.com''')
            help_msg_7_label.place(x=2, y=210)

            #   <-----------Go Back Button ------------>
            back_from_help_center_btn = Button(self.help_window, text='Go Back', bg='#C5CDE8',
                                               command=self.go_back)
            back_from_help_center_btn.place(x=420, y=217)

            self.help_window.mainloop()

        # <-----------Quit button is not working freak -------------->
        # def go_back(self):
        #     self.help_window.destroy()

        help_center_menu()


qr_Code_app()  # <------ Calling the Class function
# break


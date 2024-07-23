#Import necessay files 
from tkinter import *
import random
import smtplib
import tkinter as tk
from tkinter import messagebox

#Global varible to track whether the OTP has been sent or not
otp_sent=False

#Generate 6 digit random OTP
def generate_otp():
    otp = ""
    for i in range(6):
         otp+=str(random.randint(0,9))      #generating a randomm 6-digit OTP
    return otp

#send OTP
def send_otp():
    global otp_sent
    emailaddress="niveditajain082@gmail.com"
    emailpass="pgdxniachkxapjce"
    recepient_email = email_entry.get()
    subject="OTP"

    if not recepient_email or not subject:
           messagebox.showerror("Error", "Please enter valid Email address")
           return
    
    try:
         global OTP 
         OTP = generate_otp()
         #otp_mesg=f"Subject: {subject}\n\n{OTP} is your OTP"
         #setting up server
         server = smtplib.SMTP('smtp.gmail.com',587)
         server.starttls()
         server.login(emailaddress,emailpass)
         #Email body and message
         body = "your OTP is "+str(OTP)+"."
         subject = "OTP verification using python"
         message = f'subject:{subject}\n\n{body}'
         server.sendmail(emailaddress,recepient_email,message)
         server.quit()
         messagebox.showinfo("Success!!","OTP sent successfully to your Email")

         #Disable the send button
         send_button.config(state="disabled")
         otp_sent=True

         #Show the otp entry and verify button
         otp_frame.pack()
    except smtplib.SMTPAuthenticationError:
         messagebox.showerror("Error","SMTP Authentication Error\n","Pls check your email address and password")
    except Exception as e:
         messagebox.showerror("Error"
                              ,f"An error occurred:{str(e)}") #error raised other than authentication


#verify OTP
def verify_otp():
     user_input = otp_entry.get()
     print(user_input)
     if user_input == OTP:
          messagebox.showinfo("success!!","OTP Verified")
          win.destroy()
     else:
          messagebox.showerror("Error","Please check your OTP again")

#Resend OTP
def resend_otp():
     send_otp()

     #Reenable the send otp button after resending
     send_button.config(state="normal")

#create GUI Window
win=tk.Tk()
win.title("OTP verification")
win.geometry("400x400")

# Drawing the canvas
c = tk.Canvas(win, bg="grey", width=200, height=200)
c.place(x=100, y=60)# Drawing the canvas

#email entry inside pop up window
email_label = tk.Label(win,text="Enter your email:")
email_label.pack(pady=5)
email_entry = tk.Entry(win)
email_entry.pack(pady=5)

#send OTP
send_button = tk.Button(win,text="send OTP",command=send_otp)
send_button.pack(pady=5)

#OTP frame which is hidden initially
otp_frame=tk.Frame(win)

#OTP entry
otp_label=tk.Label(otp_frame,text="Enter your OTP:")
otp_label.pack(pady=5)
otp_entry = tk.Entry(otp_frame)
otp_entry.pack(pady=5)

#verify button
verify_button=tk.Button(otp_frame,text="verify OTP",bg="lightblue",fg="black",
                        command=verify_otp)
verify_button.pack(side=LEFT,padx=5,pady=5)

#Resend OTP button
resend_button=tk.Button(otp_frame,text="Resend OTP",bg="lightblue",fg="black",
                        command=resend_otp)
resend_button.pack(side=RIGHT,padx=5,pady=5)

win.mainloop()









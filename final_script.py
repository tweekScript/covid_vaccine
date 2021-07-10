import tkinter as tk
import requests
import json
from tkinter import *
from tkinter import ttk


canvas = tk.Tk()
canvas.geometry("500x550")
canvas.title("COVID-19 Vaccination Availibility")
canvas.config(bg="#000000")

label_0=tk.Label()
label_0.config(bg="#000000",height="50")
font1=("Raleway",20,"bold")
font2=("Raleway",15)

#pincode text-----------------------------------------------
label1=tk.Label(font=font1)
label1.config(text="Enter your PINCODE:",bg="#000000",fg="#6AF2F0")
label1.pack(pady=10)

#pincode text entry-----------------------------------------
textfield_pincode=tk.Entry(canvas,justify="center",font=font2,bd="5")
textfield_pincode.pack(pady=10)
textfield_pincode.focus()

#date text--------------------------------------------------
label2=tk.Label(font=font1)
label2.config(text="Enter Today's DATE",bg="#000000",fg="#6AF2F0")
label2.pack(pady=10)
label2=tk.Label(font=font2)
label2.config(text="(date format >>> DD-MM-YYY):",bg="#000000",fg="#6AF2F0")
label2.pack(pady=5)

#date entry------------------------------------------------
textfield_date=tk.Entry(canvas,justify="center",font=font2,bd="5")
textfield_date.pack(pady=10)
textfield_date.focus()

#age text---------------------------------------------------
label3=tk.Label(font=font1)
label3.config(text="Enter AGE category:",bg="#000000",fg="#6AF2F0")
label3.pack(pady=10)
label3=tk.Label(font=font2)
label3.config(text="(For 18+ vaccines enter 18,",bg="#000000",fg="#6AF2F0")
label3.pack(pady=5)
label3=tk.Label(font=font2)
label3.config(text="For 45+ vaccines enter 45)",bg="#000000",fg="#6AF2F0")
label3.pack(pady=5)

#age text entry---------------------------------------------
textfield_age=tk.Entry(canvas,justify="center",font=font2,bd="5")
textfield_age.pack(pady=10)
textfield_age.focus()

#button ----------------------------------------------------
btn=tk.Button(canvas,text="Find Vaccines",bd=5,command=lambda:out())
btn.config(font=font2,bg="#6AF2F0",fg="#000000")
btn.pack(pady=2)

#output_canvas_code------------------------------------------
def out():
    # scrollbar code------------------------------------------
    root = Tk()
    root.geometry("500x550")
    root.title("COVID-19 Vaccination Availibility")
    root.config(bg="#000000")
    # create a main frame------------------------
    main_frame = Frame(root)
    main_frame.pack(fill="both", expand=1)
    # create a canvas----------------------------
    canvas = Canvas(main_frame)
    canvas.config(bg="#000000")
    canvas.pack(side="left", fill="both", expand=1)
    # add a scrollbar----------------------------
    sb = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    sb.pack(side="right", fill="y")
    # configure the canvas-------------------------
    canvas.configure(yscrollcommand=sb.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # create another frame inside canvas-------------------
    second_frame = Frame(canvas)
    second_frame.config(bg="#000000")
    # add that new frame to a window in the canvas-----------------
    canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # ----------output code-------------------------
    font1 = ("Raleway", 18, "bold")
    font2 = ("Raleway", 15)
    label_0 = Label(second_frame, font=font1)
    label_0.config(text="************** Vaccines Availability *************", bg="#000000", fg="#6AF2F0")
    label_0.pack(pady=15)
    #user data input-----------------------------------
    pincode = str(textfield_pincode.get())
    date = str(textfield_date.get())
    age = str(textfield_age.get())
    #finding the function results--------------------------
    api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + date
    r = requests.get(url=api)
    if r.status_code == 200:
        response = r.json()['centers']
    for each in response:
        center_id = each['name']

        for ses in each['sessions']:
            date = str(ses['date'])
            avail_cap = str(ses['available_capacity'])
            if avail_cap == "0":
                continue
            vac = str(ses['vaccine'])
            min_age = str(ses['min_age_limit'])
            label_1 = Label(second_frame, font=font1)
            label_1.config(text="Center Name: " + center_id, font=font1, bg="#000000", fg="#6AF2F0")
            label_1.pack(pady=10)
            if min_age != age:
                label_2 = Label(second_frame, font=font2)
                label_2.config(text="No Vaccines for the selected age category", font=font2, bg="#000000", fg="#6AF2F0")
                label_2.pack(pady=0)
            else:
                label_3 = Label(second_frame, font=font2)
                label_3.config(text="DATE: " + date, font=font2, bg="#000000", fg="#6AF2F0")
                label_3.pack(pady=0)
                label_4 = Label(second_frame, font=font2)
                label_4.config(text="AVAILABLE CAPACITY: " + avail_cap, font=font2, bg="#000000", fg="#6AF2F0")
                label_4.pack(pady=0)
                label_5 = Label(second_frame, font=font2)
                label_5.config(text="AGE CATEGORY: " + min_age, font=font2, bg="#000000", fg="#6AF2F0")
                label_5.pack(pady=0)
                label_6 = Label(second_frame, font=font2)
                label_6.config(text="VACCINE: " + vac, font=font2, bg="#000000", fg="#6AF2F0")
                label_6.pack(pady=0)

    root.mainloop()

canvas.mainloop()


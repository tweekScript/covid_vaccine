import tkinter as tk
import requests
import json

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

#getting the user input--------------------------------------
def results():
    pincode=str(textfield_pincode.get())
    date=str(textfield_date.get())
    age=str(textfield_age.get())
    find(pincode,date,age)

#button ----------------------------------------------------
btn=tk.Button(canvas,text="Find Vaccines",bd=5,command=lambda:results())
btn.config(font=font2,bg="#6AF2F0",fg="#000000")
btn.pack(pady=2)

#find_function
def find(pincode: str, date: str, age: str):
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
            print(center_id)
            if min_age != age:
                print("No Vaccines Available\n")
            else:
                print("Date: " + date + "\n" + "Available Capacity: " + avail_cap + "\n" + "Minimum Age: " + min_age + "\n" + "Vaccine Name: " + vac + "\n")


canvas.mainloop()


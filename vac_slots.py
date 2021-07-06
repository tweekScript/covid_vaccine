import requests
import json

def find(pincode:str,date:str,age:str):
    api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode+"&date="+date
    r = requests.get(url=api)
    if r.status_code==200:
        response=r.json()['centers']
    for each in response:
        center_id=each['name']

        for ses in each['sessions']:
            date=str(ses['date'])
            avail_cap=str(ses['available_capacity'])
            if avail_cap=="0":
                continue
            vac=str(ses['vaccine'])
            min_age=str(ses['min_age_limit'])
            print(center_id)
            if min_age!=age:
                print("No Vaccines Available\n")
            else:
                print("Date: "+date+"\n"+"Available Capacity: "+avail_cap+"\n"+"Minimum Age: "+min_age+"\n"+"Vaccine Name: "+vac+"\n")

print("\n\n**********************************CHECK VACCINE AVAILABILITY**********************************\n")
print("Enter Your Area Pincode:")
pincode=str(input())
print("Enter today's date (date format --> DD-MM-YYY):")
date=str(input())
print("Enter the valid age group\n(For 18+ vaccines enter 18/For 45+ vaccines enter 45):")
age=str(input())
find(pincode,date,age)
print("*******************************************************************************************")
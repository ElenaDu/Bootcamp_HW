person={
     "name": "",
     "age": 21,
     "hobbies": ["cats","food","Python"],
     "wake_up": {
           "Sun": "7.00 a.m",
           "Mon": "6.15 a.m",
           "Tue": "6.30 a.m"
     }
     
}
hob_q=len(person["hobbies"])
print("My name is "+person["name"]+". I have "+str(hob_q)+" hobbies. I got up at "+person["wake_up"]["Sun"]+","+person["wake_up"]["Mon"])
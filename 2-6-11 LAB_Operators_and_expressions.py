hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print(str((hour*60+mins+dura)//60%24)+":"+str((hour*60+mins+dura)%60))

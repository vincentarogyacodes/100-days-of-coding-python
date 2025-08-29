# time_of_day = ["morning","afternoon","evening","night"]
# traffic_level = ["heavy","medium","light"]
# emergency_vehicle = ["True","False"]
# pedestrians = ["True","False"]
# lights = ["override","60","45","30","25","15"]

time_of_day = str(input("What is the time of day: morning, afternoon, evening, or night?\n"))
traffic_level = str(input("What is the traffic level: heavy, medium, light\n"))
emergency_vehicle = str(input("Is there an emergency vehicle on the road? : True or False\n"))
pedestrians = str(input("Are there any pedestrians waiting to cross the road? : True or False\n"))

if emergency_vehicle == "True":
    print("override")
elif traffic_level == "heavy":
    if time_of_day == "morning" or time_of_day == "evening":
        print("60 seconds")
    else:
        print("45 seconds")
elif traffic_level == "medium":
    print("30 seconds")
elif traffic_level == "light":
    if pedestrians == "True":
        print("25 seconds")
    else:
        print("15 seconds")
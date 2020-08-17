import time

oul = input("Enter the out-look weather(Sunny/Overcast/Rainy)\t")
hu = input("Enter the level of humidity(High/Normal)\t")
win = input("Is it windy or not?(true/false)\t")

time.sleep(2)

print("Weather Conditions:")
print("OutLook: ",oul)
print("Humidity: ",hu)
print("Windy: ",win)

print("Processing your Awesomeness.....")
time.sleep(2)

print("Making ready the best possible result")
time.sleep(3)


if(oul == "sunny" or oul == "Sunny"):
    if((hu == "high" or hu == "High") and (win == "true" or win == "True")):
        play = "no"
    else:
        play = "yes"

elif(oul == "overcast" or oul == "Overcast"):
    play = "yes"

else:
    if(win == "true"or win == "True"):
        play = "no"
    else:
        play = "yes"

print("\n\n")
if(play == "yes"):
    print("Hurrah!! The Match can be conducted\n\n")
else:
    print("The weather doesnt support us today !! We will catch up later after the weather clears\n\n")

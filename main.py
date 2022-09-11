import random

name = input("Hey there! What's your name? ")
response1 = [
    "Greetings, " + name + ". My name is ChanBot, nice to meet you.",
    "Welcome, " + name + ". My name is ChanBot, nice to meet you.",
    "Nice to meet you, " + name + ". My name is ChanBot."
]
randresp1 = random.randint(0, 2)
print(response1[randresp1])


def theWeather(weather):
  randresp2 = random.randint(1, 2)
  
  if weather == "sunny":
    if randresp2 == 1:
      print("Thats great! I love clear skies.")
    else:
      print("Nice! Perfect weather to go outside.")
  elif weather == "rainy" or weather == "stormy":
    if randresp2 == 1:
      print("Perfect. The rain is very calming.")
    else:
      print("Darn! It's best to stay inside.")
  elif weather == "cloudy" or weather == "gloomy":
    if randresp2 == 1:
      print("Nice! I love watching the clouds.")
    else:
      print("Great! Perfect weather to go outside.")
  elif weather == "snowy":
    if randresp2 == 1:
      print("Yay! Lets go play in the snow!")
    else:
      print("I hate the cold, make sure to wear your coat.")
  else:
    print("Beautiful, lets move on.")

weather = input("\nWhat is the weather like today? ").lower()
theWeather(weather)

print('test')
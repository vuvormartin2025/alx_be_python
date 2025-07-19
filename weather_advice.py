# weather_advice.py

weather = input("what's the weather like today? (sunny/rainy/cold):").lower()

#check weather condition and give advice

if weather == "sunny":
    print("wear a t-shirt and sunglasses.")


elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("sorry, I don't have recommendations for this weather.")

    
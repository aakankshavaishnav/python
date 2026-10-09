w = input("Enter weather: ")
match w:
    case "sunny": 
        print("Wear sunglasses")
    case "rainy": 
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy": 
        print("Wear warm clothes")
    case _: 
        print("Unknown Weather")
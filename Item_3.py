import requests
def determinarDistancia(desde,hasta):
    params = {"key":"3M4wHsBNfJk8BzNrHBFBvXDx0UKjyblM","from":desde, "to": hasta, "unit": "k","locale": "es_MX"}
    try:
        response = requests.get("http://www.mapquestapi.com/directions/v2/route", params).json()['route']
        distance = round(response['distance'],1)   
        legs = response['legs']
        maniobras = list(map(lambda x: x["maneuvers"],legs))
        maniobras = [item for sublist in maniobras for item in sublist]
        time = response['formattedTime']
        print("---------------S---------------")
        print("Tiempo:",time)
        print("Distancia:",distance,'Km')
        print("Narrativa:")
        for man in maniobras:
            print(man["narrative"])
    except:
        print("Hubo un error de comunicación con la API")

desde = input("Ciudad de origen: ")
hasta = input("Ciudad de destino: ")
determinarDistancia(desde,hasta)


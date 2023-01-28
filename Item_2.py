from math import pi 

def calculoCircunferencia(r):
    roundPi = round(pi, 6)
    return 2*roundPi*r

radios = [3,5,10]
for radio in radios:
    print("La circunferencia para el radio",radio, "es", calculoCircunferencia(radio))
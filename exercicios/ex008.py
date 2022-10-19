# conversor de medidas

d = int(input('distância em metros: '))

# km
km = d / 10 / 10 / 10
print(f'{km}km')

# hm 
hm = d / 10 / 10
print(f'{hm}hm')

# dam 
dam = d / 10
print(f'{dam}dam')

# dm
dm = d * 10
print(f'{dm}dm')

# cm
cm = d * 10 * 10
print(f'{cm}cm')

# mm
mm = d * 10 * 10 * 10
print(f'{mm}mm')
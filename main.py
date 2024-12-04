import random
import time

# number generating function 
def lotto (l):
    lotto_numbers = []
    i = 0
    while i in range(l):           
        rand = random.randrange(1,10)
        lotto_numbers.append(rand)
        i+=1
    return(lotto_numbers)
    
# CLI
print("Witamy w generatorze liczb lotto!")
lenght = int(input("Ile cyfr chcesz wylosować? "))
if lenght <= 0:
    print("Niepoprawna wartość, spróbuj ponownie.")
elif lenght > 10000:
    print("Proszę czekać, generowanie numerów (to potrwa chwilę)......")
    print(* lotto(lenght))
else:
    print("Proszę czekać, generowanie numerów")
    time.sleep(random.uniform(1, 10)) 
    print(* lotto(lenght))


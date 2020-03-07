import os, time

slogen = 'a commercial slogen I want to make it longer!'

for i in range(2): # should be while True:

    for i in range(-len(slogen),0):
        os.system('clear')
        print(slogen[i:],slogen[0:i])
        time.sleep(0.7)
os.system('clear')
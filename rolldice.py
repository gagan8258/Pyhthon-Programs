import random
print("It is a dice roller")
a="y"
while (a=="y" or a=="Y"):
    x=random.choice([1,2,3,4,5,6])
    if(x==1):
        print("[-----------]",end='\n')
        print("[     O     ]",end='\n')
        print("[           ]",end='\n')
        print("[     O     ]",end='\n')
        print("[-----------]",end='\n')
    if(x==2):
        print("[-----------]",end='\n')
        print("[     O     ]",end='\n')
        print("[           ]",end='\n')
        print("[     O     ]",end='\n')
        print("[-----------]",end='\n')
    if(x==3):
        print("[-----------]",end='\n')
        print("[     O     ]",end='\n')
        print("[     O     ]",end='\n')
        print("[     O     ]",end='\n')
        print("[-----------]",end='\n')
    if(x==4):
        print("[-----------]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[           ]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[-----------]",end='\n')
    if(x==5):
        print("[-----------]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[     O     ]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[-----------]",end='\n')
    if(x==6):
        print("[-----------]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[   O   O   ]",end='\n')
        print("[-----------]",end='\n')
    a=input("Please enter y to roll the dice")

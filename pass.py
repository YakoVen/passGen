from progress.bar import Bar 
from time import sleep
from colorama import init ,Fore ,Style


print("   1) costume inpute \n 2) wordlist combinition     ")

method= input("method choose :")


minletters=0
maxletters=100



t = input(" input a word : ")
words=[]
passwords =[]

init()


def combine():
    bar=Bar("PROCESS 001 -> COMBINING WORDS  ",fill='Y',max=len(words))
    for a in words:
        for b in words:
            passwords.append(str(a) + str (b))
        sleep(0.5)           
        bar.next()
    bar.finish()

def addnumber():
    i =0
    bar=Bar("PROCESS 002 -> adding numbers less than /00/  ",fill='Y',max=99)
    
    while i<100 :
        for a  in words :
            passwords.append(str(a)+str(i))
        sleep(0.05)           
        i=i+1
        bar.next()
    bar.finish()

    i=i+1

def add_third_p():
    pas_copy=passwords.copy()
    bar=Bar("PROCESS 001 -> third part  ",fill='Y',max=len(pas_copy))
    for a in pas_copy:
        for b in words : 
            passwords.append(str(a)+str(b))
        sleep(0.01)           
        bar.next()
    bar.finish()

def add_values():
    list_of_common=["fuckyou","azertyui","azertyuiop","azerty","algerie123","madrid"]
    for a in list_of_common:
        passwords.append(str(a))

def count_results():
    return len(passwords)









y="y"

if method=="1":
    while t!="" :
        words.append(t.replace(" ",""))
        t=input(" next one : ->")
else:
    wrdlist = open(input(" what wordlist you wanna use :"),"r")
    for line in wrdlist.readlines():
        words.append(line.replace(" ","").replace("\n",""))

if input("  wanna add comon pass ??? y/n")==y:
    print(f"{Fore.RED}Ok{Style.RESET_ALL}")
    add_values()

print(f"{Fore.RED}ASEBRI !!{Style.RESET_ALL}")
combine()

if input("  wanna a third part ??? y/n")==y:
    print(f"{Fore.RED}ASEBRI !!{Style.RESET_ALL}")
    add_third_p()

if input("  wanna add combinison word/num ??? y/n")==y:
    print(f"{Fore.RED}OK {Style.RESET_ALL}")
    addnumber()
fil =open(input("select output file name : ")+".pass","w")
minletters=int(input("add the min length of the pass word"))
maxletters =int(input("add the max length of the pass word"))
for a in passwords:
    if len(a) > minletters and len(a) < maxletters :
        fil.write(str(a)+"\n") 
print(f""" {Fore.RED}Results {Style.RESET_ALL}
kayen {count_results()} mdps !

it will be stored in {Fore.GREEN}pass.lst{Style.RESET_ALL}
        made by Ven_H00
""")
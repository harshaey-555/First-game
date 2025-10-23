''' stone  1
paper     0
  scissor -1



'''
import random
computer=random.choice([1,0,-1])
d=computer
print("Enter s for stone")
print("Enter p for paper")
print("Enter ss for scissors")
you_str= input("What is your choice?  ")
dict={ "s":1,"p":0,"ss":-1}
reverse_dict={1:"Stone",0:"Paper",-1:"Scissor"}
you=dict[you_str]

print(f" You chose {reverse_dict[you]}\nComputer chose {reverse_dict[d]}")
if (d==you):
    print("It's draw!")
else :
    if d==1 and you==0 :
        print("You win!")
    elif d==1 and you==-1:
        print("You lose!")
    elif d==0 and you==-1 :
        print("You win!")
    elif d==0 and you==1:
        print("You lose!")
    elif d==-1 and you==1:
        print("You win!")
    elif d==-1 and you==0:
        print("You lose!")
    else:
        print("Something went wrong!")
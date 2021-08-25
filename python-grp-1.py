#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
overs=int(input("Enter the number of overs: "))
Total_balls=(overs*6)
print("Total balls available to you will be: ",Total_balls)
score=0
n=1
game="continue"
computer_score=random.randrange(0,(overs*36)) #benchmark to reach
bench_mark=print("Score to beat: ",computer_score)
while (score<computer_score) and (n<=Total_balls):
    computer=random.randrange(0,6)
    player=int(input("Enter your number [between 1 to 6]: "))
    if(player != computer):
        score+=player
        print("Score: ",score)
    else:
        print("OUT!!!")
        #player gets out
        break
    n+=1
if(score>computer_score):
    print("Your score is ",score,"\n")
    print("Hurray!!You won the game.")
elif(score<computer_score):
    print("Your score is ",score)
    print("Sorry! Better Luck next time")
else:
    print("Oops!!Its a draw")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
def number_guessing(n):    
    n3=n
    l1=[]
    #prepared a list to compare each digit one by one
    while(n>0):                       
        rem=n%10                                                             #delete the repeitions in the generated random number
        if(rem not in l1):
            l1.append(rem)
        n//=10
    total=20
    choice="yes"
    while(choice=="yes"):
        for i in range(10,0,-1):
            n1=int(input("Enter a 4 digit number:"))
            if(n1==n3):  
                total+=5                                                  #condition to check if the provided number is equal or not
                print("All Digits in the Correct Place.You have won the game!!")
                print("Your Score :",total)
                break
            else:
                n2=n1                                                      
                l2=[]
                #prepared a list to compare each digit one by one
                while(n1>0):
                    rem=n1%10                                                    #delete the repeitions in the generated random 
                    if(rem not in l2):
                        l2.append(rem)
                    n1//=10
                l4=[]
                l5=[]
                count1=0
                count2=0
                for a in range(len(l2)):
                    for b in range(len(l1)):
                        if((l2[a]==l1[b]) and (a==b)):                 #condition to check the position and which digits are correctly guessed 
                            count1+=1
                            l4.append(l2[a])
                        elif ((l2[a]==l1[b]) and (a!=b)):
                            l5.append(l2[a])
                            count2+=1
                l4.reverse()
                l5.reverse()
                l4.extend(l5)
                total-=2
                print((count1+count2),"digits: ",l4,"guessed correctly ",count1," in the correct position and ",count2," are in the wrong position")
                print("Turns remaining - ",(i-1))
        #provided a choice to the user to play again
        choice=str(input("Do you want to play again?"))
    print("Your total score is:",total);
def main():
    n=random.randrange(1000,9999)
    number_guessing(n)
main()


# In[ ]:





# In[ ]:





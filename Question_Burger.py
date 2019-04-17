import matplotlib.pyplot as plt
import numpy as np
from math import *

def Question_type1(res1='str', res2='str', res3='str', res4='str', res5='str', res6='str', res7='str', res8='str'):
    total=8 #to be changed if more questions
    class answer:
        def __init__(self, res1, res2, res3, res4, res5, res6, res7, res8):
            self.q1 = res1
            self.q2 = res2
            self.q3 = res3
            self.q4 = res4
            self.q5 = res5
            self.q6 = res6
            self.q7 = res7
            self.q8 = res8
            
            
    answer=answer(res1, res2,res3,res4,res5,res6,res7,res8 )
    if answer.q1=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q1=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q1=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q1=='d':
        print("Incorrect, look at the second derivative.")
        
    if answer.q2=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q2=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q2=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q2=='d':
        print("Incorrect, look at the second derivative.")
        
    if answer.q3=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q3=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q3=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q3=='d':
        print("Incorrect, look at the second derivative.")
        
    if answer.q4=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q4=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q4=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q4=='d':
        print("Incorrect, look at the second derivative.")
        
    if answer.q5=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q5=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q5=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q5=='d':
        print("Incorrect, look at the second derivative.")
        
    if answer.q6=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q6=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q6=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q6=='d':
        print("Incorrect, look at the second derivative.")
        
    
    if answer.q7=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q7=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q7=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q7=='d':
        print("Incorrect, look at the second derivative.")
        
    if answer.q8=='a':
        print("correct, the equation is indeed non-linear and thus cannot be solve using regular parameter separation, and it is of the first order")
    elif answer.q8=='b':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q8=='c':
        print("Incorrect, look at the u in the equation... it is multiplying its own spatial derivation. This implies a non-linearity")
    elif answer.q8=='d':
        print("Incorrect, look at the second derivative.")

        
        
        
        
def Question_type2(res1='str', res2='str', res3='str', res4='str', res5='str', res6='str', res7='str', res8='str', Finished=False):
    total=8 #to be changed if more questions
    res=0
    class answer:
        def __init__(self, res1, res2, res3, res4, res5, res6, res7, res8, res, Validate):
            self.q1 = res1
            self.q2 = res2
            self.q3 = res3
            self.q4 = res4
            self.q5 = res5
            self.q6 = res6
            self.q7 = res7
            self.q8 = res8
            self.total=res
            self.finish=Finished
            
            
    answer=answer(res1, res2,res3,res4,res5,res6,res7,res8, res, Finished)
    if answer.q1=='a':
        answer.total+=1
    else:
        answer.total+=0
    if answer.q2=='a':
        answer.total+=1
    else:
        answer.total+=0
          
    if answer.q3=='a':
        answer.total+=1
    else:
        answer.total+=0
            
    if answer.q4=='a':
        answer.total+=1
    else:
        answer.total+=0
           
    if answer.q5=='a':
        answer.total+=1
    else:
        answer.total+=0
           
    if answer.q6=='a':
        answer.total+=1
    else:
        answer.total+=0
            
    if answer.q7=='a':
        answer.total+=1
    else:
        answer.total+=0
            
    if answer.q8=='a': 
        answer.total+=1
    else:
        answer.total+=0
    if answer.finish==True:
        print("You've responded {} correctly, out of {}".format(answer.total, total))
    else :
        print('Validate your answers when finished')
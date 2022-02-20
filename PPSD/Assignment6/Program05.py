#Description of this Program
#Author : Predee Chaiyakit
#Since : 2021-07-28
#Program Name : Statistics05
#Program Languagu : Python
#Program Purpose : practice programming skills
from math import sqrt#import square root.
import statistics as stats#import statistics.
from functools import reduce#import reduce.
def main():#Function main.
    data01 = [62,41,46,58,35,76,67,58,42,33]#data.
    def vol(n):#Data quantity function
        n = len(data01)#Declare a variable to store quantity data. 
        return n#return quantity data. 

    def min(mn):#Function min number.
        mn = reduce(lambda cv ,v:(v if v < cv else cv),data01)#Declare a variable to store the max number.
        return mn#return min number.

    def max(mx):#Function max number.
        mx = reduce(lambda cv ,v:(v if v > cv else cv),data01)#Declare a variable to store the max number.
        return mx#return max number

    def mean(mn):#Mean value function.
        mn = stats.mean(data01)#Determine the variable  mean of the data.
        return mn#return the variable  mean of the data.

    def median(md):#Median value function.
        md = stats.median(data01)#Determine the variable median of the data.
        return md#return the variable median of the data.

    def stdev(data01):#Standard deviation value function.
        n = len(data01)#Declare a variable to store quantity data. 
        xbar = sum(data01)/len(data01)#Declare a variable to store xbar. 
        total = []
        for xi in data01:#Loop Standard deviation value function.
            total.append((xbar-xi)**2)#Declare a variable to store total.
        return sqrt(sum(total)/(n-1))#return Standard deviation value function.
    print(f'Volume : {vol(data01)}')
    print(f'Min : {min(data01)}')
    print(f'Max : {max(data01)}')
    print(f'Mean : {mean(data01)}')
    print(f'Median : {median(data01)}')
    print(f'Standard deviation : {stdev(data01)}')
    print('----------------------------------------')
    data02 = [689,663,132,479,560,37,84,744,754]#data.
    def vol(n):#Data quantity function.
        n = len(data02)#Declare a variable to store quantity data.
        return n#return quantity data. 

    def min(mn):#Function min number.
        mn = reduce(lambda cv ,v:(v if v < cv else cv),data02)#Declare a variable to store the max number.
        return mn#return min number.

    def max(mx):#Function max number.
        mx = reduce(lambda cv ,v:(v if v > cv else cv),data02)#Declare a variable to store the max number.
        return mx#return max number

    def mean(mn):#Mean value function.
        mn = stats.mean(data02)#Determine the variable  mean of the data.
        return mn#return the variable  mean of the data.

    def median(md):#Median value function.
        md = stats.median(data02)#Determine the variable median of the data.
        return md#return the variable median of the data.

    def stdev(data02):#Standard deviation value function.
        n = len(data02)#Declare a variable to store quantity data. 
        xbar = sum(data02)/len(data02)#Declare a variable to store xbar.
        total = []
        for xi in data02:#Loop Standard deviation value function.
            total.append((xbar-xi)**2)#Declare a variable to store total.
        return sqrt(sum(total)/(n-1))#return Standard deviation value function.
    print(f'Volume : {vol(data02)}')
    print(f'Min : {min(data02)}')
    print(f'Max : {max(data02)}')
    print(f'Mean : {mean(data02)}')
    print(f'Median : {median(data02)}')
    print(f'Standard deviation : {stdev(data02)}')
    
    
main()#Declare use the program.

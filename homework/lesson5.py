input1 = float(input("money i start with"))#money can be decimals 
input2 = input("Enter large or small cookie")
big_sold = input2.count('b')
small_sold = input2.count('c') #.count() cycles through each element and checks if its equal to the condition 
total = big_sold + small_sold
profit1 = (2-0.75)*big_sold
profit2 = (1.25-0.5)* small_sold
totalprofit = profit1 + profit2
finalmoney = input1+totalprofit
print(f"Total cookies sold is {total}, total profit is {totalprofit}, The final amount of money is {finalmoney}")

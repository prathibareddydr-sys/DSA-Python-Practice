# Question : store apples stock price for 5 days and answer.
1.What was the price on day1
2.What was the price on day3
Ans:
stock_price = [298,305,320,301,291]
print(stock_price[0]) #stock price on day 1
print(stock_price[1]) #stock price on day 2
print(stock_price[2]) #stock price on day 3



#Question : store apples stock price from march 4 to march 7 and answer.
1.What was the price on march 7
2.Waht was the price on march 3
Ans:
stock_price = {'march 4' : 298,
               'march 5' : 305,
               'march 6' : 320,
               'march 7' : 301,
              }
print(stock_price['march 7'])       
price =(stock_price.get('march3',"data not available"))      
print(price)

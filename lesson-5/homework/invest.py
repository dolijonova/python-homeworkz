def invest(amount, rate, years):
    for i in range(years):
        amount=round((amount*rate+amount),2)
        print("year",i+1,": $",amount )


print("Enter your values in an order: amount of investment, interest rate and years")

amount=int(input())
rate=float(input())
years=int(input())

print(invest(amount,rate,years))
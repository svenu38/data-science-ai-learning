monthly_sales = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
target = 5000
for sale,month in zip(monthly_sales,month):
    if sale > target:
        print(f'sales amount {sale} has greather than target {target}')
        break
    print(f'In {month}, the sales were {sale}')
print("A month has exceeded the sales target. Stopping the report.")
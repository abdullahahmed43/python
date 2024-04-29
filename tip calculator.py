meal_price = input (' what is the meal price ?')
tip_percent = input ( ' what is the tip percent ? ' )
tip_price = int(meal_price) * int(tip_percent)/100
print (tip_price)
print("you will tip " + str(tip_price) +  " for your meal")

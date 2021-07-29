# store description
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
# price of loveseat
lovely_loveseat_price = 254.00

# adding a new furniture option
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
# price of stylish settee
stylish_settee_price = 180.50

#adding a new item
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
# price of luxurious lamp
luxurious_lamp_price = 52.15

# sales tax variable
sales_tax = .088

#first customer variable
customer_one_total = 0

# itemization variable
customer_one_itemization = ""

# customer decides to purchase loveseat adding to total
customer_one_total += lovely_loveseat_price

# adding description of loveseat to itemization
customer_one_itemization += lovely_loveseat_description

# customer decides to purchase lamp adding to total
customer_one_total += luxurious_lamp_price

# adding lamp description to itemization
customer_one_itemization += luxurious_lamp_description

# customer is ready to check out, variable to sales tax on total
customer_one_tax = customer_one_total * sales_tax

# adding sales tax to total
customer_one_total += customer_one_tax

# print heading on the receipt
print("Customer One Items")

# print itemization
print(customer_one_itemization)

# print heading for total cost on receipt
print("Customer One Total:")
# print total on receipt
print(customer_one_total)


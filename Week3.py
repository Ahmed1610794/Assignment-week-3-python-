# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(original_price, discount_percentage)

# Print the appropriate result
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")￼Enter

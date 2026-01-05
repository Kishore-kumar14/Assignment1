def calculate_bill(units):
    bill = 0.0
    
    if units <= 100:
        # First 100 units -> 2/unit
        bill = units * 2
    elif units <= 200:
        # First 100 at 2, remaining at 3
        bill = (100 * 2) + ((units - 100) * 3)
    else:
        # First 100 at 2, next 100 at 3, remaining at 5
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
        
    return bill
if __name__ == "__main__":
    print("--- Electricity Bill Calculator ---")
    try:
        units_input = int(input("Enter number of units consumed: "))
        if units_input < 0:
            print("Units cannot be negative.")
        else:
            total_bill = calculate_bill(units_input)
            print(f"Total Bill Amount: {total_bill}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
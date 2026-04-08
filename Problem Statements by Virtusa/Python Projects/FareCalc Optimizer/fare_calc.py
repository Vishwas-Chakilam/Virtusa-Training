# function to get the actual price
def get_price(distance, car, time):
    # dictionary for car prices per km
    prices = {
        'economy': 10,
        'premium': 18,
        'suv': 25
    }

    # checking if we have that car
    if car.lower() not in prices:
        return None # car not found

    km_rate = prices[car.lower()]
    total = distance * km_rate

    # surge pricing if it is between 5pm and 8pm
    peak = False
    if time >= 17 and time <= 20:
        total = total * 1.5
        peak = True

    return total, peak

def start_app():
    print("--- CityCab Trip Calculator ---")
    
    try:
        # getting data from user
        d = float(input("Enter KM: "))
        c = input("Type (Economy/Premium/SUV): ").strip().lower()
        h = int(input("Hour (0-23): "))

        if h < 0 or h > 23:
            print("Invalid hour entered!")
            return

        res = get_price(d, c, h)

        if res is None:
            print(f"Sorry, we don't have {c} cars right now.")
        else:
            final_amt, surge = res
            
            # printing the receipt
            print("\n" + "*"*25)
            print("      TRIP RECEIPT")
            print("*"*25)
            print(f"Car:      {c.capitalize()}")
            print(f"Distance: {d} KM")
            print(f"Time:     {h}:00")
            print("-" * 25)
            
            if surge:
                print("!! PEAK HOUR SURGE !!")
            
            print(f"TOTAL: ${final_amt:,.2f}")
            print("*"*25)
            print("Thanks for riding!")

    except:
        print("Error: check your inputs (numbers only for distance/hour)")

if __name__ == "__main__":
    start_app()

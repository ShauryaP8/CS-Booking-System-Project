import datetime

# Codes and prices for each stage
stage_codes = ['C1', 'C2', 'C3', 'C4', 'C5']
stage_prices = [1.50, 3.00, 4.50, 6.00, 8.00]

# Passenger accounts
passenger_accounts = []
account_counter = 1

# Bookings
bookings = []
booking_counter = 1

# Task 1: Setting up the booking system
# Already provided in the previous response


# Task 2: Using the booking system
def open_account():
    global account_counter
    name = input("Enter passenger name: ")
    passenger_accounts.append({
        'account_number': account_counter,
        'name': name
    })
    print("Account successfully created. Your account number is:",
          account_counter)
    account_counter += 1


def make_booking():
    account_number = int(input("Enter your account number: "))
    start_time_str = input("Enter start time of the journey (format: HH:MM): ")
    start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()

    # Check if passenger account exists
    account_exists = False
    for account in passenger_accounts:
        if account['account_number'] == account_number:
            account_exists = True
            break

    if not account_exists:
        print("Invalid account number. Please open an account first.")
        return

    stage_codes_input = []
    for i in range(3):
        stage_code = input("Enter code for stage {}: ".format(i + 1))
        if stage_code not in stage_codes:
            print("Invalid stage code.")
            return
        stage_codes_input.append(stage_code)

    # Generate a unique booking number
    global booking_counter
    booking_number = booking_counter
    booking_counter += 1

    # Calculate total price without discount
    total_price = sum(
        [stage_prices[stage_codes.index(code)] for code in stage_codes_input])

    # Store the journey details
    bookings.append({
        'account_number': account_number,
        'start_time': start_time,
        'stage_codes': stage_codes_input,
        'booking_number': booking_number,
        'total_price': total_price
    })

    print("Booking successful. Your booking number is:", booking_number)


# Task 3: Applying a discount and checking the entry
def apply_discount(total_price, start_time):
    if start_time > datetime.time(10, 0):
        total_price *= 0.6
    return total_price


def confirm_booking():
    booking_number = int(input("Enter your booking number: "))

    # Check if booking exists
    booking_exists = False
    for booking in bookings:
        if booking['booking_number'] == booking_number:
            booking_exists = True
            break

    if not booking_exists:
        print("Invalid booking number.")
        return

    booking = bookings[booking_number - 1]
    print("Booking Details:")
    print("Account Number:", booking['account_number'])
    print("Start Time:", booking['start_time'])
    print("Stage Codes:", booking['stage_codes'])
    print("Total Price:", booking['total_price'])

    confirmation = input("Are the details correct? (yes/no): ")
    if confirmation.lower() == "yes":
        print("Thank you for confirming.")
    else:
        print("Please start again.")


# Main program loop
while True:
    print("Integrated Transport Booking System")
    print("1. Open Account")
    print("2. Make Booking")
    print("3. Confirm Booking Details")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        open_account()
    elif choice == "2":
        make_booking()
    elif choice == "3":
        confirm_booking()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

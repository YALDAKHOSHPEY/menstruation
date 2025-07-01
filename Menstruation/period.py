import datetime

def track_menstrual_cycle():
    try:
        # Get input from the user
        cycle_length = int(input("Enter your average menstrual cycle length (in days): "))
        period_length = int(input("Enter the duration of your period (in days): "))

        # Calculate ovulation day
        ovulation_day = (cycle_length - period_length) // 2

        # Calculate fertile window
        fertile_start = ovulation_day - 5
        fertile_end = ovulation_day + 4

        # Ask if the user is currently on their period
        on_period = input("Are you currently on your period? (yes/no): ").lower()

        # Initialize today outside of the conditional block
        today = datetime.date.today()

        if on_period == "yes":
            # Calculate period start date
            period_start_date = today - datetime.timedelta(days=period_length)
            print(f"Okay, you are currently on your period. Your period started around {period_start_date}.")

            # Display ovulation day
            print(f"Your ovulation day is around day {ovulation_day}. This is when you're most fertile.")

            # Remember fertile window dates
            print(f"Your fertile window is from day {fertile_start} to {fertile_end}.")
            print("Tip: Consider tracking basal body temperature during your fertile window.")

            # Save dates to a calendar (you can customize this part)
            with open("menstrual_calendar.txt", "a") as calendar_file:
                calendar_file.write(f"Period start: {period_start_date}, Ovulation day: {ovulation_day}\n")

        else:
            # Provide general tips
            if fertile_start > 0:
                print("Tip: Consider tracking basal body temperature during your fertile window.")
            else:
                print("Tip: Consult a healthcare professional if your cycle length is irregular.")
                print("Don't forget to mark your calendar for the next cycle!")

            # Symptom tracking
            symptoms = input("Enter any symptoms you're experiencing (separated by commas): ")
            # You can store the symptoms in a database or file for future analysis.

            # Severity levels (optional)
            # severity = input("Rate the severity of your symptoms (mild/moderate/severe): ")

            # Reminder for the next cycle
            next_cycle_date = today + datetime.timedelta(days=cycle_length)
            print(f"Your next cycle is expected around {next_cycle_date}.")
            print("Remember to track your symptoms!")

            # Save dates to a calendar (you can customize this part)
            with open("menstrual_calendar.txt", "a") as calendar_file:
                calendar_file.write(f"Next cycle: {next_cycle_date}\n")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    track_menstrual_cycle()
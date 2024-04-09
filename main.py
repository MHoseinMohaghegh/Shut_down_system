# Import necessary modules
import os
import time

# Function to get shutdown time from the user


def get_shutdown_time_from_user():
    while True:
        try:
            # Prompt the user to enter shutdown time
            shutdown_time = input(
                "Enter the time in format HH:MM (24-hour format): ")
            # Split the input into hours and minutes
            shutdown_hour, shutdown_minute = map(int, shutdown_time.split(':'))
            # Check if the input time is valid
            if 0 <= shutdown_hour < 24 and 0 <= shutdown_minute < 60:
                # If valid, return the shutdown hour and minute
                return shutdown_hour, shutdown_minute
            else:
                # If invalid, prompt the user to enter a valid time
                print("Invalid time format! Please enter a valid time.")
        except ValueError:
            # Handle the case where input cannot be converted to integers
            print("Invalid time format! Please enter a valid time.")

# Function to calculate seconds until shutdown


def calculate_seconds_until_shutdown(shutdown_hour, shutdown_minute):
    # Calculate total seconds until shutdown
    timer = shutdown_hour * 3600 + shutdown_minute * 60
    # Loop until timer reaches 0
    while timer > 0:
        # Calculate hours, minutes, and seconds remaining
        hours = timer // 3600
        minutes = (timer % 3600) // 60
        seconds = timer % 60
        # Format timer as HH:MM:SS
        timer_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        # Print remaining time until shutdown
        print(f'The PC will shut down in: {timer_str}', end='\r')
        # Wait for 1 second
        time.sleep(1)
        # Decrement timer by 1 second
        timer -= 1

    # Print message indicating shutdown initiation
    print("Shutdown initiated!")
    # Execute system shutdown command with a delay of 1 second
    os.system("shutdown /s /t 1")

# Main function


def main():
    # Print welcome message
    print("Welcome to the Auto Shutdown App!")
    # Get shutdown time from the user
    shutdown_hour, shutdown_minute = get_shutdown_time_from_user()
    # Calculate seconds until shutdown
    seconds_until_shutdown = calculate_seconds_until_shutdown(
        shutdown_hour, shutdown_minute)


# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()

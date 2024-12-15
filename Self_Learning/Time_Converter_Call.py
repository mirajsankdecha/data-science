from Time_Converter import TimeConverter

def main() : 
    print("Welcome to the time program")
    value = float(input("Enter the value to convert > "))
    converter = TimeConverter(value)
    
    print("\nChoose the options : ")
    print("1. Seconds to Minutes")
    print("2. Seconds to Hours")
    print("3. Minutes to Seconds")
    print("4. Hours to Seconds")
    print("5. Hours to Minutes")
    
    choice = int(input("Enter your choice from given options > "))
    
    if choice == 1 :
        print(f"{value} second = {converter.seconds_to_minutes()} minutes")
    elif choice == 2:
        print(f"{value} seconds = {converter.seconds_to_hours()} hours")
    elif choice == 3:
        print(f"{value} minutes = {converter.minutes_to_seconds()} seconds")
    elif choice == 4:
        print(f"{value} hours = {converter.hours_to_seconds()} seconds")
    elif choice == 5:
        print(f"{value} hours = {converter.hours_to_minutes()} minutes")
    else:
        print("Invalid choice!")
        
if __name__ == "__main__" :
    main()            
from nepali_datetime import date as nep_date
import datetime

def convert_date():
    print("Choose input type:")
    print("1. Nepali Date (BS)")
    print("2. English Date (AD)")
    
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        # User inputs Nepali date
        year = int(input("Enter Nepali year (BS): "))
        month = int(input("Enter Nepali month (1-12): "))
        day = int(input("Enter Nepali day (1-32): "))

        try:
            nep = nep_date(year, month, day)
            eng = nep.to_datetime_date()
            print(f"English Date (AD): {eng}")
        except Exception as e:
            print("Invalid Nepali date:", e)

    elif choice == "2":
        # User inputs English date
        year = int(input("Enter English year (AD): "))
        month = int(input("Enter English month (1-12): "))
        day = int(input("Enter English day (1-31): "))

        try:
            eng = datetime.date(year, month, day)
            nep = nep_date.from_datetime_date(eng)
            print(f"Nepali Date (BS): {nep}")
        except Exception as e:
            print("Invalid English date:", e)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    convert_date()

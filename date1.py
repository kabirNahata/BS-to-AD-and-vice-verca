from nepali_datetime import date as nep_date
import datetime

def detect_and_convert():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    ad_date = None
    bs_date = None

    # Detect BS if year is clearly in BS range
    if year > 2100:
        try:
            # Treat as BS
            bs_date = nep_date(year, month, day)
            ad_date = bs_date.to_datetime_date()
        except Exception:
            # If failed, try as AD
            try:
                ad_date = datetime.date(year, month, day)
                bs_date = nep_date.from_datetime_date(ad_date)
            except Exception:
                print("Invalid date format for both AD and BS.")
                return
    else:
        try:
            # Treat as AD
            ad_date = datetime.date(year, month, day)
            bs_date = nep_date.from_datetime_date(ad_date)
        except Exception:
            # If failed, try as BS
            try:
                bs_date = nep_date(year, month, day)
                ad_date = bs_date.to_datetime_date()
            except Exception:
                print("Invalid date format for both AD and BS.")
                return

    print(f"Detected AD: {ad_date}")
    print(f"Detected BS: {bs_date}")

if __name__ == "__main__":
    detect_and_convert()

from nepali_datetime import date as nep_date
import datetime

def detect_and_convert():
    today = datetime.date.today()

    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    #  Try as AD first
    try:
        ad_candidate = datetime.date(year, month, day)
        bs_from_ad = nep_date.from_datetime_date(ad_candidate)
        diff1 = bs_from_ad.year - ad_candidate.year
        if ad_candidate <= today and 56 <= diff1 <= 58:
            print(f"Nepali Date (BS): {bs_from_ad}")
            return
    except Exception:
        pass

    #  Try as BS next
    try:
        bs_candidate = nep_date(year, month, day)
        ad_from_bs = bs_candidate.to_datetime_date()
        diff2 = bs_candidate.year - ad_from_bs.year
        if ad_from_bs <= today and 56 <= diff2 <= 58:
            print(f"English Date (AD): {ad_from_bs}")
            return
    except Exception:
        pass

    print("Invalid date format for both AD and BS.")

if __name__ == "__main__":
    detect_and_convert()

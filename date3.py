from nepali_datetime import date as nep_date
import datetime

def detect_and_convert():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    # Try as AD
    try:
        ad_candidate = datetime.date(year, month, day)
        bs_from_ad = nep_date.from_datetime_date(ad_candidate)
        diff1 = bs_from_ad.year - ad_candidate.year
    except Exception:
        ad_candidate, bs_from_ad, diff1 = None, None, None

    # Try as BS
    try:
        bs_candidate = nep_date(year, month, day)
        ad_from_bs = bs_candidate.to_datetime_date()
        diff2 = bs_candidate.year - ad_from_bs.year
    except Exception:
        bs_candidate, ad_from_bs, diff2 = None, None, None

    # Decision & output
    if ad_candidate and bs_from_ad and 56 <= diff1 <= 58:
        # User entered AD → print BS
        print(f"Nepali Date (BS): {bs_from_ad}")
    elif bs_candidate and ad_from_bs and 56 <= diff2 <= 58:
        # User entered BS → print AD
        print(f"English Date (AD): {ad_from_bs}")
    elif ad_candidate and bs_from_ad:
        print(f"Nepali Date (BS): {bs_from_ad}")
    elif bs_candidate and ad_from_bs:
        print(f"English Date (AD): {ad_from_bs}")
    else:
        print("Invalid date format for both AD and BS.")

if __name__ == "__main__":
    detect_and_convert()

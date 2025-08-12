from nepali_datetime import date as nep_date
import datetime

def detect_and_convert():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    ad_date = None
    bs_date = None
    is_bs = None

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

    # Decision logic
    if ad_candidate and bs_from_ad and 56 <= diff1 <= 58:
        ad_date, bs_date = ad_candidate, bs_from_ad
        is_bs = False
    elif bs_candidate and ad_from_bs and 56 <= diff2 <= 58:
        ad_date, bs_date = ad_from_bs, bs_candidate
        is_bs = True
    elif ad_candidate and bs_from_ad:
        # Fall back to AD assumption
        ad_date, bs_date = ad_candidate, bs_from_ad
        is_bs = False
    elif bs_candidate and ad_from_bs:
        # Fall back to BS assumption
        ad_date, bs_date = ad_from_bs, bs_candidate
        is_bs = True
    else:
        print("Invalid date format for both AD and BS.")
        return

    # Output
    print(f"Detected format: {'BS' if is_bs else 'AD'}")
    print(f"AD: {ad_date}")
    print(f"BS: {bs_date}")

if __name__ == "__main__":
    detect_and_convert()

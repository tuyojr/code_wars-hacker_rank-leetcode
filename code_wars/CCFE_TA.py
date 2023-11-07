def solve(haab_date: str) -> str:
    # Define the Haab month names and Tzolkin day names
    haab_months = [
        "pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin",
        "mol", "chen", "yax", "zac", "ceh", "mac", "kankin",
        "muan", "pax", "koyab", "cumhu", "uayet"
    ]

    tzolkin_days = [
        "imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik",
        "lamat", "muluk", "ok", "chuen", "eb", "ben", "ix",
        "mem", "cib", "caban", "eznab", "canac", "ahau"
    ]

    # Split the input date string and extract the day, month, and year from the input
    haab_day_month_and_year = haab_date.split()
    if len(haab_day_month_and_year) != 3:
        return ""

    day, month, year = int(haab_day_month_and_year[0][:-1]), haab_day_month_and_year[1], int(haab_day_month_and_year[2])

    # Check for valid year range and calculate the total number of days from the Haab date
    if year >= 5000 or year < 0:
        return ""

    total_days = year * 365 + haab_months.index(month) * 20 + day

    # Calculate the Tzolkin day and number
    tzolkin_number = (total_days % 13) + 1
    tzolkin_day = tzolkin_days[total_days % 20]

    return f"{tzolkin_number} {tzolkin_day} {year}"

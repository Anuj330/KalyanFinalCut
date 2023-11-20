from datetime import datetime, timedelta

def months_between_dates(start_date, end_date):
    current_date = start_date
    while current_date < end_date:
        yield current_date.strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM'
        # Move to the next month
        year = current_date.year + (current_date.month // 12)
        month = current_date.month % 12 + 1
        current_date = current_date.replace(year, month, 1)

# Example usage:
start = datetime(2022, 4, 1)  # Start date
end = datetime(2023, 12, 31)  # End date

for month in months_between_dates(start, end):
    print(month)

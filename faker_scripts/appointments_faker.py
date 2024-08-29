import csv
from faker import Faker
import datetime as dt

def main():
    # Initialize Faker
    fake = Faker()

    # Number of fake records to generate
    num_records = 20

    start_date = dt.date.today()
    end_date = dt.date.today()+dt.timedelta(5)

    # Generate fake data
    data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        time = fake.time(pattern="%H:%M:%S")  # e.g., "14:23:11"
        date = fake.date_between(start_date = start_date, end_date=end_date)  # e.g., "2024-08-30"
        condition = fake.word()  # e.g., "flu"
        data.append([first_name, last_name, time, date, condition])

    # Define CSV file path
    csv_file_path = '.data/appointments.csv'

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['FIRST', 'LAST', 'TIME', 'DATE', 'CONDITION'])
        # Write data rows
        writer.writerows(data)

    print(f"Fake data has been written to {csv_file_path}")

if __name__=='__main__':
    main()
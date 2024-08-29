import csv
from faker import Faker
from faker.providers import address
import pandas as pd

def main():

    appointments = pd.read_csv(".data/appointments.csv")

    # Initialize Faker
    fake = Faker()
    fake.add_provider(address)

    # Number of fake records to generate
    num_records = len(appointments)

    # Generate fake data
    data = []
    for _ in range(num_records):
        first_name = appointments['FIRST'].values[_]
        last_name = appointments['LAST'].values[_]
        adds = fake.street_address() 
        city = fake.city()
        state = fake.state()
        ctry = fake.current_country()
        data.append([first_name, last_name, adds, city, state, ctry])

    # Define CSV file path
    csv_file_path = '.data/address.csv'

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['FIRST', 'LAST', 'ADDRESS', 'CITY', 'STATE','COUNTRY'])
        # Write data rows
        writer.writerows(data)

    print(f"Fake data has been written to {csv_file_path}")

if __name__=='__main__':
    main()
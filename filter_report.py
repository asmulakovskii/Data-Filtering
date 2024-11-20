import sys
from data_io import read_csv
from filters import apply_filters


def display_data(data):
    if not data:
        print("No data matches the filter criteria.")
        return

    headers = data[0].keys()
    print(', '.join(headers))

    for row in data:
        print(', '.join(str(row[header]) for header in headers))


def main():
    # Hardcoded filename for the CSV file
    filename = 'advertising.csv'

    # Check if the required filter arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main.py filters")
        print("Example: python main.py Age=25-30")
        sys.exit(1)

    # sys.argv[1:] contains all filter conditions
    filters = sys.argv[1:]

    try:
        data = read_csv(filename)
        filtered_data = apply_filters(data, filters)
        display_data(filtered_data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()


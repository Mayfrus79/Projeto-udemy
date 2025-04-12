import csv
from pathlib import Path

# Make sure the filename ends with .csv
CSV = Path(__file__).parent / 'Teste_CSV.csv'

data = [
    ["Name", "Age", "Job"],
    ["SpongeBob SquarePants", 20, "Fry Cook"],
    ["Patrick Star", 21, "Unemployed"],
    ["Squidward Tentacles", 25, "Cashier"],
    ["Mr. Krabs", 50, "Restaurant Owner"],
    ["Sandy Cheeks", 22, "Scientist"],
    ["Plankton", 35, "Restaurant Owner"],
    ["Mrs. Puff", 40, "Boating School Teacher"],
    ["Pearl Krabs", 16, "Student"],
    ["Larry the Lobster", 28, "Lifeguard"]
]

if CSV.exists():
    print('The file was already created, have a nice day!')
else:
    with open(CSV, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')  # Changed to delimiter=';'
        writer.writerows(data)

    print("CSV file created successfully!")

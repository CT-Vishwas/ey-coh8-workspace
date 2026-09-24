# Create a script to read sample.csv in data folder
# use pydantic for data validation
# csv module for reading
# pathlib for file path handling, from current directory
# make it modular and reusable
import csv
from pathlib import Path
from pydantic import BaseModel, ValidationError, EmailStr

class User(BaseModel):
    name: str
    city: str
    salary: int
    email: EmailStr

def read_csv(file_path: Path):
    users = []
    with file_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                user = User(**row)
                users.append(user)
            except ValidationError as e:
                print(f"Validation error for row {row}: {e}")
    return users

if __name__ == "__main__":
    data_file = Path("data/sample.csv")
    validated_users = read_csv(data_file)
    for user in validated_users:
        print(user)
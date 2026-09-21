"""Convert the MovieLens CSV files in this folder into a single SQLite database (movies.db)."""
import sqlite3
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent
DB_PATH = DATA_DIR / "movies.db"

# Maps each CSV file to the table name it should be loaded into
CSV_TO_TABLE = {
    "movies.csv": "movies",
    "ratings.csv": "ratings",
    "tags.csv": "tags",
    "links.csv": "links",
}


def convert_csv_to_sqlite() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        for csv_name, table_name in CSV_TO_TABLE.items():
            csv_path = DATA_DIR / csv_name
            if not csv_path.exists():
                print(f"Skipping {csv_name}: file not found")
                continue

            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Loaded {len(df)} rows from {csv_name} into '{table_name}' table")

        conn.execute("CREATE INDEX IF NOT EXISTS idx_ratings_movieId ON ratings(movieId)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ratings_userId ON ratings(userId)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_tags_movieId ON tags(movieId)")
        conn.commit()

    print(f"\nDatabase created at {DB_PATH}")


if __name__ == "__main__":
    convert_csv_to_sqlite()

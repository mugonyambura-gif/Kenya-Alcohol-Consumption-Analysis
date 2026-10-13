
import pandas as pd
import pyreadstat
from pathlib import Path

folder = Path(__file__).resolve().parent
sav_file = folder / "2015 STEPS Data.sav"
csv_file = folder / "alcohol_analysis.csv"

# Read the original SPSS dataset
df, meta = pyreadstat.read_sav(str(sav_file))

# Keep only the demographic and alcohol-related columns
wanted = [
    "age", "agerange", "sex", "X1", "residence",
    "A1", "A2", "A3", "A4", "A5", "A6", "A7",
    "A8", "A9", "A10a", "A10b", "A10c", "A10d",
    "A10e", "A10f", "A10g", "A11", "A12a", "A12b",
    "A12c", "A12d", "A12e"
]

# Check for any unexpected column names
missing = [col for col in wanted if col not in df.columns]

if missing:
    print("These columns were not found:", missing)
    print("Please share this message before continuing.")
else:
    result = df[wanted].copy()

    # Add a simple row identifier
    result.insert(0, "respondent_id", range(1, len(result) + 1))

    result.to_csv(csv_file, index=False, encoding="utf-8-sig")

    print("CSV created successfully!")
    print("Rows:", len(result))
    print("Columns:", len(result.columns))
    print("Saved to:", csv_file)

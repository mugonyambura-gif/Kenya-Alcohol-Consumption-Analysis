
import pandas as pd
from pathlib import Path

# Folder containing this script
folder = Path(__file__).resolve().parent

# Find the SPSS SAV file
sav_files = list(folder.glob("*.sav"))

if not sav_files:
    print("ERROR: No .sav file found in this folder.")
    print("Move your downloaded SAV file into:")
    print(folder)
else:
    sav_file = sav_files[0]
    csv_file = folder / f"{sav_file.stem}.csv"

    print(f"Reading: {sav_file.name}")

    # Read the SPSS dataset
    df, metadata = pd.read_spss(
        sav_file,
        user_missing=True
    ), None

    # Export to CSV
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")

    print("\nConversion completed!")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns):,}")
    print(f"CSV saved to: {csv_file}")

    print("\nColumn names:")
    for column in df.columns:
        print(column)
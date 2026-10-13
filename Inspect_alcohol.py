
import pyreadstat

file_path = "2015 STEPS Data.sav"

df, meta = pyreadstat.read_sav(
    file_path,
    metadataonly=True
)

print("\n=== ALCOHOL QUESTION LABELS ===\n")

for name, label in meta.column_names_to_labels.items():
    if name.startswith("A") and name[1:2].isdigit():
        print(f"{name}: {label}")

print("\n=== RESPONSE VALUE LABELS ===\n")

for name, labels in meta.variable_value_labels.items():
    if name.startswith("A") and name[1:2].isdigit():
        print(f"\n{name}:")
        for value, meaning in labels.items():
            print(f"  {value} = {meaning}")
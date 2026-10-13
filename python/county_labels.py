import pyreadstat

df, meta = pyreadstat.read_sav(
    "2015 STEPS Data.sav",
    metadataonly=True
)

print("X1 label:", meta.column_names_to_labels.get("X1"))
print("X1 value labels:")

for variable, labels in meta.variable_value_labels.items():
    if variable == "X1":
        for code, county in labels.items():
            print(code, "=", county)

import yaml

# File paths
input_file = "postgres-operator.crunchydata.com_postgresclusters.yaml"
output_file = "trimmed_postgresclusters.yaml"

# Function to recursively remove description and examples fields
def clean_large_fields(data):
    if isinstance(data, dict):
        keys_to_remove = []
        for key, value in data.items():
            if key in ("description", "examples"):  # Fields to remove
                keys_to_remove.append(key)
            else:
                clean_large_fields(value)
        for key in keys_to_remove:
            del data[key]
    elif isinstance(data, list):
        for item in data:
            clean_large_fields(item)

# Load the CRD file
with open(input_file, "r") as file:
    crd_data = yaml.safe_load(file)

# Clean the CRD data
clean_large_fields(crd_data)

# Save the cleaned CRD to a new file
with open(output_file, "w") as file:
    yaml.dump(crd_data, file)

print(f"Trimmed CRD saved to {output_file}")


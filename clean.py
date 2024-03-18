import os
import re

# Set the path to the folder containing the markdown files
data_path = os.path.join(os.getcwd(), "data")
folder_path = os.path.join(data_path, "journal_raw")
output_file = os.path.join(data_path, "journal_cleaned.txt")

# Initialize an empty string to store the cleaned journal entries
cleaned_entries = ""

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        file_path = os.path.join(folder_path, filename)
        print(f"Processing {file_path}")

        # Read the contents of the file
        with open(file_path, "r") as file:
            content = file.read()

        # Extract the date from the first line
        date_match = re.search(r"# (\d{2}\.\d{2}\.\d{4})", content)
        if date_match:
            date = date_match.group(1)
            date_parts = date.split(".")
            day = int(date_parts[0])
            assert day >= 1 and day <= 31, f"Invalid date format: {date}"
            month = int(date_parts[1])
            assert month >= 1 and month <= 12, f"Invalid date format: {date}"
            year = int(date_parts[2])
            
            # Convert month number to month name
            month_names = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]
            month_name = month_names[month - 1]
            
            formatted_date = f"{month_name} {day}, {year}"
        else:
            formatted_date = ""

        # Extract all journal entries
        entry_matches = re.findall(
            r"(\d{1,2}:\d{2}(?:am|pm).*?)(?=\n\n|\Z)", content, re.DOTALL
        )
        for entry in entry_matches:
            cleaned_entry = entry.strip()

            # Add the formatted date and entry to the cleaned_entries string
            cleaned_entries += f"{formatted_date} at {cleaned_entry}\n"

            # Print the cleaned entry
            print(cleaned_entry)

# Write the cleaned entries to the output file
with open(output_file, "w") as file:
    file.write(cleaned_entries)

print(f"Cleaned journal entries saved to {output_file}")

# Print the intermediate results
print("Data Path:", data_path)
print("Folder Path:", folder_path)
print("Output File:", output_file)
print("Cleaned Entries:")
print(cleaned_entries)

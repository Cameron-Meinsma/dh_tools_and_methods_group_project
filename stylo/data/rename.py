import os

# Set the path to your folder with the .txt files
folder_path = "data/us_fantasy"

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        old_path = os.path.join(folder_path, filename)
        new_filename = "USF_" + filename
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed "{filename}" to "{new_filename}"')

print("All .txt files renamed successfully!")

import os

# Path to your folder with Project Gutenberg texts
folder_path = "./corpus"

# Loop through all txt files
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # Read the original content
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        # Find start and end markers
        start_idx, end_idx = 0, len(lines)
        for i, line in enumerate(lines):
            if "*** START OF" in line:
                start_idx = i + 1  # start after this line
            if "*** END OF" in line:
                end_idx = i
                break  # stop after finding END
        
        # Extract main content
        main_content = lines[start_idx:end_idx]
        
        # Overwrite the file with cleaned content
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(main_content)
        
        print(f"Cleaned {filename}")

print("All files cleaned successfully!")

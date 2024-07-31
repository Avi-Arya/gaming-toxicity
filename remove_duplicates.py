mega_dict = {}
def remove_duplicates_in_file(file_path):
    # Read lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove duplicates while preserving order
    curr_game = None
    for line in lines:
        if line == '\n': continue
        elif line.startswith("==="):
            curr_game = line[4:-4]
            curr_game = curr_game.strip()
            print(curr_game)
            continue
        else:
            if curr_game in mega_dict:
                mega_dict[curr_game].add(line)
            else:
                mega_dict[curr_game] = {line}

def remove_duplicates_across_files(file_paths):
    for file_path in file_paths:
        remove_duplicates_in_file(file_path)

def write_back_to_file(mega_dict):
    with open("video_urls.txt", "w") as file:
        for game, urls in mega_dict.items():
            file.write(f"=== {game} ===\n")
            for url in urls:
                file.write(f"{url}")
            file.write("\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py file1.txt file2.txt ...")
        sys.exit(1)

    file_paths = sys.argv[1:]

    try:
        remove_duplicates_across_files(file_paths)
        print("Duplicates removed successfully.")
        write_back_to_file(mega_dict)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
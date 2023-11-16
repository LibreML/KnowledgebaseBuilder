import os
import argparse

def is_text_file(filename):
    text_file_extensions = ['.rs', '.py', '.txt', '.md', '.js', '.css', '.html', '.json']  # Add or remove extensions as needed
    return any(filename.endswith(ext) for ext in text_file_extensions)

def process_directory(directory, output_file):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if is_text_file(filename):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    output_file.write(f"## {os.path.relpath(file_path, start=directory)}\n")
                    output_file.write(file.read() + "\n\n")

def main():
    parser = argparse.ArgumentParser(description='Combine text files into a Markdown file.')
    parser.add_argument('directory', type=str, help='Directory to search for text files')
    args = parser.parse_args()

    output_filename = 'combined_files.md'
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(f"# {os.path.basename(args.directory)}\n\n")
        process_directory(args.directory, output_file)

    print(f"All files combined into {output_filename}")

if __name__ == "__main__":
    main()

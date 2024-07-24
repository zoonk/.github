# This script will read all markdown files in the current directory and its subdirectories and write the contents to a single text file.
# It's used to create a single file that can be used to train an LLM.
# Run `python llm.py` to create the file.

import os

def write_markdown_contents_to_txt(root_dir, output_file):
    with open(output_file, 'w') as outfile:
        for subdir, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r', encoding='utf-8') as md_file:
                        outfile.write(f"{os.path.relpath(file_path, root_dir)}\n")
                        outfile.write(md_file.read())
                        outfile.write("\n\n")

root_directory = './'
output_file_path = 'llm.txt'

write_markdown_contents_to_txt(root_directory, output_file_path)

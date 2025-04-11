from pathlib import Path


orig_folder = Path.home() / 'Downloads' / 'New_folder'
sub_folder = orig_folder / 'subfolder'
text_file = sub_folder / 'File.txt'

orig_folder.mkdir(exist_ok=True)
sub_folder.mkdir(exist_ok=True)

with open(text_file, 'w', encoding='utf-8') as file:
    file.write('This is the first line')

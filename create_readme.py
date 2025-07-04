import os

BASE_DIR = r'C:\Users\User\OneDrive\Desktop\fullstack-codio-migration'  # Change this to your docs root folder if needed
HOME_LINK = '- [🏠 Full Course Overview](/README)\n'

def process_sidebar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith(HOME_LINK.strip()):
        print(f"Home link already present in {file_path}")
        return
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(HOME_LINK + '\n' + content)
    print(f"Added home link to {file_path}")

def walk_dir(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == '_sidebar.md':
                process_sidebar(os.path.join(root, file))

if __name__ == '__main__':
    walk_dir(BASE_DIR)

import os
import re

REPO_PATH = r'C:\Users\keren\fullstack-codio-migration'  # ← Change this to your course root folder

def get_first_linked_file(sidebar_path):
    if not os.path.exists(sidebar_path):
        return None
    with open(sidebar_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Match markdown links like [Title](./filename.md)
            match = re.search(r'\[.*?\]\(\./([^./][^)]+\.md)\)', line)
            if match:
                return match.group(1)
    return None

def update_module_readme(module_path):
    module_sidebar = os.path.join(module_path, '_sidebar.md')
    first_chapter = None

    # Find first chapter folder from module _sidebar.md
    if not os.path.exists(module_sidebar):
        print(f"No _sidebar.md in module {module_path}, skipping")
        return
    with open(module_sidebar, 'r', encoding='utf-8') as f:
        for line in f:
            # Match chapter folder name in sidebar, e.g. - [iterator-challenge](./iterator-challenge/README.md)
            match = re.search(r'\[.*?\]\(\./([^/]+)/README\.md\)', line)
            if match:
                first_chapter = match.group(1)
                break

    if not first_chapter:
        print(f"No chapters found in {module_path}/_sidebar.md, skipping")
        return

    chapter_path = os.path.join(module_path, first_chapter)
    chapter_sidebar = os.path.join(chapter_path, '_sidebar.md')

    # Get first file from chapter sidebar
    first_file = get_first_linked_file(chapter_sidebar)
    if not first_file:
        print(f"No linked files found in {chapter_path}/_sidebar.md, skipping")
        return

    first_file_path = os.path.join(chapter_path, first_file)
    if not os.path.exists(first_file_path):
        print(f"File {first_file_path} does not exist, skipping")
        return

    # Read first file content
    with open(first_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Write to module README.md
    readme_path = os.path.join(module_path, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {readme_path} with content from {first_file_path}")

def main():
    for module in os.listdir(REPO_PATH):
        module_path = os.path.join(REPO_PATH, module)
        if os.path.isdir(module_path) and not module.startswith('.'):
            update_module_readme(module_path)

if __name__ == '__main__':
    main()

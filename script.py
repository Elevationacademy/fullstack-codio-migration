import os

REPO_PATH = r'C:\Users\keren\fullstack-codio-migration'  # ← Set this to your course root folder

def write_clean_readme(path, title):
    readme_path = os.path.join(path, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n')

def clean_all_readmes():
    for module in os.listdir(REPO_PATH):
        module_path = os.path.join(REPO_PATH, module)
        if not os.path.isdir(module_path) or module.startswith('.'):
            continue

        write_clean_readme(module_path, module)

        for chapter in os.listdir(module_path):
            chapter_path = os.path.join(module_path, chapter)
            if not os.path.isdir(chapter_path) or chapter.startswith('.'):
                continue

            write_clean_readme(chapter_path, chapter)

if __name__ == '__main__':
    clean_all_readmes()

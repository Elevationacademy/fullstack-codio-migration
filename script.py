import os
import re

ROOT_DIR = '.'  # Your course root

def humanize(name):
    return name.replace('-', ' ').title()

def generate_root_sidebar(modules):
    lines = [f'* [{humanize(m)}]({m}/README.md)' for m in sorted(modules)]
    with open(os.path.join(ROOT_DIR, '_sidebar.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('✅ Root _sidebar.md generated.')

def generate_module_sidebar(module_path, chapters):
    lines = [f'- {humanize(os.path.basename(module_path))}']
    for chapter in sorted(chapters):
        lines.append(f'  - [{humanize(chapter)}]({chapter}/README.md)')
    with open(os.path.join(module_path, '_sidebar.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def generate_module_readme(module_path, chapters):
    lines = [f'# {humanize(os.path.basename(module_path))}', '']
    for chapter in sorted(chapters):
        lines.append(f'- [{humanize(chapter)}]({chapter}/README.md)')
    with open(os.path.join(module_path, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def extract_chapter_sidebar_entries(sidebar_path):
    entries = []
    with open(sidebar_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'\[(.*?)\]\((\.\/.*?\.md)', line.strip())
            if match:
                entries.append((match.group(1), match.group(2)))
    return entries

def generate_chapter_sidebar(chapter_path, entries, module_name):
    lines = [f'- [⬅ Back to {humanize(module_name)}](../README.md)', '']
    lines += [f'- [{label}]({path})' for label, path in entries]
    with open(os.path.join(chapter_path, '_sidebar.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def generate_chapter_readme(chapter_path, first_entry):
    label, path = first_entry
    content_path = os.path.join(chapter_path, path)
    if not os.path.exists(content_path):
        print(f'⚠️ Missing file for README.md: {content_path}')
        return
    with open(content_path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(os.path.join(chapter_path, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(f'# {label}\n\n{content.strip()}')

def process_course():
    modules = []
    for module in os.listdir(ROOT_DIR):
        module_path = os.path.join(ROOT_DIR, module)
        if not os.path.isdir(module_path) or module.startswith('.'):
            continue
        modules.append(module)
        chapters = []
        for chapter in os.listdir(module_path):
            chapter_path = os.path.join(module_path, chapter)
            if os.path.isdir(chapter_path) and not chapter.startswith('.'):
                chapters.append(chapter)

                # Process chapter _sidebar.md
                original_sidebar_path = os.path.join(chapter_path, '_sidebar.md')
                if os.path.exists(original_sidebar_path):
                    entries = extract_chapter_sidebar_entries(original_sidebar_path)
                else:
                    # Fallback to .md files if no _sidebar.md exists
                    entries = []
                    for file in sorted(os.listdir(chapter_path)):
                        if file.endswith('.md') and not file.startswith('_') and file != 'README.md':
                            label = humanize(file.replace('.md', ''))
                            entries.append((label, f'./{file}'))

                if entries:
                    generate_chapter_sidebar(chapter_path, entries, module)
                    generate_chapter_readme(chapter_path, entries[0])

        generate_module_sidebar(module_path, chapters)
        generate_module_readme(module_path, chapters)

    generate_root_sidebar(modules)

process_course()

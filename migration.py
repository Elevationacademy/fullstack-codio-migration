import os
import shutil
import tarfile
import zstandard as zstd
import re
import json
import io
import traceback

BASE_DIR = r"C:\Users\User\Downloads\FS-course-unzipped"
TARGET_DIR = r"C:\Users\User\OneDrive\Desktop\fullstack-codio-migration"

def extract_tar_zst(tar_zst_path, extract_to):
    dctx = zstd.ZstdDecompressor()
    try:
        with open(tar_zst_path, 'rb') as compressed:
            try:
                with dctx.stream_reader(compressed) as reader:
                    with tarfile.open(fileobj=reader, mode='r|*') as tar:
                        tar.extractall(path=extract_to)
            except tarfile.StreamError:
                compressed.seek(0)
                decompressed = dctx.decompress(compressed.read())
                with tarfile.open(fileobj=io.BytesIO(decompressed), mode='r:*') as tar:
                    tar.extractall(path=extract_to)
    except Exception as e:
        raise RuntimeError(f"Failed to extract {tar_zst_path}: {e}")

def clean_md_filename(filename):
    return re.sub(r'-[a-zA-Z0-9]{4,}\.md$', '.md', filename)

def fix_image_paths(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = re.sub(
        r'(!\[[^\]]*\])\((?:\.\.?/)*\.?guides/img/([^)\s]+)\)',
        r'\1(./\2)',
        content
    )

    if content != updated_content:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

def generate_sidebar(metadata_path, target_chapter_dir, chapter_title):
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"  ⚠️ Could not read metadata.json: {e}")
        return []

    lines = [f"- {chapter_title}"]
    md_filenames = []

    for section in data.get("sections", []):
        title = section.get("title")
        content_file = section.get("content-file", "")
        if not title or not content_file:
            continue
        md_name = os.path.basename(content_file)
        clean_name = clean_md_filename(md_name)
        lines.append(f'  - [{title}](./{clean_name} "{title}")')
        md_filenames.append(clean_name)

    sidebar_path = os.path.join(target_chapter_dir, "_sidebar.md")
    with open(sidebar_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    return md_filenames

def generate_test_links(module_name, chapter_name, md_filenames):
    base_url = "http://localhost:3000/#"
    return [
        f"{base_url}/{module_name}/{chapter_name}/{name}"
        for name in md_filenames
    ]

def process_chapter(module_name, chapter_file):
    chapter_name = os.path.splitext(os.path.splitext(chapter_file)[0])[0]
    module_path = os.path.join(BASE_DIR, module_name)
    chapter_tar_path = os.path.join(module_path, chapter_file)
    target_chapter_dir = os.path.join(TARGET_DIR, module_name, chapter_name)
    os.makedirs(target_chapter_dir, exist_ok=True)

    tmp_extract_path = os.path.join(module_path, "__tmp_extract__")
    if os.path.exists(tmp_extract_path):
        shutil.rmtree(tmp_extract_path)
    os.makedirs(tmp_extract_path)

    extract_tar_zst(chapter_tar_path, tmp_extract_path)

    for unwanted in [".codio", ".settings", "README.md"]:
        unwanted_path = os.path.join(tmp_extract_path, unwanted)
        if os.path.exists(unwanted_path):
            if os.path.isdir(unwanted_path):
                shutil.rmtree(unwanted_path)
            else:
                os.remove(unwanted_path)

    guides_path = os.path.join(tmp_extract_path, ".guides")
    if os.path.exists(guides_path):
        # Move JSONs
        for json_file in ["metadata.json", "book.json", "assessments.json"]:
            src = os.path.join(guides_path, json_file)
            if os.path.exists(src):
                shutil.move(src, os.path.join(target_chapter_dir, json_file))

        # Move markdown
        content_dir = os.path.join(guides_path, "content")
        if os.path.exists(content_dir):
            for md_file in os.listdir(content_dir):
                if md_file.endswith(".md"):
                    new_name = clean_md_filename(md_file)
                    target_md_path = os.path.join(target_chapter_dir, new_name)
                    shutil.move(
                        os.path.join(content_dir, md_file),
                        target_md_path
                    )
                    fix_image_paths(target_md_path)

        # Move images if any
        img_dir = os.path.join(guides_path, "img")
        if os.path.exists(img_dir) and os.listdir(img_dir):
            for img_file in os.listdir(img_dir):
                shutil.move(
                    os.path.join(img_dir, img_file),
                    os.path.join(target_chapter_dir, img_file)
                )

        shutil.rmtree(guides_path)

    for f in os.listdir(tmp_extract_path):
        full_path = os.path.join(tmp_extract_path, f)
        if os.path.isfile(full_path):
            shutil.move(full_path, os.path.join(target_chapter_dir, f))
        elif os.path.isdir(full_path):
            shutil.move(full_path, os.path.join(target_chapter_dir, f))

    shutil.rmtree(tmp_extract_path)

    metadata_path = os.path.join(target_chapter_dir, "metadata.json")
    links = []
    formatted_chapter_title = chapter_name.replace("-", " ").title()

    if os.path.exists(metadata_path):
        md_filenames = generate_sidebar(metadata_path, target_chapter_dir, formatted_chapter_title)
        links = generate_test_links(module_name, chapter_name, md_filenames)

    return chapter_name, formatted_chapter_title, links

def main():
    errors = []
    all_links = []

    for module_name in os.listdir(BASE_DIR):
        module_path = os.path.join(BASE_DIR, module_name)
        if not os.path.isdir(module_path):
            continue

        module_sidebar = []
        for chapter_file in os.listdir(module_path):
            if chapter_file.endswith(".tar.zst"):
                print(f"Processing {module_name}/{chapter_file}")
                try:
                    chapter_name, chapter_title, links = process_chapter(module_name, chapter_file)

                    if links:
                        all_links.append(f"# {module_name}/{chapter_file}")
                        all_links.extend(links)
                        all_links.append("")

                        sub_items = [f'  - [{os.path.splitext(link.split("/")[-1])[0]}]({link.replace("http://localhost:3000/#", ".")})'
                                     for link in links]
                        module_sidebar.append(f"- {chapter_title}")
                        module_sidebar.extend(sub_items)

                except Exception:
                    tb = traceback.format_exc()
                    error_msg = f"ERROR: {module_name}/{chapter_file}\n{tb}\n"
                    errors.append(error_msg)

        if module_sidebar:
            module_sidebar_path = os.path.join(TARGET_DIR, module_name, "_sidebar.md")
            with open(module_sidebar_path, "w", encoding="utf-8") as f:
                f.write("\n".join(module_sidebar) + "\n")

    if errors:
        with open(os.path.join(TARGET_DIR, "errors.txt"), "w", encoding="utf-8") as f:
            f.writelines(errors)
        print(f"\n⚠️ Finished with {len(errors)} errors. See 'errors.txt'.")

    if all_links:
        with open(os.path.join(TARGET_DIR, "links.txt"), "w", encoding="utf-8") as f:
            f.write('\n'.join(all_links))
        print(f"\n🔗 Test links saved to 'links.txt'.")

    if not errors:
        print("\n✅ All chapters processed successfully.")

if __name__ == "__main__":
    main()

import os, shutil, re

from functions_blocks import markdown_to_html_node

public_dir = "./public"
static_dir = "./static"
content_dir = "./content"

def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    copy_file_tree(static_dir, public_dir)

    generate_page("./content/index.md", "./template.html")



def generate_page(path_to_file, path_template):
    path_file = path_to_file.removeprefix(content_dir)
    path = "/".join(path_file.split("/")[:-1])
    file_name = path_to_file.split("/")[-1]
    file_name = file_name.replace("md", "html")
    print(f"Generating page from {content_dir}{path_file} to {public_dir}{path_file} using {path_template}")

    with open(path_template) as f:
        page = f.read()
    with open(path_to_file) as f:
        markdown = f.read()

    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()
    page = page.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    if not os.path.exists(f"{public_dir}{path}"):
        os.makedirs(f"{public_dir}{path}")

    with open(f"{public_dir}{path}/{file_name}", "w") as page_file:
        page_file.write(page)
    


def extract_title(markdown):
    pattern = "(?<=# )(.*?)(?=\n)"
    return re.findall(pattern, markdown)[0]

def copy_file_tree(path_from, path_to, subfolders=""):
    dir = os.listdir(f"{path_from}{subfolders}")

    for file in dir:
        if os.path.isdir(f"{path_from}{subfolders}/{file}"):
            os.mkdir(f"{path_to}{subfolders}/{file}")
            copy_file_tree(path_from, path_to, (subfolders + f"/{file}"))
        else:
            shutil.copy(f"{path_from}{subfolders}/{file}", f"{path_to}{subfolders}")
            print(f"Copied {path_from}{subfolders}/{file} to {path_to}{subfolders}/{file}")



if __name__ == "__main__":
    main()
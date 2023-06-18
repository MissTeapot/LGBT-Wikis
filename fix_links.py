"""
Script for renaming the internal links in the subreddit wikis.

Author: MissTeapot
Disclaimer: This code is absolutely shit, but it did what I needed it to do, so... ¯\_(ツ)_/¯
Runtime: ~0.5 seconds
"""

import os, re


def fix_links_batch(input_path: str, output_path: str) -> None:
    """
    Renames the internal links in the subreddit wikis for all wikis in a folder.

    All wiki pages are connected by hyperlinks, but all of those will link to the
    page on Reddit. This function simply removes the part that links to Reddit so
    that it links to the page in the folder instead.
    """

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    wiki_folders = os.listdir(input_path)

    for subreddit in wiki_folders:
        fix_links(
            root=os.path.join(input_path, subreddit).lower(),
            output_path=os.path.join(output_path, subreddit).lower()
        )


def fix_links(root: str, output_path: str) -> None:
    """Renames the internal links in the subreddit wikis for a single wiki folder."""

    # Traverse all markdown files in the wiki
    file_paths: list[str] = []
    subdir_paths: list[str] = []
    for path, subdirs, files in os.walk(root):
        for subdir in subdirs:
            x = os.path.join(path, subdir)
            subdir_paths.append(x.removeprefix(root).replace("\\", "/").removeprefix("/").lower())
        for name in files:
            file_paths.append(os.path.join(path, name).lower())

    # Make folders at output location
    os.mkdir(output_path)
    for subdir in subdir_paths:
        os.mkdir(os.path.join(output_path, subdir))

    # Fix the links
    for file in file_paths:
        with open(file, mode="r", encoding="utf-8") as fh_r:
            p = file.removeprefix(root).replace("\\", "/").removeprefix("/")
            with open(os.path.join(output_path, p), mode="w", encoding="utf-8") as fh_w:
                for line in fh_r.readlines():
                    fh_w.write(fix_line(line))


def fix_line(line: str) -> str:
    """
    Update the line to have the correct link in it
    NOTE: This only works for links formatted like so: `[text](link.url)`
    Fortunately 99 % of all internal links are like this
    """
    line_to_write = line
    matches = re.findall(r"\(w\/.*?\)", line)
    for match in matches:
        replacement = "(https://github.com/MissTeapot/LGBT-Wikis/blob/main/github_wiki/" + match.removeprefix("(w/").removesuffix(")").lower() + ".md)"
        line_to_write = line_to_write.replace(match, replacement)

    return line_to_write


def main() -> None:
    # The `w` folder is a clean folder with all headers/formatting fixed
    fix_links_batch("w", "github_wiki")


if __name__ == "__main__":
    main()

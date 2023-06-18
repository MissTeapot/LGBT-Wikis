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
    NOTE: This only works for links formatted like so: `[text](link.url#header)` or with alt-text: `[text](link.url "description")`
    as opposed to just having the link 'bare' like so: `go to the index: link.url/index` Fortunately 99.5 % of all internal links are like this
    """
    line_to_write = line

    # alt-text in hyperlink (e.g. r/estrogel)
    alt_matches = re.findall(r"\([\/]?w\/.*?\s\".*?\"\)", line)
    for a_m in alt_matches:
        if "#" in a_m:
            a_m_a, a_m_b = a_m.split("#")
            replacement = "(https://github.com/MissTeapot/LGBT-Wikis/blob/main/github_wiki/" + a_m_a.removeprefix("(w/").lower() + ".md#" + a_m_b
        else:
            a_m_a = a_m.split(" ")[0]
            replacement = "(https://github.com/MissTeapot/LGBT-Wikis/blob/main/github_wiki/" + a_m_a.removeprefix("(w/").lower() + ".md " + " ".join(a_m.split(" ")[1:])
        line_to_write = line_to_write.replace(a_m, replacement)

    # no alt-text in hyperlink
    matches = re.findall(r"\([\/]?w\/.*?\)", line)
    for m in matches:
        if "#" in m:
            m_a, m_b = m.split("#")
            replacement = "(https://github.com/MissTeapot/LGBT-Wikis/blob/main/github_wiki/" + m_a.removeprefix("(w/").lower() + ".md#" + m_b
        else:
            replacement = "(https://github.com/MissTeapot/LGBT-Wikis/blob/main/github_wiki/" + m.removeprefix("(w/").removesuffix(")").lower() + ".md)"

        line_to_write = line_to_write.replace(m, replacement)

    return line_to_write


def main() -> None:
    # The `w` folder is a clean folder with all headers/formatting fixed
    fix_links_batch("w", "github_wiki")


if __name__ == "__main__":
    main()

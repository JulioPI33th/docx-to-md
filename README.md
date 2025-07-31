# DOCX to Markdown Converter

This Python project converts `.docx` files to `.md` (Markdown), extracting any embedded images into a dedicated folder, using [Pandoc](https://pandoc.org/).

## Features

- Converts DOCX documents to Markdown format
- Extracts embedded images into `converted_md/img/`
- Compatible with MkDocs, Docusaurus, and static site generators

## Requirements

- [Pandoc](https://pandoc.org/installing.html) must be installed and available in PATH
- Python 3.8+
- Pip (for managing optional Python packages)

## Usage

1. Place your `.docx` files into the `docs/` folder.
2. Run the script:

```bash
python convert_pandoc.py
```

3. Converted Markdown files will be in the `converted_md/` folder.

## Output structure

- `converted_md/your_file.md`
- `converted_md/img/` contains all extracted images

## License

This project uses [Pandoc](https://pandoc.org/), licensed under GPL.

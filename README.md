# Static Site Generator

Tool for converting Markdown to HTML built as a Boot.dev project.

Current website - https://unluckynikolay.github.io/static-site-generator/  
Cheatsheet for Markdown - https://www.boot.dev/lessons/220f456c-ad0b-4455-a236-31f4ebab3bc5

## Installation

1. Install [Python](https://www.python.org/downloads) 3.10 or higher.

2. Clone the repository:

    ```bash
	git clone https://github.com/UnLuckyNikolay/static-site-generator
    cd static-site-generator
	```

## Usage

1. Place CSS file and images into `static/`

2. Place Markdown pages into `content/`

3. Configure `template.html` if needed

4. Run the `build` script for a ready-to-deploy website:
	```bash
	./build.sh
	```
	
	or run the `main` script to build and host locally at `http://localhost:8888`:

	```bash
	./main.sh
	```

**Note**: built website goes into `docs/` for future GitHub Pages deployment.

## Unittests

Run the `test` script:

```bash
./test.sh
```

## Supported Markdown Features

* Block elements:
	* Paragraphs
	* Headings (H1-H6)
	* Code blocks
	* Blockquotes
	* Unordered lists
	* Ordered lists

* Inline elements:
	* Bold text
	* Italic text
	* Inline code
	* Links
	* Images

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
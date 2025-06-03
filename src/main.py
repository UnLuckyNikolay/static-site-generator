from textnode import *


def main():
    textnode = TextNode("Testing this bs", TextType.LINK, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print(repr(textnode))


if __name__ == "__main__":
    main()
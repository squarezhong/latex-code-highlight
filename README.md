# Code Highlight for $\LaTeX$

[![License](https://img.shields.io/github/license/squarezhong/latex-code-highlight)](LICENSE)

## Update 2024-09-19
Redundant work, minted is a much better and easier way to achieve code highlighting in LaTeX, please refer to [Code Highlight with minted in LaTeX](https://gist.github.com/squarezhong/c844bea19d4aa60719555db0a6e84975).

## Introduction
A $\LaTeX$ package that provides both inline code and code block support for Python&Matlab.

You can view the example at [.tex](example.tex)  or [.pdf](example.pdf) format.

## Usage
Make sure you have put "codehl.sty" in the same directory with ".tex" file, then use the package by `\usepackage{codehl}` .

### Inline Code

Use  `\pycode{}` and `\mcode` to insert inline code.

### Code Block

Use `\pyblock{file path}{start line}{end line}` and `\mblock{}{}{}` to insert a code block from a file.

### Code Environment

- Use `\begin{python} ... \end{python}` to insert a Python code block directly.
- Use  `\begin{matlab} ... \end{matlab}` to insert a Matlab code block directly.

## Contribution
This project exists thanks to all the people who contribute. 

<a href="https://github.com/squarezhong/latex-code-highlight/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=squarezhong/latex-code-highlight" />
</a>

## License
[MIT](LICENSE) © Square Zhong


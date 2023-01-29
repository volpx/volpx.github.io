---
title: "Adding Latex Package"
date: 2023-01-29T18:01:00+01:00
---

To add a latex package like [tikz-timing](https://www.ctan.org/pkg/tikz-timing).

1. search it on [CTAN](https://www.ctan.org)
2. Download the zip 

{{<figure src="./Screenshot_20230129_180510.png" width="500">}}

3. extract it in `$TEXMFHOME/tex/latex/<packagename>/`
    I have `export TEXMFHOME=$LOCAL_USR/share/texmf/` in the environment.
4. `cd` to that directory
5. Run `pdflatex <packagename>.ins`
6. Run `texhash`

Now the package should be available to pdflatex.

If you are using VSCode with "LaTeX Workshop" extension then you have to tell it about the environment variable `$TEXMFHOME`.

Similarly to what is explained [here](https://tex.stackexchange.com/questions/526320/how-can-i-get-vscodes-latex-workshop-to-find-the-right-installation-of-tex).

1. go to extension settings
2. search tools
3. edit json
4. add the 'env' variable to match your `$TEXMFHOME` variable
{{<figure src="./Screenshot_20230129_193346.png" width="500">}}

The reason you have to use the absolute path is that the extension can't expand the variable as written in it's [wiki](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install)
{{<figure src="./Screenshot_20230124_165523.png" width="700">}}

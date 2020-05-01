\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{elteikthesis}[2019/06/10 ELTE FI bachelor and master thesis template]

\RequirePackage{etoolbox}
\RequirePackage{xparse}
\RequirePackage{ifthen}

\newtoggle{oneside}\toggletrue{oneside}
\newtoggle{hypenation}\toggletrue{hypenation}
\newtoggle{parspace}\togglefalse{parspace}
\newtoggle{indent}\toggletrue{indent}

\DeclareOption{nohyp}{\togglefalse{hypenation}}
\DeclareOption{parspace}{\toggletrue{parspace}}
\DeclareOption{noindent}{\togglefalse{indent}}
\DeclareOption{twoside}{
	\PassOptionsToClass{\CurrentOption}{report}
	\PassOptionsToClass{openright}{report}
	\togglefalse{oneside}
}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions \relax

\LoadClass[a4paper, 12pt, oneside]{report}

\DeclareDocumentCommand{\author}{m}{\newcommand{\authorname}{#1}\renewcommand{\@author}{#1}}
\NewDocumentCommand{\degree}{m}{\newcommand{\degreename}{#1}}

\NewDocumentCommand{\supervisor}{m}{\newcommand{\supname}{#1}}
\NewDocumentCommand{\affiliation}{m}{\newcommand{\supaff}{#1}}

\NewDocumentCommand{\extsupervisor}{m}{\newcommand{\extsupname}{#1}}
\NewDocumentCommand{\extaffiliation}{m}{\newcommand{\extsupaff}{#1}}

\NewDocumentCommand{\university}{m}{\newcommand{\univname}{#1}}
\NewDocumentCommand{\faculty}{m}{\newcommand{\facname}{#1}}
\NewDocumentCommand{\department}{m}{\newcommand{\deptname}{#1}}
\NewDocumentCommand{\city}{m}{\newcommand{\cityname}{#1}}
\NewDocumentCommand{\logo}{m}{\newcommand{\logofilename}{#1}}

\DeclareDocumentCommand{\title}{m}{\newcommand{\thesistitle}{#1}\renewcommand{\@title}{#1}}
\DeclareDocumentCommand{\date}{m}{\newcommand{\thesisyear}{#1}\renewcommand{\@date}{#1}}

\DeclareDocumentCommand{\documentlang}{m}{
	\selectlanguage{#1}

	\ifthenelse{\equal{\detokenize{#1}}{\detokenize{magyar}}}
	{
		\newcommand{\authorlabel}{Szerző}
		\newcommand{\suplabel}{Témavezető}
		\newcommand{\intsuplabel}{Belső témavezető}
		\newcommand{\extsuplabel}{Külső témavezető}

		\newcommand{\deflabel}{Definíció}
		\newcommand{\theolabel}{Tétel}
		\newcommand{\remlabel}{Emlékeztető}
		\newcommand{\notelabel}{Megjegyzés}

		\newcommand{\codelabel}{forráskód}
		\newcommand{\alglabel}{Algoritmus}

		\newcommand{\biblabel}{Irodalomjegyzék}
		\newcommand{\lstfigurelabel}{Ábrajegyzék}
		\newcommand{\lsttablelabel}{Táblázatjegyzék}
		\newcommand{\lstcodelabel}{Forráskódjegyzék}
		\newcommand{\lstnomencl}{Jelölésjegyzék}
		\newcommand{\todolabel}{Teendők listája}
		
		\newcommand{\declarationplaceholder}{Az eredeti szakdolgozati / diplomamunka témabjelentő helye.}
	}
	{
		\newcommand{\authorlabel}{Author}
		\newcommand{\suplabel}{Supervisor}
		\newcommand{\intsuplabel}{Internal supervisor}
		\newcommand{\extsuplabel}{External supervisor}

		\newcommand{\deflabel}{Definiton}
		\newcommand{\theolabel}{Theorem}
		\newcommand{\remlabel}{Remark}
		\newcommand{\notelabel}{Note}

		\newcommand{\codelabel}{Code}
		\newcommand{\alglabel}{Algorithm}

		\newcommand{\biblabel}{Bibliography}
		\newcommand{\lstfigurelabel}{List of Figures}
		\newcommand{\lsttablelabel}{List of Tables}
		\newcommand{\lstcodelabel}{List of Codes}
		\newcommand{\lstnomencl}{List of Symbols}
		\newcommand{\todolabel}{Todo list}
		
		\newcommand{\declarationplaceholder}{This page should be the original Thesis Topic Declaration.}
	}
}

\RequirePackage{fancyhdr}
\pagestyle{fancy}

\renewcommand{\chaptermark}[1]{\markboth{\thechapter.\ #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}{}}
\renewcommand{\headrulewidth}{1pt}
\renewcommand{\footrulewidth}{0pt}

\fancyhead{}
\iftoggle{oneside}{
	\fancyhead[C]{\slshape \leftmark}
}{
	\fancyhead[EC]{\slshape \leftmark}
	\fancyhead[OC]{\slshape \rightmark}
}

\topskip = 15pt
\footskip = 40pt

\fancyfoot{}
\fancyfoot[C]{\thepage}

\fancypagestyle{plain}{
	\renewcommand{\headrulewidth}{0pt}
	\fancyhf{}
    \fancyfoot[C]{\thepage}
}

\let\origdoublepage\cleardoublepage
 \newcommand{\clearemptydoublepage}{
   \clearpage
   {\pagestyle{empty}\origdoublepage}
 }
\let\cleardoublepage\clearemptydoublepage

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[english,magyar]{babel}
\RequirePackage{indentfirst}

\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage[export]{adjustbox}
\RequirePackage[center]{subfigure}
\RequirePackage{rotating}

\RequirePackage{epstopdf}
\DeclareGraphicsExtensions{.pdf,.eps,.png,.jpg}
\graphicspath{{./images/}}
\renewcommand{\listfigurename}{\lstfigurelabel}

\paperwidth 210mm
\paperheight 297mm

\RequirePackage[left=35mm, right=25mm, top=25mm, bottom=25mm]{geometry}

\iftoggle{parspace}{
	\RequirePackage{parskip}
	\iftoggle{indent}{
		\setlength{\parindent}{3.5ex}
	}{}
}{
	\nottoggle{indent}{
		\RequirePackage[skip=0pt]{parskip}
	}{
	}
}

\clubpenalty=3000
\widowpenalty=3000

\linespread{1.5}
\frenchspacing
\sloppy
\nottoggle{hypenation}{\RequirePackage[none]{hyphenat}}{}
\uchyph=0

\RequirePackage{paralist}
\RequirePackage{amsthm}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\DeclareMathAlphabet{\mathpzc}{OT1}{pzc}{m}{it}

\newtheorem{definition}{\deflabel}
\newtheorem{theorem}{\theolabel}
\newtheorem*{remark}{\remlabel}
\newtheorem*{note}{\notelabel}

\RequirePackage{color}
\RequirePackage{xcolor}
\definecolor{codebackg}{rgb}{0.95,0.95,0.95}
\definecolor{codecomment}{rgb}{0,0.6,0}
\definecolor{codestring}{rgb}{0.58,0,0.82}
\colorlet{todobackg}{orange!10}

\newcommand{\hyperrefComp}{}

\RequirePackage[pdfborder={0 0 0}, unicode, \hyperrefComp]{hyperref}
\RequirePackage[all]{hypcap}
\RequirePackage{url}
\RequirePackage{bookmark}

\RequirePackage{multirow}
\RequirePackage{longtable}
\RequirePackage{array}
\RequirePackage{makecell}
\renewcommand{\listtablename}{\lsttablelabel}

\newcommand{\superscript}[1]{\ensuremath{^{\textrm{\scriptsize{#1}}}}}
\newcommand{\subscript}[1]{\ensuremath{_{\textrm{\scriptsize{#1}}}}}

\RequirePackage{chngcntr}
\interfootnotelinepenalty=10000
\RequirePackage{appendix}
\RequirePackage[style=english]{csquotes}
\RequirePackage[
	backend=bibtex,
	style=numeric,
	sorting=none
]{biblatex}

\RequirePackage[justification=centering]{caption}
\RequirePackage[subfigure]{tocloft}

\RequirePackage{makeidx}
\makeindex

\RequirePackage[intoc,noprefix,refpage]{nomencl}
\setlength{\nomitemsep}{-\parsep}
\renewcommand{\nomlabel}[1]{\hfil \hfil #1}
\renewcommand{\pagedeclaration}[1]{, #1}
\renewcommand{\nomname}{\lstnomencl}
\makenomenclature

\RequirePackage{algorithm}
\RequirePackage{algorithmic}
\RequirePackage{listingsutf8}
\lstset{
	basicstyle=\footnotesize\ttfamily,
	numbers=left,
    numberstyle=\tiny,
    backgroundcolor=\color{codebackg},
	keywordstyle=\color{blue},
	commentstyle=\color{codecomment},
	stringstyle=\color{codestring},
	stepnumber=1,
	firstnumber=1,
	numbersep=5pt,
	showspaces=false,
	showstringspaces=false,
	showtabs=false,
	tabsize=2,
	breaklines=true,
	breakatwhitespace=false,
	float,
	frame=linesc,
	captionpos=b
}
\renewcommand{\lstlistingname}{\codelabel}
\renewcommand{\lstlistlistingname}{\lstcodelabel}
\renewcommand{\algorithmiccomment}[1]{\hfill {\it #1}}
\renewcommand{\ALG@name}{\alglabel}

\RequirePackage[textwidth=30mm, textsize=small, color=todobackg, linecolor=orange, colorinlistoftodos, shadow, obeyFinal]{todonotes}
\RequirePackage[displaymath, tightpage]{preview}
\reversemarginpar
\setlength{\marginparwidth}{30mm}

\renewcommand{\maketitle}{
	\begin{titlepage}

		\begin{center}

			\begin{tabular}{ c c }
				\multirow{4}{*}{\hspace{-1.0cm}\includegraphics[width=0.25\textwidth]{\logofilename}}

				& {\sc \Large \makecell{\univname}} \vspace{0.3cm}\\
				& {\sc \Large \makecell{\facname}} \vspace{0.5cm}\\
				& {\sc \large \makecell{\deptname}}
			\end{tabular}

			\vspace{5.0cm}
			{\bf \LARGE \thesistitle}
			\vspace{4.0cm}

			\ifdefined\extsupaff
				{\it \large \authorlabel:}\\
				{\large \authorname}\\
				\degreename\\
				\vspace{2.0cm}

				\begin{tabular}{ l c l }
					{\it \large \intsuplabel:} &
					\hspace{4.0cm} &
					{\it \large \extsuplabel:}\\

					{\large \supname} &
					\hspace{4.0cm} &
					{\large \extsupname}\\

					\supaff &
					\hspace{4.0cm} &
					\extsupaff\\
				\end{tabular}
			\else
				\vspace{1.0cm}
				\begin{tabular}{ l c l }
					{\it \large \suplabel:} &
					\hspace{4.0cm} &
					{\it \large \authorlabel:}\\

					{\large \supname} &
					\hspace{4.0cm} &
					{\large \authorname}\\

					\supaff &
					\hspace{4.0cm} &
					\degreename\\
				\end{tabular}
			\fi

			\vfill

			{\it \cityname, \thesisyear}

		\end{center}

	\end{titlepage}
}

\newcommand{\topicdeclaration}{
	\thispagestyle{empty}
	\begin{center}
		\vspace*{\fill}
		
		{\large \declarationplaceholder}
		
		\vspace*{\fill}
	\end{center}


	\cleardoublepage
	\setcounter{page}{1}
}

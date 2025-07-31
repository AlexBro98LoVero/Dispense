\LoadClass[a4paper,12pt]{article} % Classe du document

%--------------------- Packages ------------------------

\RequirePackage[italian]{babel} % Language of the document
\RequirePackage[utf8]{inputenc}
\RequirePackage[section]{placeins}
\RequirePackage[T1]{fontenc}
\RequirePackage{mathtools}
\RequirePackage{siunitx}
\RequirePackage{float}
\RequirePackage{graphicx}
\RequirePackage[justification=centering]{caption}
\RequirePackage{subcaption}
\RequirePackage{wallpaper}
\RequirePackage{nomencl}
\RequirePackage{fancyhdr}
\RequirePackage{url}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage[left=2.5cm,right=2.5cm,top=2cm,bottom=3.5cm]{geometry}

%-------------------- Report information ----------------------

\newcommand{\subject}[1]{\renewcommand{\subject}{#1}}
\newcommand{\topic}[1]{\renewcommand{\topic}{#1}}
\newcommand{\ttitle}[1]{\renewcommand{\ttitle}{#1}}
\newcommand{\professor}[1]{\renewcommand{\professor}{#1}}
\newcommand{\students}[1]{\renewcommand{\students}{#1}}
\newcommand{\logo}[1]{\renewcommand{\logo}{#1}}
\newcommand{\uni}[1]{\renewcommand{\uni}{#1}}

\newcommand{\buildmargins}{
\makenomenclature
\pagestyle{fancy}
\fancyheadoffset{1cm}
\setlength{\headheight}{2cm}
\lhead{\includegraphics[scale=0.25]{logos/feit.png}}
\rhead{\nouppercase{\leftmark}}
\rfoot{\thepage}
\cfoot{}
\lfoot{\subject}
}

\newcommand{\buildcover}{
\begin{titlepage}

	\centering
	\includegraphics[width=0.3\textwidth]{\logo}\par\vspace{1cm} % Logo insertion on the front cover
	{\scshape\LARGE \uni \par} % name of university
	\vspace{1.5cm}
    \rule{\linewidth}{0.2 mm} \\[0.4 cm]
	{\huge\bfseries \ttitle \par} \
    \rule{\linewidth}{0.2 mm} \\[1.5 cm]
	\vspace{1cm}
    
	\begin{minipage}{0.5\textwidth}
		\begin{flushleft} \large
		\emph{\textbf{Student :}}\\
        \students\\ % each student should be added using this command
		\end{flushleft}
	\end{minipage}
	~
	\begin{minipage}{0.4\textwidth}
		\begin{flushright} \large
		\emph{\textbf{Teacher :}} \\
		 \professor \\
		\end{flushright}
	\end{minipage}\\[4cm]
    
	\vfill
	{\large \today\par} % Date

\end{titlepage}
}

\newcommand{\toc}{
\tableofcontents
\newpage
}

\newcommand{\insererfigure}[4]{
\begin{figure}[ht]
\centering
\includegraphics[height=#2]{#1}
\caption{#3}
\label{fig: #4}
\end{figure}
}




\usepackage{xcolor}
\usepackage{listings}


\definecolor{maincolor}{HTML}{1E90FF}
\definecolor{arancione}{HTML}{FF4500}

% Define darker VS Code-like colors
\definecolor{vscodebg}{rgb}{0.97, 0.97, 0.97} 
\definecolor{vscodefunction}{HTML}{B9954B} % Functions (darker yellow)
\definecolor{vscodevariable}{HTML}{2F66AE} % Variables (darker blue)
\definecolor{vscodekeyword}{rgb}{0.66, 0.12, 0.36}  % Keywords (darker purple)
\definecolor{vscodecomment}{HTML}{6A9955}  % Comments (darker green)
\definecolor{vscodestring}{HTML}{975532}   % Strings (darker gold)
\definecolor{vscodeline}{rgb}{0.5, 0.5, 0.5}        % Line color (gray)

% Configure listings
\lstset{
    backgroundcolor=\color{vscodebg},
    basicstyle=\ttfamily\small\color{black},  % Basic text style
    frame=lines,                              % Lines on top and bottom
    framesep=5pt,                             % Space between frame and code
    rulecolor=\color{vscodeline},             % Frame line color
    numbers=left,                             % Line numbers on the left
    numberstyle=\tiny\color{gray},            % Style for line numbers
    numbersep=10pt,                           % Space between numbers and code
    keywordstyle=\color{vscodekeyword}\bfseries,
    commentstyle=\color{vscodecomment}\itshape,
    stringstyle=\color{vscodestring},
    showstringspaces=false,                   % Don't show spaces in strings
}

% Define custom keyword categories for functions and variables
\lstdefinelanguage{CustomPython}{
    language=Python,
    keywords=[1]{def, return, import, from, if, else, elif, for, in, while}, % Keywords
    keywords=[2]{numeroPrimo, inversoModulare, richiediChiave , inviaMessaggio, cripta, print,all, append, ord, riceviMessaggio , decripta, chr,long_to_bytes, join, stampa, isPrime, ceil, encode ,range, open, getPrime, bytes_to_long , write, sqrt, time, pow}, % Functions
    keywords=[3]{chiavePublica, chiavePrivata, p, q, n, phi, e, d, M, k, C, messaggio,  messCriptato, lett, mess_byte, cript, num, up, mess, i, f, bits, x, start, finish, bit}, % Variables
    keywordstyle=[1]\color{vscodekeyword}\bfseries,
    keywordstyle=[2]\color{vscodefunction},
    keywordstyle=[3]\color{vscodevariable},
}

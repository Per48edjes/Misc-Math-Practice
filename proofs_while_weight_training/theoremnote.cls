\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{theoremnote}[2025/05/23 Minimal theorem-proof class]

\LoadClass[10pt]{article}

% Core packages
\RequirePackage{amsmath,amssymb,amsthm}
\RequirePackage{lmodern}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{microtype}
\RequirePackage{setspace}
\setstretch{1.15}

\usepackage{enumitem}
\usepackage{etoolbox}

% Induction environment without heading
\newenvironment{induction}
  {\begin{description}[leftmargin=2em, labelsep=1em, style=nextline]}
  {\end{description}}

\newcommand{\basecase}[1]{\item[\textbf{Base Case(s).}] #1}
\newcommand{\inductivestep}[1]{\item[\textbf{Inductive Step.}] #1}
\newcommand{\inductionconclusion}[1]{\item[\textbf{Conclusion.}] #1}

% Theorem environments
\newtheorem*{theorem}{Theorem}
\newtheorem*{claim}{Claim}
\newtheorem*{lemma}{Lemma}
\newtheorem*{proposition}{Proposition}

\makeatletter
% Safe initialization
\newcommand\@mytitle{Theorem and Proof}
\newcommand\@myauthors{}
\newcommand\@mydate{\today}

% Public macros to override them
\newcommand{\settitletext}[1]{\renewcommand\@mytitle{#1}}
\newcommand{\setauthors}[1]{\renewcommand\@myauthors{#1}}
\newcommand{\setdate}[1]{\renewcommand\@mydate{#1}}
\makeatother

% Section-like wrappers
\newenvironment{ProblemStatement}{
  \section*{Statement}
}

\newenvironment{ProofSolution}{
  \section*{Solution}
}

% Compact title block
\makeatletter
\AtBeginDocument{
  \begingroup
    \renewcommand{\baselinestretch}{1.1}
    \parindent=0pt
    \vspace*{-2em}
    \begin{center}
      \ifx\@mytitle\@empty\else
        {\Large\bfseries \@mytitle \par}
        \vspace{0.5em}
      \fi
      \ifx\@myauthors\@empty\else
        {\normalsize \@myauthors \par}
        \vspace{0.5em}
      \fi
      \ifx\@mydate\@empty\else
        {\small \@mydate \par}
      \fi
    \end{center}
  \endgroup
  \vspace{0.75em}
  \hrule
  \vspace{1.25em}
}
\makeatother

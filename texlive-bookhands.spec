%global tl_name bookhands
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of book-hand fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bookhands
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a set of book-hand (Metafont) fonts and packages covering
manuscript scripts from the 1st century until Gutenberg and Caxton. The
included hands are: Square Capitals (1st century onwards); Roman Rustic
(1st-6th centuries); Insular Minuscule (6th century onwards);
Carolingian Minuscule (8th-12th centuries); Early Gothic (11th-12th
centuries); Gothic Textura Quadrata (13th-15th centuries); Gothic
Textura Prescisus vel sine pedibus (13th century onwards); Rotunda
(13-15th centuries); Humanist Minuscule (14th century onwards); Uncial
(3rd-6th centuries); Half Uncial (3rd-9th centuries); Artificial Uncial
(6th-10th centuries); and Insular Majuscule (6th-9th centuries).


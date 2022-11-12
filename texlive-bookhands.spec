Name:		texlive-bookhands
Version:	46480
Release:	1
Summary:	A collection of book-hand fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bookhands
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.r46480.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.doc.r46480.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.source.r46480.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a set of book-hand (MetaFont) fonts and packages
covering manuscript scripts from the 1st century until
Gutenberg and Caxton. The included hands are: Square Capitals
(1st century onwards); Roman Rustic (1st-6th centuries);
Insular Minuscule (6th cenury onwards); Carolingian Minuscule
(8th-12th centuries); Early Gothic (11th-12th centuries);
Gothic Textura Quadrata (13th-15th centuries); Gothic Textura
Prescisus vel sine pedibus (13th century onwards); Rotunda (13-
15th centuries); Humanist Minuscule (14th century onwards);
Uncial (3rd-6th centuries); Half Uncial (3rd-9th centuries);
Artificial Uncial (6th-10th centuries); and Insular Majuscule
(6th-9th centuries).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/bookhands
%{_texmfdistdir}/fonts/map/dvips/bookhands
%{_texmfdistdir}/fonts/source/public/bookhands
%{_texmfdistdir}/fonts/tfm/public/bookhands
%{_texmfdistdir}/fonts/type1/public/bookhands
%{_texmfdistdir}/tex/latex/bookhands
%doc %{_texmfdistdir}/doc/fonts/bookhands
#- source
%doc %{_texmfdistdir}/source/fonts/bookhands

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}

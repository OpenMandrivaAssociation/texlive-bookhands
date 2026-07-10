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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/source/fonts/bookhands
%dir %{_datadir}/texmf-dist/tex/latex/bookhands
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/auncial
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/carolmin
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/egothic
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/humanist
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/huncial
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmaj
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmin
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/pgothic
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/rotunda
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/rustic
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/sqrcaps
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/tgothic
%dir %{_datadir}/texmf-dist/doc/fonts/bookhands/uncial
%dir %{_datadir}/texmf-dist/fonts/afm/public/bookhands
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bookhands
%dir %{_datadir}/texmf-dist/fonts/source/public/bookhands
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bookhands
%dir %{_datadir}/texmf-dist/fonts/type1/public/bookhands
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/README.PRW
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/allsqrcaps.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/auncial-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/auncial-tryfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/auncial-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/auncial/allfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/auncial/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/bsamples.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/bsamples.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/carolmin-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/carolmin-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/carolmin/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/egothic-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/egothic-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/egothic/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/humanist-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/humanist-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/humanist/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/huncial-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/huncial-tryfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/huncial-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/huncial/allfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/huncial/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmaj-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmaj-tryfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmaj-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmaj/allfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmaj/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmin-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmin-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/inslrmin/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/pgothic-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/pgothic-tryfont.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/pgothic-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/pgothic/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rotunda-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rotunda-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rotunda/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rustic-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rustic-tryfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rustic-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rustic/allfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/rustic/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/sqrcaps-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/sqrcaps.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/sqrcaps/allsqrcaps.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/tgothic-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/tgothic-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/tgothic/allfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/trysqrcaps.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/trysqrcaps.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/uncial-README
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/uncial-tryfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/uncial-tryfont.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/uncial/allfont.ps.gz
%doc %{_datadir}/texmf-dist/doc/fonts/bookhands/uncial/allfont.tex
%{_datadir}/texmf-dist/fonts/afm/public/bookhands/sqrc10.afm
%{_datadir}/texmf-dist/fonts/afm/public/bookhands/sqrcb10.afm
%{_datadir}/texmf-dist/fonts/map/dvips/bookhands/sqrcaps.map
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncl17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncl7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/aunclb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/aunclb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/aunclb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncldig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncll.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncllig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/aunclpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/auncltitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/aunclu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cmin10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cmin17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cmin7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cmindig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cmintitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/cminu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egoth10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egoth17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egoth7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothdig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothtitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/egothu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hmin10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hmin17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hmin7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hmindig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hmintitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hminu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncl17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncl7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hunclb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hunclb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hunclb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncldig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncll.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncllig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hunclpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/huncltitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/hunclu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imaj10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imaj17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imaj7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajdig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imajtitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imaju.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imin10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imin17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imin7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imindig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/imintitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/iminu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgoth10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgoth17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgoth7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothdig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothtitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/pgothu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtnd10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtnd17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtnd7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtnddig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndtitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rtndu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rust10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rust17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rust7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustdig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rusttitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/rustu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothdig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothr17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothr7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothtitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/tgothu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncl17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncl7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/unclb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/unclb17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/unclb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncldig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncll.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncllig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/unclpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/uncltitle.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bookhands/unclu.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/auncl17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/auncl7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/aunclb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/aunclb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/cmin10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/cmin17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/cmin7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/cminb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/cminb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/cminb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/egoth10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/egoth17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/egoth7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/egothb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/egothb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/egothb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hmin10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hmin17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hmin7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hminb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hminb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hminb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/huncl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/huncl17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/huncl7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hunclb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hunclb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/hunclb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imaj10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imaj17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imaj7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imajb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imajb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imajb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imin10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imin17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/imin7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/iminb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/iminb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/iminb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/pgoth10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/pgoth17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/pgoth7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/pgothb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/pgothb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rtnd10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rtnd17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rtnd7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rtndb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rtndb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rtndb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rust10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rust17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rust7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rustb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rustb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/rustb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/sqrc10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/sqrcb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/tgothb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/tgothb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/tgothr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/tgothr17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/tgothr7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/uncl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/uncl17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/uncl7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/unclb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/unclb17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bookhands/unclb7.tfm
%{_datadir}/texmf-dist/fonts/type1/public/bookhands/sqrc10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bookhands/sqrcb10.pfb
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/auncial.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/auncial.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/carolmin.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/carolmin.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/egothic.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/egothic.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/humanist.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/humanist.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/huncial.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/huncial.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/inslrmaj.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/inslrmaj.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/inslrmin.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/inslrmin.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/pgothic.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/pgothic.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/rotunda.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/rotunda.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/rustic.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/rustic.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/sqrcaps.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/sqrcaps.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/tgothic.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/tgothic.ins
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/uncial.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bookhands/uncial.ins
%{_datadir}/texmf-dist/tex/latex/bookhands/allcmin.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allegoth.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allhmin.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allhuncl.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allimaj.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allimin.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allpgoth.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allrtnd.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allrust.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/allsqrc.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/alltgoth.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/alluncl.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/carolmin.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/egothic.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/humanist.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/huncial.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/inslrmaj.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/inslrmin.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1auncl.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1cmin.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1egoth.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1hmin.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1huncl.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1imaj.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1imin.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1pgoth.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1rtnd.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1rust.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1sqrc.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1tgoth.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/ot1uncl.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/pgothic.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/rotunda.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/rustic.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/sqrcaps.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/t1auncl.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1cmin.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1egoth.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1hmin.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1huncl.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1imaj.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1imin.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1pgoth.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1rtnd.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1rust.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1sqrc.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1tgoth.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/t1uncl.fd
%{_datadir}/texmf-dist/tex/latex/bookhands/tgothic.sty
%{_datadir}/texmf-dist/tex/latex/bookhands/uncial.sty

# revision 23609
# category Package
# catalog-ctan /fonts/bookhands
# catalog-date 2008-01-03 17:18:54 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-bookhands
Version:	20170414
Release:	2
Summary:	A collection of book-hand fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bookhands
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookhands.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/bookhands/sqrc10.afm
%{_texmfdistdir}/fonts/afm/public/bookhands/sqrcb10.afm
%{_texmfdistdir}/fonts/map/dvips/bookhands/sqrcaps.map
%{_texmfdistdir}/fonts/source/public/bookhands/auncl10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/auncl17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/auncl7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/aunclb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/aunclb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/aunclb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/auncldig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/auncll.mf
%{_texmfdistdir}/fonts/source/public/bookhands/auncllig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/aunclpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/auncltitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/aunclu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cmin10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cmin17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cmin7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cmindig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cmintitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/cminu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egoth10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egoth17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egoth7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothdig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothtitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/egothu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hmin10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hmin17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hmin7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hmindig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hmintitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hminu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncl10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncl17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncl7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hunclb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hunclb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hunclb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncldig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncll.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncllig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hunclpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/huncltitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/hunclu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imaj10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imaj17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imaj7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajdig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imajtitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imaju.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imin10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imin17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imin7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imindig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/imintitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/iminu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgoth10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgoth17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgoth7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothdig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothtitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/pgothu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtnd10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtnd17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtnd7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtnddig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndtitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rtndu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rust10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rust17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rust7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustdig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustl.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustlig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rusttitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/rustu.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncl10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncl17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncl7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/unclb10.mf
%{_texmfdistdir}/fonts/source/public/bookhands/unclb17.mf
%{_texmfdistdir}/fonts/source/public/bookhands/unclb7.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncldig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncll.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncllig.mf
%{_texmfdistdir}/fonts/source/public/bookhands/unclpunct.mf
%{_texmfdistdir}/fonts/source/public/bookhands/uncltitle.mf
%{_texmfdistdir}/fonts/source/public/bookhands/unclu.mf
%{_texmfdistdir}/fonts/tfm/public/bookhands/auncl17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/auncl7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/aunclb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/aunclb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/cmin10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/cmin17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/cmin7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/cminb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/cminb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/cminb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/egoth10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/egoth17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/egoth7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/egothb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/egothb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/egothb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hmin10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hmin17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hmin7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hminb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hminb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hminb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/huncl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/huncl17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/huncl7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hunclb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hunclb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/hunclb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imaj10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imaj17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imaj7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imajb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imajb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imajb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imin10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imin17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/imin7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/iminb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/iminb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/iminb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/pgoth10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/pgoth17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/pgoth7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/pgothb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/pgothb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rtnd10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rtnd17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rtnd7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rtndb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rtndb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rtndb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rust10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rust17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rust7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rustb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rustb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/rustb7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/sqrc10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/sqrcb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/uncl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/uncl17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/uncl7.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/unclb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/unclb17.tfm
%{_texmfdistdir}/fonts/tfm/public/bookhands/unclb7.tfm
%{_texmfdistdir}/fonts/type1/public/bookhands/sqrc10.pfb
%{_texmfdistdir}/fonts/type1/public/bookhands/sqrcb10.pfb
%{_texmfdistdir}/tex/latex/bookhands/allcmin.sty
%{_texmfdistdir}/tex/latex/bookhands/allegoth.sty
%{_texmfdistdir}/tex/latex/bookhands/allhmin.sty
%{_texmfdistdir}/tex/latex/bookhands/allhuncl.sty
%{_texmfdistdir}/tex/latex/bookhands/allimaj.sty
%{_texmfdistdir}/tex/latex/bookhands/allimin.sty
%{_texmfdistdir}/tex/latex/bookhands/allpgoth.sty
%{_texmfdistdir}/tex/latex/bookhands/allrtnd.sty
%{_texmfdistdir}/tex/latex/bookhands/allrust.sty
%{_texmfdistdir}/tex/latex/bookhands/allsqrc.sty
%{_texmfdistdir}/tex/latex/bookhands/alluncl.sty
%{_texmfdistdir}/tex/latex/bookhands/carolmin.sty
%{_texmfdistdir}/tex/latex/bookhands/egothic.sty
%{_texmfdistdir}/tex/latex/bookhands/humanist.sty
%{_texmfdistdir}/tex/latex/bookhands/huncial.sty
%{_texmfdistdir}/tex/latex/bookhands/inslrmaj.sty
%{_texmfdistdir}/tex/latex/bookhands/inslrmin.sty
%{_texmfdistdir}/tex/latex/bookhands/ot1auncl.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1cmin.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1egoth.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1hmin.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1huncl.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1imaj.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1imin.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1pgoth.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1rtnd.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1rust.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1sqrc.fd
%{_texmfdistdir}/tex/latex/bookhands/ot1uncl.fd
%{_texmfdistdir}/tex/latex/bookhands/pgothic.sty
%{_texmfdistdir}/tex/latex/bookhands/rotunda.sty
%{_texmfdistdir}/tex/latex/bookhands/rustic.sty
%{_texmfdistdir}/tex/latex/bookhands/sqrcaps.sty
%{_texmfdistdir}/tex/latex/bookhands/t1auncl.fd
%{_texmfdistdir}/tex/latex/bookhands/t1cmin.fd
%{_texmfdistdir}/tex/latex/bookhands/t1egoth.fd
%{_texmfdistdir}/tex/latex/bookhands/t1hmin.fd
%{_texmfdistdir}/tex/latex/bookhands/t1huncl.fd
%{_texmfdistdir}/tex/latex/bookhands/t1imaj.fd
%{_texmfdistdir}/tex/latex/bookhands/t1imin.fd
%{_texmfdistdir}/tex/latex/bookhands/t1pgoth.fd
%{_texmfdistdir}/tex/latex/bookhands/t1rtnd.fd
%{_texmfdistdir}/tex/latex/bookhands/t1rust.fd
%{_texmfdistdir}/tex/latex/bookhands/t1sqrc.fd
%{_texmfdistdir}/tex/latex/bookhands/t1uncl.fd
%{_texmfdistdir}/tex/latex/bookhands/uncial.sty
%doc %{_texmfdistdir}/doc/fonts/bookhands/README.PRW
%doc %{_texmfdistdir}/doc/fonts/bookhands/allsqrcaps.pdf
%doc %{_texmfdistdir}/doc/fonts/bookhands/auncial-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/auncial-tryfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/auncial-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/auncial/allfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/auncial/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/bsamples.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/bsamples.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/carolmin-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/carolmin-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/carolmin/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/egothic-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/egothic-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/egothic/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/humanist-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/humanist-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/humanist/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/huncial-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/huncial-tryfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/huncial-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/huncial/allfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/huncial/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmaj-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmaj-tryfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmaj-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmaj/allfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmaj/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmin-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmin-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/inslrmin/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/pgothic-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/pgothic-tryfont.pdf
%doc %{_texmfdistdir}/doc/fonts/bookhands/pgothic-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/pgothic/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/rotunda-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/rotunda-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/rotunda/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/rustic-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/rustic-tryfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/rustic-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/rustic/allfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/rustic/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/sqrcaps-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/sqrcaps.pdf
%doc %{_texmfdistdir}/doc/fonts/bookhands/sqrcaps/allsqrcaps.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/tgothic/README
%doc %{_texmfdistdir}/doc/fonts/bookhands/tgothic/allfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/tgothic/tgothic.dtx
%doc %{_texmfdistdir}/doc/fonts/bookhands/tgothic/tgothic.ins
%doc %{_texmfdistdir}/doc/fonts/bookhands/tgothic/tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/trysqrcaps.pdf
%doc %{_texmfdistdir}/doc/fonts/bookhands/trysqrcaps.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/uncial-README
%doc %{_texmfdistdir}/doc/fonts/bookhands/uncial-tryfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/uncial-tryfont.tex
%doc %{_texmfdistdir}/doc/fonts/bookhands/uncial/allfont.ps.gz
%doc %{_texmfdistdir}/doc/fonts/bookhands/uncial/allfont.tex
#- source
%doc %{_texmfdistdir}/source/fonts/bookhands/auncial.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/auncial.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/carolmin.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/carolmin.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/egothic.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/egothic.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/humanist.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/humanist.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/huncial.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/huncial.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/inslrmaj.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/inslrmaj.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/inslrmin.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/inslrmin.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/pgothic.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/pgothic.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/rotunda.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/rotunda.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/rustic.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/rustic.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/sqrcaps.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/sqrcaps.ins
%doc %{_texmfdistdir}/source/fonts/bookhands/uncial.dtx
%doc %{_texmfdistdir}/source/fonts/bookhands/uncial.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080103-2
+ Revision: 749834
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080103-1
+ Revision: 717965
- texlive-bookhands
- texlive-bookhands
- texlive-bookhands
- texlive-bookhands
- texlive-bookhands


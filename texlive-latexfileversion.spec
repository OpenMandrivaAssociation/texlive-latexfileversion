# revision 25012
# category Package
# catalog-ctan /support/latexfileversion
# catalog-date 2012-01-02 14:24:13 +0100
# catalog-license lppl
# catalog-version v0.3
Name:		texlive-latexfileversion
Version:	v0.3
Release:	1
Summary:	Prints the version and date of a LaTeX class or style file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexfileversion
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileversion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileversion.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-latexfileversion.bin

%description
This simple shell script prints the version and date of a LaTeX
class or style file. Syntax: latexfileversion <file> This
programme handles style files (extension .sty), class files
(extension .cls), and other tex input files. The file extension
must be given.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/latexfileversion/latexfileversion
%doc %{_texmfdistdir}/doc/support/latexfileversion/ChangeLog
%doc %{_texmfdistdir}/doc/support/latexfileversion/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}

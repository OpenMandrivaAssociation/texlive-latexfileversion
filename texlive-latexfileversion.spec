# revision 29349
# category Package
# catalog-ctan /support/latexfileversion
# catalog-date 2012-05-22 13:29:11 +0200
# catalog-license lppl
# catalog-version v0.3
Name:		texlive-latexfileversion
Version:	v0.3
Release:	6
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
Provides:	texlive-latexfileversion.bin = %{EVRD}

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
%{_bindir}/latexfileversion
%{_texmfdistdir}/scripts/latexfileversion/latexfileversion
%doc %{_texmfdistdir}/doc/support/latexfileversion/ChangeLog
%doc %{_texmfdistdir}/doc/support/latexfileversion/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/latexfileversion/latexfileversion latexfileversion
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}

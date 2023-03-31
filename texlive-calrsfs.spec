Name:		texlive-calrsfs
Version:	17125
Release:	2
Summary:	Copperplate calligraphic letters in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calrsfs
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calrsfs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calrsfs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a maths interface to the rsfs fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calrsfs/OMSrsfs.fd
%{_texmfdistdir}/tex/latex/calrsfs/calrsfs.sty
%doc %{_texmfdistdir}/doc/latex/calrsfs/README
%doc %{_texmfdistdir}/doc/latex/calrsfs/calrsfs.pdf
%doc %{_texmfdistdir}/doc/latex/calrsfs/calrsfs.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

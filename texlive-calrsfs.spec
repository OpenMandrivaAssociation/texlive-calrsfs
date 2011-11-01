Name:		texlive-calrsfs
Version:	20100220
Release:	1
Summary:	Copperplate calligraphic letters in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calrsfs
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calrsfs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calrsfs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides a maths interface to the rsfs fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

# revision 17125
# category Package
# catalog-ctan /macros/latex/contrib/calrsfs
# catalog-date 2010-02-20 21:59:31 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-calrsfs
Version:	20100220
Release:	3
Summary:	Copperplate calligraphic letters in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calrsfs
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calrsfs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calrsfs.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100220-2
+ Revision: 749965
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100220-1
+ Revision: 717997
- texlive-calrsfs
- texlive-calrsfs
- texlive-calrsfs
- texlive-calrsfs
- texlive-calrsfs


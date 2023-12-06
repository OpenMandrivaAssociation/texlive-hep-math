Name:		texlive-hep-math
Version:	67632
Release:	1
Summary:	Extended math macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep-math
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-math.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-math package provides some additional features beyond
the mathtools and amsmath packages. To use the package place
\usepackage{hep-math} in the preamble

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-math
%{_texmfdistdir}/tex/latex/hep-math
%doc %{_texmfdistdir}/doc/latex/hep-math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

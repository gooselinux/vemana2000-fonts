%global fontname vemana2000
%global fontconf 69-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.1.2
Release: 3%{?dist}
Summary: Unicode compliant OpenType font for Telugu

Group: User Interface/X
License: GPLv2+ with exceptions
URL: http://www.kavya-nandanam.com/dload.htm

Source0: http://www.kavya-nandanam.com/Vemana2k-Li.zip
Source1: %{name}-fontconfig.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch
BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description
A free OpenType font for Telugu created by
Dr. Tirumala Krishna Desikacharyulu. 

%prep
%setup -q -c -n %{name}
sed -i 's/\r//' gpl.txt

%build

%install
rm -fr %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p vemana2000.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
 %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
 %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -fr %{buildroot}

%_font_pkg -f %{fontconf} vemana2000.ttf

%doc gpl.txt

%changelog
* Tue Feb 02 2010 Sandeep Shedmake <sshedmak@redhat.com> - 1.1.2-3
- Fixed Source0 url
- Resolves: rhbz#560879

* Tue Feb 02 2010 Sandeep Shedmake <sshedmak@redhat.com> - 1.1.2-2
- Resolves: rhbz#560879

* Tue Dec 15 2009 Sandeep Shedmake <sshedmak@redhat.com> - 1.1.2-1
- Rebase from upstream for RHEL 6
- Resolves: bug 547620

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1.1-2.1
- Rebuilt for RHEL 6

* Tue Aug 31 2009 <sshedmak@redhat.com> - 1.1.1-2
- Changed the Pothana2000 strings to Vemana2000

* Tue Jun 23 2009 <sshedmak@redhat.com> - 1.1.1-1
- Initial packaging

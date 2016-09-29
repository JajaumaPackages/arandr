Name:           arandr
Version:        0.1.9
Release:        1%{?dist}
Summary:        Another XRandR GUI

License:        GPLv3
URL:            https://christian.amsuess.com/tools/arandr/
Source0:        http://christian.amsuess.com/tools/arandr/files/arandr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python-docutils
BuildRequires:  gettext
BuildRequires:  python-setuptools
BuildRequires:  desktop-file-utils
Requires:       python
Requires:       pygtk2
Requires:       xorg-x11-server-utils

%description
ARandR is designed to provide a simple visual front end for XRandR. Relative
monitor positions are shown graphically and can be changed in a drag-and-drop
way.

%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/arandr.desktop
%find_lang %{name}


%files -f %{name}.lang
%doc README TODO ChangeLog NEWS COPYING
%{_bindir}/*
%{python_sitelib}/screenlayout/
%{python_sitelib}/arandr-%{version}-py*.egg-info
%{_mandir}/man1/*.1*
%{_datadir}/applications/*.desktop


%changelog
* Thu Sep 29 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.9-1
- Public release

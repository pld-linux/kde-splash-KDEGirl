
%define		_splash		KDEGirl

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	03
Release:	5
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	%{_splash}-%{version}.zip
# Source0-md5:	c773e8219631b496aba14ae3ddba8658
Source1:        %{name}-themerc
URL:		http://www.kde-look.org/content/show.php?content=1706
BuildRequires:	unzip
Requires:	kdebase-desktop
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"KDE Girl" KDE splash screen.

%description -l pl
Ekran startowy KDE "KDE Girl".

%package -n kde-logoutpic-%{_splash}
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Requires:	kdebase-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic
Obsoletes:	kde-sdscreen

%description -n kde-logoutpic-%{_splash}
"KDE Girl" KDE "Logout" picture.

%description -n kde-logoutpic-%{_splash} -l pl
Obrazek "KDE Girl" okna "Wyloguj" KDE.

%prep
%setup  -q -c -T
unzip %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash} \
	$RPM_BUILD_ROOT%{_datadir}/apps/ksmserver/pics

install splash*.png $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install shutdownkonq.png $RPM_BUILD_ROOT%{_datadir}/apps/ksmserver/pics

install %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}

%files -n kde-logoutpic-%{_splash}
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/pics/shutdownkonq.png

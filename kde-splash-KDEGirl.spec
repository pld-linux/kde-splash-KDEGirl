
%define		_splash		KDEGirl

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	03
Release:	4
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	%{_splash}-%{version}.zip
URL:		http://www.kde-look.org/content/show.php?content=1706
BuildRequires:	unzip
Provides:	kde-splash
Obsoletes:	kde-splash
Obsoletes:	kde-splash-default
Obsoletes:	kde-splash-keramik
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
"KDE Girl" KDE splash screen.

%description -l pl
Ekran startowy KDE "KDE Girl".

%package -n kde-sdscreen-%{_splash}
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Provides:	kde-sdscreen
Obsoletes:	kde-sdscreen
Obsoletes:	kde-sdscreen-default

%description -n kde-sdscreen-%{_splash}
"KDE Girl" KDE "Logout" picture.

%description -n kde-sdscreen-%{_splash} -l pl
Obrazek "KDE Girl" okna "Wyloguj" KDE.

%prep
%setup  -q -c -T
unzip %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/pics"
install -d "$RPM_BUILD_ROOT/%{_datadir}/apps/ksmserver/pics"
install * "$RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/pics"

mv $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/pics/shutdownkonq.png \
	$RPM_BUILD_ROOT/%{_datadir}/apps/ksmserver/pics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*

%files -n kde-sdscreen-%{_splash}
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/*


%define		_splash		KDEGirl

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	03
Release:	8
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	%{_splash}-%{version}.zip
# Source0-md5:	c773e8219631b496aba14ae3ddba8658
URL:		http://www.kde-look.org/content/show.php?content=1706
BuildRequires:	unzip
Provides:	kde-splash
Requires:	kdebase-core >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"KDE Girl" KDE splash screen.

%description -l pl
Ekran startowy KDE "KDE Girl".

%package -n kde-sdscreen-%{_splash}
Summary:	KDE "Logout" picture
Summary(pl):	Obrazek okna "Wyloguj" KDE
Group:		X11/Amusements
Provides:	kde-sdscreen
Requires:	kdebase-core
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
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksmserver/pics
mv shutdownkonq.png $RPM_BUILD_ROOT%{_datadir}/apps/ksmserver/pics

install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
cp * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

cat > $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc << _EOF_
[KSplash Theme: %{_splash}]
Name = %{_splash} Splash Theme
Description = This is a %{_splash} Splash Screen for KDE
Engine = Default
Version = %{version}
Icons Flashing = true
_EOF_

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}

%files -n kde-sdscreen-%{_splash}
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/*

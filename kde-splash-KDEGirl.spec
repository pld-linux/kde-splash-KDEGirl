
%define		_splash		KDEGirl

Summary:	"KDE Girl" splash screen
Summary(pl):	Ekran startowy "KDE Girl"
Name:		kde-splash-%{_splash}
Version:	03
Release:	2
License:	GPL
Group:		Themes/Gtk
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	%{_splash}-%{version}.zip
URL:		http://www.kde-look.org/content/show.php?content=1706
Obsoletes:	kde-splash
Provides:	kde-splash
BuildRequires:	unzip
Requires:	kdebase >= 3.0.2-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
"KDE Girl" splash screen.

%description -l pl
Ekran startowy "KDE Girl".

%package -n kde-sdscreen-%{_splash}
Summary:	"KDE Girl" Logout logo
Summary(pl):	Logo okna  Logout "KDE Girl"
Group:		Themes/Gtk
Requires:	kdebase >= 3.0.2-7
Obsoletes:	kde-sdscreen
Provides:	kde-sdscreen

%description -n kde-sdscreen-%{_splash}
"KDE Girl" Logout logo.

%description -n kde-sdscreen-%{_splash} -l pl
Logo okna  Logout "KDE Girl".

%prep
%setup  -q -c -T
unzip %{SOURCE0}

%build

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
%{_datadir}/apps/ksplash/pics/*

%files -n kde-sdscreen-%{_splash}
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/pics/*

Name:		qarma
Summary:	Call Qt dialog boxes from the command line
Version:	0.20180619
Release:	2
License:	LGPLv2+
Group:		Development/KDE and Qt
URL:		https://github.com/luebking/qarma
Source0:	https://github.com/luebking/qarma/archive/master.tar.gz

BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5X11Extras)

Requires(post,preun):	update-alternatives

# Not exactly, but qarma 20180619 should be pretty much feature
# compatible with zenity 3.32.0-1
Provides:	zenity = 3.32.0-1
Obsoletes:	zenity < 3.32.0-1

%description
Qarma allows you to display dialog boxes from the commandline and shell
scripts.

It is a drop-in replacement for the GTK based zenity tool.

%prep
%autosetup -p1 -n qarma-master
qmake-qt5 *.pro

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/zenity zenity %{_bindir}/qarma 50

%preun
%{_sbindir}/update-alternatives --remove zenity %{_bindir}/qarma

%files
%{_bindir}/*

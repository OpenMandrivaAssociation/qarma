%define debug_package %{nil}
Name:		qarma
Summary:	Call Qt dialog boxes from the command line
Version:	0.20240419
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
URL:		https://github.com/luebking/qarma
Source0:	https://github.com/luebking/qarma/archive/master.tar.gz

BuildRequires:	qmake-qt6
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6DBus)

Requires(post,preun):	update-alternatives

# Not exactly, but qarma 20180619 should be pretty much feature
# compatible with zenity 3.32.0-1
Provides:	zenity = 3.32.0-1
Obsoletes:	zenity < 3.32.0-1

%patchlist
dont-error-out-when-called-by-absolute-path.patch
autoclose-on-closed-stdin.patch

%description
Qarma allows you to display dialog boxes from the commandline and shell
scripts.

It is a drop-in replacement for the GTK based zenity tool.

%prep
%autosetup -p1 -n qarma-master
%{_qtdir}/bin/qmake6 *.pro

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

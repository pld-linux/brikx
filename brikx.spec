Summary:	Puzzle game
Summary(pl.UTF-8):	Gra logiczna
Name:		brikx
Version:	0.4.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/brikx/%{name}-%{version}-src.tar.bz2
# Source0-md5:	7a2a034d71d074bf75e289adbaaefc44
URL:		http://sourceforge.net/projects/brikx/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small puzzle game in which your goal is to remove all tiles. You are
held up by other tiles, gravity, walls, and other things.

%description -l pl.UTF-8
Mała gra logiczna, w której celem gracza jest pozbycie się wszystkich
kulek. W dokonaniu tego przeszkadzają inne kulki, grawitacja, ściany
oraz inne rzeczy.

%prep
%setup -q -n %{name}
%{__sed} -i 's@data@%{_datadir}/%{name}@' src/brikx.h

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r src/data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

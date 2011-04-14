Name:           gnome-shell-extensions-gajim
Version:        3.0.0
Release:        2.6d56cfgit%{?dist}
Summary:        GNOME Shell Extension for Gajim IM Client
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            http://live.gnome.org/GnomeShell/Extensions

#  using git archive since upstream hasn't created tarballs.  Picking up a post 3.0.0 release snapshot for a couple of minor but relevant changes
#  git archive --format=tar --prefix=gnome-shell-extensions/ git_commithash  | xz  > gnome-shell-extensions-<git_commithash_abbr>.tar.xz
Source0:       gnome-shell-extensions-6d56cf.tar.xz  

# since we build from a git checkout
BuildRequires:  gnome-common
BuildRequires:  intltool

BuildRequires:  glib2-devel
Requires:       gnome-shell
Requires:       gnome-shell-extensions-common
Requires:       gajim >= 0.15
BuildArch:      noarch


%description
GNOME Shell Extension for Gajim IM Client


%prep
%setup -q -n gnome-shell-extensions


%build
# since we build from a git checkout
[ -x autogen.sh ] && NOCONFIGURE=1 ./autogen.sh 

%configure  --enable-extensions="gajim"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# locales are in gnome-shell-extensions-common
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale


%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/gnome-shell/extensions/gajim*


%changelog
* Thu Apr 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 3.0.0-2.6d56cfgit
- require gnome-shell-extensions-common not gnome-shell-extensions-gajim-common

* Thu Apr 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 3.0.0-1.6d56cfgit
- build gajim extension

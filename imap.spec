Summary:	provides support for IMAP and POP network mail protocols
Summary(de):	Bietet Unterstützung für IMAP- und POP-Netz-Mail-Protokolle
Summary(fr):	Fournit un support pour les protocoles de mail IMAP et POP.
Summary(pl):	Wspomaganie dla protoko³ów pocztowych IMAP i POP 
Summary(tr):	IMAP ve POP posta indirme protokollarý için sunucu
Name:		imap
Version:	4.5
Release:	3
Copyright:	BSD
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.cac.washington.edu/mail/%{name}-%{version}.tar.Z
Source1:	%{name}.pamd
Patch0:		%{name}-pld.patch
Buildroot:	/tmp/%{name}-%{version}-root
Requires:	pam >= 0.66
Requires:	krb5-lib >= 1.0.5

%description
IMAP is a server for the POP (Post Office Protocol) and IMAP mail protocols.
The POP protocol allows a "post office" machine to collect mail for users
and have that mail downloaded to the user's local machine for reading. The
IMAP protocol provides the functionality of POP, and allows a user to
read mail on a remote machine without moving it to his local mailbox.

%description -l pl
Imapd jest serwerem dla POP (Post Office Protocol) i protoko³u IMAP. Protokó³ 
POP pozwala serwerowi poczty elektronicznej na przechowywanie przesy³ek i 
nastêpnie pobieranie ich przez maszyny klienckie w sieci. Protokó³ IMAP pozwala
zdalnemu u¿ytkownikowi na czytanie poczty na zdalnej maszynie bez konieczno¶ci
jej pobierania.

%prep
%setup -q 
%patch -p1 

%build
make CC="gcc" OPTIMIZE="$RPM_OPT_FLAGS -pipe" slx

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/pam.d,usr/{sbin,man/man8}}

install ./src/ipopd/ipopd.8c $RPM_BUILD_ROOT/usr/man/man8/ipopd.8
install ./src/imapd/imapd.8c $RPM_BUILD_ROOT/usr/man/man8/imapd.8

install -s ./ipopd/{ipop2d,ipop3d} $RPM_BUILD_ROOT/usr/sbin
install -s ./imapd/imapd $RPM_BUILD_ROOT/usr/sbin

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/imap

gzip -9fn $RPM_BUILD_ROOT/usr/man/man8/*

bzip2 -9 README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.bz2

%attr(640,root,root) %config /etc/pam.d/imap
%attr(755,root,root) /usr/sbin/ipop2d
%attr(755,root,root) /usr/sbin/ipop3d
%attr(755,root,root) /usr/sbin/imapd

/usr/man/man8/*

%changelog
* Wed Feb 10 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.5-2d]
- updated to stable release,
- added Group(pl),
- fixed group of ELF binaries.

* Thu Nov 12 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.5-1d]
- build for Linux PLD,
- major changes,
- build against GNU libc-2.1,
- start at RH spec file.

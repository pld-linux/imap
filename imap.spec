Summary:	Provides support for IMAP network mail protocol
Summary(pl):	Wspomaganie dla protokoЁu pocztowego IMAP
Summary(ru):	Обеспечивает поддержку сетевого почтового протокола IMAP
Summary(uk):	Забезпечу╓ п╕дтримку мережевого поштового протоколу IMAP
Name:		imap
%define		snap	0107022325
Version:	2001
Release:	0.BETA.20%{snap}.10
Epoch:		1
License:	BSD
Group:		Networking/Daemons
Source0:	ftp://ftp.cac.washington.edu/mail/%{name}-%{version}.BETA.SNAP-%{snap}.tar.Z
Source1:	%{name}.pamd
Source2:	%{name}-%{name}d.inetd
Source3:	%{name}-pop2d.inetd
Source4:	%{name}-pop3d.inetd
Source5:	%{name}-%{name}s.inetd
Source6:	%{name}-pop3s.inetd
Source7:	%{name}-pop.pamd
Patch0:		%{name}.patch
Patch1:		%{name}-pop2d-mbox-param.patch
Patch2:		%{name}-sharedlib.patch
Patch3:		%{name}-sstupidity.patch
Patch4:		%{name}-mailpath.patch
Patch5:		%{name}-starttls.patch
Patch6:		%{name}-man.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	pam-devel
BuildRequires:	openssl-devel
Requires:	pam >= 0.66
Requires:	%{name}-common
PreReq:		/etc/rc.d/init.d/rc-inetd
Requires:	rc-inetd >= 0.8.1
Provides:	imapdaemon
Obsoletes:	imapdaemon

%define		_includedir	%{_prefix}/include/imap

%description
IMAP is a server for the POP (Post Office Protocol) and IMAP mail
protocols. The POP protocol allows a "post office" machine to collect
mail for users and have that mail downloaded to the user's local
machine for reading. The IMAP protocol provides the functionality of
POP, and allows a user to read mail on a remote machine without moving
it to his local mailbox.

%description -l cs
BalМХek imap obsahuje server pro po╧tovnМ protokoly POP (Post Office
Protocol) a IMAP (Internet Message Access Protocol). Protokol POP
umo╬Рuje, aby u╬ivatel mohl naХМtat svoji do╧lou po╧tu ze vzdАlenИho
poХМtaХe. Protokol IMAP umo╬Рuje u╬ivateli ХtenМ po╧ty na vzdАlenИm
stroji bez pЬesouvАnМ na mМstnМ poХМtaХ.

%description -l pl
Imap jest serwerem dla POP (Post Office Protocol) i protokoЁu IMAP.
ProtokСЁ POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyЁek i nastЙpnie pobieranie ich przez maszyny klienckie w sieci.
ProtokСЁ IMAP pozwala zdalnemu u©ytkownikowi na czytanie poczty na
zdalnej maszynie bez konieczno╤ci jej pobierania.

%description -l ru
IMAP это сервер для почтовых протоколов POP (Post Office Protocol) и
IMAP. Протокол POP позволяет почтовой машине (post office) принимать
почту для пользователей, которые затем могут забирать ее на свои
локальные машины для чтения. Протокол IMAP предоставляет все
возможности POP и позволяет пользователю читать почту на удаленной
машине без перекачки ее на свою локальную машину.

%description -l uk
IMAP це сервер для поштових протокол╕в POP (Post Office Protocol) та
IMAP. Протокол POP дозволя╓ поштов╕й машин╕ (post office) приймати
пошту для користувач╕в, як╕ пот╕м можуть забирати ╖╖ на сво╖ локальн╕
машини для читання. Протокол IMAP нада╓ вс╕ можливост╕ POP ╕ дозволя╓
користувачу читати пошту на в╕ддален╕й машин╕ без перекачування ╖╖ на
свою локальну машину.

%package pop2
Summary:	Provides support for POP2 network mail protocol
Summary(pl):	Wspomaganie dla protokoЁu pocztowego POP2
Summary(ru):	Обеспечивает поддержку сетевого почтового протокола POP2
Summary(uk):	Забезпечу╓ п╕дтримку мережевого поштового протоколу POP2
Group:		Networking/Daemons
Prereq:		/etc/rc.d/init.d/rc-inetd
Requires:	%{name}-common
Requires:	rc-inetd >= 0.8.1
Provides:	pop2daemon
Obsoletes:	pop2daemon

%description pop2
IMAP is a server for the POP (Post Office Protocol) and IMAP mail
protocols. The POP protocol allows a "post office" machine to collect
mail for users and have that mail downloaded to the user's local
machine for reading. POP2 is an older POP protocol.

%description pop2 -l pl
Imap jest serwerem dla POP (Post Office Protocol) i protokoЁu IMAP.
ProtokСЁ POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyЁek i nastЙpnie pobieranie ich przez maszyny klienckie w sieci.
POP2 jest starsz╠ wersj╠ protokoЁu POP.

%description pop2 -l ru
IMAP это сервер для почтовых протоколов POP (Post Office Protocol) и
IMAP. Протокол POP позволяет почтовой машине (post office) принимать
почту для пользователей, которые затем могут забирать ее на свои
локальные машины для чтения. POP2 это старая версия протокола POP.

%description pop2 -l uk
IMAP це сервер для поштових протокол╕в POP (Post Office Protocol) та
IMAP. Протокол POP дозволя╓ поштов╕й машин╕ (post office) приймати
пошту для користувач╕в, як╕ пот╕м можуть забирати ╖╖ на сво╖ локальн╕
машини для читання. POP2 это стара верс╕я протоколу POP.

%package pop3
Summary:	Provides support for POP3 network mail protocol
Summary(pl):	Wspomaganie dla protokoЁu pocztowego POP3
Summary(ru):	Обеспечивает поддержку сетевого почтового протокола POP3
Summary(uk):	Забезпечу╓ п╕дтримку мережевого поштового протоколу POP3
Group:		Networking/Daemons
Prereq:		/etc/rc.d/init.d/rc-inetd
Requires:	%{name}-common
Requires:	rc-inetd >= 0.8.1
Provides:	pop3daemon
Obsoletes:	pop3daemon
Obsoletes:	qpopper
Obsoletes:	solid-pop3d

%description pop3
IMAP is a server for the POP (Post Office Protocol) and IMAP mail
protocols. The POP protocol allows a "post office" machine to collect
mail for users and have that mail downloaded to the user's local
machine for reading. POP3 is a newer POP protocol.

%description pop3 -l pl
Imap jest serwerem dla POP (Post Office Protocol) i protokoЁu IMAP.
ProtokСЁ POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyЁek i nastЙpnie pobieranie ich przez maszyny klienckie w sieci.
POP3 jest nowsz╠ wersj╠ protokoЁu POP.

%description pop3 -l ru
IMAP это сервер для почтовых протоколов POP (Post Office Protocol) и
IMAP. Протокол POP позволяет почтовой машине (post office) принимать
почту для пользователей, которые затем могут забирать ее на свои
локальные машины для чтения. POP3 это новая версия протокола POP.

%description pop3 -l uk
IMAP це сервер для поштових протокол╕в POP (Post Office Protocol) та
IMAP. Протокол POP дозволя╓ поштов╕й машин╕ (post office) приймати
пошту для користувач╕в, як╕ пот╕м можуть забирати ╖╖ на сво╖ локальн╕
машини для читання. POP3 это нова верс╕я протоколу POP.

%package devel
Summary:	Development files for IMAP
Summary(pl):	Pliki nagЁСwkowe IMAP
Summary(ru):	Хедера для разработки программ с использованием библиотеки IMAP
Summary(uk):	Хедери для розробки програм з використанням б╕бл╕отек╕ IMAP
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description devel
Development files for IMAP.

%description devel -l cs
BalМХek imap-devel obsahuje hlaviХkovИ soubory pro vЩvoj programЫ,
kterИ pou╬МvajМ knihovnu IMAP (Internet Message Access Protocol).

%description devel -l pl
Pliki nagЁСwkowe dla IMAP.

%description devel -l ru
Хедера для разработки программ с использованием библиотеки IMAP.

%description devel -l uk
Хедери для розробки програм з використанням б╕бл╕отек╕ IMAP.

%package lib
Summary:	IMAP client library
Summary(pl):	Biblioteka IMAP
Summary(ru):	Библиотека IMAP
Summary(uk):	Б╕бл╕отека IMAP
Group:		Development/Libraries

%description lib
IMAP client library.

%description lib -l pl
Biblioteka IMAP.

%description lib -l ru
Разделяемая библиотека для POP/IMAP-программ.

%description lib -l uk
Б╕бл╕отека сп╕льного використання для POP/IMAP-програм.

%package static
Summary:	IMAP static library
Summary(pl):	Statyczna biblioteka IMAP
Summary(ru):	Статическая библиотека IMAP
Summary(uk):	Статична б╕бл╕отека IMAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
IMAP static library.

%description devel -l cs
BalМХek imap-static obsahuje statickИ knihovny pro vЩvoj programЫ,
kterИ pou╬МvajМ knihovnu IMAP.

%description static -l pl
Statyczna biblioteka IMAP.

%description static -l ru
Статическая библиотека, необходимая для разработки POP/IMAP-программ.

%description static -l uk
Статична б╕бл╕отека, необх╕дна для розробки POP/IMAP-програм.

%package common
Summary:	Common files for WU imap and pop daemons.
Summary(pl):	Pliki wspСlne dla serwerСw imap i pop.
Group:		Networking/Daemons

%description common
Common files for WU imap and pop daemons.

%description common -l pl
Pliki wspСlne dla serwerСw imap i pop.

%prep
%setup -q -n imap-%{version}.BETA.SNAP-%{snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags} -pipe -fPIC" LDOPT="%{rpmldflags}" SSLTYPE=unix VERSION="20%{snap}" lnp
mv c-client/c-client.a libc-client.a
%{__make} clean
%{__make} CC="%{__cc}" OPT="%{rpmcflags} -pipe -fPIC" LDOPT="%{rpmldflags}" SSLTYPE=unix VERSION="20%{snap}" lnps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{pam.d,security,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_includedir},%{_libdir}}

install ./src/ipopd/ipopd.8c $RPM_BUILD_ROOT%{_mandir}/man8/ipop2d.8
install ./src/ipopd/ipopd.8c $RPM_BUILD_ROOT%{_mandir}/man8/ipop3d.8
install ./src/imapd/imapd.8c $RPM_BUILD_ROOT%{_mandir}/man8/imapd.8

install ./c-client/*.h $RPM_BUILD_ROOT%{_includedir}
install ./c-client/linkage.c $RPM_BUILD_ROOT%{_includedir}
install libc-client.a $RPM_BUILD_ROOT%{_libdir}/libc-client.a
install ./c-client/libc-client.so $RPM_BUILD_ROOT%{_libdir}/libc-client.so.20%{snap}.0
ln -s libc-client.so.20%{snap}.0 $RPM_BUILD_ROOT%{_libdir}/libc-client.so

rm -f 	$RPM_BUILD_ROOT%{_includedir}/unix.h \
	$RPM_BUILD_ROOT%{_includedir}/os_*

install ./ipopd/{ipop2d,ipop3d} $RPM_BUILD_ROOT%{_sbindir}
install ./imapd/imapd $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/imap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imapd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop2d
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3d
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imaps
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3s
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/pop

touch $RPM_BUILD_ROOT/etc/security/blacklist.{pop,imap}

( cd docs/rfc; ls rfc* > ../INDEX.rfc )
rm -rf docs/{rfc,BUILD}

gzip -9nf README docs/*

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%post pop2
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%post pop3
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pop2
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pop3
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%post   lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/sysconfig/rc-inetd/imapd
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/sysconfig/rc-inetd/imaps
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/pam.d/imap
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.imap
%attr(755,root,root) %{_sbindir}/imapd
%{_mandir}/man8/imapd.8*

%files pop2
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/sysconfig/rc-inetd/ipop2d
%attr(755,root,root) %{_sbindir}/ipop2d
%{_mandir}/man8/ipop2d.8*

%files pop3
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/sysconfig/rc-inetd/ipop3d
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/sysconfig/rc-inetd/ipop3s
%attr(755,root,root) %{_sbindir}/ipop3d
%{_mandir}/man8/ipop3d.8*

%files common
%defattr(644,root,root,755)
%doc README.gz docs/*
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size, mtime, md5) /etc/pam.d/pop
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.pop

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc-client.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}
%{_libdir}/libc-client.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libc-client.a

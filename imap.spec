Summary:	Support for IMAP network mail protocol
Summary(es):	Provee soporte para los protocolos de mail IMAP y POP
Summary(pl):	ObsЁuga protokoЁu pocztowego IMAP
Summary(pt_BR):	ProvЙ suporte para os protocolos de mail IMAP e POP
Summary(ru):	Обеспечивает поддержку сетевого почтового протокола IMAP
Summary(uk):	Забезпечу╓ п╕дтримку мережевого поштового протоколу IMAP
Summary(zh_CN):	IMAP╨мPOP╥ЧнЯфВ
Name:		imap
Version:	2004d
Release:	2
Epoch:		1
License:	BSD
Group:		Networking/Daemons
Source0:	ftp://ftp.cac.washington.edu/mail/%{name}-%{version}.tar.Z
# Source0-md5:	9bee45a210138d4a924ab95539f5ef35
Source1:	%{name}.pamd
Source2:	%{name}-%{name}d.inetd
Source3:	%{name}-pop2d.inetd
Source4:	%{name}-pop3d.inetd
Source5:	%{name}-%{name}s.inetd
Source6:	%{name}-pop3s.inetd
Source7:	%{name}-pop.pamd
Source8:	shared-ssl-key.pem
Patch0:		%{name}.patch
Patch1:		%{name}-pop2d-mbox-param.patch
Patch2:		%{name}-sharedlib.patch
Patch3:		%{name}-sstupidity.patch
Patch4:		%{name}-mailpath.patch
Patch5:		%{name}-man.patch
Patch6:		%{name}-overflow.patch
Patch7:		%{name}-version-pld.patch
Patch8:		%{name}-headers_fix.patch
URL:		http://www.washington.edu/imap/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
PreReq:		rc-inetd >= 0.8.1
Requires:	pam >= 0.77.3
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	imapdaemon
Obsoletes:	imapdaemon
Conflicts:	courier-imap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es
IMAP es un servidor para los protocolos de mail POP (Post Office
Protocol) y IMAP. El protocolo POP permite a una mАquina de correo
colectar mail para usuarios y permite download del mail a la mАquina
local del usuario para lectura. El protocolo IMAP nos ofrece la
funcionalidad de POP, y permite a un usuario leer su mail en una
mАquina remota sin moverlo a su caja postal local.

%description -l pl
Imap jest serwerem dla POP (Post Office Protocol) i protokoЁu IMAP.
ProtokСЁ POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyЁek i nastЙpnie pobieranie ich przez maszyny klienckie w sieci.
ProtokСЁ IMAP pozwala zdalnemu u©ytkownikowi na czytanie poczty na
zdalnej maszynie bez konieczno╤ci jej pobierania.

%description -l pt_BR
IMAP И um servidor para os protocolos de mail POP (Post Office
Protocol) e IMAP. O protocolo POP permite uma mАquina de correio
coletar mail para usuАrios e permite o download do mail para a mАquina
local do usuАrio para leitura. O protocolo IMAP oferece a
funcionalidade de POP, e permite um usuАrio ler seu mail em uma
mАquina remota sem movЙ-lo para a sua caixa postal local.

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
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Provides:	pop3daemon
Obsoletes:	pop3daemon
Obsoletes:	qpopper
Obsoletes:	solid-pop3d
Conflicts:	courier-imap-pop3
Conflicts:	tpop3d

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

%package common
Summary:	Common files for WU imap and pop daemons
Summary(pl):	Pliki wspСlne dla serwerСw imap i pop
Group:		Networking/Daemons
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3

%description common
Common files for WU imap and pop daemons.

%description common -l pl
Pliki wspСlne dla serwerСw imap i pop.

%package devel
Summary:	Development files for IMAP
Summary(pl):	Pliki nagЁСwkowe IMAP
Summary(pt_BR):	Bibliotecas, arquivos de inclusЦo, etc para desenvolver programas IMAP
Summary(ru):	Хедера для разработки программ с использованием библиотеки IMAP
Summary(uk):	Хедери для розробки програм з використанням б╕бл╕отек╕ IMAP
Summary(zh_CN):	IMAP╨мPOP╥ЧнЯфВ©╙╥╒╧╓╬ъ╪╞
Group:		Development/Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description devel
Development files for IMAP.

%description devel -l cs
BalМХek imap-devel obsahuje hlaviХkovИ soubory pro vЩvoj programЫ,
kterИ pou╬МvajМ knihovnu IMAP (Internet Message Access Protocol).

%description devel -l pl
Pliki nagЁСwkowe dla IMAP.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusЦo, etc para desenvolver programas que
utilizem POP/IMAP.

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
Summary(pt_BR):	Bibliotecas estАticas para desenvolver programas IMAP
Summary(ru):	Статическая библиотека IMAP
Summary(uk):	Статична б╕бл╕отека IMAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

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

%package utils
Summary:	IMAP tools: mailutil, dmail, tmail
Summary(pl):	NarzЙdzia IMAP: mailutil, dmail, tmail
Group:		Applications/Mail
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description utils
IMAP tools: mailutil (mail utility program), dmail (procmail mail
delivery module), tmail (direct mail delivery module).

%description utils -l pl
NarzЙdzia IMAP: mailutil (program narzЙdziowy do poczty), dmail (moduЁ
dostarczaj╠cy pocztЙ dla procmaila), tmail (moduЁ dostarczaj╠cy pocztЙ
bezpo╤rednio).

%description static -l pt_BR
Bibliotecas estАticas para desenvolver programas que utilizem
POP/IMAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
# build with non-recommended SSLTYPE (unix) since unix.nopwd would remove
# support for plain-text auth w/o SSL/TLS
# (but it should be made some runtime option!
echo 'y' | %{__make} lnp \
	CC="%{__cc}" OPT="%{rpmcflags} -pipe -fPIC" LDOPT="%{rpmldflags}" \
	SSLTYPE=unix VERSION="%{version}"
mv -f c-client/c-client.a libc-client.a

%{__make} clean
echo 'y' | %{__make} lnps \
	CC="%{__cc}" OPT="%{rpmcflags} -pipe -fPIC" LDOPT="%{rpmldflags}" \
	SSLTYPE=unix VERSION="%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,security,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_includedir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,8},%{_var}/lib/imap} \
	$RPM_BUILD_ROOT%{_var}/lib/openssl/certs

install ./src/ipopd/ipopd.8 $RPM_BUILD_ROOT%{_mandir}/man8/ipop2d.8
install ./src/ipopd/ipopd.8 $RPM_BUILD_ROOT%{_mandir}/man8/ipop3d.8
install ./src/imapd/imapd.8 $RPM_BUILD_ROOT%{_mandir}/man8/imapd.8
install ./src/dmail/dmail.1 $RPM_BUILD_ROOT%{_mandir}/man1
install ./src/mailutil/mailutil.1 $RPM_BUILD_ROOT%{_mandir}/man1
install ./src/tmail/tmail.1 $RPM_BUILD_ROOT%{_mandir}/man1

install ./c-client/*.h $RPM_BUILD_ROOT%{_includedir}
install ./c-client/linkage.c $RPM_BUILD_ROOT%{_includedir}
install libc-client.a $RPM_BUILD_ROOT%{_libdir}/libc-client.a
install ./c-client/libc-client.so $RPM_BUILD_ROOT%{_libdir}/libc-client.so.%{version}.0
ln -sf libc-client.so.%{version}.0 $RPM_BUILD_ROOT%{_libdir}/libc-client.so

rm -f 	$RPM_BUILD_ROOT%{_includedir}/unix.h \
	$RPM_BUILD_ROOT%{_includedir}/os_*

install ./ipopd/{ipop2d,ipop3d} $RPM_BUILD_ROOT%{_sbindir}
install ./imapd/imapd $RPM_BUILD_ROOT%{_sbindir}
install ./dmail/dmail $RPM_BUILD_ROOT%{_bindir}
install ./mailutil/mailutil $RPM_BUILD_ROOT%{_bindir}
install ./tmail/tmail $RPM_BUILD_ROOT%{_bindir}
#./mlock/mlock - (sgid mail) standalone mailbox lock program

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/imap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imapd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop2d
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3d
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imaps
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3s
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/pop
install %{SOURCE8} $RPM_BUILD_ROOT%{_var}/lib/openssl/certs/imapd.pem
install %{SOURCE8} $RPM_BUILD_ROOT%{_var}/lib/openssl/certs/ipop3d.pem

touch $RPM_BUILD_ROOT/etc/security/blacklist.{pop,imap}

cd docs/rfc
ls rfc* > ../INDEX.rfc
cd ../..
rm -rf docs/{rfc,BUILD}

%clean
rm -rf $RPM_BUILD_ROOT

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

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/imapd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/imaps
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/imap
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.imap
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/openssl/certs/imapd.pem
%attr(755,root,root) %{_sbindir}/imapd
%{_mandir}/man8/imapd.8*

%files pop2
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ipop2d
%attr(755,root,root) %{_sbindir}/ipop2d
%{_mandir}/man8/ipop2d.8*

%files pop3
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ipop3d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ipop3s
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/openssl/certs/ipop3d.pem
%attr(755,root,root) %{_sbindir}/ipop3d
%{_mandir}/man8/ipop3d.8*

%files common
%defattr(644,root,root,755)
%doc README docs/*
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/pop
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.pop
%dir %{_var}/lib/openssl/certs

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc-client.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc-client.so
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/libc-client.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man1/*

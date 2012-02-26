Summary:	Support for IMAP network mail protocol
Summary(es.UTF-8):	Provee soporte para los protocolos de mail IMAP y POP
Summary(pl.UTF-8):	Obsługa protokołu pocztowego IMAP
Summary(pt_BR.UTF-8):	Provê suporte para os protocolos de mail IMAP e POP
Summary(ru.UTF-8):	Обеспечивает поддержку сетевого почтового протокола IMAP
Summary(uk.UTF-8):	Забезпечує підтримку мережевого поштового протоколу IMAP
Summary(zh_CN.UTF-8):	IMAP和POP服务器
Name:		imap
Version:	2007f
Release:	2
Epoch:		1
License:	Apache v2.0
Group:		Networking/Daemons
Source0:	ftp://ftp.cac.washington.edu/mail/%{name}-%{version}.tar.gz
# Source0-md5:	2126fd125ea26b73b20f01fcd5940369
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
Patch9:		%{name}-annotations.patch
URL:		http://www.washington.edu/imap/
BuildRequires:	/sbin/ldconfig
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	rc-inetd >= 0.8.1
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Provides:	imapdaemon
Obsoletes:	imapdaemon
Conflicts:	courier-imap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/imap

%define		skip_post_check_so	libc-client.so.%{version}.0

%description
IMAP is a server for the POP (Post Office Protocol) and IMAP mail
protocols. The POP protocol allows a "post office" machine to collect
mail for users and have that mail downloaded to the user's local
machine for reading. The IMAP protocol provides the functionality of
POP, and allows a user to read mail on a remote machine without moving
it to his local mailbox.

%description -l cs.UTF-8
Balíček imap obsahuje server pro poštovní protokoly POP (Post Office
Protocol) a IMAP (Internet Message Access Protocol). Protokol POP
umožňuje, aby uživatel mohl načítat svoji došlou poštu ze vzdáleného
počítače. Protokol IMAP umožňuje uživateli čtení pošty na vzdáleném
stroji bez přesouvání na místní počítač.

%description -l es.UTF-8
IMAP es un servidor para los protocolos de mail POP (Post Office
Protocol) y IMAP. El protocolo POP permite a una máquina de correo
colectar mail para usuarios y permite download del mail a la máquina
local del usuario para lectura. El protocolo IMAP nos ofrece la
funcionalidad de POP, y permite a un usuario leer su mail en una
máquina remota sin moverlo a su caja postal local.

%description -l pl.UTF-8
Imap jest serwerem dla POP (Post Office Protocol) i protokołu IMAP.
Protokół POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyłek i następnie pobieranie ich przez maszyny klienckie w sieci.
Protokół IMAP pozwala zdalnemu użytkownikowi na czytanie poczty na
zdalnej maszynie bez konieczności jej pobierania.

%description -l pt_BR.UTF-8
IMAP é um servidor para os protocolos de mail POP (Post Office
Protocol) e IMAP. O protocolo POP permite uma máquina de correio
coletar mail para usuários e permite o download do mail para a máquina
local do usuário para leitura. O protocolo IMAP oferece a
funcionalidade de POP, e permite um usuário ler seu mail em uma
máquina remota sem movê-lo para a sua caixa postal local.

%description -l ru.UTF-8
IMAP это сервер для почтовых протоколов POP (Post Office Protocol) и
IMAP. Протокол POP позволяет почтовой машине (post office) принимать
почту для пользователей, которые затем могут забирать ее на свои
локальные машины для чтения. Протокол IMAP предоставляет все
возможности POP и позволяет пользователю читать почту на удаленной
машине без перекачки ее на свою локальную машину.

%description -l uk.UTF-8
IMAP це сервер для поштових протоколів POP (Post Office Protocol) та
IMAP. Протокол POP дозволяє поштовій машині (post office) приймати
пошту для користувачів, які потім можуть забирати її на свої локальні
машини для читання. Протокол IMAP надає всі можливості POP і дозволяє
користувачу читати пошту на віддаленій машині без перекачування її на
свою локальну машину.

%package pop2
Summary:	Provides support for POP2 network mail protocol
Summary(pl.UTF-8):	Wspomaganie dla protokołu pocztowego POP2
Summary(ru.UTF-8):	Обеспечивает поддержку сетевого почтового протокола POP2
Summary(uk.UTF-8):	Забезпечує підтримку мережевого поштового протоколу POP2
Group:		Networking/Daemons
Requires(post,postun):	rc-inetd >= 0.8.1
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Provides:	pop2daemon
Obsoletes:	pop2daemon

%description pop2
IMAP is a server for the POP (Post Office Protocol) and IMAP mail
protocols. The POP protocol allows a "post office" machine to collect
mail for users and have that mail downloaded to the user's local
machine for reading. POP2 is an older POP protocol.

%description pop2 -l pl.UTF-8
Imap jest serwerem dla POP (Post Office Protocol) i protokołu IMAP.
Protokół POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyłek i następnie pobieranie ich przez maszyny klienckie w sieci.
POP2 jest starszą wersją protokołu POP.

%description pop2 -l ru.UTF-8
IMAP это сервер для почтовых протоколов POP (Post Office Protocol) и
IMAP. Протокол POP позволяет почтовой машине (post office) принимать
почту для пользователей, которые затем могут забирать ее на свои
локальные машины для чтения. POP2 это старая версия протокола POP.

%description pop2 -l uk.UTF-8
IMAP це сервер для поштових протоколів POP (Post Office Protocol) та
IMAP. Протокол POP дозволяє поштовій машині (post office) приймати
пошту для користувачів, які потім можуть забирати її на свої локальні
машини для читання. POP2 это стара версія протоколу POP.

%package pop3
Summary:	Provides support for POP3 network mail protocol
Summary(pl.UTF-8):	Wspomaganie dla protokołu pocztowego POP3
Summary(ru.UTF-8):	Обеспечивает поддержку сетевого почтового протокола POP3
Summary(uk.UTF-8):	Забезпечує підтримку мережевого поштового протоколу POP3
Group:		Networking/Daemons/POP3
Requires(post,postun):	rc-inetd >= 0.8.1
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

%description pop3 -l pl.UTF-8
Imap jest serwerem dla POP (Post Office Protocol) i protokołu IMAP.
Protokół POP pozwala serwerowi poczty elektronicznej na przechowywanie
przesyłek i następnie pobieranie ich przez maszyny klienckie w sieci.
POP3 jest nowszą wersją protokołu POP.

%description pop3 -l ru.UTF-8
IMAP это сервер для почтовых протоколов POP (Post Office Protocol) и
IMAP. Протокол POP позволяет почтовой машине (post office) принимать
почту для пользователей, которые затем могут забирать ее на свои
локальные машины для чтения. POP3 это новая версия протокола POP.

%description pop3 -l uk.UTF-8
IMAP це сервер для поштових протоколів POP (Post Office Protocol) та
IMAP. Протокол POP дозволяє поштовій машині (post office) приймати
пошту для користувачів, які потім можуть забирати її на свої локальні
машини для читання. POP3 это нова версія протоколу POP.

%package common
Summary:	Common files for WU imap and pop daemons
Summary(pl.UTF-8):	Pliki wspólne dla serwerów imap i pop
Group:		Networking/Daemons
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.79.0

%description common
Common files for WU imap and pop daemons.

%description common -l pl.UTF-8
Pliki wspólne dla serwerów imap i pop.

%package devel
Summary:	Development files for IMAP
Summary(pl.UTF-8):	Pliki nagłówkowe IMAP
Summary(pt_BR.UTF-8):	Bibliotecas, arquivos de inclusão, etc para desenvolver programas IMAP
Summary(ru.UTF-8):	Хедера для разработки программ с использованием библиотеки IMAP
Summary(uk.UTF-8):	Хедери для розробки програм з використанням бібліотекі IMAP
Summary(zh_CN.UTF-8):	IMAP和POP服务器开发工具集
Group:		Development/Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description devel
Development files for IMAP.

%description devel -l cs.UTF-8
Balíček imap-devel obsahuje hlavičkové soubory pro vývoj programů,
které používají knihovnu IMAP (Internet Message Access Protocol).

%description devel -l pl.UTF-8
Pliki nagłówkowe dla IMAP.

%description devel -l pt_BR.UTF-8
Bibliotecas, arquivos de inclusão, etc para desenvolver programas que
utilizem POP/IMAP.

%description devel -l ru.UTF-8
Хедера для разработки программ с использованием библиотеки IMAP.

%description devel -l uk.UTF-8
Хедери для розробки програм з використанням бібліотекі IMAP.

%package lib
Summary:	IMAP client library
Summary(pl.UTF-8):	Biblioteka IMAP
Summary(ru.UTF-8):	Библиотека IMAP
Summary(uk.UTF-8):	Бібліотека IMAP
Group:		Libraries

%description lib
IMAP client library.

%description lib -l pl.UTF-8
Biblioteka IMAP.

%description lib -l ru.UTF-8
Разделяемая библиотека для POP/IMAP-программ.

%description lib -l uk.UTF-8
Бібліотека спільного використання для POP/IMAP-програм.

%package static
Summary:	IMAP static library
Summary(pl.UTF-8):	Statyczna biblioteka IMAP
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolver programas IMAP
Summary(ru.UTF-8):	Статическая библиотека IMAP
Summary(uk.UTF-8):	Статична бібліотека IMAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
IMAP static library.

%description static -l cs.UTF-8
Balíček imap-static obsahuje statické knihovny pro vývoj programů,
které používají knihovnu IMAP.

%description static -l pl.UTF-8
Statyczna biblioteka IMAP.

%description static -l ru.UTF-8
Статическая библиотека, необходимая для разработки POP/IMAP-программ.

%description static -l uk.UTF-8
Статична бібліотека, необхідна для розробки POP/IMAP-програм.

%package utils
Summary:	IMAP tools: mailutil, dmail, tmail
Summary(pl.UTF-8):	Narzędzia IMAP: mailutil, dmail, tmail
Group:		Applications/Mail
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description utils
IMAP tools: mailutil (mail utility program), dmail (procmail mail
delivery module), tmail (direct mail delivery module).

%description utils -l pl.UTF-8
Narzędzia IMAP: mailutil (program narzędziowy do poczty), dmail (moduł
dostarczający pocztę dla procmaila), tmail (moduł dostarczający pocztę
bezpośrednio).

%description utils -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolver programas que utilizem
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
%patch9 -p1

cd docs/rfc
ls rfc* > ../INDEX.rfc
cd ../..
rm -rf docs/{rfc,BUILD}

%build
# build with non-recommended SSLTYPE (unix) since unix.nopwd would remove
# support for plain-text auth w/o SSL/TLS
# (but it should be made some runtime option!
echo 'y' | %{__make} lnp \
	CC="%{__cc}" \
	GCCOPTLEVEL="%{rpmcflags} -pipe -fPIC" \
	LDOPT="%{rpmldflags}" \
	SSLTYPE=unix \
%if "%{pld_release}" != "th"
	SSLCERTS=/var/lib/openssl/certs \
	SSLKEYS=/var/lib/openssl/private \
%else
	SSLCERTS=/etc/openssl/certs \
	SSLKEYS=/etc/openssl/private \
%endif
	VERSION="%{version}"
mv -f c-client/c-client.a libc-client.a

%{__make} clean
echo 'y' | %{__make} lnps \
	CC="%{__cc}" \
	GCCOPTLEVEL="%{rpmcflags} -pipe -fPIC" \
	LDOPT="%{rpmldflags}" \
	SSLTYPE=unix \
%if "%{pld_release}" != "th"
	SSLCERTS=/var/lib/openssl/certs \
	SSLKEYS=/var/lib/openssl/private \
%else
	SSLCERTS=/etc/openssl/certs \
	SSLKEYS=/etc/openssl/private \
%endif
	VERSION="%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,security,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_includedir},%{_libdir}} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,8} \
%if "%{pld_release}" != "th"
	$RPM_BUILD_ROOT%{_var}/lib/openssl/certs
%else
	$RPM_BUILD_ROOT/etc/openssl/certs
%endif

install src/ipopd/ipopd.8 $RPM_BUILD_ROOT%{_mandir}/man8/ipop2d.8
install src/ipopd/ipopd.8 $RPM_BUILD_ROOT%{_mandir}/man8/ipop3d.8
install src/imapd/imapd.8 $RPM_BUILD_ROOT%{_mandir}/man8/imapd.8
install src/dmail/dmail.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/mailutil/mailutil.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/tmail/tmail.1 $RPM_BUILD_ROOT%{_mandir}/man1

install c-client/*.h $RPM_BUILD_ROOT%{_includedir}
install c-client/linkage.c $RPM_BUILD_ROOT%{_includedir}
install libc-client.a $RPM_BUILD_ROOT%{_libdir}/libc-client.a
install c-client/libc-client.so $RPM_BUILD_ROOT%{_libdir}/libc-client.so.%{version}.0
ln -sf libc-client.so.%{version}.0 $RPM_BUILD_ROOT%{_libdir}/libc-client.so

rm -f	$RPM_BUILD_ROOT%{_includedir}/unix.h \
	$RPM_BUILD_ROOT%{_includedir}/os_*

install ipopd/{ipop2d,ipop3d} $RPM_BUILD_ROOT%{_sbindir}
install imapd/imapd $RPM_BUILD_ROOT%{_sbindir}
install dmail/dmail $RPM_BUILD_ROOT%{_bindir}
install mailutil/mailutil $RPM_BUILD_ROOT%{_bindir}
install tmail/tmail $RPM_BUILD_ROOT%{_bindir}
#./mlock/mlock - (sgid mail) standalone mailbox lock program

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/imap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imapd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop2d
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3d
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imaps
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3s
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/pop
%if "%{pld_release}" != "th"
install %{SOURCE8} $RPM_BUILD_ROOT%{_var}/lib/openssl/certs/imapd.pem
install %{SOURCE8} $RPM_BUILD_ROOT%{_var}/lib/openssl/certs/ipop3d.pem
%else
install %{SOURCE8} $RPM_BUILD_ROOT/etc/openssl/certs/imapd.pem
install %{SOURCE8} $RPM_BUILD_ROOT/etc/openssl/certs/ipop3d.pem
%endif

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

touch $RPM_BUILD_ROOT/etc/security/blacklist.{pop3,imap}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q rc-inetd reload

%post pop2
%service -q rc-inetd reload

%post pop3
%service -q rc-inetd reload

%postun
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%postun pop2
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%postun pop3
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post   lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/imapd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/imaps
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/imap
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.imap
%if "%{pld_release}" != "th"
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/openssl/certs/imapd.pem
%else
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/openssl/certs/imapd.pem
%endif
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
%if "%{pld_release}" != "th"
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/openssl/certs/ipop3d.pem
%else
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/openssl/certs/ipop3d.pem
%endif
%attr(755,root,root) %{_sbindir}/ipop3d
%{_mandir}/man8/ipop3d.8*

%files common
%defattr(644,root,root,755)
%doc README docs/*
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/pop
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.pop3

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc-client.so.*.*
%ghost %{_libdir}/libc-client.so.2007f

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
%{_mandir}/man1/*

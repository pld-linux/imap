Summary:	provides support for IMAP network mail protocol
Summary(pl):	Wspomaganie dla protokołu pocztowego IMAP
Name:		imap
Version:	4.7b
Release:	1
Copyright:	BSD
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.cac.washington.edu/mail/%{name}-%{version}.tar.Z
Source1:	%{name}.pamd
Source2:	%{name}-imapd.inetd
Source3:	%{name}-pop2d.inetd
Source4:	%{name}-pop3d.inetd
Patch:		%{name}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	pam-devel
Requires:	pam >= 0.66
Prereq:		/etc/rc.d/init.d/rc-inetd
Requires:	rc-inetd >= 0.8.1
Provides:	imapdaemon
Obsoletes:	imapdaemon

%description
IMAP is a server for the POP (Post Office Protocol) and IMAP mail protocols.
The POP protocol allows a "post office" machine to collect mail for users
and have that mail downloaded to the user's local machine for reading. The
IMAP protocol provides the functionality of POP, and allows a user to
read mail on a remote machine without moving it to his local mailbox.

%description -l pl
Imapd jest serwerem dla POP (Post Office Protocol) i protokołu IMAP. Protokół 
POP pozwala serwerowi poczty elektronicznej na przechowywanie przesyłek i 
następnie pobieranie ich przez maszyny klienckie w sieci. Protokół IMAP pozwala
zdalnemu użytkownikowi na czytanie poczty na zdalnej maszynie bez konieczności
jej pobierania.

%package pop
Summary:	provides support for POP network mail protocol
Summary(pl):	Wspomaganie dla protokołu pocztowego POP
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		/etc/rc.d/init.d/rc-inetd
Requires:	rc-inetd >= 0.8.1

%description pop
IMAP is a server for the POP (Post Office Protocol) and IMAP mail protocols.
The POP protocol allows a "post office" machine to collect mail for users
and have that mail downloaded to the user's local machine for reading. The
IMAP protocol provides the functionality of POP, and allows a user to
read mail on a remote machine without moving it to his local mailbox.

%description pop -l pl
Imapd jest serwerem dla POP (Post Office Protocol) i protokołu IMAP. Protokół 
POP pozwala serwerowi poczty elektronicznej na przechowywanie przesyłek i 
następnie pobieranie ich przez maszyny klienckie w sieci. Protokół IMAP pozwala
zdalnemu użytkownikowi na czytanie poczty na zdalnej maszynie bez konieczności
jej pobierania.

%package devel
Summary:        Development files for IMAP.
Summary(pl):    Pliki nagłówkowe IMAP.
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki

%description devel 
Development files for IMAP.

%description -l pl
Pliki nagłówkowe dla IMAP.

#%package static
#Summary:        IMAP static library.
#Summary(pl):    Statyczna biblioteka IMAP.
#Group:          Development/Libraries 
#Group(pl):      Programowanie/Biblioteki
#
#%description static
#IMAP static library.
#
#%description -l pl
#Statyczna biblioteka IMAP.

%prep
%setup -q 
%patch -p1 

%build
make CC="gcc" OPTIMIZE="$RPM_OPT_FLAGS -pipe" slx

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/{pam.d,sysconfig/rc-inetd},usr/{sbin,share/man/man8},%{_includedir},%{_libdir}}

install ./src/ipopd/ipopd.8c $RPM_BUILD_ROOT%{_mandir}/man8/ipopd.8
install ./src/imapd/imapd.8c $RPM_BUILD_ROOT%{_mandir}/man8/imapd.8

install ./src/c-client/*.h $RPM_BUILD_ROOT%{_includedir}
install ./src/osdep/tops-20/*.h $RPM_BUILD_ROOT%{_includedir}
install ./src/osdep/unix/*.h $RPM_BUILD_ROOT%{_includedir}
install ./c-client/c-client.a $RPM_BUILD_ROOT%{_libdir}/libimap.a

rm -f 	$RPM_BUILD_ROOT%{_includedir}/unix.h \
	$RPM_BUILD_ROOT%{_includedir}/os_*
	
install -s ./ipopd/{ipop2d,ipop3d} $RPM_BUILD_ROOT%{_sbindir}
install -s ./imapd/imapd $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/imap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/imapd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop2d
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ipop3d

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man8/* README

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%post pop
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pop
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/imap
%attr(640,root,root) /etc/sysconfig/rc-inetd/imapd
%attr(755,root,root) %{_sbindir}/imapd
%{_mandir}/man8/imapd.8.gz

%files pop
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/imap
%attr(640,root,root) /etc/sysconfig/rc-inetd/ipop2d
%attr(640,root,root) /etc/sysconfig/rc-inetd/ipop3d
%attr(755,root,root) %{_sbindir}/ipop2d
%attr(755,root,root) %{_sbindir}/ipop3d
%{_mandir}/man8/ipopd.8.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

#%files static
#%defattr(644,root,root,755)
%{_libdir}/libimap.a

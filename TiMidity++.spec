Summary:	TiMidity++ - MIDI to WAV converter and player
Name:		TiMidity++
Version:	2.9.0
Release:	1
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
License:	GPL
Vendor:		Masanao Izumo <mo@goice.co.jp>
Source0:	http://www.goice.co.jp/member/mo/timidity/dist/%{name}-%{version}.tar.bz2
Patch0:		TiMidity++-config.patch
URL:		http://www.goice.co.jp/member/mo/timidity/
BuildRequires:	alsa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TiMidity++ is a converter that converts some of MIDI files ( formats :
Standard MIDI file (*.MID), Recomposer files (*.RCP, *.R36, *.G18,
*.G36) and Module file (*.mod) ) into formatted audio file (ex. RIFF
WAVE). TiMidity uses Gravis Ultrasound-compatible patch files or
Soundfonts (*.sfx, *.sf2) to generate digital audio data from MIDI
files. The digital audio data generated by TiMidity can be stored in a
file for processing, or played in real time through an audio device.
In real time playing, TiMidity if able to show the lylic contained in
KAR file or WRD file.

%package slang
Summary:	Slang interface for TiMidity++.
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description slang
Slang interface for TiMidity++.

%package motif
Summary:	Motif interface for TiMidity++.
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description motif
Motif interface for TiMidity++.

%package tcltk
Summary:	Tcl/Tk interface for TiMidity++.
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description tcltk
Tcl/Tk interface for TiMidity++.

%package xaw
Summary:	Athena interface for TiMidity++.
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description xaw
Athena interface for TiMidity++.

%package gtk
Summary:	GTK+ interface for TiMidity++.
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description gtk
GTK+ interface for TiMidity++.

%package vt100
Summary:	VT100 interface for TiMidity++.
Group:		Applications/Sound
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description vt100
VT100 interface for TiMidity++.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoheader
autoconf
automake
%configure \
	--with-elf \
	--enable-alsa \
	--enable-dynamic \
	--enable-ncurses=dynamic \
	--enable-slang=dynamic \
	--enable-motif=dynamic \
	--enable-tcltk=dynamic \
	--enable-emacs=dynamic \
	--enable-xaw=dynamic \
	--enable-xskin=dynamic \
	--enable-gtk=dynamic \
	--enable-vt100=dynamic \
	--enable-network \
	--enable-server \
	--enable-spectrogram
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/GUSpatches}
install timidity.cfg $RPM_BUILD_ROOT%{_sysconfdir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* \
	$RPM_BUILD_ROOT%{_libdir}/timidity/*.so || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	AUTHORS README* ChangeLog* NEWS doc/C/{CHANGES*,FAQ,README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README*,ChangeLog*,NEWS,doc/C/{CHANGES*,FAQ,README.{dl,sf,xskin}*}}.gz
%attr(755,root,root) %{_bindir}/timidity
%attr(755,root,root) %{_libdir}/timidity/interface_n.so
%attr(755,root,root) %{_libdir}/timidity/interface_e.so
%attr(755,root,root) %{_libdir}/timidity/interface_i.so
%{_libdir}/timidity/bitmaps
%{_mandir}/man*/*
%config %{_sysconfdir}/timidity.cfg
%ghost %dir %{_datadir}/GUSpatches

%files slang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_s.so

%files motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_m.so

%files tcltk
%defattr(644,root,root,755)
%doc doc/C/README.tk.gz
%attr(755,root,root) %{_libdir}/timidity/interface_k.so
%{_libdir}/timidity/*.tcl

%files xaw
%defattr(644,root,root,755)
%doc doc/C/README.xaw.gz
%attr(755,root,root) %{_libdir}/timidity/interface_a.so

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_g.so

%files vt100
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_v.so

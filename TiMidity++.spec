#
# Conditional build:
# bcond_off_alsa - without ALSA support
#
Summary:	TiMidity++ - MIDI to WAV converter and player
Name:		TiMidity++
Version:	2.10.3a2
Release:	1
License:	GPL
Vendor:		Masanao Izumo <mo@goice.co.jp>
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Source0:	http://www.goice.co.jp/member/mo/timidity/dist/%{name}-%{version}.tar.bz2
Patch0:		%{name}-config.patch
%ifnarch sparc sparc64
%{!?bcond_off_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	gtk+-devel
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel
BuildRequires:	slang-devel
BuildRequires:	tk-devel >= 8.3.2
URL:		http://www.goice.co.jp/member/mo/timidity/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TiMidity++ is a converter that converts some of MIDI files ( formats :
Standard MIDI file (MID), Recomposer files (RCP, R36, G18, G36) and
Module file (mod) ) into formatted audio file (ex. RIFF WAVE).
TiMidity uses Gravis Ultrasound-compatible patch files or Soundfonts
(sfx, sf2) to generate digital audio data from MIDI files. The digital
audio data generated by TiMidity can be stored in a file for
processing, or played in real time through an audio device. In real
time playing, TiMidity if able to show the lylic contained in KAR file
or WRD file.

%package slang
Summary:	Slang interface for TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description slang
Slang interface for TiMidity++.

%package motif
Summary:	Motif interface for TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description motif
xmmidi -- Motif interface for TiMidity++.

%package tcltk
Summary:	Tcl/Tk interface for TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description tcltk
tkmidi -- Tcl/Tk interface for TiMidity++.

%package xaw
Summary:	Athena interface for TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description xaw
xawmidi -- Athena interface for TiMidity++.

%package gtk
Summary:	GTK+ interface for TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description gtk
gtkmidi -- GTK+ interface for TiMidity++.

%package vt100
Summary:	VT100 interface for TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D德i瘯
Requires:	%{name} = %{version}

%description vt100
VT100 interface for TiMidity++.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-elf \
%ifnarch sparc sparc64
	%{!?bcond_off_alsa:--enable-alsa} \
%endif
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/GUSpatches}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install timidity.cfg $RPM_BUILD_ROOT%{_sysconfdir}

## based on timidity/timidity.c
##ln -s timidity $RPM_BUILD_ROOT%{_bindir}/kmidi # does it work?
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/gtkmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/tkmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/xmmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/xawmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/xskinmidi

gzip -9nf AUTHORS README* ChangeLog* NEWS doc/C/{CHANGES*,FAQ,README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz ,doc/C/*.gz
%attr(755,root,root) %{_bindir}/timidity
%attr(755,root,root) %{_libdir}/timidity/interface_n.so
%attr(755,root,root) %{_libdir}/timidity/interface_e.so
%attr(755,root,root) %{_libdir}/timidity/interface_i.so
%{_libdir}/timidity/bitmaps
%{_mandir}/man*/*
%config(noreplace) %{_sysconfdir}/timidity.cfg
%ghost %dir %{_datadir}/GUSpatches

%files slang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_s.so

%files motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_m.so
%attr(755,root,root) %{_bindir}/xmmidi

%files tcltk
%defattr(644,root,root,755)
%doc doc/C/README.tk.gz
%attr(755,root,root) %{_libdir}/timidity/interface_k.so
%{_libdir}/timidity/*.tcl
%attr(755,root,root) %{_bindir}/tkmidi

%files xaw
%defattr(644,root,root,755)
%doc doc/C/README.xaw.gz
%attr(755,root,root) %{_libdir}/timidity/interface_a.so
%attr(755,root,root) %{_bindir}/xawmidi

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_g.so
%attr(755,root,root) %{_bindir}/gtkmidi

%files vt100
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_T.so

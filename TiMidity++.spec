#
# Conditional build:
# _without_alsa - without ALSA support
#
Summary:	TiMidity++ - MIDI to WAV converter and player
Summary(pl):	TiMidity++ - konwerter do WAV oraz odtwarzacz plik�w MIDI
Name:		TiMidity++
Version:	2.10.4
Release:	2
License:	GPL
Vendor:		Masanao Izumo <mo@goice.co.jp>
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://www.goice.co.jp/member/mo/timidity/dist/%{name}-%{version}.tar.bz2
Source1:	http://archive.cs.umbc.edu/pub/midia/instruments.tar.gz
Source2:	timidity.cfg
Patch0:		%{name}-config.patch
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	gtk+-devel
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel
BuildRequires:	slang-devel
BuildRequires:	tk-devel >= 8.3.2
URL:		http://www.goice.co.jp/member/mo/timidity/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	timidity
Obsoletes:	timidity++
Obsoletes:	timidity++-X11

%description
TiMidity++ is a converter that converts some of MIDI files ( formats :
Standard MIDI file (MID), Recomposer files (RCP, R36, G18, G36) and
Module file (mod) ) into formatted audio file (ex. RIFF WAVE).
TiMidity uses Gravis Ultrasound-compatible patch files or Soundfonts
(sfx, sf2) to generate digital audio data from MIDI files. The digital
audio data generated by TiMidity can be stored in a file for
processing, or played in real time through an audio device. In real
time playing, TiMidity if able to show the lyric contained in KAR file
or WRD file.

%description -l pl
TiMidity++ jest konwerterem z niekt�rych plik�w MIDI (formaty:
Standard MIDI (MID), Recomposer (RCP, R36, G18, G36), Module (mod)) do
plik�w audio (np. RIFF WAVE). Do generowania danych z plik�w MIDI
TiMidity u�ywa patchy takich jak Gravis Ultrasound albo Soundfont�w
(sfx, sf2). Cyfrowe dane audio mog� by� zapisane do pliku albo
odtwarzane w czasie rzeczywistym. Przy odtwarzaniu TiMidity mo�e
pokazywa� s�owa zawarte w pliku KAR lub WRD.

%package slang
Summary:	Slang interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o bibliotek� Slang
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}

%description slang
Slang interface for TiMidity++.

%description slang -l pl
Interfejs do TiMidity++ oparty o bibliotek� Slang.

%package motif
Summary:	Motif interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o Motif
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}

%description motif
xmmidi -- Motif interface for TiMidity++.

%description motif -l pl
xmmidi - interfejs do TiMidity++ oparty o bibliotek� Motif.

%package tcltk
Summary:	Tcl/Tk interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o Tcl/Tk
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}

%description tcltk
tkmidi -- Tcl/Tk interface for TiMidity++.

%description tcltk -l pl
tkmidi - interfejs do TiMidity++ oparty o Tcl/Tk.

%package xaw
Summary:	Athena interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o Athena Widgets
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}

%description xaw
xawmidi -- Athena interface for TiMidity++.

%description xaw -l pl
xawmidi - interfejs do TiMidity++ oparty o biblitek� widget�w Athena.

%package gtk
Summary:	GTK+ interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o bibliotek� gtk+
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}

%description gtk
gtkmidi -- GTK+ interface for TiMidity++.

%description gtk -l pl
gtkmidi - interfejs do TiMidity++ oparty o bibliotek� gtk+.

%package vt100
Summary:	VT100 interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ dzia�aj�cy na terminalu VT100
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name} = %{version}

%description vt100
VT100 interface for TiMidity++.

%description vt100 -l pl
Interfejs do TiMidity++ mog�cy dzia�a� na terminalu VT100.

%package instruments
Summary:	instruments for TiMidity++
Summary(pl):	instrumenty dla TiMidity++
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Requires:	%{name}

%description instruments
instruments for TiMidity++.

%description instruments -l pl
instrumenty dla TiMidity++

%prep
%setup -q
%patch0 -p1

%build
aclocal
automake -a -c
autoconf
%configure \
	--with-elf \
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
	--enable-spectrogram \
%ifnarch sparc sparc64
	--enable-audio=default,oss,%{!?_without_alsa:alsa,}esd \
	%{!?_without_alsa:--enable-alsaseq} \
%else
	--enable-audio=default,oss,esd \
%endif
	--enable-default-output=default
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/GUSpatches}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

## based on timidity/timidity.c
##ln -s timidity $RPM_BUILD_ROOT%{_bindir}/kmidi # does it work?
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/gtkmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/tkmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/xmmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/xawmidi
ln -s timidity $RPM_BUILD_ROOT%{_bindir}/xskinmidi

install %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}

(cd $RPM_BUILD_ROOT%{_datadir}/GUSpatches ;tar xfvz %{SOURCE1})

gzip -9nf AUTHORS README* ChangeLog* NEWS doc/C/{CHANGES*,FAQ,README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/C/*.gz
%attr(755,root,root) %{_bindir}/timidity
%dir %{_libdir}/timidity
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

%files instruments
%defattr(644,root,root,755)
%{_datadir}/GUSpatches/*

#
# Conditional build:
%bcond_without	x	# without X based interfaces (implies libX11 deps)
%bcond_without	alsa	# without ALSA support
%bcond_with	arts	# enable ARTS support (implies also glib(2) deps)
%bcond_with	esd	# enable ESD support
%bcond_with	jack	# enable JACK support
%bcond_with	nas	# enable NAS support
%bcond_with	vorbis	# enable Ogg Vorbis support
#
Summary:	TiMidity++ - MIDI to WAV converter and player
Summary(pl.UTF-8):	TiMidity++ - konwerter do WAV oraz odtwarzacz plików MIDI
Summary(pt_BR.UTF-8):	Sintetizador MIDI por software
Summary(ru.UTF-8):	Проигрыватель MIDI файлов и конвертор их в WAV формат
Summary(uk.UTF-8):	Програвач MIDI-файлів та конвертор їх в WAV формат
Name:		TiMidity++
Version:	2.13.2
Release:	9
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/timidity/%{name}-%{version}.tar.bz2
# Source0-md5:	a82ceeb2245e22f4de2b41da21eaee32
Source1:	http://archive.cs.umbc.edu/pub/midia/instruments.tar.gz
# Source1-md5:	4959787a78ee39d44a36185bd303cf20
Source2:	britepno.pat.bz2
# Source2-md5:	324e265362f812883024b58cf3470d1a
Source3:	pistol.pat.bz2
# Source3-md5:	f961325db679de6e0ea402ebe6a268f9
Source4:	timidity.cfg
Source5:	timidity.init
Source6:	timidity.sysconfig
Source7:	timidity-modules-load.conf
Source8:	timidity.service
Patch0:		%{name}-detach.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-configure.patch
Patch3:		%{name}-stop_polling.patch
URL:		http://timidity.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf
%{?with_esd:BuildRequires:	esound-devel}
%{?with_x:BuildRequires:	gtk+-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_vorbis:BuildRequires:	libvorbis-devel}
%{?with_x:BuildRequires:	motif-devel}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.626
BuildRequires:	slang-devel >= 2.0.0
%{?with_x:BuildRequires:	tk-devel >= 8.3.2}
%{?with_x:Provides:	%{name}(X) = %{version}-%{release}}
Obsoletes:	timidity
Obsoletes:	timidity++
Obsoletes:	timidity++-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
TiMidity++ jest konwerterem z niektórych plików MIDI (formaty:
Standard MIDI (MID), Recomposer (RCP, R36, G18, G36), Module (mod)) do
plików audio (np. RIFF WAVE). Do generowania danych z plików MIDI
TiMidity używa patchy takich jak Gravis Ultrasound albo Soundfontów
(sfx, sf2). Cyfrowe dane audio mogą być zapisane do pliku albo
odtwarzane w czasie rzeczywistym. Przy odtwarzaniu TiMidity może
pokazywać słowa zawarte w pliku KAR lub WRD.

%description -l pt_BR.UTF-8
O TiMidity++ é um sintetizador MIDI por software. Este pacote permite
ouvir arquivos do tipo MIDI com a mesma qualidade de som que as placas
que utilizam o recurso de "wavetable" via hardware (como a AWE32),
mesmo que esta não possua o recurso de "wavetable" (a SB16 por
exemplo).

%description -l ru.UTF-8
Проигрыватель MIDI файлов, не требующий поддержки инструментов MIDI
звуковой платой. Использует файлы инструментов в формате GUS/patch,
может также использовать данные в формате SoundFont. Обеспечивает
отличное качество звука MIDI за счет интенсивного использования
процессора.

%description -l uk.UTF-8
Програвач MIDI файлів, якому не потрібна підтримка інструментів MIDI
звуковою платою. Використовує файли інструментів у форматі GUS/patch,
розуміє також формат SoundFont. Забезпечує відмінну якість звуку MIDI
за рахунок інтенсивного використання процесора.

%package gspdir
Summary:	Directory for TiMidity++ instruments
Summary(pl.UTF-8):	Katalog na instrumenty TiMidity++
Group:		Applications/Sound

%description gspdir
Directory where TiMidity++ instruments should be placed in.

%description gspdir -l pl.UTF-8
Katalog, w którym powinny być instalowane instrumenty dla TiMidity++.

%package instruments
Summary:	Instruments for TiMidity++
Summary(pl.UTF-8):	Instrumenty dla TiMidity++
Summary(pt_BR.UTF-8):	Instrumentos básicos para o TiMidity++
Group:		Applications/Sound
Requires:	%{name}-gspdir = %{version}-%{release}
Obsoletes:	timidity-patches

%description instruments
Instruments for TiMidity++.

%description instruments -l pl.UTF-8
Instrumenty dla TiMidity++.

%description instruments -l pt_BR.UTF-8
Este pacote inclui um conjunto básico de instrumentos (chamados de
patches no meio musical) para o TiMidity++.

%package gtk
Summary:	GTK+ interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ oparty o bibliotekę GTK+
Group:		Applications/Sound
Requires:	%{name}(X) = %{version}-%{release}

%description gtk
gtkmidi - GTK+ interface for TiMidity++.

%description gtk -l pl.UTF-8
gtkmidi - interfejs do TiMidity++ oparty o bibliotekę GTK+.

%package motif
Summary:	Motif interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ oparty o Motif
Group:		Applications/Sound
Requires:	%{name}(X) = %{version}-%{release}

%description motif
xmmidi - Motif interface for TiMidity++.

%description motif -l pl.UTF-8
xmmidi - interfejs do TiMidity++ oparty o bibliotekę Motif.

%package slang
Summary:	Slang interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ oparty o bibliotekę Slang
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description slang
Slang interface for TiMidity++.

%description slang -l pl.UTF-8
Interfejs do TiMidity++ oparty o bibliotekę Slang.

%package tcltk
Summary:	Tcl/Tk interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ oparty o Tcl/Tk
Group:		Applications/Sound
Requires:	%{name}(X) = %{version}-%{release}

%description tcltk
tkmidi - Tcl/Tk interface for TiMidity++.

%description tcltk -l pl.UTF-8
tkmidi - interfejs do TiMidity++ oparty o Tcl/Tk.

%package vt100
Summary:	VT100 interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ działający na terminalu VT100
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description vt100
VT100 interface for TiMidity++.

%description vt100 -l pl.UTF-8
Interfejs do TiMidity++ mogący działać na terminalu VT100.

%package xaw
Summary:	Athena interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ oparty o Athena Widgets
Group:		Applications/Sound
Requires:	%{name}(X) = %{version}-%{release}

%description xaw
xawmidi - Athena interface for TiMidity++.

%description xaw -l pl.UTF-8
xawmidi - interfejs do TiMidity++ oparty o biblitekę widgetów Athena.

%package xskin
Summary:	"X Skin" interface for TiMidity++
Summary(pl.UTF-8):	Interfejs TiMidity++ "X Skin"
Group:		Applications/Sound
Requires:	%{name}(X) = %{version}-%{release}
Obsoletes:	TiMidity++ < 2.13.0-3

%description xskin
xskinmidi - "X Skin" interface for TiMidity++.

%description xskin -l pl.UTF-8
xskinmidi - interfejs do TiMidity++ "X Skin".

%package alsaseq
Summary:	TiMidity++ ALSA sequencer interface
Summary(pl.UTF-8):	TiMidity++ jako interfejs sekwencera ALSA
Group:		Applications/Sound
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts
Requires:	systemd-units >= 38

%description alsaseq
The ALSA sequencer interface communicates between ALSA sequencer core
and timidity. The interface receives events from sequencer and plays
it in (quasi-)real-time. In this mode, TiMidity works purely as the
software real-time MIDI render, that is as a software MIDI synth
engine on ALSA.

%description alsaseq -l pl.UTF-8
Interfejs sekwencera ALSA komunikuje się między rdzeniem sekwencera
ALSA a timidity. Interfejs odbiera zdarzenia od sekwencera od odtwarza
je w czasie (prawie) rzeczywistym. W tym trybie TiMidity działa
wyłącznie jako programowy odtwarzacz MIDI czasu rzeczywistego, czyli
jako silnik syntezatora MIDI w architekturze ALSA.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

for f in doc/ja_JP.eucJP/README*; do
	mv -f $f ${f}.ja
done

%build
cp -f /usr/share/automake/config.sub autoconf
%{__autoconf}

AUDIO=oss%{?with_alsa:,alsa}%{?with_arts:,arts}%{?with_esd:,esd}\
%{?with_jack:,jack}%{?with_nas:,nas}%{?with_vorbis:,vorbis}

%configure \
	%{?with_alsa:--enable-alsaseq} \
	--enable-audio=$AUDIO \
	--enable-dynamic \
	%{?with_x:--enable-gtk=dynamic} \
	--enable-emacs=dynamic \
	%{?with_x:--enable-motif=dynamic} \
	--enable-ncurses=dynamic \
	--enable-network \
	--enable-server \
	--enable-slang=dynamic \
	%{?with_x:--enable-spectrogram} \
	%{?with_x:--enable-tcltk=dynamic} \
	--enable-vt100=dynamic \
	%{?with_x:--enable-xaw=dynamic} \
	%{?with_x:--enable-xskin=dynamic} \
	--with-default-path=%{_sysconfdir} \
	--with-elf \
	%{!?with_x:--without-x}

%{__make} \
	SHLIB_DIR=%{_libdir}/timidity

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/GUSpatches,/etc/{rc.d/init.d,sysconfig}} \
	$RPM_BUILD_ROOT{%{systemdunitdir},/etc/modules-load.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SHLIB_DIR=%{_libdir}/timidity

## based on timidity/timidity.c
##ln -s timidity $RPM_BUILD_ROOT%{_bindir}/kmidi # does it work?
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/gtkmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/tkmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/xmmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/xawmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/xskinmidi

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man{1,5}
install doc/ja_JP.eucJP/timidity.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1
install doc/ja_JP.eucJP/timidity.cfg.5 $RPM_BUILD_ROOT%{_mandir}/ja/man5

install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}

cd $RPM_BUILD_ROOT%{_datadir}/GUSpatches
tar xzf %{SOURCE1}
mv -f instruments/* .
rmdir instruments
bzip2 -cd %{SOURCE2} > britepno.pat
bzip2 -cd %{SOURCE3} > pistol.pat

install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/timidity
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/timidity

install %{SOURCE7} $RPM_BUILD_ROOT/etc/modules-load.d/timidity.conf
install %{SOURCE8} $RPM_BUILD_ROOT%{systemdunitdir}/timidity.service

%clean
rm -rf $RPM_BUILD_ROOT

%post alsaseq
/sbin/chkconfig --add timidity
%service timidity restart "TiMidity++ ALSA sequencer interface"
%systemd_post timidity.service

%preun alsaseq
if [ "$1" = "0" ]; then
	%service timidity stop
	/sbin/chkconfig --del timidity
fi
%systemd_preun timidity.service

%postun alsaseq
%systemd_reload

%triggerpostun alsaseq -- %{name}-alsaseq < 2.13.2-8
%systemd_trigger timidity.service

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README TODO doc/C/{CHANGES*,FAQ,README.[!tx]*}
%lang(ja) %doc README.ja doc/ja_JP.eucJP/README.[!tx]*.ja
%attr(755,root,root) %{_bindir}/timidity
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/timidity.cfg
%dir %{_libdir}/timidity
%attr(755,root,root) %{_libdir}/timidity/interface_e.so
%attr(755,root,root) %{_libdir}/timidity/interface_n.so
%{_libdir}/timidity/interface_e.txt
%{_libdir}/timidity/interface_n.txt
%if "%{_lib}" != "lib"
%dir %{_prefix}/lib/timidity
%endif
%{?with_x:%{_prefix}/lib/timidity/bitmaps}
%{_mandir}/man1/timidity.1*
%{_mandir}/man5/timidity.cfg.5*
%lang(ja) %{_mandir}/ja/man1/timidity.1*
%lang(ja) %{_mandir}/ja/man5/timidity.cfg.5*

%files gspdir
%defattr(644,root,root,755)
%dir %{_datadir}/GUSpatches

%files instruments
%defattr(644,root,root,755)
%{_datadir}/GUSpatches/*

%if %{with x}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkmidi
%attr(755,root,root) %{_libdir}/timidity/interface_g.so
%{_libdir}/timidity/interface_g.txt
%endif

%if %{with x}
%files motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmmidi
%attr(755,root,root) %{_libdir}/timidity/interface_m.so
%{_libdir}/timidity/interface_m.txt
%endif

%files slang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_s.so
%{_libdir}/timidity/interface_s.txt

%if %{with x}
%files tcltk
%defattr(644,root,root,755)
%doc doc/C/README.tk
%lang(ja) %doc doc/ja_JP.eucJP/README.tk.ja
%attr(755,root,root) %{_bindir}/tkmidi
%attr(755,root,root) %{_libdir}/timidity/interface_k.so
%{_libdir}/timidity/interface_k.txt
%{_prefix}/lib/timidity/tclIndex
%{_prefix}/lib/timidity/*.tcl
%endif

%files vt100
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_T.so
%{_libdir}/timidity/interface_T.txt

%if %{with x}
%files xaw
%defattr(644,root,root,755)
%doc doc/C/README.xaw
%lang(ja) %doc doc/ja_JP.eucJP/README.xaw.ja
%attr(755,root,root) %{_bindir}/xawmidi
%attr(755,root,root) %{_libdir}/timidity/interface_a.so
%{_libdir}/timidity/interface_a.txt

%files xskin
%defattr(644,root,root,755)
%doc doc/C/README.xskin
%lang(ja) %doc doc/ja_JP.eucJP/README.xskin.ja
%attr(755,root,root) %{_bindir}/xskinmidi
%attr(755,root,root) %{_libdir}/timidity/interface_i.so
%{_libdir}/timidity/interface_i.txt
%endif

%if %{with alsa}
%files alsaseq
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/timidity
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/timidity
%config(noreplace) %verify(not md5 mtime size) /etc/modules-load.d/timidity.conf
%{systemdunitdir}/timidity.service
%endif

#
# Conditional build:
%bcond_without	alsa	# disable ALSA support
%bcond_with	arts	# enable ARTS support
%bcond_with	esd	# enable ESD support
%bcond_with	jack	# enable JACK support
%bcond_with	nas	# enable NAS support
%bcond_with	vorbis	# enable Ogg Vorbis support
#

%define		_pkgname	timidity
%define		_ver		2.12.1
%define		_snap		040103

Summary:	TiMidity++ - MIDI to WAV converter and player
Summary(pl):	TiMidity++ - konwerter do WAV oraz odtwarzacz plik�w MIDI
Summary(pt_BR):	Sintetizador MIDI por software
Summary(ru):	������������� MIDI ������ � ��������� �� � WAV ������
Summary(uk):	��������� MIDI-���̦� �� ��������� �� � WAV ������
Name:		TiMidity++
Version:	%{_ver}
Release:	0.%{_snap}.1
License:	GPL
Vendor:		Masanao Izumo <mo@goice.co.jp>
Group:		Applications/Sound
#Source0:	http://www.goice.co.jp/member/mo/timidity/dist/%{name}-%{version}.tar.bz2
#Source0:	http://www.goice.co.jp/member/mo/timidity/dist/%{name}-%{_ver}-%{_pre}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/pld/%{_pkgname}-%{_snap}.tar.bz2
# Source0-md5:	29695ccdb64247ef48f41cb279f00e76
Source1:	instruments.tar.gz
# Source1-md5:	4959787a78ee39d44a36185bd303cf20
Source2:	britepno.pat.bz2
# Source2-md5:	324e265362f812883024b58cf3470d1a
Source3:	pistol.pat.bz2
# Source3-md5:	f961325db679de6e0ea402ebe6a268f9
Source4:	timidity.cfg
URL:		http://timidity.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-devel}
%{?with_esd:BuildRequires:	esound-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_nas:BuildRequires:	nas-devel}
%{?with_vorbis:BuildRequires:	libvorbis-devel}
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel
BuildRequires:	slang-devel
BuildRequires:	tk-devel >= 8.3.2
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

%description -l pt_BR
O TiMidity++ � um sintetizador MIDI por software. Este pacote permite
ouvir arquivos do tipo MIDI com a mesma qualidade de som que as placas
que utilizam o recurso de "wavetable" via hardware (como a AWE32),
mesmo que esta n�o possua o recurso de "wavetable" (a SB16 por
exemplo).

%description -l ru
������������� MIDI ������, �� ��������� ��������� ������������ MIDI
�������� ������. ���������� ����� ������������ � ������� GUS/patch,
����� ����� ������������ ������ � ������� SoundFont.
������������ �������� �������� ����� MIDI �� ���� ������������
������������� ����������.

%description -l uk
��������� MIDI ���̦�, ����� �� ���Ҧ��� Ц������� ���������Ԧ� MIDI
�������� ������. ����������դ ����� ���������Ԧ� � �����Ԧ GUS/patch,
����ͦ� ����� ������ SoundFont.
��������դ צ�ͦ��� �˦��� ����� MIDI �� ������� ������������
������������ ���������.

%package gtk
Summary:	GTK+ interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o bibliotek� gtk+
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description gtk
gtkmidi - GTK+ interface for TiMidity++.

%description gtk -l pl
gtkmidi - interfejs do TiMidity++ oparty o bibliotek� gtk+.

%package instruments
Summary:	Instruments for TiMidity++
Summary(pl):	Instrumenty dla TiMidity++
Summary(pt_BR):	Instrumentos b�sicos para o TiMidity++
Group:		Applications/Sound
Obsoletes:	timidity-patches

%description instruments
Instruments for TiMidity++.

%description instruments -l pl
Instrumenty dla TiMidity++.

%description instruments -l pt_BR
Este pacote inclui um conjunto b�sico de instrumentos (chamados de
patches no meio musical) para o TiMidity++.

%package motif
Summary:	Motif interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o Motif
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description motif
xmmidi - Motif interface for TiMidity++.

%description motif -l pl
xmmidi - interfejs do TiMidity++ oparty o bibliotek� Motif.

%package slang
Summary:	Slang interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o bibliotek� Slang
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description slang
Slang interface for TiMidity++.

%description slang -l pl
Interfejs do TiMidity++ oparty o bibliotek� Slang.

%package tcltk
Summary:	Tcl/Tk interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o Tcl/Tk
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description tcltk
tkmidi - Tcl/Tk interface for TiMidity++.

%description tcltk -l pl
tkmidi - interfejs do TiMidity++ oparty o Tcl/Tk.

%package vt100
Summary:	VT100 interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ dzia�aj�cy na terminalu VT100
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description vt100
VT100 interface for TiMidity++.

%description vt100 -l pl
Interfejs do TiMidity++ mog�cy dzia�a� na terminalu VT100.

%package xaw
Summary:	Athena interface for TiMidity++
Summary(pl):	Interfejs TiMidity++ oparty o Athena Widgets
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description xaw
xawmidi - Athena interface for TiMidity++.

%description xaw -l pl
xawmidi - interfejs do TiMidity++ oparty o biblitek� widget�w Athena.

%prep
%setup -q -n %{_pkgname}-%{_snap}

%build

AUDIO=oss%{?with_alsa:,alsa}%{?with_arts:,arts}%{?with_esd:,esd}\
%{?with_jack:,jack}%{?with_nas:,nas}%{?with_vorbis:,vorbis}

%configure \
	%{?with_alsa:--enable-alsaseq} \
	--enable-audio=$AUDIO \
	--enable-dynamic \
	--enable-gtk=dynamic \
	--enable-emacs=dynamic \
	--enable-motif=dynamic \
	--enable-ncurses=dynamic \
	--enable-network \
	--enable-server \
	--enable-slang=dynamic \
	--enable-spectrogram \
	--enable-tcltk=dynamic \
	--enable-vt100=dynamic \
	--enable-xaw=dynamic \
	--enable-xskin=dynamic \
	--with-default-path=%{_sysconfdir} \
	--with-elf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/GUSpatches}

## based on timidity/timidity.c
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/gtkmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/tkmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/xawmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/xmmidi
ln -sf timidity $RPM_BUILD_ROOT%{_bindir}/xskinmidi

install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}

cd $RPM_BUILD_ROOT%{_datadir}/GUSpatches
tar xzf %{SOURCE1}
mv -f instruments/* .
rmdir instruments
bzip2 -cd %{SOURCE2} > britepno.pat
bzip2 -cd %{SOURCE3} > pistol.pat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc A* Ch* N* R* TO* doc/C/{C*,F*,README.[!tx]*,README.xs*}
%config(noreplace) %{_sysconfdir}/timidity.cfg
%attr(755,root,root) %{_bindir}/timidity
%dir %{_libdir}/timidity
%attr(755,root,root) %{_libdir}/timidity/interface_n.so
%attr(755,root,root) %{_libdir}/timidity/interface_e.so
%attr(755,root,root) %{_libdir}/timidity/interface_i.so
%{_libdir}/timidity/bitmaps
%{_mandir}/man*/*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_g.so
%attr(755,root,root) %{_bindir}/gtkmidi

%files instruments
%defattr(644,root,root,755)
%{_datadir}/GUSpatches/*

%files motif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_m.so
%attr(755,root,root) %{_bindir}/xmmidi

%files slang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_s.so

%files tcltk
%defattr(644,root,root,755)
%doc doc/C/README.tk
%attr(755,root,root) %{_libdir}/timidity/interface_k.so
%{_libdir}/timidity/tclIndex
%{_libdir}/timidity/*.tcl
%attr(755,root,root) %{_bindir}/tkmidi

%files vt100
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/timidity/interface_T.so

%files xaw
%defattr(644,root,root,755)
%doc doc/C/README.xaw
%attr(755,root,root) %{_libdir}/timidity/interface_a.so
%attr(755,root,root) %{_bindir}/xawmidi

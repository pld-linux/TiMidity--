Summary:	TiMidity++ - MIDI to WAV converter and player
Name:		-
Version:	-
Release:	-
Group:		-
Copyright:	GPL
Vendor:		Masanao Izumo <mo@goice.co.jp>
Icon:		-
Source0:	http://www.goice.co.jp/member/mo/timidity/dist/%{name}-%{version}.tar.bz2
URL:		http://www.goice.co.jp/member/mo/timidity/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
TiMidity++ is a converter that converts some of MIDI files ( formats :
Standard MIDI file (*.MID), Recomposer files (*.RCP, *.R36, *.G18, *.G36)
and Module file (*.mod) ) into formatted audio file (ex. RIFF WAVE).
TiMidity uses Gravis Ultrasound-compatible patch files or Soundfonts (*.sfx,
*.sf2) to generate digital audio data from MIDI files. The digital audio
data generated by TiMidity can be stored in a file for processing, or played
in real time through an audio device. In real time playing, TiMidity if able
to show the lylic contained in KAR file or WRD file.

%prep
%setup -q

%build
(autoheader/autoconf/automake)
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	$RPM_BUILD_ROOT%{_mandir}/man*/* \
	README ChangeLog 

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%changelog

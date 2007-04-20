%define branch_date 20070418

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/
%define multiarch_bindir               %_bindir/%{multiarch_platform}
%define multiarch_includedir           /usr/include/%{multiarch_platform}
%define multiarch_x11bindir            /usr//X11R6/bin/%{multiarch_platform}
%define multiarch_x11includedir        /usr/X11R6/include/%{multiarch_platform}

%define multiarch_binaries() \
/usr/lib/rpm/mkmultiarch binaries %* 

%define multiarch_includes() \
/usr/lib/rpm/mkmultiarch includes %* 




%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif
 
%define lib_name_orig %mklibname kdepim4
%define lib_major 2
%define lib_name %lib_name_orig%lib_major

%define lib_name_orig_akregator %mklibname akregator
%define lib_major_akregator 0
%define lib_name_akregator %lib_name_orig_akregator%lib_major_akregator

Name: 		kdepim4
Version: 	3.80.3
Release: 	%mkrel 0.%branch_date.5
Epoch: 		1
Group: 		Graphical desktop/KDE
Summary:	K Desktop Environment - Person Information Management
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
License:	GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version-%branch_date.tar.bz2
%else
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.tar.bz2
%endif
Source1:	kdepim-3.2-kontact-addressbook.sh  
Source2:	kdepim-3.2-kontact-knotes.sh
Source3:	kdepim-3.2-kontact-kmail.sh        
Source4:	kdepim-3.2-kontact-korganizer.sh
Source5:	kdepim-3.2-kontact-knode.sh
Source6:	kdepim-3.2-kontact-akregator.sh
######   Patches   ########
Patch85:	kdepim-3.4.0-kmail-first-message.patch
Patch86:	kdepim-3.3.2-fix-kmail-column-info.patch
Patch111:	kdepim-3.4.0-fix-kmail-dont-empty-trash-in-exit.patch
Patch113:	kdepim-3.4.0-fix-kmail-dimap-speedup.patch
Patch200:	kdepim-3.4.0-use-point-kmail.patch
Patch203:	kdepim-3.4.2-knode-disable-first-start.patch
Patch204:	kdepim-3.5.2-fix-akregator-bug-15569.patch
Patch205:	kdepim-3.5.3-fix-config-clear-trash.patch
Patch207:       kdepim-3.5.3-kaddressbook-resources.patch
Patch208:       kdepim-3.5.4-fix-kalarm-call-twice-dialogbox.patch
Patch209:       kdepim-3.5.4-korganizer-avoid-spam-example_net.patch
Patch210:       kdepim-3.5.4-korganizer-use-sys-timezone.patch
Patch211:       kdepim-3.5.4-kontact-sidebar-disable-show-text.patch
Patch212:	kdepim-3.5.5-fix-korganizer.patch
Patch213:	kdepim-3.5.5-fix-korganizer-mem-leak.patch
BuildRoot: 	%_tmppath/%name-%version-%release-root

%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires:  kdepimlibs4-devel >= %version-%mini_release
#Need by kontact/plugins/weather
BuildRequires:	kdetoys4-devel >= %version-%mini_release
BuildRequires:	gpgme-devel 
BuildRequires: X11-devel 
BuildRequires: flex 
BuildRequires: byacc 
BuildRequires: pam
BuildRequires: libmal-devel >= 0.31
BuildRequires: libncurses-devel
BuildRequires: readline-devel
BuildRequires: pilot-link-devel
BuildRequires: libgpg-error-devel
BuildRequires: gnokii-devel
BuildRequires: libxml2-utils
BuildRequires: gnupg
BuildRequires: bluez-devel 
BuildRequires: libsasl-devel
BuildRequires:	pilot-link-devel
BuildRequires:	libxslt-proc

BuildRequires:	opensync-devel

Requires:	%name-karm = %epoch:%version-%release
Requires:	%name-knotes = %epoch:%version-%release
Requires:	%name-kaddressbook = %epoch:%version-%release
Requires:	%name-kpilot = %epoch:%version-%release
Requires:	%name-kmail = %epoch:%version-%release
Requires:	%name-knode = %epoch:%version-%release
Requires:	%name-kontact = %epoch:%version-%release
Requires:	%name-korganizer = %epoch:%version-%release
Requires:	%name-korn = %epoch:%version-%release
Requires:	%name-ktnef = %epoch:%version-%release
Requires:	%name-akregator = %epoch:%version-%release


%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kpilot: to sync with your PalmPilot
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer and
           kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- karm: Time tracker.
	- kitchensync: Synchronisation framework, still under heavy development.
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client
	- kmailcvt: converst addressbooks to kmail format

%files

#----------------------------------------------------------------------

%package common
Summary:	Common files for kdepim
Group:		Graphical desktop/KDE
Provides:	kdepim4
Requires:       sasl-plug-digestmd5
Requires:       sasl-plug-login
Requires:       sasl-plug-plain
Requires:       kde-custom-icons
Requires:       %lib_name-common = %epoch:%version-%release

%description common
Common files for kdepim

%post common -p /sbin/ldconfig 
%postun common -p /sbin/ldconfig

%files common
%defattr(-,root,root,-)
%dir %_datadir/apps/akonadi/agents/
%_datadir/apps/akonadi/agents/ical.svg
%_datadir/apps/akonadi/agents/icalresource.desktop
%_datadir/apps/akonadi/agents/knut.svg
%_datadir/apps/akonadi/agents/knutresource.desktop
%_iconsdir/*/*/*/button_*
%_datadir/kde4/services/imap4.protocol
%_datadir/kde4/services/imaps.protocol
%_datadir/kde4/services/kcmsdsummary.desktop
%_datadir/kde4/servicetypes/dbusimap.desktop
%_datadir/kde4/servicetypes/kaddressbook_contacteditorwidget.desktop
%_datadir/kde4/servicetypes/kaddressbookimprotocol.desktop
%_bindir/kode
%_bindir/kxml_compiler
%_bindir/kleopatra
%_bindir/kwatchgnupg
%_bindir/sloxwizard
%_bindir/akonadi_control
%_bindir/akonadi_ical_resource
%_bindir/akonadi_knut_resource
%_bindir/akonadiconsole
%_bindir/akonadiserver
%_bindir/akonadi
%_bindir/akonadi_nntp_resource
%_bindir/akonadi_vcard_resource
%_bindir/egroupwarewizard
%_bindir/groupwarewizard
%_bindir/kabcclient
%_bindir/kagenda
%_bindir/ktimetracker
%_bindir/kung
%_bindir/kwsdl_compiler
%_bindir/kxforms
%_bindir/schematest

%_datadir/kde4/services/akonadi.protocol

%dir %_datadir/apps/akonadi/agents/
%_datadir/apps/akonadi/agents/nntpresource.desktop
%_datadir/apps/akonadi/agents/vcard.svg
%_datadir/apps/akonadi/agents/vcardresource.desktop

%_datadir/icons/crystalsvg/16x16/actions/new_from_template.png
%_datadir/icons/crystalsvg/22x22/actions/new_from_template.png

%_datadir/kde4/services/kcmapptsummary.desktop
%_datadir/kde4/services/kcmtodosummary.desktop
%_datadir/config.kcfg/kxforms.kcfg
%_datadir/config.kcfg/mailtransport.kcfg

%_datadir/apps/kleopatra/kleopatraui.rc
%dir %_datadir/apps/libkleopatra/
%_datadir/apps/libkleopatra/*
%_datadir/applications/kde4/kleopatra_import.desktop
%dir %_datadir/apps/kwatchgnupg/
%_datadir/apps/kwatchgnupg/*
%dir %_datadir/apps/libkdepim
%_datadir/apps/libkdepim/*
%dir %_datadir/apps/kdepimwidgets
%_datadir/apps/kdepimwidgets/*
%_datadir/config.kcfg/custommimeheader.kcfg
%_datadir/config.kcfg/groupwise.kcfg
%_datadir/config.kcfg/pimemoticons.kcfg
%_datadir/config.kcfg/replyphrases.kcfg

%_libdir/kde4/kcm_sdsummary.*
%_libdir/kde4/kio_imap4.*
%_libdir/kde4/kio_mbox.*
%_libdir/kde4/kio_sieve.*
%_libdir/kde4/kcal_*

%_libdir/strigi/strigiea_ics.so
%_libdir/strigi/strigiea_rfc822.so

%_libdir/kcal_resourcefeatureplan.so.*
%_libdir/kabc_groupdav.so.*
%_libdir/kcal_groupdav.so.*
%_libdir/kde4/kcm_kleopatra.*
%_libdir/kde4/kcm_kontactsummary.*

%_libdir/kde4/kcm_mailtransport.so
%_datadir/kde4/services/kcm_mailtransport.desktop


%_datadir/applications/kde4/groupwarewizard.desktop
%_datadir/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%_datadir/apps/kconf_update/kpgp.upd
%dir %_datadir/kde4/services/kresources
%_datadir/kde4/services/kresources/*
%_datadir/kde4/services/kcmkontactsummary.desktop
%_datadir/kde4/services/kleopatra_*
%_datadir/config.kcfg/egroupware.kcfg
%_datadir/config.kcfg/knoteconfig.kcfg
%_datadir/config.kcfg/slox.kcfg
%_datadir/kde4/services/sieve.protocol
%_datadir/kde4/servicetypes/dbuscalendar.desktop
%_datadir/kde4/servicetypes/korgprintplugin.desktop		 
%_datadir/applications/kde4/konsolekalendar.desktop
%_iconsdir/*/*/*/konsolekalendar.*

%_iconsdir/*/*/*/korganizer*
%_datadir/apps/korgac/icons/crystalsvg/22x22/actions/korgac.png
%_datadir/apps/korgac/icons/crystalsvg/22x22/actions/korgac_disabled.png
%_datadir/kde4/services/mbox.protocol
%exclude %_datadir/kde4/services/kresources/knotes_manager.desktop
%exclude %_datadir/kde4/services/kresources/kabc

%_datadir/applications/kde4/kwsdl_compiler.desktop
%_datadir/apps/kconf_update/migrate-transports.pl
%_datadir/apps/kxforms/kxformsui.rc
%_datadir/config.kcfg/kolab.kcfg

%_datadir/dbus-1/services/org.kde.Akonadi.Control.service

%dir %_docdir/HTML/en/ktimetracker/
%doc %_docdir/HTML/en/ktimetracker/*.bz2
%doc %_docdir/HTML/en/ktimetracker/*.docbook
%doc %_docdir/HTML/en/ktimetracker/*.png
%dir %_docdir/HTML/en/konsolekalendar/*
%doc %_docdir/HTML/en/konsolekalendar/*.bz2
%doc %_docdir/HTML/en/konsolekalendar/*.docbook

#----------------------------------------------------------------------

%package    korn
Group:      Graphical desktop/KDE
Summary:    korn
Provides:   korn4
Requires:   %lib_name-common = %epoch:%version-%release

%description korn
A mail checker


%files korn
%defattr(-,root,root,-)
%_bindir/korn             
%_datadir/applications/kde4/KOrn.desktop
%_datadir/apps/kconf_update/korn-*
%_iconsdir/*/*/*/korn*
%dir %_docdir/HTML/en/korn/
%doc %_docdir/HTML/en/korn/*.bz2
%doc %_docdir/HTML/en/korn/*.docbook

#----------------------------------------------------------------------

%package akregator
Group:      Graphical desktop/KDE
Summary:    aKregator is KDE RSS aggregator with great look and feel.
Provides:   akregator4 = %epoch:%version-%release

%description akregator
aKregator is KDE RSS aggregator with great look and feel.


%files akregator
%defattr(-,root,root,0755)
%_bindir/akregator
%_bindir/kontact-akregator.sh
%_libdir/kde4/libakregator*
%_libdir/libakregatorprivate.*
%_datadir/kde4/services/kontact/akregatorplugin.desktop
%_datadir/applications/kde4/akregator.desktop
%dir %_datadir/apps/akregator
%_datadir/apps/akregator/*
%_iconsdir/*/*/*/rss_tag*
%_iconsdir/*/*/*/akregator*
%_datadir/config.kcfg/akregator.kcfg
%_datadir/kde4/services/akregator_part.desktop   
%_datadir/kde4/services/feed.protocol
%_datadir/kde4/services/kontact/akregatorplugin3.2.desktop
%_datadir/kde4/services/akregator_mk4storage_plugin.desktop
%_datadir/kde4/servicetypes/akregator_plugin.desktop
%dir %_docdir/HTML/en/akregator/
%doc %_docdir/HTML/en/akregator/*.png
%doc %_docdir/HTML/en/akregator/*.bz2
%doc %_docdir/HTML/en/akregator/*.docbook

#----------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Devel stuff for kdepim
Group:		Development/KDE and Qt
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	%lib_name-ktnef = %epoch:%version-%release
Provides:	%lib_name-devel = %epoch:%version-%release
Provides:	kdepim4-devel = %epoch:%version-%release

%description -n %lib_name-common-devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files -n %lib_name-common-devel
%defattr(-,root,root)
%_libdir/kde4/plugins/designer/*
%_includedir/akregator/*.h
%dir %_includedir/qgpgme/
%_includedir/qgpgme/*.h
%_libdir/libkocorehelper.so
%_libdir/libkholidays.so
%_libdir/libkgroupwarebase.so
%_libdir/libkgroupwaredav.so
%_libdir/libkode.so
%_libdir/libkcal_*.so
%_libdir/libknotes_xmlrpc.so
%_libdir/libkorganizer_calendar.so
%_libdir/libkslox.so
%_libdir/libkschema.so
%_libdir/libkschemawidgets.so
%_libdir/libkxmlcommon.so
%_libdir/libmailtransport.so
%_libdir/libschema.so
%_libdir/libwscl.so
%_libdir/libwsdl.so
%_libdir/libakonadiprivate.so
%_libdir/libgpgme++.so
%_libdir/libkdepim.so
%_libdir/libkleopatra.so
%_libdir/libkpgp.so
%_libdir/libkpimidentities.so
%_libdir/libksieve.so
%_libdir/libmimelib.so
%_libdir/libqgpgme.so


%dir %_includedir/ksieve/
%_includedir/ksieve/*.h
%dir %_includedir/mimelib/
%_includedir/mimelib/*.h

%_datadir/dbus-1/interfaces/*.xml

%_datadir/apps/cmake/modules/FindKode.cmake
%_datadir/apps/cmake/modules/KodeMacros.cmake

%_libdir/kcal_resourcefeatureplan.so

%_libdir/libakonadi.so
%_libdir/libakonadicomponents.so
%_libdir/libakonadiresources.so
%_libdir/libakonadisearchprovider.so
%_libdir/kcal_groupdav.so

%dir %_includedir/libakonadi/
%_includedir/libakonadi/*.h
%dir %_includedir/libakonadiresources/
%_includedir/libakonadiresources/*.h
%_libdir/kabc_groupdav.so

%_includedir/kcal/*.h
%_includedir/kdepimprotocols.h
%dir %_includedir/libakonadi/components/
%_includedir/libakonadi/components/*.h

#----------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Library for kdepim
Group:		Development/KDE and Qt
Provides:	%lib_name_orig-common = %epoch:%version-%release
Provides:	%lib_name = %epoch:%version-%release

%description -n %lib_name-common
This package contains header files needed if you wish to build applications
based on kdepim.

%post -n %lib_name-common -p /sbin/ldconfig
%postun -n %lib_name-common -p /sbin/ldconfig

%files -n %lib_name-common
%defattr(-,root,root)
%_libdir/libakonadiprivate.so.*
%_libdir/libkgroupwarebase.so.*
%_libdir/libkgroupwaredav.so.*
%_libdir/libkpgp.so.*
%_libdir/libkdepim.so.*
%_libdir/libkholidays.so.*
%_libdir/libksieve.so.*
%_libdir/libmimelib.so.*
%_libdir/libkode.so.*
%_libdir/libkocorehelper.so.*
%_libdir/libgpgme++.so.*

%_libdir/kde4/kio_akonadi.so
%_libdir/libkcal_*.so.*
%_libdir/libkleopatra.so.*
%_libdir/libknotes_xmlrpc.so.*
%_libdir/libkorganizer_calendar.so.*
%_libdir/libkpimidentities.so.*
%_libdir/libkslox.so.*
%_libdir/libqgpgme.so.*

%_libdir/libkschema.so.*
%_libdir/libkschemawidgets.so.*
%_libdir/libkxmlcommon.so.*
%_libdir/libmailtransport.so.*
%_libdir/libschema.so.*
%_libdir/libwscl.so.*
%_libdir/libwsdl.so.*

%_libdir/libakonadi.so.*
%_libdir/libgpgme++.so.*
%_libdir/libkdepim.so.*
%_libdir/libkleopatra.so.*
%_libdir/libkpgp.so.*
%_libdir/libkpimidentities.so.*
%_libdir/libksieve.so.*
%_libdir/libmimelib.so.*
%_libdir/libqgpgme.so.*
%_libdir/libakonadicomponents.so.*
%_libdir/libakonadiresources.so.*
%_libdir/libakonadisearchprovider.so.*
%_libdir/kde4/kpartsdesignerplugin.so


#----------------------------------------------------------------------

%package kmail
Group:      Graphical desktop/KDE
Summary:    KDE Mailer
Requires:   %name-common >= %epoch:%version-%release
Provides:   kmail4
Requires:   indexhtml >= 10.0-6mdk
#Requires:  pinentry-qt

%description -n %name-kmail
KDE Mailer

%post kmail -p /sbin/ldconfig


%postun kmail -p /sbin/ldconfig


%files kmail
%defattr(-,root,root,-)
%_bindir/kmail            
%_bindir/kmailcvt         
%_bindir/kontact-kmail.sh
%_bindir/kmail_antivir.sh
%_bindir/kmail_clamav.sh
%_bindir/kmail_fprot.sh
%_bindir/kmail_sav.sh
%_libdir/kde4/kcm_kmail.*
%_libdir/kde4/kcm_kmailsummary.*
%_libdir/libkmailprivate.so.*
%_libdir/kde4/libkmailpart.*
%_libdir/kde4/libkmail_*
%_datadir/kde4/services/kcmkmailsummary.desktop
%_datadir/kde4/services/kmail_*
%_datadir/config.kcfg/kmail.kcfg
%_datadir/apps/kconf_update/kmail*
%_datadir/applications/kde4/KMail.desktop
%_iconsdir/*/*/*/gpg*
%_iconsdir/*/*/*/kmail*
%dir %_datadir/apps/kmail
%_datadir/apps/kmail/*
%_datadir/config/kmail.antivirusrc
%_datadir/applications/kde4/kmail_view.desktop
%_datadir/config/kmail.antispamrc
%_datadir/apps/kconf_update/upgrade-signature.pl
%_datadir/apps/kconf_update/upgrade-transport.pl
%dir %_datadir/apps/kmailcvt/
%_datadir/apps/kmailcvt/*
%_datadir/kde4/servicetypes/dbusmail.desktop

%dir %_docdir/HTML/en/kmail/
%doc %_docdir/HTML/en/kmail/*.bz2
%doc %_docdir/HTML/en/kmail/*.docbook

%_datadir/config.kcfg/customtemplates_kfg.kcfg
%_datadir/config.kcfg/templatesconfiguration_kfg.kcfg
#----------------------------------------------------------------------

%package knode
Group:      Graphical desktop/KDE
Summary:    KDE News Reader
Requires:   %name-common = %epoch:%version-%release
Provides:   knode4
Requires:	%lib_name-knode = %epoch:%version-%release

%description knode
KDE News Reader.

%files knode
%defattr(-,root,root,-)
%_bindir/knode            
%_bindir/kontact-knode.sh
%_libdir/kde4/libknodepart.*
%_datadir/kde4/services/knewsservice.protocol
%_datadir/applications/kde4/KNode.desktop
%_iconsdir/*/*/*/knode*
%dir %_datadir/apps/knode
%_datadir/apps/knode/*
%_datadir/kde4/services/knode_*
%_libdir/kde4/kcm_knode.*
%dir %_docdir/HTML/en/knode/
%doc %_docdir/HTML/en/knode/*.png
%doc %_docdir/HTML/en/knode/*.bz2
%doc %_docdir/HTML/en/knode/*.docbook

%package -n %lib_name-knode
Summary:    Library for Knode program
Group:      Development/KDE and Qt

%description -n %lib_name-knode
Library for Knode.

%post -n %lib_name-knode -p /sbin/ldconfig
%postun -n %lib_name-knode -p /sbin/ldconfig

%files -n %lib_name-knode
%defattr(-,root,root,-)
%_libdir/libknodecommon.so.*


%package -n %lib_name-knode-devel
Group:      Development/KDE and Qt
Summary:    Devel files for knode
Requires:   %lib_name-knode = %epoch:%version-%release

%description -n %lib_name-knode-devel
Devel files for knode

%files -n %lib_name-knode-devel
%defattr(-,root,root,-)
%_libdir/libknodecommon.so


#----------------------------------------------------------------------

%package -n %lib_name-kmail-devel
Group:      Development/KDE and Qt
Summary:    Devel files for kmail

%description -n %lib_name-kmail-devel
Devel files for kmail

%files -n %lib_name-kmail-devel
%defattr(-,root,root,-)
%dir %_includedir/gpgme++/
%_includedir/gpgme++/*.h
%dir %_includedir/gpgme++/interfaces/
%_includedir/gpgme++/interfaces/*.h
%dir %_includedir/kleo/
%_includedir/kleo/*.h
%dir %_includedir/kmail/interfaces/
%_includedir/kmail/interfaces/*.h
%_libdir/libkmailprivate.so

#----------------------------------------------------------------------

%package karm
Summary:	Karm program
Group:		Graphical desktop/KDE
Provides:	karm4

%description karm
Time tracker.

#%post karm 


#%postun karm 


%files karm
%defattr(-,root,root)
%_bindir/karm
%_datadir/kde4/services/karm_part.desktop
%_iconsdir/*/*/*/karm*
%_libdir/kde4/libkarmpart.*
%dir %_datadir/apps/karm/
%_datadir/apps/karm/*
%_datadir/applications/kde4/karm.desktop
%dir %_datadir/apps/karmpart
%_datadir/apps/karmpart/*

#----------------------------------------------------------------------

%package ktnef
Summary:    Ktnef program
Group:      Graphical desktop/KDE
Provides:   ktnef4
Requires:   %lib_name-ktnef = %epoch:%version-%release

%description ktnef
Ktnef.


%files ktnef
%defattr(-,root,root,-)
%_bindir/ktnef
%dir %_datadir/apps/ktnef/
%_datadir/apps/ktnef/*
%_iconsdir/*/*/*/ktnef*
%_datadir/applications/kde4/ktnef.desktop

#----------------------------------------------------------------------

%package -n %lib_name-ktnef
Summary:    Library for Ktnef program
Group:      Development/KDE and Qt 

%description -n %lib_name-ktnef
Library for Ktnef.

%post -n %lib_name-ktnef -p /sbin/ldconfig
%postun -n %lib_name-ktnef -p /sbin/ldconfig

%files -n %lib_name-ktnef
%defattr(-,root,root,-)

#----------------------------------------------------------------------

%package -n %lib_name-ktnef-devel
Summary:    Devel files for Ktnef program
Group:      Development/KDE and Qt
Requires:   %lib_name-ktnef = %epoch:%version-%release

%description -n %lib_name-ktnef-devel
Devel files for Ktnef.

%files -n %lib_name-ktnef-devel
%defattr(-,root,root,-)

#----------------------------------------------------------------------

%package knotes
Group:		Graphical desktop/KDE
Summary:	A color configurable tooltip notes application for desktop
Provides:	knotes4

%description knotes
A color configurable tooltip notes application for desktop

%files knotes
%defattr(-,root,root)
%_bindir/knotes
%_bindir/kontact-knotes.sh
%dir %_datadir/apps/knotes/
%_datadir/apps/knotes/*
%_libdir/kde4/knotes_*
%_iconsdir/*/*/*/knotes*
%_datadir/applications/kde4/knotes.desktop
%_datadir/config.kcfg/knotesglobalconfig.kcfg
%_datadir/kde4/services/kresources/knotes_manager.desktop
%dir %_docdir/HTML/en/knotes/
%doc %_docdir/HTML/en/knotes/*.bz2
%doc %_docdir/HTML/en/knotes/*.docbook
#----------------------------------------------------------------------

%package kaddressbook
Summary:	Kaddressbook program
Group:		Graphical desktop/KDE
Provides:	kaddressbook4

%description kaddressbook
The KDE addressbook application.

%files kaddressbook
%defattr(-,root,root)
%_bindir/kaddressbook
%_bindir/kabc2mutt
%dir %_datadir/apps/kaddressbook
%_datadir/apps/kaddressbook/*
%_iconsdir/*/*/*/kaddressbook*
%_bindir/kontact-addressbook.sh
%_datadir/applications/kde4/kaddressbook.desktop
%_libdir/kde4/kabc_*
%_libdir/kde4/libkaddressbookpart.*
%_libdir/kde4/kcm_kabconfig.*
%_libdir/kde4/kcm_kabldapconfig.*
%_libdir/kde4/libkaddrbk_*.*
%_libdir/kde4/ldifvcardthumbnail.*
%_libdir/kde4/kcm_kabcustomfields.*
%dir %_datadir/kde4/services/kaddressbook/
%_datadir/kde4/services/kaddressbook/*
%_datadir/kde4/services/kabconfig.desktop
%_datadir/kde4/services/kabldapconfig.desktop
%_datadir/kde4/services/ldifvcardthumbnail.desktop
%_datadir/kde4/servicetypes/dbusaddressbook.desktop
%_datadir/kde4/servicetypes/kaddressbook_*
%_datadir/kde4/services/kabcustomfields.desktop
%dir %_datadir/kde4/services/kresources/kabc/
%_datadir/kde4/services/kresources/kabc/*
%dir %_docdir/HTML/en/kaddressbook/
%doc %_docdir/HTML/en/kaddressbook/*.png
%doc %_docdir/HTML/en/kaddressbook/*.bz2
%doc %_docdir/HTML/en/kaddressbook/*.docbook
#----------------------------------------------------------------------

%package -n %lib_name-kaddressbook-devel
Summary:	Devel file for Kaddressbook
Group:		Development/KDE and Qt
Requires:	%lib_name-kaddressbook = %epoch:%version-%release
Provides:	libkdepim4-kaddressbook-devel = %epoch:%version-%release

%description  -n %lib_name-kaddressbook-devel
Devel file for kaddressbook

%files -n %lib_name-kaddressbook-devel
%defattr(-,root,root)
%dir %_includedir/kaddressbook/
%_includedir/kaddressbook/*.h
%_libdir/libkaddressbook.so
%_libdir/libkabinterfaces.so
%_libdir/libkabc*.so

#----------------------------------------------------------------------

%package -n %lib_name-kaddressbook
Summary:    Library file for Kaddressbook
Group:      Development/KDE and Qt
Provides:   %lib_name_orig-kaddressbook = %epoch:%version-%release

%description  -n %lib_name-kaddressbook
Library file for kaddressbook

%post -n %lib_name-kaddressbook -p /sbin/ldconfig
%postun -n %lib_name-kaddressbook -p /sbin/ldconfig

%files -n %lib_name-kaddressbook
%defattr(-,root,root)
%_libdir/libkaddressbook.so.*
%_libdir/libkabinterfaces.so.*
%_libdir/libkabc*.so.*

#----------------------------------------------------------------------

%package korganizer
Summary:	Korganizer program
Group:		Graphical desktop/KDE
Provides:	korganizer4, kalarm4, kalarmd4
Requires:	%lib_name-korganizer = %epoch:%version-%release
Requires:       %lib_name-common = %epoch:%version-%release
Requires:	%name-common = %epoch:%version-%release

%description korganizer
A calendar-of-events and todo-list manager.

#%post korganizer 


#%postun korganizer


%files korganizer
%defattr(-,root,root)

%config(noreplace) %_datadir/config/korganizer.knsrc

%_bindir/kalarm
%_bindir/kalarmd
%_bindir/konsolekalendar
%_bindir/korgac
%_bindir/korganizer
%_bindir/kontact-korganizer.sh
%_bindir/ical2vcal
%_datadir/apps/kconf_update/korganizer.upd
%dir %_datadir/apps/korganizer
%_datadir/apps/korganizer/*
%dir %_datadir/apps/kalarm/
%_datadir/apps/kalarm/*
%dir %_datadir/apps/libkholidays/
%_datadir/applications/kde4/kalarmd.desktop
%_datadir/applications/kde4/korganizer-import.desktop
%_datadir/apps/libkholidays/*
%_datadir/autostart/kalarm.tray.desktop
%_datadir/autostart/kalarmd.autostart.desktop
%_datadir/autostart/korgac.desktop
%_libdir/kde4/libkorg_*
%_libdir/kde4/kcm_korganizer.*
%_libdir/kde4/libkorganizerpart.*
%_datadir/applications/kde4/kalarm.desktop
%_datadir/applications/kde4/korganizer.desktop
%_iconsdir/*/*/*/kalarm*
%_datadir/config.kcfg/korganizer.kcfg
%_datadir/kde4/services/korganizer_*
%dir %_datadir/kde4/services/korganizer/
%_datadir/kde4/services/korganizer/*
%dir %_datadir/kde4/services/webcal.protocol
%_datadir/kde4/servicetypes/calendardecoration.desktop
%_datadir/kde4/servicetypes/calendarplugin.desktop
%_datadir/kde4/servicetypes/korganizerpart.desktop

%_datadir/config.kcfg/kalarmconfig.kcfg

%_datadir/apps/kconf_update/kalarm-1.2.1-general.pl
%_datadir/apps/kconf_update/kalarm-1.9.5-defaults.pl
%_datadir/apps/kconf_update/kalarm-version.pl
%_datadir/apps/kconf_update/kalarm.upd

%dir %_docdir/HTML/en/kalarm/
%doc %_docdir/HTML/en/kalarm/*.png
%doc %_docdir/HTML/en/kalarm/*.bz2
%doc %_docdir/HTML/en/kalarm/*.docbook

#----------------------------------------------------------------------

%package -n %lib_name-korganizer
Summary:    Librairy for korganizer program
Group:      Development/KDE and Qt
Provides:   %lib_name_orig-korganizer = %epoch:%version-%release

%description -n %lib_name-korganizer
Librairy for korganizer program

%post -n %lib_name-korganizer -p /sbin/ldconfig
%postun -n %lib_name-korganizer -p /sbin/ldconfig


%files -n %lib_name-korganizer
%defattr(-,root,root)
%_libdir/libkorganizer.so.*
%_libdir/libkorganizer_eventviewer.so.*
%_libdir/libkorg_stdprinting.so.*
%_libdir/kde4/kalarm_local.so
%_libdir/kde4/kalarm_localdir.so
%_libdir/kde4/kalarm_remote.so
%_libdir/kde4/kcm_apptsummary.so
%_libdir/kde4/kcm_todosummary.so
%_libdir/libkalarm_resources.so.*
%_libdir/libkholidays_ng.so.*
%_libdir/libkorganizer_interfaces.so.*


#----------------------------------------------------------------------

%package -n %lib_name-korganizer-devel
Summary:    Devel files for korganizer program
Group:      Development/KDE and Qt
Requires:   %lib_name-korganizer = %epoch:%version-%release
Provides:   libkdepim4-korganizer-devel = %epoch:%version-%release

%description -n %lib_name-korganizer-devel
Devel files for korganizer program

%files -n %lib_name-korganizer-devel
%defattr(-,root,root)
%_libdir/libkorganizer.so
%_libdir/libkorganizer_eventviewer.so
%_libdir/libkorg_stdprinting.so
%dir %_includedir/calendar/
%_includedir/calendar/*.h
%dir %_includedir/korganizer/
%_includedir/korganizer/*.h

%dir %_includedir/kabc/
%_includedir/kabc/kabc_resourcexmlrpc.h
%_includedir/kabc/kcal_resourcexmlrpc.h

%_libdir/libkalarm_resources.so
%_libdir/libkholidays_ng.so
%_libdir/libkorganizer_interfaces.so
%dir %_includedir/libkholiday_ng/
%_includedir/libkholiday_ng/*.h
#----------------------------------------------------------------------

%package kpilot
Summary:	Kpilot program
Group:		Graphical desktop/KDE
Requires:	%lib_name-kpilot = %epoch:%version-%release
Provides:	kpilot4, kpilotDaemon4
Requires:       %lib_name-common = %epoch:%version-%release

%description kpilot
To sync with your PalmPilot
Sync phone book entries between your palmtop and computer

#%post kpilot 

#update-alternatives --install %_sysconfdir/dynamic/launchers/visor/kde.desktop visor.kde.dynamic %_sysconfdir/dynamic/launchers/visor/kpilot.desktop 30

#%postun kpilot

#if [ $1 = 0 ] ; then
#	update-alternatives --remove visor.kde.dynamic %_sysconfdir/dynamic/launchers/visor/kpilot.desktop
#fi

%files kpilot
%defattr(-,root,root)
#%dir %_sysconfdir/dynamic/
#%dir %_sysconfdir/dynamic/launchers/
#%dir %_sysconfdir/dynamic/launchers/visor/
#%config(noreplace) %_sysconfdir/dynamic/launchers/visor/kpilot.desktop
#/etc/dynamic/launchers/visor/kpilot.desktop
%_iconsdir/crystalsvg/128x128/apps/mobile_phone.png
%_iconsdir/crystalsvg/16x16/actions/hotsync.png
%_iconsdir/crystalsvg/16x16/actions/playsound.png
%_iconsdir/crystalsvg/16x16/apps/mobile_phone.png
%_iconsdir/crystalsvg/22x22/actions/hotsync.png
%_iconsdir/crystalsvg/32x32/actions/hotsync.png
%_iconsdir/crystalsvg/32x32/apps/mobile_phone.png
%_iconsdir/crystalsvg/48x48/actions/hotsync.png
%_iconsdir/crystalsvg/48x48/apps/mobile_phone.png
%_iconsdir/crystalsvg/64x64/apps/mobile_phone.png
%_iconsdir/hicolor/16x16/apps/kitchensync.png
%_iconsdir/hicolor/22x22/apps/kitchensync.png
%_iconsdir/hicolor/32x32/apps/kitchensync.png
%_iconsdir/hicolor/48x48/apps/kitchensync.png

%_datadir/apps/kitchensync/about/kitchensync.css
%_datadir/apps/kitchensync/about/main.html
%_datadir/apps/kitchensync/about/top-right-kitchensync.png
%_datadir/apps/kitchensync/kitchensync_part.rc
%_datadir/apps/kitchensync/kitchensyncui.rc

%_datadir/applications/kde4/kitchensync.desktop

#----------------------------------------------------------------------

%package -n %lib_name-kpilot
Summary:    Librairy for kpilot program
Group:      Development/KDE and Qt
Provides:   %lib_name_orig-kpilot = %epoch:%version-%release
Requires:   %lib_name-common = %epoch:%version-%release

%description -n %lib_name-kpilot
Librairy for kpilot program

%files -n %lib_name-kpilot
%defattr(-,root,root)

%_bindir/kitchensync

%_libdir/kde4/ktexteditorkabcbridge.so
%_libdir/kde4/libkitchensyncpart.so
%_libdir/libkitchensyncprivate.so.*
%_libdir/libqopensync.so.*

#----------------------------------------------------------------------

%package -n %lib_name-kpilot-devel
Summary:    Devel files for kpilot program
Group:      Development/KDE and Qt
Requires:   %lib_name-kpilot = %epoch:%version-%release
Provides:   libkdepim-kpilot-devel = %epoch:%version-%release

%description -n %lib_name-kpilot-devel
Devel files for kpilot program

%files -n %lib_name-kpilot-devel
%defattr(-,root,root)
%_libdir/libqopensync.so
%_libdir/libkitchensyncprivate.so

#----------------------------------------------------------------------


%package kontact
Summary:	Kontact program
Group:		Graphical desktop/KDE
Provides:	kontact4
Requires:       %name-kmail = %epoch:%version-%release
Requires:       %name-knotes = %epoch:%version-%release
Requires:       %name-kaddressbook = %epoch:%version-%release
Requires:       %name-knode = %epoch:%version-%release
Requires:       %name-korganizer = %epoch:%version-%release
Requires:	kdetoys4-kweather
Requires:	%name-akregator = %epoch:%version-%release

%description kontact
KDE Kontact, an integrated personal information suite container application for KDE.

%post kontact -p /sbin/ldconfig


%postun kontact -p /sbin/ldconfig


%files kontact
%defattr(-,root,root)
%_bindir/kontact
%dir %_datadir/kde4/services/kontact/
%_datadir/kde4/services/kontact/*
%_datadir/kde4/services/kontactconfig.desktop
%_datadir/applications/kde4/Kontact.desktop
%dir %_datadir/apps/kontact/
%_datadir/apps/kontact/*
%dir %_datadir/apps/kontactsummary/
%_datadir/apps/kontactsummary/*
%_libdir/kde4/libkontact*
%_libdir/kde4/kcm_kontact*
%_datadir/config.kcfg/kontact.kcfg
%_datadir/kde4/servicetypes/kontactplugin.desktop
%_iconsdir/*/*/*/kontact*
%dir %_docdir/HTML/en/kontact/
%doc %_docdir/HTML/en/kontact/*.png
%doc %_docdir/HTML/en/kontact/*.bz2
%doc %_docdir/HTML/en/kontact/*.docbook
#----------------------------------------------------------------------

%package -n %lib_name-kontact
Summary:    Librairy for kontact program
Group:      Development/KDE and Qt
Provides:   %lib_name_orig-kontact = %epoch:%version-%release

%description -n %lib_name-kontact
Librairy for kontact program

%files -n %lib_name-kontact
%defattr(-,root,root)
%_libdir/libkontact.so.*
%_libdir/libkpinterfaces.so.*

#----------------------------------------------------------------------

%package -n %lib_name-kontact-devel
Summary:    Devel files for kontact program
Group:      Development/KDE and Qt
Requires:   %lib_name-kontact = %epoch:%version-%release
Provides:   libkdepim4-kontact-devel = %epoch:%version-%release

%description -n %lib_name-kontact-devel
Devel files for kontact program

%files -n %lib_name-kontact-devel
%defattr(-,root,root)
%dir %_includedir/kontact/
%_includedir/kontact/*.h
%_libdir/libkontact.so
%_libdir/libkpinterfaces.so

#----------------------------------------------------------------------

%prep

%setup -q -nkdepim-%version-%branch_date
#%patch85 -p1 -b .fix_first_mail
#%patch86 -p1 -b .fix_kmail_info_column
#%patch111 -p1 -b .fix_kmail_dont_empty_trash
#%patch113 -p1 -b .fix_dimap_speed
#%patch200 -p1 -b .fix_use_point_kmail
#%patch203 -p1 -b .disable_knode_first_start
#%patch204 -p1 -b .fix_akregator_bug_15569
#%patch205 -p1 -b .fix_config_empty_trash
#%patch207 -p1 -b .fix_add_resource_to_kaddressbook
#%patch208 -p1 -b .fix_kalarm_call_twice_dialog
#%patch209 -p1 -b .korganizer_dont_spam_example_net
#%patch210 -p1 -b .korganizer_use_sys_timezone
#%patch211 -p1 -b .kontact_sidebar_dont_show_text
#%patch212 -p1 -b .fix_launch_korganizer
#%patch213 -p1 -b .fix_korganizer_mem_leak

%build
cd $RPM_BUILD_DIR/kdepim-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make



%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdepim-%version-%branch_date
cd build

make DESTDIR=%buildroot install

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/korganizer.desktop "Office/Time Management" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kalarm.deskto "Office/Time Management" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kaddressbook.desktop "Office/Address Books" 
#perl -pi -e "s|command=\"kaddressbook\"|command=\"kontact-addressbook.sh\"|" %buildroot/%_menudir/kdepim-kaddressbook
#perl -pi -e "s|kde_command=\"kaddressbook %u\"|kde_command=\"kontact-addressbook.sh %u\"|" %buildroot/%_menudir/kdepim-kaddressbook

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpilot.desktop "Office/Communications/PDA"
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpilotdaemon.desktop "Office/Communications/PDA" kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/karm.desktop "Office/Time Management" kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/knotes.desktop "Office/Accessories"  kde
#perl -pi -e "s|command=\"knotes\"|command=\"kontact-knotes.sh\"|" %buildroot/%_menudir/kdepim-knotes


mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KMail.desktop KMail.desktop 
#perl -pi -e "s|command=\"kmail\"|command=\"kontact-kmail.sh\"|" %buildroot/%_menudir/kdepim-kmail
#perl -pi -e 's|kde_command="kmail -caption.*kde_opt|kde_command="kontact-kmail.sh" kde_opt|' %buildroot/%_menudir/kdepim-kmail
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kmail_view.desktop Internet/Mail 
#perl -pi -e 's|title="KMail"|title="KMail View"|' %buildroot/%_menudir/kdepim-kmailview

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KNode.desktop Internet/News 
#perl -pi -e "s|command=\"knode\"|command=\"kontact-knode.sh\"|" %buildroot/%_menudir/kdepim-knode
#perl -pi -e 's|kde_command=\"knode -caption.*kde_opt|kde_command="kontact-knode.sh -caption \\"%c\\" %i %m" kde_opt|' %buildroot/%_menudir/kdepim-knode

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ktnef.desktop Internet/Mail kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpalmdoc.desktop "Office/Communications/PDA" kde
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KOrn.desktop Internet/Mail 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/Kontact.desktop Internet/Mail 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kleopatra_import.desktop Internet/Mail 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/groupwarewizard.desktop Internet/Mail 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/akregator.desktop Internet/News 
#perl -pi -e "s|command=\"akregator\"|command=\"kontact-akregator.sh\"|" %buildroot/%_menudir/kdepim-akregator
#perl -pi -e 's|kde_command=\"akregator.*kde_opt|kde_command="kontact-akregator.sh -caption \\"%c\\" %i %m" kde_opt|' %buildroot/%_menudir/kdepim-akregator


#perl -pi -e "s|kontact.png|kontact-mdk.png|" %buildroot/%_menudir/kdepim-kontact

#perl -pi -e "s|X-KDE-PluginInfo-Name=.*|X-KDE-PluginInfo-Name=knode\nX-KDE-KontactPartLoadOnStart=true|" %buildroot/%_datadir/services/kontact/knodeplugin.desktop
#perl -pi -e "s|X-KDE-PluginInfo-EnabledByDefault=.*|X-KDE-PluginInfo-EnabledByDefault=true|" %buildroot/%_datadir/services/kontact/knodeplugin.desktop

#%define launchers /etc/dynamic/launchers/visor
#mkdir -p $RPM_BUILD_ROOT%launchers
#cat > $RPM_BUILD_ROOT%launchers/kpilot.desktop << EOF
#[Desktop Entry]
#Name=Kpilot \$devicename
#Comment=PalmPilot Tool
#Exec=%_bindir/kpilot
#Terminal=false
#Icon=kpilot.png
#Type=Application
#EOF

install -m 0755 %SOURCE1 %buildroot/%_bindir/kontact-addressbook.sh
install -m 0755 %SOURCE2 %buildroot/%_bindir/kontact-knotes.sh
install -m 0755 %SOURCE3 %buildroot/%_bindir/kontact-kmail.sh
install -m 0755 %SOURCE4 %buildroot/%_bindir/kontact-korganizer.sh
install -m 0755 %SOURCE5 %buildroot/%_bindir/kontact-knode.sh
install -m 0755 %SOURCE6 %buildroot/%_bindir/kontact-akregator.sh

install -d -m 0755 %buildroot/%_sysconfdir/xdg/menus/

install -d -m 0755 %buildroot/%_libdir/rpm/
install -d -m 0755 %buildroot/%_libdir/rpm/mkmultiarch



%clean
rm -fr %buildroot



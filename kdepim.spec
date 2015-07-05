Summary:	An application suite to manage personal information
Name:		kdepim
Epoch:		3
Version:	4.14.10
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kdepim-4.12.1-cmake-libkaddressbookgrantlee.patch
Patch1:		kdepim-4.14.1-storageservicemanager-desktop.patch
BuildRequires:	xsltproc
BuildRequires:	baloo-devel
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	grantlee-devel >= 0.4.0
BuildRequires:	kdelibs-devel >= 4.14.8
BuildRequires:	kdepimlibs-devel >= 4.14.8
BuildRequires:	kdepim-runtime-devel >= 4.14.8
BuildRequires:	libassuan-devel
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libkgapi) >= 2.2.0
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(Prison)
Suggests:	akonadi-common
Suggests:	kleopatra
Suggests:	akregator
Suggests:	knode
Suggests:	kaddressbook
Suggests:	kalarm
Suggests:	ktimetracker
Suggests:	kmail
Suggests:	kmailcvt
Suggests:	knotes
Suggests:	kontact
Suggests:	korganizer
Suggests:	ksendemail
Suggests:	kjots
%rename		kdepim4

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer
	  and kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- ktimetracker: Time tracker.
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client
	- kmailcvt: converst addressbooks to kmail format

%files

#----------------------------------------------------------------------

%package core
Summary:	Core files for KDE PIM
Group:		Graphical desktop/KDE
Requires:	akonadi-kde >= 3:%{version}
Requires:	kde-runtime
Requires:	kdelibs-core
Requires:	storageservicemanager = %{EVRD}
Conflicts:	%{_lib}kdepim4 < 3:4.11.0
Conflicts:	%{_lib}kpgp4 < 3:4.11.0
Conflicts:	%{name}-devel < 3:4.11.0
Obsoletes:	akonadi-folderarchive-agent < 3:4.13.0
Obsoletes:	pimactivity < 3:4.13.0
%rename	kdepim4-core
Provides:	kdepim4-core = 3:4.14.3-1

%description core
Core files for KDE PIM.

%files core -f %{name}.lang
%exclude %{_kde_docdir}/HTML/en/*
%dir %{_kde_services}/kontact
%{_kde_iconsdir}/oxygen/*/mimetypes/x-mail-distribution-list.*
%{_kde_appsdir}/kdepimwidgets
%{_kde_plugindir}/designer/kdepimwidgets.so
%{_kde_plugindir}/designer/mailcommonwidgets.so
%{_kde_plugindir}/designer/pimcommonwidgets.so
%{_kde_appsdir}/kconf_update/kpgp-3.1-upgrade-address-data.pl
%{_kde_appsdir}/kconf_update/kpgp.upd
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml

#-----------------------------------------------------------------------------

%package -n akonadiconsole
Summary:	Console that help to debug akonadi
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Conflicts:	kdepim4-core < 2:4.4.2-5

%description -n akonadiconsole
Console that help to debug akonadi.

%files -n akonadiconsole
%{_kde_bindir}/akonadiconsole
%{_kde_applicationsdir}/akonadiconsole.desktop
%{_kde_appsdir}/akonadiconsole/akonadiconsoleui.rc
%{_kde_iconsdir}/hicolor/*/apps/akonadiconsole.png

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent
%doc %{_kde_docdir}/HTML/en/akonadi_archivemail_agent
%{_kde_bindir}/akonadi_archivemail_agent
%{_kde_datadir}/akonadi/agents/archivemailagent.desktop
%{_kde_appsdir}/akonadi_archivemail_agent/

#-----------------------------------------------------------------------------

%package -n akonadi-followupreminder-agent
Summary:	Akonadi followupreminder agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-followupreminder-agent
Akonadi followup reminder agent allows to remind you when an email was not
answered.

%files -n akonadi-followupreminder-agent
%doc %{_kde_docdir}/HTML/en/akonadi_followupreminder_agent
%{_kde_bindir}/akonadi_followupreminder_agent
%{_kde_datadir}/akonadi/agents/followupreminder.desktop
%{_kde_appsdir}/akonadi_followupreminder_agent/

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent
%{_kde_bindir}/akonadi_mailfilter_agent
%{_kde_datadir}/akonadi/agents/mailfilteragent.desktop
%{_kde_appsdir}/akonadi_mailfilter_agent/
%{_kde_appsdir}/kconf_update/mailfilteragent.upd
%{_kde_appsdir}/kconf_update/migrate-kmail-filters.pl

#-----------------------------------------------------------------------------

%package -n akonadi-notes-agent
Summary:	Akonadi notes agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	knotes = %{EVRD}

%description -n akonadi-notes-agent
Akonadi notes agent. It adds notes received via network and handles note
alarm notifications.

%files -n akonadi-notes-agent
%doc %{_kde_docdir}/HTML/en/akonadi_notes_agent
%{_kde_bindir}/akonadi_notes_agent
%{_kde_datadir}/akonadi/agents/notesagent.desktop
%{_kde_appsdir}/akonadi_notes_agent/
%{_kde_appsdir}/kconf_update/noteglobalsettings.upd

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent
%doc %{_kde_docdir}/HTML/en/akonadi_sendlater_agent
%{_kde_bindir}/akonadi_sendlater_agent
%{_kde_datadir}/akonadi/agents/sendlateragent.desktop
%{_kde_appsdir}/akonadi_sendlater_agent/

#-----------------------------------------------------------------------------

%package -n akregator
Summary:	A Feed Reader for KDE
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Akregator
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-akregator = %{EVRD}
Conflicts:	%{name}-core < 2:4.5.77
Conflicts:	%{name}-devel < 3:4.11.0

%description -n akregator
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%files -n akregator
%doc %{_kde_docdir}/HTML/en/akregator
%{_kde_bindir}/akregator
%{_kde_bindir}/akregatorstorageexporter
%{_kde_applicationsdir}/akregator.desktop
%{_kde_appsdir}/akregator
%{_kde_appsdir}/akregator_sharemicroblog_plugin
%{_kde_datadir}/config.kcfg/akregator.kcfg
%{_kde_iconsdir}/*/*/apps/akregator.*
%{_kde_iconsdir}/*/*/apps/akregator_empty.*
%{_kde_services}/kontact/akregatorplugin.desktop
%{_kde_services}/akregator_*
%{_kde_services}/feed.protocol
%{_kde_servicetypes}/akregator_plugin.desktop
%{_kde_libdir}/kde4/akregator*
%{_kde_libdir}/kde4/kontact_akregatorplugin.so
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml

#-----------------------------------------------------------------------------

%package -n blogilo
Summary:	Blogging client for kde
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n blogilo
Blogilo is a blogging client for KDE, which supports famous blogging
APIs.

It was known as Bilbo blogger before, But because of a trademark
issue, We (Blogilo developers) decided to choose a new name for it.
More information about the decision can be found at
http://blogilo.gnufolks.org/news/.

Its current features:

* A full featured WYSIWYG editor.
* An HTML editor with syntax highlighting.
* Previewing your post with your blog style! like when you are
visiting it at your blog.
* Support for Blogger1.0, MetaWeblog, MovableType (Wordpress supports
All of these!) and Google GData (used on Blogspot.com blogs) APIs!
* Support for Creating/Modifying/Deleting posts.
* Support for creating drafts and scheduled posts!
* Support for uploading media files to your blog (Just on supported
APIs e.g. MetaWeblog and MovableType)
* Support for uploading to FTP server.
* Support for Fetching your recent blog entries.
* Support for adding Images to post from your system. It will upload
them on Submitting post to blog (Just on supported APIs e.g.
MetaWeblog and MovableType)
* Support for saving local entries before publishing.
* Saving your writing copy to prevent data loss, at configurable
intervals.
* and ...

%files -n blogilo
%doc %{_kde_docdir}/HTML/en/blogilo
%{_kde_bindir}/blogilo
%{_kde_appsdir}/blogilo
%{_kde_applicationsdir}/blogilo.desktop
%{_kde_datadir}/config.kcfg/blogilo.kcfg
%{_kde_iconsdir}/*/*/apps/blogilo.*
%{_kde_iconsdir}/*/*/actions/format-text-blockquote.*
%{_kde_iconsdir}/*/*/actions/format-text-code.*
%{_kde_iconsdir}/*/*/actions/insert-more-mark.*
%{_kde_iconsdir}/*/*/actions/remove-link.*
%{_kde_iconsdir}/*/*/actions/upload-media.*

#-----------------------------------------------------------------------------

%package -n headerthemeeditor
Summary:	KMail Header Theme Editor
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n headerthemeeditor
KMail Header Theme Editor.

%files -n headerthemeeditor
%doc %{_kde_docdir}/HTML/en/headerthemeeditor
%{_kde_bindir}/headerthemeeditor
%{_kde_appsdir}/headerthemeeditor
%{_kde_applicationsdir}/headerthemeeditor.desktop

#-----------------------------------------------------------------------------

%package -n contactthemeeditor
Summary:	KDE Contact Theme Editor
Group:		Graphical desktop/KDE
Requires:	kaddressbook

%description -n contactthemeeditor
KDE Contact Theme Editor.

%files -n contactthemeeditor
%doc %{_kde_docdir}/HTML/en/contactthemeeditor
%{_kde_bindir}/contactthemeeditor
%{_kde_appsdir}/contactthemeeditor
%{_kde_appsdir}/kconf_update/grantleetheme.upd
%{_kde_applicationsdir}/contactthemeeditor.desktop

#-----------------------------------------------------------------------------

%package -n importwizard
Summary:	Import Wizard allows to migrate data from mailer as thunderbird/evolution etc
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n importwizard
Import Wizard allows to migrate data from mailer as thunderbird/evolution etc.

%files -n importwizard
%doc %{_kde_docdir}/HTML/en/importwizard
%{_kde_bindir}/importwizard
%{_kde_applicationsdir}/importwizard.desktop
%{_kde_iconsdir}/*/*/apps/kontact-import-wizard.*

#-----------------------------------------------------------------------------

%package -n kaddressbook
Summary:	The KDE addressbook application
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAddressBook
Requires:	%{name}-core = %{EVRD}
# Grantlee is needed for the simple view in kaddressbook
Requires:	grantlee
Requires:	akonadi-common
Suggests:	contactthemeeditor = %{EVRD}
Provides:	kde4-kaddressbook = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kaddressbook
The KDE addressbook application.

%files -n kaddressbook
%doc %{_kde_docdir}/HTML/en/kabcclient
%{_kde_bindir}/kaddressbook
%{_kde_bindir}/kabc2mutt
%{_kde_bindir}/kabcclient
%{_kde_applicationsdir}/kaddressbook.desktop
%{_kde_applicationsdir}/kaddressbook-importer.desktop
%{_kde_appsdir}/kaddressbook
%{_kde_configdir}/kaddressbook_themes.knsrc
%{_kde_libdir}/kde4/kcm_ldap.so
%{_kde_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_kde_libdir}/kde4/kaddressbookpart.so
%{_kde_libdir}/kde4/kontact_kaddressbookplugin.so
%{_kde_iconsdir}/*/*/apps/kaddressbook.*
%{_kde_services}/kaddressbookpart.desktop
%{_kde_services}/kontact/kaddressbookplugin.desktop
%{_kde_services}/kcmldap.desktop
%{_kde_mandir}/man1/kabcclient.1.*
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml

#-----------------------------------------------------------------------------

%package -n kalarm
Summary:	A personal alarm message, command and email scheduler
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KAlarm
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kalarm = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kalarm
KAlarm is a personal alarm message, command and email scheduler. It lets you
set up personal alarm messages which pop up on the screen at the chosen time,
or you can schedule commands to be executed or emails to be sent.

%files -n kalarm
%doc %{_kde_docdir}/HTML/en/kalarm
%{_kde_bindir}/kalarm
%{_kde_bindir}/kalarmautostart
%{_kde_libdir}/kde4/libexec/kalarm_helper
%{_kde_applicationsdir}/kalarm.desktop
%{_kde_appsdir}/kalarm
%{_kde_appsdir}/kconf_update/kalarm-1.2.1-general.pl
%{_kde_appsdir}/kconf_update/kalarm-1.9.5-defaults.pl
%{_kde_appsdir}/kconf_update/kalarm-2.0.2-general.pl
%{_kde_appsdir}/kconf_update/kalarm-2.1.5-general.pl
%{_kde_appsdir}/kconf_update/kalarm-version.pl
%{_kde_appsdir}/kconf_update/kalarm.upd
%{_kde_autostart}/kalarm.autostart.desktop
%{_kde_datadir}/config.kcfg/kalarmconfig.kcfg
%{_kde_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_kde_iconsdir}/*/*/apps/kalarm.*
%{_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml

#---------------------------------------------------------------------------

%package -n kincidenceeditor
Summary:	kincidenceeditor
Group:		Graphical desktop/KDE

%description -n kincidenceeditor
New incidince editor.

%files -n kincidenceeditor
%{_kde_bindir}/kincidenceeditor

#-----------------------------------------------------------------------------

%package -n kjots
Summary:	KDE note taking utility
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KJots
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kjots = %{EVRD}

%description -n kjots
A small program which is handy for keeping and organizing miscellaneous
notes.

%files -n kjots
%doc %{_kde_docdir}/HTML/en/kjots
%{_kde_bindir}/kjots
%{_kde_appsdir}/desktoptheme/default/widgets/stickynote.svgz
%{_kde_appsdir}/kjots
%{_kde_applicationsdir}/Kjots.desktop
%{_kde_libdir}/kde4/kcm_kjots.so
%{_kde_libdir}/kde4/kjotspart.so
%{_kde_libdir}/kde4/kontact_kjotsplugin.so
%{_kde_libdir}/kde4/plasma_applet_akonotes_list.so
%{_kde_libdir}/kde4/plasma_applet_akonotes_note.so
%{_kde_datadir}/config.kcfg/kjots.kcfg
%{_kde_iconsdir}/*/*/apps/kjots.*
%{_kde_iconsdir}/*/*/actions/edit-delete-page.*
%{_kde_services}/akonotes_list.desktop
%{_kde_services}/akonotes_note.desktop
%{_kde_services}/kjots_config_misc.desktop
%{_kde_services}/kjotspart.desktop
%{_kde_services}/kontact/kjots_plugin.desktop

#-----------------------------------------------------------------------------

%package -n kleopatra
Summary:	KDE Certificate Manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kleopatra = %{EVRD}

%description -n kleopatra
KDE Certificate Manager.

%files -n kleopatra
%doc %{_kde_docdir}/HTML/en/kleopatra
%doc %{_kde_docdir}/HTML/en/kwatchgnupg
%{_kde_bindir}/kleopatra
%{_kde_bindir}/kgpgconf
%{_kde_bindir}/kwatchgnupg
%{_kde_applicationsdir}/kleopatra.desktop
%{_kde_applicationsdir}/kleopatra_import.desktop
%{_kde_configdir}/libkleopatrarc
%{_kde_appsdir}/kleopatra
%{_kde_appsdir}/libkleopatra
%{_kde_appsdir}/kwatchgnupg
%{_kde_iconsdir}/*/*/apps/kleopatra.*
%{_kde_services}/kleopatra_*
%{_kde_libdir}/kde4/kcm_kleopatra.so

#-----------------------------------------------------------------------------

%package -n kmail
Summary:	KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Requires:	kdepimlibs-core
Requires:	sasl-plug-plain
Requires:	sasl-plug-ntlm
Requires:	sasl-plug-login
Requires:	sasl-plug-digestmd5
Requires:	kio4-pop3
Requires:	kio4-smtp
Requires:	kio4-mbox
Requires:	kio4-imap
Requires:	kio4-sieve
Requires:	akonadi-archivemail-agent = %{EVRD}
Requires:	akonadi-followupreminder-agent = %{EVRD}
Requires:	akonadi-mailfilter-agent = %{EVRD}
Requires:	akonadi-sendlater-agent = %{EVRD}
Requires:	headerthemeeditor = %{EVRD}
Requires:	messageviewer = %{EVRD}
Suggests:	kaddressbook = %{EVRD}
Suggests:	kmailcvt = %{EVRD}
Suggests:	pinentry-qt4
Suggests:	openssh-askpass-qt4
Suggests:	pimsettingexporter
Suggests:	importwizard
Suggests:	mboximporter
Suggests:	sieveeditor
Provides:	kde4-kmail = %{EVRD}
Provides:	kmail2 = %{EVRD}
Conflicts:	kmail-common < 3:4.11.0
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kmail
KMail is the email component of Kontact, the integrated personal
information manager of KDE.

%files -n kmail
%doc %{_kde_docdir}/HTML/en/kmail
%{_kde_bindir}/kmail
%{_kde_bindir}/kmail_antivir.sh
%{_kde_bindir}/kmail_clamav.sh
%{_kde_bindir}/kmail_fprot.sh
%{_kde_bindir}/kmail_sav.sh
%{_kde_applicationsdir}/KMail2.desktop
%{_kde_applicationsdir}/kmail_view.desktop
%{_kde_appsdir}/composereditor/composereditorinitialhtml
%{_kde_appsdir}/kconf_update/kmail*
%{_kde_appsdir}/kconf_update/upgrade-signature.pl
%{_kde_appsdir}/kconf_update/upgrade-transport.pl
%{_kde_appsdir}/kmail2
%{_kde_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kde_datadir}/config.kcfg/kmail.kcfg
%{_kde_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kde_configdir}/kmail.antispamrc
%{_kde_configdir}/kmail.antivirusrc
%{_kde_configdir}/ksieve_script.knsrc
%{_kde_iconsdir}/*/*/apps/kmail.*
%{_kde_services}/kontact/kmailplugin.desktop
%{_kde_services}/kmail_config_accounts.desktop
%{_kde_services}/kmail_config_appearance.desktop
%{_kde_services}/kmail_config_composer.desktop
%{_kde_services}/kmail_config_identity.desktop
%{_kde_services}/kmail_config_misc.desktop
%{_kde_services}/kmail_config_security.desktop
%{_kde_services}/kcmkmailsummary.desktop
%{_kde_services}/kcm_kpimidentities.desktop
%{_kde_services}/ServiceMenus/kmail_addattachmentservicemenu.desktop
%{_kde_servicetypes}/dbusmail.desktop
%{_kde_libdir}/kde4/kcm_kmail.so
%{_kde_libdir}/kde4/kcm_kpimidentities.so
%{_kde_libdir}/kde4/kmailpart.so
%{_kde_libdir}/kde4/kcm_kmailsummary.so
%{_kde_libdir}/kde4/kontact_kmailplugin.so
%{_kde_libdir}/kde4/ktexteditorkabcbridge.so
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmail.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmailpart.xml

#-----------------------------------------------------------------------------

%package -n kmailcvt
Summary:	KDE Mail Import tool
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kmailcvt = %{EVRD}

%description -n kmailcvt
KDE Mail Import tool

%files -n kmailcvt
%doc %{_kde_docdir}/HTML/en/kmailcvt
%{_kde_bindir}/kmailcvt
%{_kde_appsdir}/kmailcvt/pics/step1.png
%{_kde_iconsdir}/*/*/apps/kmailcvt.*

#-----------------------------------------------------------------------------

%package -n knode
Summary:	A newsreader for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNode
Requires:	%{name}-core = %{EVRD}
Requires:	kdepimlibs-core
Requires:	kio4-nntp
Provides:	kde4-knode = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n knode
KNode is a newsreader for the K Desktop Environment.

It is GNKSA compliant (unfortunally a review is still pending), and has
support for MIME and multiple servers.

It is a online-reader, but in combination with a local newsserver like
leafnode also usable with dial-up connections.

%files -n knode
%doc %{_kde_docdir}/HTML/en/knode
%doc %{_kde_docdir}/HTML/en/kioslave/news
%{_kde_bindir}/knode
%{_kde_applicationsdir}/KNode.desktop
%{_kde_appsdir}/knode
%{_kde_appsdir}/kconf_update/knode.upd
%{_kde_iconsdir}/*/*/apps/knode.*
%{_kde_services}/kontact/knodeplugin.desktop
%{_kde_services}/knode_config_accounts.desktop
%{_kde_services}/knode_config_appearance.desktop
%{_kde_services}/knode_config_cleanup.desktop
%{_kde_services}/knode_config_identity.desktop
%{_kde_services}/knode_config_post_news.desktop
%{_kde_services}/knode_config_privacy.desktop
%{_kde_services}/knode_config_read_news.desktop
%{_kde_libdir}/kde4/kcm_knode.so
%{_kde_libdir}/kde4/knodepart.so
%{_kde_libdir}/kde4/kontact_knodeplugin.so
%{_datadir}/dbus-1/interfaces/org.kde.knode.xml

#-----------------------------------------------------------------------------

%package -n knotes
Summary:	Notes for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNotes
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-kresources
Requires:	akonadi-notes-agent = %{EVRD}
Requires:	kio4-nntp
Provides:	kde4-knotes = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%doc %{_kde_docdir}/HTML/en/knotes
%{_kde_bindir}/knotes
%{_kde_applicationsdir}/knotes.desktop
%{_kde_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_kde_datadir}/config/knotes_printing_theme.knsrc
%{_kde_appsdir}/knotes
%{_kde_iconsdir}/*/*/apps/knotes.*
%{_kde_iconsdir}/*/*/actions/knotes_*
%{_kde_services}/kcmknotessummary.desktop
%{_kde_services}/kontact/knotesplugin.desktop
%{_kde_services}/knote_config_action.desktop
%{_kde_services}/knote_config_collection.desktop
%{_kde_services}/knote_config_display.desktop
%{_kde_services}/knote_config_editor.desktop
%{_kde_services}/knote_config_misc.desktop
%{_kde_services}/knote_config_network.desktop
%{_kde_services}/knote_config_print.desktop
%{_kde_libdir}/kde4/kcm_knote.so
%{_kde_libdir}/kde4/kcm_knotessummary.so
%{_kde_libdir}/kde4/kontact_knotesplugin.so
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml

#-----------------------------------------------------------------------------

%package -n kontact
Summary:	Kontact Container
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Kontact
Requires:	%{name}-core = %{EVRD}
Requires:	kio4-ldap
Provides:	kde4-kontact = %{EVRD}
Suggests:	akregator
Suggests:	kmail
Suggests:	knotes
Suggests:	ktimetracker
Suggests:	knode
Suggests:	kalarm
Suggests:	kaddressbook
Suggests:	korganizer
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kontact
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -n kontact
%doc %{_kde_docdir}/HTML/en/kontact
%doc %{_kde_docdir}/HTML/en/kontact-admin
%{_kde_bindir}/kontact
%{_kde_appsdir}/kontact
%{_kde_appsdir}/kontactsummary
%{_kde_applicationsdir}/Kontact.desktop
%{_kde_applicationsdir}/kontact-admin.desktop
%{_kde_datadir}/config.kcfg/kontact.kcfg
%{_kde_iconsdir}/*/*/apps/kontact.*
%{_kde_services}/kontactconfig.desktop
%{_kde_services}/kcmapptsummary.desktop
%{_kde_services}/kcmkontactsummary.desktop
%{_kde_services}/kcmsdsummary.desktop
%{_kde_services}/kontact/summaryplugin.desktop
%{_kde_services}/kontact/specialdatesplugin.desktop
%{_kde_libdir}/kde4/kcm_apptsummary.so
%{_kde_libdir}/kde4/kcm_kontact.so
%{_kde_libdir}/kde4/kcm_kontactsummary.so
%{_kde_libdir}/kde4/kontact_journalplugin.so
%{_kde_libdir}/kde4/kcm_sdsummary.so
%{_kde_libdir}/kde4/kontact_specialdatesplugin.so
%{_kde_libdir}/kde4/kontact_summaryplugin.so
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml

#-----------------------------------------------------------------------------

%package -n korganizer
Summary:	Calendar and scheduling component
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KOrganizer
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-kresources
Requires:	kio4-ldap
Suggests:	kincidenceeditor
Provides:	kde4-korganizer = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n korganizer
KOrganizer provides management of events and tasks, alarm notification,
web export, network transparent handling of data, group scheduling,
import and export of calendar files and more. It is able to work together
with a wide variety of groupware servers, for example Kolab, Open-Xchange,
Citadel or OpenGroupware.org.

%files -n korganizer
%doc %{_kde_docdir}/HTML/en/korganizer
%doc %{_kde_docdir}/HTML/en/konsolekalendar
%{_kde_bindir}/calendarjanitor
%{_kde_bindir}/ical2vcal
%{_kde_bindir}/konsolekalendar
%{_kde_bindir}/korgac
%{_kde_bindir}/korganizer
%{_kde_applicationsdir}/konsolekalendar.desktop
%{_kde_applicationsdir}/korganizer-import.desktop
%{_kde_applicationsdir}/korganizer.desktop
%{_kde_appsdir}/kconf_update/korganizer.upd
%{_kde_appsdir}/korgac
%{_kde_appsdir}/korganizer
%{_kde_iconsdir}/*/*/apps/konsolekalendar.*
%{_kde_iconsdir}/*/*/apps/korganizer.*
%{_kde_iconsdir}/*/*/actions/checkmark.*
%{_kde_iconsdir}/*/*/actions/smallclock.*
%{_kde_iconsdir}/*/*/actions/upindicator.*
%{_kde_iconsdir}/*/*/apps/korg-journal.*
%{_kde_iconsdir}/*/*/apps/korg-todo.*
%{_kde_autostart}/korgac.desktop
%{_kde_datadir}/config.kcfg/korganizer.kcfg
%{_kde_configdir}/korganizer.knsrc
%{_kde_services}/kontact/korganizerplugin.desktop
%{_kde_services}/kontact/todoplugin.desktop
%{_kde_services}/kcmtodosummary.desktop
%{_kde_services}/kontact/journalplugin.desktop
%{_kde_services}/korganizer*
%{_kde_services}/webcal.protocol
%{_kde_servicetypes}/calendardecoration.desktop
%{_kde_servicetypes}/calendarplugin.desktop
%{_kde_servicetypes}/dbuscalendar.desktop
%{_kde_libdir}/kde4/kcm_todosummary.so
%{_kde_libdir}/kde4/kontact_todoplugin.so
%{_kde_libdir}/kde4/kcm_korganizer.so
%{_kde_libdir}/kde4/korg_*
%{_kde_libdir}/kde4/korganizerpart.so
%{_kde_libdir}/kde4/kontact_korganizerplugin.so
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml

#-----------------------------------------------------------------------------

%package kresources
Summary:	KDE pim resource plugins
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description kresources
This package includes several plugins needed to interface with groupware
servers. It also includes plugins for features such as blogging and
tracking feature plans.

%files kresources
%{_kde_libdir}/kde4/kcal_blog.so
%{_kde_libdir}/kde4/kcal_remote.so
%{_kde_services}/kresources/kcal/blog.desktop
%{_kde_services}/kresources/kcal/remote.desktop

#-----------------------------------------------------------------------------

%package -n ksendemail
Summary:	%{name} ksendemail
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n ksendemail
%{name} ksendemail.

%files -n ksendemail
%{_kde_bindir}/ksendemail

#-----------------------------------------------------------------------------

%package -n ktimetracker
Summary:	Tracks time spent on various tasks
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/Ktimetracker
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-ktimetracker = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n ktimetracker
KTimeTracker tracks time spent on various tasks. It is useful for tracking
hours to be billed to different clients or just to find out what percentage
of your day is spent playing Doom or reading Slashdot.

%files -n ktimetracker
%doc %{_kde_docdir}/HTML/en/ktimetracker
%{_kde_bindir}/karm
%{_kde_bindir}/ktimetracker
%{_kde_appsdir}/ktimetracker
%{_kde_applicationsdir}/ktimetracker.desktop
%{_kde_iconsdir}/*/*/apps/ktimetracker.*
%{_kde_services}/ktimetrackerpart.desktop
%{_kde_services}/ktimetracker_config_behavior.desktop
%{_kde_services}/ktimetracker_config_display.desktop
%{_kde_services}/ktimetracker_config_storage.desktop
%{_kde_libdir}/kde4/ktimetrackerpart.so
%{_kde_libdir}/kde4/kcm_ktimetracker.so
%{_datadir}/dbus-1/interfaces/org.kde.ktimetracker.ktimetracker.xml

#-----------------------------------------------------------------------------

%package -n ktnef
Summary:	KDE TNEF File Viewer
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n ktnef
The TNEF File Viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n ktnef
%doc %{_kde_docdir}/HTML/en/ktnef
%{_kde_bindir}/ktnef
%{_kde_applicationsdir}/ktnef.desktop
%{_kde_appsdir}/ktnef
%{_kde_iconsdir}/*/*/apps/ktnef*.*
%{_kde_iconsdir}/*/*/actions/ktnef*.*

#-----------------------------------------------------------------------------

%package -n mboximporter
Summary:	MBoxImporter allows to migrate data from MBox
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n mboximporter
MBoxImporter allows to migrate data from MBox.

%files -n mboximporter
%{_kde_bindir}/mboximporter
%{_kde_applicationsdir}/mboximporter.desktop

#-----------------------------------------------------------------------------

%package -n messageviewer
Summary:	Message viewer for KDE Email Client
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KMail
Conflicts:	akonadi-mailfilter-agent < 3:4.11.0
Conflicts:	kmail-common < 3:4.11.0
Obsoletes:	kmail-common < 3:4.11.0

%description -n messageviewer
Message viewer for KDE Email Client.

%files -n messageviewer
%{_kde_appsdir}/libmessageviewer
%{_kde_appsdir}/messageviewer
%{_kde_appsdir}/messagelist
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_application_mstnef.so
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_text_calendar.so
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_text_vcard.so
%{_kde_libdir}/kde4/messageviewer_bodypartformatter_text_xdiff.so
%{_kde_plugindir}/accessible/messagevieweraccessiblewidgetfactory.so
%{_kde_plugindir}/grantlee/0.4/grantlee_messageheaderfilters.so
%{_kde_datadir}/config/messageviewer_header_themes.knsrc

#-----------------------------------------------------------------------------

%libpackage pimsettingexporterprivate 4

%package -n pimsettingexporter
Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Group:		Graphical desktop/KDE
Requires:	kmail
Obsoletes:	backupmail < 3:4.10.0
Requires:	%{mklibname pimsettingexporterprivate 4}

%description -n pimsettingexporter
Allows to save data from KDE PIM applications and restore them in other
systems. Successor of Backup Mail from KDE 4.9.

%files -n pimsettingexporter
%doc %{_kde_docdir}/HTML/en/pimsettingexporter
%{_kde_bindir}/pimsettingexporter
%{_kde_applicationsdir}/pimsettingexporter.desktop
%{_kde_appsdir}/pimsettingexporter/backup-structure.txt
%{_kde_appsdir}/pimsettingexporter/pimsettingexporter.rc

#-----------------------------------------------------------------------------

%package -n sieveeditor
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n sieveeditor
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n sieveeditor
%doc %{_kde_docdir}/HTML/en/sieveeditor
%{_kde_bindir}/sieveeditor
%{_kde_applicationsdir}/sieveeditor.desktop
%{_kde_appsdir}/sieve/scripts/
%{_kde_appsdir}/sieveeditor/

#-----------------------------------------------------------------------------

%package -n storageservicemanager
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n storageservicemanager
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n storageservicemanager
%{_kde_bindir}/storageservicemanager
%{_kde_applicationsdir}/storageservicemanager.desktop
%{_kde_appsdir}/storageservicemanager/
%{_kde_iconsdir}/*/*/apps/kdepim-dropbox.*
%{_kde_iconsdir}/*/*/apps/kdepim-googledrive.*

#-----------------------------------------------------------------------------

%define akonadi_next_major 4
%define libakonadi_next %mklibname akonadi-next %{akonadi_next_major}

%package -n %{libakonadi_next}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakonadi_next}
KDE 4 library.

%files -n %{libakonadi_next}
%{_kde_libdir}/libakonadi_next.so.%{akonadi_next_major}*

#-----------------------------------------------------------------------------

%define akregatorinterfaces_major 4
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE 4 library.

%files -n %{libakregatorinterfaces}
%{_kde_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#-----------------------------------------------------------------------------

%define akregatorprivate_major 4
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE 4 library.

%files -n %{libakregatorprivate}
%{_kde_libdir}/libakregatorprivate.so.%{akregatorprivate_major}*

#------------------------------------------------------------------------------

%libpackage calendarsupportcollectionpage 4

%define calendarsupport_major 4
%define libcalendarsupport %mklibname calendarsupport %{calendarsupport_major}

%package -n %{libcalendarsupport}
Summary:	KDE 4 library
Group:		System/Libraries
Requires:	%{mklibname calendarsupportcollectionpage 4}

%description -n %{libcalendarsupport}
KDE 4 library for korganizer-Mobile.

%files -n %{libcalendarsupport}
%{_kde_libdir}/libcalendarsupport.so.%{calendarsupport_major}*

#-----------------------------------------------------------------------------

%define composereditorng_major 4
%define libcomposereditorng %mklibname composereditorng %{composereditorng_major}

%package -n %{libcomposereditorng}
Summary:	Library providing autospell checking
Group:		System/Libraries

%description -n %{libcomposereditorng}
This library provides autospell checking.

%files -n %{libcomposereditorng}
%{_kde_libdir}/libcomposereditorng.so.%{composereditorng_major}*

#-----------------------------------------------------------------------------

%define eventviews_major 4
%define libeventviews %mklibname eventviews %{eventviews_major}

%package -n %{libeventviews}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libeventviews}
KDE 4 library.

%files -n %{libeventviews}
%{_kde_libdir}/libeventviews.so.%{eventviews_major}*

#-----------------------------------------------------------------------------

%define followupreminder_major 4
%define libfollowupreminder %mklibname followupreminder %{followupreminder_major}

%package -n %{libfollowupreminder}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libfollowupreminder}
KDE 4 library.

%files -n %{libfollowupreminder}
%{_kde_libdir}/libfollowupreminder.so.%{followupreminder_major}*

#-----------------------------------------------------------------------------

%define grantleetheme_major 4
%define libgrantleetheme %mklibname grantleetheme %{grantleetheme_major}

%package -n %{libgrantleetheme}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libgrantleetheme}
KDE 4 library.

%files -n %{libgrantleetheme}
%{_kde_libdir}/libgrantleetheme.so.%{grantleetheme_major}*

#-----------------------------------------------------------------------------

%define grantleethemeeditor_major 4
%define libgrantleethemeeditor %mklibname grantleethemeeditor %{grantleethemeeditor_major}

%package -n %{libgrantleethemeeditor}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libgrantleethemeeditor}
KDE 4 library.

%files -n %{libgrantleethemeeditor}
%{_kde_libdir}/libgrantleethemeeditor.so.%{grantleethemeeditor_major}*

#----------------------------------------------------------------------------

%define incidenceeditorsng_major 4
%define libincidenceeditorsng %mklibname incidenceeditorsng %{incidenceeditorsng_major}

%package -n %{libincidenceeditorsng}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}incidenceeditors4 < 2:4.5.68

%description -n %{libincidenceeditorsng}
KDE 4 library.

%files -n %{libincidenceeditorsng}
%{_kde_libdir}/libincidenceeditorsng.so.%{incidenceeditorsng_major}*

#-----------------------------------------------------------------------------

%define incidenceeditorsngmobile_major 4
%define libincidenceeditorsngmobile %mklibname incidenceeditorssngmobile %{incidenceeditorsngmobile_major}

%package -n %{libincidenceeditorsngmobile}
Summary:	KDEPIM Mobile Library
Group:		System/Libraries

%description -n %{libincidenceeditorsngmobile}
KDE PIM Mobile library.

%files -n %{libincidenceeditorsngmobile}
%{_kde_libdir}/libincidenceeditorsngmobile.so.%{incidenceeditorsngmobile_major}*

#-----------------------------------------------------------------------------

%define kaddressbookgrantlee_major 4
%define libkaddressbookgrantlee %mklibname kaddressbookgrantlee %{kaddressbookgrantlee_major}

%package -n %{libkaddressbookgrantlee}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkaddressbookgrantlee}
KDE 4 library.

%files -n %{libkaddressbookgrantlee}
%{_kde_libdir}/libkaddressbookgrantlee.so.%{kaddressbookgrantlee_major}*

#-----------------------------------------------------------------------------

%define kaddressbookprivate_major 4
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %{libkaddressbookprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkaddressbookprivate}
KDE 4 library.

%files -n %{libkaddressbookprivate}
%{_kde_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*

#-----------------------------------------------------------------------------

%define kcal_resourceblog 4
%define libkcal_resourceblog %mklibname kcal_resourceblog %{kcal_resourceblog}

%package -n %{libkcal_resourceblog}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkcal_resourceblog}
KDE 4 library.

%files -n %{libkcal_resourceblog}
%{_kde_libdir}/libkcal_resourceblog.so.%{kcal_resourceblog}*

#-----------------------------------------------------------------------------

%define kcal_resourceremote_major 4
%define libkcal_resourceremote %mklibname kcal_resourceremote %{kcal_resourceremote_major}

%package -n %{libkcal_resourceremote}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkcal_resourceremote}
KDE 4 library.

%files -n %{libkcal_resourceremote}
%{_kde_libdir}/libkcal_resourceremote.so.%{kcal_resourceremote_major}*

#-----------------------------------------------------------------------------

%define kdepim_major 4
%define libkdepim %mklibname kdepim %{kdepim_major}

%package -n %{libkdepim}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdepim}
KDE 4 library.

%files -n %{libkdepim}
%{_kde_libdir}/libkdepim.so.%{kdepim_major}*

#-----------------------------------------------------------------------

%define kdgantt2_major 0
%define libkdgantt2 %mklibname kdgantt2 %{kdgantt2_major}

%package -n %{libkdgantt2}
Summary:	KDE4 library
Group:		System/Libraries

%description -n %{libkdgantt2}
KDE 4 library.

%files -n %{libkdgantt2}
%{_kde_libdir}/libkdgantt2.so.%{kdgantt2_major}*

#-----------------------------------------------------------------------------

%define kleo_major 4
%define libkleo %mklibname kleo %{kleo_major}

%package -n %{libkleo}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkleo}
KDE 4 library.

%files -n %{libkleo}
%{_kde_libdir}/libkleo.so.%{kleo_major}*

#-----------------------------------------------------------------------------

%define kmailprivate_major 4
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %{libkmailprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkmailprivate}
KDE 4 library.

%files -n %{libkmailprivate}
%{_kde_libdir}/libkmailprivate.so.%{kmailprivate_major}*

#-----------------------------------------------------------------------------

%define kmanagesieve_major 4
%define libkmanagesieve %mklibname kmanagesieve %{kmanagesieve_major}

%package -n %{libkmanagesieve}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkmanagesieve}
KDE 4 library.

%files -n %{libkmanagesieve}
%{_kde_libdir}/libkmanagesieve.so.%{kmanagesieve_major}*

#-----------------------------------------------------------------------------

%define knodecommon_major 4
%define libknodecommon %mklibname knodecommon %{knodecommon_major}

%package -n %{libknodecommon}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libknodecommon}
KDE 4 library.

%files -n %{libknodecommon}
%{_kde_libdir}/libknodecommon.so.%{knodecommon_major}*

#-----------------------------------------------------------------------------

%define knotesprivate_major 4
%define libknotesprivate %mklibname knotesprivate %{knotesprivate_major}

%package -n %{libknotesprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libknotesprivate}
KDE 4 library.

%files -n %{libknotesprivate}
%{_kde_libdir}/libknotesprivate.so.%{knotesprivate_major}*

#-----------------------------------------------------------------------------

%define kontactprivate_major 4
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %{libkontactprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE 4 library.

%files -n %{libkontactprivate}
%{_kde_libdir}/libkontactprivate.so.%{kontactprivate_major}*

#-----------------------------------------------------------------------------

%define korganizer_core_major 4
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE 4 library.

%files -n %{libkorganizer_core}
%{_kde_libdir}/libkorganizer_core.so.%{korganizer_core_major}*

#-----------------------------------------------------------------------------

%define korganizer_interfaces_major 4
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE 4 library.

%files -n %{libkorganizer_interfaces}
%{_kde_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*

#-----------------------------------------------------------------------------

%define korganizerprivate_major 4
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %{libkorganizerprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkorganizerprivate}
KDE 4 library.

%files -n %{libkorganizerprivate}
%{_kde_libdir}/libkorganizerprivate.so.%{korganizerprivate_major}*

#-----------------------------------------------------------------------------

%define kpgp_major 4
%define libkpgp %mklibname kpgp %{kpgp_major}

%package -n %{libkpgp}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkpgp}
KDE 4 library.

%files -n %{libkpgp}
%{_kde_libdir}/libkpgp.so.%{kpgp_major}*

#----------------------------------------------------------------------------

%define ksieve_major 4
%define libksieve %mklibname ksieve %{ksieve_major}

%package -n %{libksieve}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libksieve}
KDE 4 library.

%files -n %{libksieve}
%{_kde_libdir}/libksieve.so.%{ksieve_major}*

#-----------------------------------------------------------------------------

%define ksieveui_major 4
%define libksieveui %mklibname ksieveui %{ksieveui_major}

%package -n %{libksieveui}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libksieveui}
KDE 4 library.

%files -n %{libksieveui}
%{_kde_libdir}/libksieveui.so.%{ksieveui_major}*

#-----------------------------------------------------------------------------

%define mailcommon_major 4
%define libmailcommon %mklibname mailcommon %{mailcommon_major}

%package -n %{libmailcommon}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmailcommon}
KDE 4 library.

%files -n %{libmailcommon}
%{_kde_libdir}/libmailcommon.so.%{mailcommon_major}*

#-----------------------------------------------------------------------------

%define mailimporter_major 4
%define libmailimporter %mklibname mailimporter %{mailimporter_major}

%package -n %{libmailimporter}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmailimporter}
KDE 4 library.

%files -n %{libmailimporter}
%{_kde_libdir}/libmailimporter.so.%{mailimporter_major}*

#-----------------------------------------------------------------------------

%define messagecore_major 4
%define libmessagecore %mklibname messagecore %{messagecore_major}

%package -n %{libmessagecore}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessagecore}
KDE 4 library.

%files -n %{libmessagecore}
%{_kde_libdir}/libmessagecore.so.%{messagecore_major}*

#-----------------------------------------------------------------------------

%define messagelist_major 4
%define libmessagelist %mklibname messagelist %{messagelist_major}

%package -n %{libmessagelist}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessagelist}
KDE 4 library.

%files -n %{libmessagelist}
%{_kde_libdir}/libmessagelist.so.%{messagelist_major}*

#-----------------------------------------------------------------------------

%define messageviewer_major 4
%define libmessageviewer %mklibname messageviewer %{messageviewer_major}

%package -n %{libmessageviewer}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessageviewer}
KDE 4 library.

%files -n %{libmessageviewer}
%{_kde_libdir}/libmessageviewer.so.%{messageviewer_major}*

#-----------------------------------------------------------------------------

%define kdepimdbusinterfaces_major 4
%define libkdepimdbusinterfaces %mklibname kdepimdbusinterfaces %{kdepimdbusinterfaces_major}

%package -n %{libkdepimdbusinterfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdepimdbusinterfaces}
KDE 4 library.

%files -n %{libkdepimdbusinterfaces}
%{_kde_libdir}/libkdepimdbusinterfaces.so.%{kdepimdbusinterfaces_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientcore_major 0
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %{libkleopatraclientcore}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientcore4 <= 2:4.5

%description -n %{libkleopatraclientcore}
KDE 4 library.

%files -n %{libkleopatraclientcore}
%{_kde_libdir}/libkleopatraclientcore.so.%{kleopatraclientcore_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientgui_major 0
%define libkleopatraclientgui %mklibname kleopatraclientgui %{kleopatraclientgui_major}

%package -n %{libkleopatraclientgui}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientgui4 <= 2:4.5

%description -n %{libkleopatraclientgui}
KDE 4 library.

%files -n %{libkleopatraclientgui}
%{_kde_libdir}/libkleopatraclientgui.so.%{kleopatraclientgui_major}*

#-----------------------------------------------------------------------------

%define messagecomposer_major 4
%define libmessagecomposer %mklibname messagecomposer %{messagecomposer_major}

%package -n %{libmessagecomposer}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libmessagecomposer}
KDE 4 library.

%files -n %{libmessagecomposer}
%{_kde_libdir}/libmessagecomposer.so.%{messagecomposer_major}*

#-----------------------------------------------------------------------------

%define noteshared_major 4
%define libnoteshared %mklibname noteshared %{noteshared_major}

%package -n %{libnoteshared}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libnoteshared}
KDE 4 library.

%files -n %{libnoteshared}
%{_kde_libdir}/libnoteshared.so.%{noteshared_major}*

#-----------------------------------------------------------------------------

%define pimcommon_major 4
%define libpimcommon %mklibname pimcommon %{pimcommon_major}

%package -n %{libpimcommon}
Summary:	Library to import/export PIM configuration
Group:		System/Libraries

%description -n %{libpimcommon}
This library provides the tool to import/export PIM configuration.

%files -n %{libpimcommon}
%{_kde_libdir}/libpimcommon.so.%{pimcommon_major}*

#-----------------------------------------------------------------------------

%define sendlater_major 4
%define libsendlater %mklibname sendlater %{sendlater_major}

%package -n %{libsendlater}
Summary:	KDE PIM library
Group:		System/Libraries

%description -n %{libsendlater}
KDE PIM library.

%files -n %{libsendlater}
%{_kde_libdir}/libsendlater.so.%{sendlater_major}*

#-----------------------------------------------------------------------------

%define templateparser_major 4
%define libtemplateparser %mklibname templateparser %{templateparser_major}

%package -n %{libtemplateparser}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libtemplateparser}
KDE 4 library.

%files -n %{libtemplateparser}
%{_kde_libdir}/libtemplateparser.so.%{templateparser_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs-devel
Requires:	kdepimlibs-devel
Requires:	kdepim-runtime-devel
Requires:	%{libakonadi_next} = %{EVRD}
Requires:	%{libakregatorinterfaces} = %{EVRD}
Requires:	%{libakregatorprivate} = %{EVRD}
Requires:	%{libcalendarsupport} = %{EVRD}
Requires:	%{libcomposereditorng} = %{EVRD}
Requires:	%{libeventviews} = %{EVRD}
Requires:	%{libfollowupreminder} = %{EVRD}
Requires:	%{libgrantleetheme} = %{EVRD}
Requires:	%{libgrantleethemeeditor} = %{EVRD}
Requires:	%{libincidenceeditorsng} = %{EVRD}
Requires:	%{libincidenceeditorsngmobile} = %{EVRD}
Requires:	%{libkaddressbookgrantlee} = %{EVRD}
Requires:	%{libkaddressbookprivate} = %{EVRD}
Requires:	%{libkcal_resourceblog} = %{EVRD}
Requires:	%{libkcal_resourceremote} = %{EVRD}
Requires:	%{libkdepim} = %{EVRD}
Requires:	%{libkdepimdbusinterfaces} = %{EVRD}
Requires:	%{libkdgantt2} = %{EVRD}
Requires:	%{libkleo} = %{EVRD}
Requires:	%{libkleopatraclientcore} = %{EVRD}
Requires:	%{libkleopatraclientgui} = %{EVRD}
Requires:	%{libkmailprivate} = %{EVRD}
Requires:	%{libkmanagesieve} = %{EVRD}
Requires:	%{libknodecommon} = %{EVRD}
Requires:	%{libknotesprivate} = %{EVRD}
Requires:	%{libkorganizer_interfaces} = %{EVRD}
Requires:	%{libkorganizerprivate} = %{EVRD}
Requires:	%{libkpgp} = %{EVRD}
Requires:	%{libksieve} = %{EVRD}
Requires:	%{libksieveui} = %{EVRD}
Requires:	%{libmailcommon} = %{EVRD}
Requires:	%{libmailimporter} = %{EVRD}
Requires:	%{libmessagecomposer} = %{EVRD}
Requires:	%{libmessagecore} = %{EVRD}
Requires:	%{libmessagelist} = %{EVRD}
Requires:	%{libmessageviewer} = %{EVRD}
Requires:	%{libnoteshared} = %{EVRD}
Requires:	%{libpimcommon} = %{EVRD}
Requires:	%{mklibname pimsettingexporterprivate 4}  = %{EVRD}
Requires:	%{libsendlater} = %{EVRD}
Requires:	%{libtemplateparser} = %{EVRD}
%rename		kdepim4-devel

%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%{_kde_libdir}/*.so

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4 -DKDEPIM_BUILD_MOBILE=false
%make

%install
%makeinstall_std -C build

# akonadi_folderarchive_agent was removed, no need to keep desktop file
rm -f %{buildroot}%{_kde_datadir}/akonadi/agents/folderarchiveagent.desktop

%find_lang %{name} --all-name --with-html


Summary:	An application suite to manage personal information
Name:		kdepim
Epoch:		3
Version:	15.08.1
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
Patch1:		kdepim-15.08.0-cmake-libkaddressbookgrantlee.patch
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	gpgme-devel
BuildRequires:	grantlee-devel >= 0.4.0
BuildRequires:	libassuan-devel
BuildRequires:	sasl-devel
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core) 
BuildRequires:	pkgconfig(Qt5Test) 
BuildRequires:	pkgconfig(Qt5Script) 
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5UiTools)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Declarative)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiCalendar)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5AkonadiSearch)
BuildRequires:	cmake(KF5AkonadiServer)
BuildRequires:	cmake(KF5AlarmCalendar)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Blog)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GAPI)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5Gpgmepp)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5Mbox)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Tnef)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WebKit)
BuildRequires:	cmake(KF5XmlRpcClient)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	cmake(Prison)
Suggests:	akonadi-common
Suggests:	kleopatra
Suggests:	akregator
Suggests:	kaddressbook
Suggests:	kalarm
Suggests:	kmail
Suggests:	knotes
Suggests:	kontact
Suggests:	korganizer
Suggests:	ksendemail
%rename		kdepim4

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer
	  and kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client

%files

#----------------------------------------------------------------------

%package core
Summary:	Core files for KDE PIM
Group:		Graphical desktop/KDE
# (tpg) probably not needed
#Requires:	kde-runtime
#Requires:	kdelibs-core
Requires:	storageservicemanager = %{EVRD}
Conflicts:	%{_lib}kdepim4 < 3:4.11.0
Conflicts:	%{_lib}kpgp4 < 3:4.11.0
Conflicts:	%{name}-devel < 3:4.11.0
Obsoletes:	akonadi-folderarchive-agent < 3:4.13.0
Obsoletes:	pimactivity < 3:4.13.0
%rename		kdepim4-core
Provides:	kdepim4-core = 3:4.14.3-1

%description core
Core files for KDE PIM.

%files core -f %{name}.lang
%exclude %{_kde5_docdir}/HTML/en/*
%{_kde5_bindir}/contactprintthemeeditor
%{_kde5_datadir}/kdepimwidgets
%{_sysconfdir}/xdg/kdepim.categories
%{_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_kde5_docdir}/HTML/en/contactthemeeditor
%{_kde5_datadir}/applications/org.kde.storageservicemanager.desktop
%{_kde5_datadir}/knotifications5/storageservicemanager.notifyrc
%{_kde5_datadir}/kxmlgui5/storageservicemanager
%{_qt5_plugindir}/designer/kdepimwidgets.so
%{_qt5_plugindir}/designer/pimcommonwidgets.so
%{_kde5_datadir}/applications/org.kde.contactprintthemeeditor.desktop
%{_kde5_datadir}/composereditor/composereditorinitialhtml
%{_kde5_datadir}/kxmlgui5/contactprintthemeeditor/contactprintthemeeditorui.rc
%{_kde5_iconsdir}/*/*/*/quickview.png
%{_kde5_iconsdir}/*/*/*/quickview.svgz
%{_kde5_iconsdir}/*/*/*/x-mail-distribution-list.png

#-----------------------------------------------------------------------------

%package -n akonadiconsole
Summary:	Console that help to debug akonadi
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Conflicts:	kdepim4-core < 2:4.4.2-5

%description -n akonadiconsole
Console that help to debug akonadi.

%files -n akonadiconsole
%{_kde5_bindir}/akonadiconsole
%{_kde5_applicationsdir}/org.kde.akonadiconsole.desktop
%{_kde5_datadir}/kxmlgui5/akonadiconsole/akonadiconsoleui.rc
%{_kde5_iconsdir}/hicolor/*/apps/akonadiconsole.png

#-----------------------------------------------------------------------------

%package -n akonadi-archivemail-agent
Summary:	Akonadi archivemail agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-archivemail-agent
Akonadi archivemail agent.

%files -n akonadi-archivemail-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_archivemail_agent
%{_kde5_bindir}/akonadi_archivemail_agent
%{_kde5_datadir}/akonadi/agents/archivemailagent.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-followupreminder-agent
Summary:	Akonadi followupreminder agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-followupreminder-agent
Akonadi followup reminder agent allows to remind you when an email was not
answered.

%files -n akonadi-followupreminder-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_followupreminder_agent
%{_kde5_bindir}/akonadi_followupreminder_agent
%{_kde5_datadir}/akonadi/agents/followupreminder.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-mailfilter-agent
Summary:	Akonadi mailfilter agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-mailfilter-agent
Akonadi mailfilter agent.

%files -n akonadi-mailfilter-agent
%{_kde5_bindir}/akonadi_mailfilter_agent
%{_kde5_datadir}/akonadi/agents/mailfilteragent.desktop

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
%doc %{_kde5_docdir}/HTML/en/akonadi_notes_agent
%{_kde5_bindir}/akonadi_notes_agent
%{_kde5_datadir}/akonadi/agents/notesagent.desktop

#-----------------------------------------------------------------------------

%package -n akonadi-sendlater-agent
Summary:	Akonadi sendlater agent
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n akonadi-sendlater-agent
Akonadi sendlater agent.

%files -n akonadi-sendlater-agent
%doc %{_kde5_docdir}/HTML/en/akonadi_sendlater_agent
%{_kde5_bindir}/akonadi_sendlater_agent
%{_kde5_datadir}/akonadi/agents/sendlateragent.desktop

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
%doc %{_kde5_docdir}/HTML/en/akregator
%{_kde5_bindir}/akregator
%{_kde5_bindir}/akregatorstorageexporter
%{_kde5_applicationsdir}/org.kde.akregator.desktop
%{_kde5_datadir}/akregator
%{_kde5_datadir}/knotifications5/akregator.notifyrc
%{_qt5_plugindir}/akregator*
%{_datadir}/appdata/akregator.appdata.xml
%{_datadir}/kxmlgui5/akregator
%{_kde5_datadir}/kservicetypes5/akregator_plugin.desktop
%{_kde5_datadir}/config.kcfg/akregator.kcfg
%{_kde5_iconsdir}/*/*/apps/akregator.*
%{_kde5_iconsdir}/*/*/apps/akregator_empty.*
%{_kde5_services}/kontact/akregatorplugin.desktop
%{_kde5_services}/akregator_*
%{_kde5_services}/feed.protocol
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
%doc %{_kde5_docdir}/HTML/en/blogilo
%{_kde5_bindir}/blogilo
%{_kde5_applicationsdir}/org.kde.blogilo.desktop
%{_datadir}/appdata/blogilo.appdata.xml
%{_kde5_datadir}/config.kcfg/blogilo.kcfg
%{_datadir}/kxmlgui5/blogilo
%{_kde5_iconsdir}/*/*/apps/blogilo.*
%{_kde5_iconsdir}/*/*/actions/format-text-blockquote.*
%{_kde5_iconsdir}/*/*/actions/format-text-code.*
%{_kde5_iconsdir}/*/*/actions/insert-more-mark.*
%{_kde5_iconsdir}/*/*/actions/remove-link.*
%{_kde5_iconsdir}/*/*/actions/upload-media.*

#-----------------------------------------------------------------------------

%package -n headerthemeeditor
Summary:	KMail Header Theme Editor
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}

%description -n headerthemeeditor
KMail Header Theme Editor.

%files -n headerthemeeditor
%doc %{_kde5_docdir}/HTML/en/headerthemeeditor
%{_kde5_bindir}/headerthemeeditor
%{_kde5_applicationsdir}/org.kde.headerthemeeditor.desktop
%{_kde5_datadir}/kxmlgui5/headerthemeeditor

#-----------------------------------------------------------------------------

%package -n contactthemeeditor
Summary:	KDE Contact Theme Editor
Group:		Graphical desktop/KDE
Requires:	kaddressbook = %{EVRD}

%description -n contactthemeeditor
KDE Contact Theme Editor.

%files -n contactthemeeditor
%doc %{_kde5_docdir}/HTML/en/contactthemeeditor
%{_kde5_bindir}/contactthemeeditor
%{_kde5_applicationsdir}/org.kde.contactthemeeditor.desktop
%{_kde5_datadir}/kxmlgui5/contactthemeeditor

#-----------------------------------------------------------------------------

%package -n importwizard
Summary:	Import Wizard allows to migrate data from mailer as thunderbird/evolution etc
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}

%description -n importwizard
Import Wizard allows to migrate data from mailer as thunderbird/evolution etc.

%files -n importwizard
%doc %{_kde5_docdir}/HTML/en/importwizard
%{_kde5_bindir}/importwizard
%{_kde5_applicationsdir}/org.kde.importwizard.desktop
%{_kde5_datadir}/importwizard
%{_kde5_iconsdir}/*/*/apps/kontact-import-wizard.*

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
%{_kde5_bindir}/kaddressbook
%{_kde5_applicationsdir}/org.kde.kaddressbook.desktop
%{_kde5_datadir}/kaddressbook
%{_sysconfdir}/xdg/kaddressbook_themes.knsrc
%{_qt5_plugindir}/kcm_ldap.so
%{_kde5_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_kde5_iconsdir}/*/*/apps/kaddressbook.*
%{_kde5_services}/kaddressbookpart.desktop
%{_kde5_services}/kontact/kaddressbookplugin.desktop
%{_kde5_services}/kcmldap.desktop
%{_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_qt5_plugindir}/kaddressbookpart.so
%{_kde5_datadir}/appdata/kaddressbook.appdata.xml
%{_kde5_datadir}/kxmlgui5/kaddressbook
%{_kde5_datadir}/applications/kaddressbook-importer.desktop

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
%doc %{_kde5_docdir}/HTML/en/kalarm
%{_kde5_bindir}/kalarm
%{_kde5_bindir}/kalarmautostart
%_kde5_libexecdir/kalarm_helper
%{_sysconfdir}/xdg/autostart/kalarm.autostart.desktop
%{_kde5_applicationsdir}/org.kde.kalarm.desktop
%{_kde5_datadir}/kalarm
%{_kde5_datadir}/kconf_update/kalarm-1.2.1-general.pl
%{_kde5_datadir}/kconf_update/kalarm-1.9.5-defaults.pl
%{_kde5_datadir}/kconf_update/kalarm-2.0.2-general.pl
%{_kde5_datadir}/kconf_update/kalarm-2.1.5-general.pl
%{_kde5_datadir}/kconf_update/kalarm-version.pl
%{_kde5_datadir}/kconf_update/kalarm.upd
%{_kde5_datadir}/config.kcfg/kalarmconfig.kcfg
%{_kde5_datadir}/polkit-1/actions/org.kde.kalarmrtcwake.policy
%{_kde5_iconsdir}/*/*/apps/kalarm.*
%{_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf
%{_datadir}/dbus-1/system-services/org.kde.kalarmrtcwake.service
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_kde5_datadir}/appdata/kalarm.appdata.xml
%{_kde5_datadir}/kxmlgui5/kalarm

#---------------------------------------------------------------------------

%package -n kincidenceeditor
Summary:	kincidenceeditor
Group:		Graphical desktop/KDE

%description -n kincidenceeditor
New incidince editor.

%files -n kincidenceeditor
%{_kde5_bindir}/kincidenceeditor

#-----------------------------------------------------------------------------

%package -n kleopatra
Summary:	KDE Certificate Manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kleopatra = %{EVRD}

%description -n kleopatra
KDE Certificate Manager.

%files -n kleopatra
%doc %{_kde5_docdir}/HTML/en/kleopatra
%doc %{_kde5_docdir}/HTML/en/kwatchgnupg
%{_sysconfdir}/xdg/libkleopatrarc
%{_kde5_bindir}/kleopatra
%{_kde5_bindir}/kgpgconf
%{_kde5_bindir}/kwatchgnupg
%{_kde5_applicationsdir}/org.kde.kleopatra.desktop
%{_kde5_applicationsdir}/kleopatra_import.desktop
%{_kde5_datadir}/kleopatra
%{_kde5_datadir}/libkleopatra
%{_kde5_datadir}/kwatchgnupg
%{_datadir}/kxmlgui5/kleopatra
%{_datadir}/kxmlgui5/kwatchgnupg
%{_kde5_iconsdir}/*/*/apps/kleopatra.*
%{_kde5_services}/kleopatra_*
%{_qt5_plugindir}/kcm_kleopatra.so
%{_kde5_datadir}/appdata/kleopatra.appdata.xml

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
Requires:	kio-pop3
Requires:	kio-smtp
Requires:	kio-mbox
Requires:	kio-imap
Requires:	kio-sieve
Requires:	akonadi-archivemail-agent = %{EVRD}
Requires:	akonadi-followupreminder-agent = %{EVRD}
Requires:	akonadi-mailfilter-agent = %{EVRD}
Requires:	akonadi-sendlater-agent = %{EVRD}
Requires:	headerthemeeditor = %{EVRD}
Requires:	messageviewer = %{EVRD}
Suggests:	kaddressbook = %{EVRD}
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
%doc %{_kde5_docdir}/HTML/en/kmail
%{_kde5_bindir}/kmail
%{_sysconfdir}/xdg/kmail.*
%{_sysconfdir}/xdg/ksieve_script.knsrc
%{_kde5_applicationsdir}/kmail_view.desktop
%{_kde5_datadir}/kmail2
%{_kde5_datadir}/kxmlgui5/kmail2
%{_kde5_datadir}/sieve
%{_kde5_datadir}/messagelist
%{_kde5_datadir}/knotifications5/kmail2.notifyrc
%{_kde5_datadir}/applications/org.kde.kmail.desktop
%{_kde5_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kde5_datadir}/config.kcfg/kmail.kcfg
%{_kde5_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kde5_datadir}/knotifications5/akonadi_archivemail_agent.notifyrc
%{_kde5_datadir}/knotifications5/akonadi_mailfilter_agent.notifyrc
%{_kde5_datadir}/knotifications5/akonadi_followupreminder_agent.notifyrc
%{_kde5_datadir}/knotifications5/akonadi_sendlater_agent.notifyrc
%{_kde5_iconsdir}/*/*/apps/kmail.*
%{_kde5_services}/kontact/kmailplugin.desktop
%{_kde5_services}/kmail_config_accounts.desktop
%{_kde5_services}/kmail_config_appearance.desktop
%{_kde5_services}/kmail_config_composer.desktop
%{_kde5_services}/kmail_config_identity.desktop
%{_kde5_services}/kmail_config_misc.desktop
%{_kde5_services}/kmail_config_security.desktop
%{_kde5_services}/kcmkmailsummary.desktop
%{_kde5_services}/kcm_kpimidentities.desktop
%{_kde5_services}/ServiceMenus/kmail_addattachmentservicemenu.desktop
%{_qt5_plugindir}/kcm_kmail.so
%{_qt5_plugindir}/kcm_kpimidentities.so
%{_qt5_plugindir}/kcm_kmailsummary.so
%{_qt5_plugindir}/kmailpart.so
%{_qt5_plugindir}/designer/mailcommonwidgets.so
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmail.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
%{_kde5_datadir}/appdata/org.kde.kmail.appdata.xml
%{_kde5_datadir}/kservicetypes5/dbusmail.desktop

#------------------------------------------------------------------------------

%package accountwizard
Summary: kincidenceeditor
Group: Graphical desktop/KDE

%description accountwizard
New incidence editors

%files accountwizard
%{_kde5_bindir}/accountwizard
%{_kde5_bindir}/ispdb
%{_sysconfdir}/xdg/accountwizard.knsrc
%{_qt5_plugindir}/accountwizard_plugin.so
%{_kde5_datadir}/akonadi/accountwizard
%{_kde5_datadir}/mime/packages/accountwizard-mime.xml
%{_kde5_datadir}/applications/org.kde.accountwizard.desktop

#-----------------------------------------------------------------------------

%package -n knotes
Summary:	Notes for the K Desktop Environment
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KNotes
Requires:	%{name}-core = %{EVRD}
Requires:	akonadi-notes-agent = %{EVRD}
Requires:	kio-nntp
Provides:	kde4-knotes = %{EVRD}
Conflicts:	%{name}-devel < 3:4.11.0

%description -n knotes
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -n knotes
%doc %{_kde5_docdir}/HTML/en/knotes
%{_kde5_bindir}/knotes
%{_sysconfdir}/xdg/knotes_printing_theme.knsrc
%{_kde5_applicationsdir}/org.kde.knotes.desktop
%{_kde5_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_kde5_datadir}/knotes
%{_kde5_datadir}/kxmlgui5/knotes
%{_kde5_iconsdir}/*/*/apps/knotes.*
%{_kde5_iconsdir}/*/*/actions/knotes_*
%{_kde5_services}/kcmknotessummary.desktop
%{_kde5_services}/kontact/knotesplugin.desktop
%{_kde5_services}/knote_config_action.desktop
%{_kde5_services}/knote_config_collection.desktop
%{_kde5_services}/knote_config_display.desktop
%{_kde5_services}/knote_config_editor.desktop
%{_kde5_services}/knote_config_misc.desktop
%{_kde5_services}/knote_config_network.desktop
%{_kde5_services}/knote_config_print.desktop
%{_qt5_plugindir}/kcm_knote.so
%{_qt5_plugindir}/kcm_knotessummary.so
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_kde5_datadir}/appdata/knotes.appdata.xml
%{_kde5_datadir}/knotifications5/akonadi_notes_agent.notifyrc

#-----------------------------------------------------------------------------

%package -n kontact
Summary:	Kontact Container
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/Kontact
Requires:	%{name}-core = %{EVRD}
Requires:	kio-ldap
Provides:	kde4-kontact = %{EVRD}
Suggests:	akregator
Suggests:	kmail
Suggests:	knotes
Suggests:	kalarm
Suggests:	kaddressbook
Suggests:	korganizer
Conflicts:	%{name}-devel < 3:4.11.0

%description -n kontact
The KDE Kontact Personal Information Management suite unites mature and
proven KDE applications under one roof. Thanks to the powerful KParts
technology, existing applications are seamlessly integrated into one.

%files -n kontact
%doc %{_kde5_docdir}/HTML/en/kontact
%doc %{_kde5_docdir}/HTML/en/kontact-admin
%{_kde5_bindir}/kontact
%{_kde5_datadir}/kontact
%{_kde5_datadir}/knode
%{_kde5_applicationsdir}/org.kde.kontact.desktop
%{_kde5_applicationsdir}/kontact-admin.desktop
%{_kde5_datadir}/config.kcfg/kontact.kcfg
%{_kde5_iconsdir}/*/*/apps/kontact.*
%{_kde5_services}/kontactconfig.desktop
%{_kde5_services}/kcmapptsummary.desktop
%{_kde5_services}/kcmkontactsummary.desktop
%{_kde5_services}/kcmsdsummary.desktop
%{_kde5_services}/kontact/summaryplugin.desktop
%{_kde5_services}/kontact/specialdatesplugin.desktop
%{_qt5_plugindir}/kcm_apptsummary.so
%{_qt5_plugindir}/kcm_kontact.so
%{_qt5_plugindir}/kcm_kontactsummary.so
%{_qt5_plugindir}/kcm_sdsummary.so
%{_qt5_plugindir}/kontact_*
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_kde5_datadir}/appdata/Kontact.appdata.xml
%{_kde5_datadir}/kxmlgui5/kontact
%{_kde5_datadir}/kxmlgui5/kontactsummary

#-----------------------------------------------------------------------------

%package -n korganizer
Summary:	Calendar and scheduling component
Group:		Graphical desktop/KDE
Url:		http://userbase.kde.org/KOrganizer
Requires:	%{name}-core = %{EVRD}
Requires:	kio-ldap
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
%doc %{_kde5_docdir}/HTML/en/korganizer
%doc %{_kde5_docdir}/HTML/en/konsolecalendar

%{_kde5_bindir}/calendarjanitor
%{_kde5_bindir}/ical2vcal
%{_kde5_bindir}/konsolekalendar
%{_kde5_bindir}/korgac
%{_kde5_bindir}/korganizer
%{_kde5_applicationsdir}/konsolekalendar.desktop
%{_kde5_applicationsdir}/korganizer-import.desktop
%{_kde5_applicationsdir}/org.kde.korganizer.desktop
%{_sysconfdir}/xdg/korganizer.knsrc
%{_kde5_datadir}/korgac
%{_kde5_datadir}/korganizer
%{_kde5_iconsdir}/*/*/apps/konsolekalendar.*
%{_kde5_iconsdir}/*/*/apps/korganizer.*
%{_kde5_iconsdir}/*/*/actions/checkmark.*
%{_kde5_iconsdir}/*/*/actions/smallclock.*
%{_kde5_iconsdir}/*/*/actions/upindicator.*
%{_kde5_iconsdir}/*/*/apps/korg-journal.*
%{_kde5_iconsdir}/*/*/apps/korg-todo.*
%{_kde5_datadir}/config.kcfg/korganizer.kcfg
%{_kde5_services}/kontact/korganizerplugin.desktop
%{_kde5_services}/kontact/todoplugin.desktop
%{_kde5_services}/kcmtodosummary.desktop
%{_kde5_services}/kontact/journalplugin.desktop
%{_kde5_services}/korganizer*
%{_kde5_services}/webcal.protocol
%{_sysconfdir}/xdg/autostart/org.kde.korgac.desktop
%{_qt5_plugindir}/kcm_todosummary.so
%{_qt5_plugindir}/kcm_korganizer.so
%{_qt5_plugindir}/korganizerpart.so
%{_qt5_plugindir}/korg_*
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.KOrgac.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.Korganizer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.Calendar.xml
%{_kde5_datadir}/appdata/korganizer.appdata.xml
%{_kde5_datadir}/kxmlgui5/korganizer
%{_kde5_datadir}/kservicetypes5/calendardecoration.desktop
%{_kde5_datadir}/kservicetypes5/calendarplugin.desktop
%{_kde5_datadir}/kservicetypes5/dbuscalendar.desktop

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
%doc %{_kde5_docdir}/HTML/en/ktnef
%{_kde5_bindir}/ktnef
%{_kde5_applicationsdir}/org.kde.ktnef.desktop
%{_kde5_iconsdir}/*/*/apps/ktnef*.*
%{_kde5_iconsdir}/*/*/actions/ktnef*.*
%{_kde5_datadir}/kxmlgui5/ktnef

#-----------------------------------------------------------------------------

%package -n mboximporter
Summary:	MBoxImporter allows to migrate data from MBox
Group:		Graphical desktop/KDE
Requires:	kmail

%description -n mboximporter
MBoxImporter allows to migrate data from MBox.

%files -n mboximporter
%{_kde5_bindir}/mboximporter
%{_kde5_applicationsdir}/org.kde.mboximporter.desktop

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
%{_kde5_datadir}/libmessageviewer
%{_kde5_datadir}/messageviewer
%{_kde5_datadir}/knotifications5/messageviewer.notifyrc
%{_qt5_plugindir}/grantlee/5.0/grantlee_messageheaderfilters.so
%{_qt5_plugindir}/messageviewer_*
%{_sysconfdir}/xdg/messageviewer_header_themes.knsrc

#-----------------------------------------------------------------------------

%define pimsettingexporterprivate_major 5
%define libpimsettingexporterprivate %mklibname pimsettingexporterprivate %{pimsettingexporterprivate_major}

%package -n %{libpimsettingexporterprivate}
Summary:        KDE 5 library
Group:          System/Libraries

%description -n %{libpimsettingexporterprivate}
KDE 5 library for korganizer-Mobile.

%files -n %{libpimsettingexporterprivate}
%{_kde5_libdir}/libpimsettingexporterprivate.so.%{pimsettingexporterprivate_major}*
%{_kde5_libdir}/libpimsettingexporterprivate.so.4*

#-----------------------------------------------------------------------------

%package -n pimsettingexporter
Summary:	Allows to save data from KDE PIM applications and restore them in other systems
Group:		Graphical desktop/KDE
Requires:	kmail = %{EVRD}
Obsoletes:	backupmail < 3:4.10.0
Requires:	%{mklibname pimsettingexporterprivate 5}

%description -n pimsettingexporter
Allows to save data from KDE PIM applications and restore them in other
systems. Successor of Backup Mail from KDE.9.

%files -n pimsettingexporter
%doc %{_kde5_docdir}/HTML/en/pimsettingexporter
%{_kde5_bindir}/pimsettingexporter
%{_kde5_bindir}/pimsettingexporterconsole
%{_kde5_datadir}/applications/org.kde.pimsettingexporter.desktop
%{_kde5_datadir}/kxmlgui5/pimsettingexporter
%{_kde5_datadir}/pimsettingexporter
#-----------------------------------------------------------------------------

%package -n sieveeditor
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n sieveeditor
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n sieveeditor
%doc %{_kde5_docdir}/HTML/en/sieveeditor
%{_kde5_bindir}/sieveeditor
%{_kde5_applicationsdir}/org.kde.sieveeditor.desktop
%{_kde5_datadir}/kxmlgui5/sieveeditor

#-----------------------------------------------------------------------------

%package -n storageservicemanager
Summary:	Storage service manager
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n storageservicemanager
KDE storage service manager. It allows to manage your storage service as
DropBox etc.

%files -n storageservicemanager
%{_kde5_bindir}/storageservicemanager
%{_kde5_iconsdir}/*/*/apps/kdepim-dropbox.*

#-----------------------------------------------------------------------------

%define akregatorinterfaces_major 5
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE library.

%files -n %{libakregatorinterfaces}
%{_kde5_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*
%{_kde5_libdir}/libakregatorinterfaces.so.4*

#-----------------------------------------------------------------------------
%define akregatorprivate_major 5
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE library.

%files -n %{libakregatorprivate}
%{_kde5_libdir}/libakregatorprivate.so.%{akregatorprivate_major}*
%{_kde5_libdir}/libakregatorprivate.so.4*

#------------------------------------------------------------------------------

%libpackage calendarsupportcollectionpage 4.81.0

%define calendarsupport_major 5
%define libcalendarsupport %mklibname calendarsupport %{calendarsupport_major}

%package -n %{libcalendarsupport}
Summary:	KDE library
Group:		System/Libraries
Requires:	%{mklibname calendarsupportcollectionpage 4.81.0}

%description -n %{libcalendarsupport}
KDE library for korganizer-Mobile.

%files -n %{libcalendarsupport}
%{_kde5_libdir}/libcalendarsupport.so.%{calendarsupport_major}*
%{_kde5_libdir}/libcalendarsupport.so.4*

#-----------------------------------------------------------------------------
%define composereditorng_major 5
%define libcomposereditorng %mklibname composereditorng %{composereditorng_major}

%package -n %{libcomposereditorng}
Summary:	Library providing autospell checking
Group:		System/Libraries

%description -n %{libcomposereditorng}
This library provides autospell checking.

%files -n %{libcomposereditorng}
%{_kde5_libdir}/libcomposereditorng.so.%{composereditorng_major}*
%{_kde5_libdir}/libcomposereditorng.so.4*

#-----------------------------------------------------------------------------

%define eventviews_major 5
%define libeventviews %mklibname eventviews %{eventviews_major}

%package -n %{libeventviews}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libeventviews}
KDE library.

%files -n %{libeventviews}
%{_kde5_libdir}/libeventviews.so.%{eventviews_major}*
%{_kde5_libdir}/libeventviews.so.4*

#-----------------------------------------------------------------------------

%define followupreminder_major 5
%define libfollowupreminder %mklibname followupreminder %{followupreminder_major}

%package -n %{libfollowupreminder}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libfollowupreminder}
KDE library.

%files -n %{libfollowupreminder}
%{_kde5_libdir}/libfollowupreminder.so.%{followupreminder_major}*
%{_kde5_libdir}/libfollowupreminder.so.4*

#-----------------------------------------------------------------------------

%define grantleetheme_major 5
%define libgrantleetheme %mklibname grantleetheme %{grantleetheme_major}

%package -n %{libgrantleetheme}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libgrantleetheme}
KDE library.

%files -n %{libgrantleetheme}
%{_kde5_libdir}/libgrantleetheme.so.%{grantleetheme_major}*
%{_kde5_libdir}/libgrantleetheme.so.4*

#-----------------------------------------------------------------------------

%define grantleethemeeditor_major 5
%define libgrantleethemeeditor %mklibname grantleethemeeditor %{grantleethemeeditor_major}

%package -n %{libgrantleethemeeditor}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libgrantleethemeeditor}
KDE library.

%files -n %{libgrantleethemeeditor}
%{_kde5_libdir}/libgrantleethemeeditor.so.%{grantleethemeeditor_major}*
%{_kde5_libdir}/libgrantleethemeeditor.so.4*

#----------------------------------------------------------------------------

%define incidenceeditorsng_major 5
%define libincidenceeditorsng %mklibname incidenceeditorsng %{incidenceeditorsng_major}

%package -n %{libincidenceeditorsng}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{_lib}incidenceeditors4 < 2:4.5.68

%description -n %{libincidenceeditorsng}
KDE library.

%files -n %{libincidenceeditorsng}
%{_kde5_libdir}/libincidenceeditorsng.so.%{incidenceeditorsng_major}*
%{_kde5_libdir}/libincidenceeditorsng.so.4*

#-----------------------------------------------------------------------------

%define incidenceeditorsngmobile_major 5
%define libincidenceeditorsngmobile %mklibname incidenceeditorssngmobile %{incidenceeditorsngmobile_major}

%package -n %{libincidenceeditorsngmobile}
Summary:	KDEPIM Mobile Library
Group:		System/Libraries

%description -n %{libincidenceeditorsngmobile}
KDE PIM Mobile library.

%files -n %{libincidenceeditorsngmobile}
%{_kde5_libdir}/libincidenceeditorsngmobile.so.%{incidenceeditorsngmobile_major}*
%{_kde5_libdir}/libincidenceeditorsngmobile.so.4*

#-----------------------------------------------------------------------------

%define kaddressbookgrantlee_major 5
%define libkaddressbookgrantlee %mklibname kaddressbookgrantlee %{kaddressbookgrantlee_major}

%package -n %{libkaddressbookgrantlee}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkaddressbookgrantlee}
KDE library.

%files -n %{libkaddressbookgrantlee}
%{_kde5_libdir}/libkaddressbookgrantlee.so.%{kaddressbookgrantlee_major}*
%{_kde5_libdir}/libkaddressbookgrantlee.so.4*

#-----------------------------------------------------------------------------

%define kaddressbookprivate_major 5
%define libkaddressbookprivate %mklibname kaddressbookprivate %{kaddressbookprivate_major}

%package -n %{libkaddressbookprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkaddressbookprivate}
KDE library.

%files -n %{libkaddressbookprivate}
%{_kde5_libdir}/libkaddressbookprivate.so.%{kaddressbookprivate_major}*
%{_kde5_libdir}/libkaddressbookprivate.so.4*

#-----------------------------------------------------------------------------

%define kdepim_major 5
%define libkdepim %mklibname kdepim %{kdepim_major}

%package -n %{libkdepim}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkdepim}
KDE library.

%files -n %{libkdepim}
%{_kde5_libdir}/libkdepim.so.%{kdepim_major}*
%{_kde5_libdir}/libkdepim.so.4*

#-----------------------------------------------------------------------

%define kdgantt2_major 1
%define libkdgantt2 %mklibname kdgantt2 %{kdgantt2_major}

%package -n %{libkdgantt2}
Summary:       KDE4 library
Group:         System/Libraries

%description -n %{libkdgantt2}
KDE library.

%files -n %{libkdgantt2}
%{_kde5_libdir}/libkdgantt2.so.%{kdgantt2_major}*

#-----------------------------------------------------------------------------

%define kleo_major 5
%define libkleo %mklibname kleo %{kleo_major}

%package -n %{libkleo}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkleo}
KDE library.

%files -n %{libkleo}
%{_kde5_libdir}/libkleo.so.%{kleo_major}*
%{_kde5_libdir}/libkleo.so.4*

#-----------------------------------------------------------------------------

%define kmailprivate_major 5
%define libkmailprivate %mklibname kmailprivate %{kmailprivate_major}

%package -n %{libkmailprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkmailprivate}
KDE library.

%files -n %{libkmailprivate}
%{_kde5_libdir}/libkmailprivate.so.%{kmailprivate_major}*
%{_kde5_libdir}/libkmailprivate.so.4*

#-----------------------------------------------------------------------------

%define kmanagesieve_major 5
%define libkmanagesieve %mklibname kmanagesieve %{kmanagesieve_major}

%package -n %{libkmanagesieve}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkmanagesieve}
KDE library.

%files -n %{libkmanagesieve}
%{_kde5_libdir}/libkmanagesieve.so.%{kmanagesieve_major}*
%{_kde5_libdir}/libkmanagesieve.so.4*

#-----------------------------------------------------------------------------

%define knotesprivate_major 5
%define libknotesprivate %mklibname knotesprivate %{knotesprivate_major}

%package -n %{libknotesprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libknotesprivate}
KDE library.

%files -n %{libknotesprivate}
%{_kde5_libdir}/libknotesprivate.so.%{knotesprivate_major}*
%{_kde5_libdir}/libknotesprivate.so.4*

#-----------------------------------------------------------------------------

%define kontactprivate_major 5
%define libkontactprivate %mklibname kontactprivate %{kontactprivate_major}

%package -n %{libkontactprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkontactprivate}
KDE library.

%files -n %{libkontactprivate}
%{_kde5_libdir}/libkontactprivate.so.%{kontactprivate_major}*
%{_kde5_libdir}/libkontactprivate.so.4*

#-----------------------------------------------------------------------------

%define korganizer_core_major 5
%define libkorganizer_core %mklibname korganizer_core %{korganizer_core_major}

%package -n %{libkorganizer_core}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizer_core}
KDE library.

%files -n %{libkorganizer_core}
%{_kde5_libdir}/libkorganizer_core.so.%{korganizer_core_major}*
%{_kde5_libdir}/libkorganizer_core.so.4*

#-----------------------------------------------------------------------------

%define korganizer_interfaces_major 5
%define libkorganizer_interfaces %mklibname korganizer_interfaces %{korganizer_interfaces_major}

%package -n %{libkorganizer_interfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizer_interfaces}
KDE library.

%files -n %{libkorganizer_interfaces}
%{_kde5_libdir}/libkorganizer_interfaces.so.%{korganizer_interfaces_major}*
%{_kde5_libdir}/libkorganizer_interfaces.so.4*

#-----------------------------------------------------------------------------

%define korganizerprivate_major 5
%define libkorganizerprivate %mklibname korganizerprivate %{korganizerprivate_major}

%package -n %{libkorganizerprivate}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkorganizerprivate}
KDE library.

%files -n %{libkorganizerprivate}
%{_kde5_libdir}/libkorganizerprivate.so.%{korganizerprivate_major}*
%{_kde5_libdir}/libkorganizerprivate.so.4*

#-----------------------------------------------------------------------------

%define kpgp_major 5
%define libkpgp %mklibname kpgp %{kpgp_major}

%package -n %{libkpgp}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkpgp}
KDE library.

%files -n %{libkpgp}
%{_kde5_libdir}/libkpgp.so.%{kpgp_major}*
%{_kde5_libdir}/libkpgp.so.4*

#----------------------------------------------------------------------------

%define ksieve_major 5
%define libksieve %mklibname ksieve %{ksieve_major}

%package -n %{libksieve}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libksieve}
KDE library.

%files -n %{libksieve}
%{_kde5_libdir}/libksieve.so.%{ksieve_major}*
%{_kde5_libdir}/libksieve.so.4*

#-----------------------------------------------------------------------------

%define ksieveui_major 5
%define libksieveui %mklibname ksieveui %{ksieveui_major}

%package -n %{libksieveui}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libksieveui}
KDE library.

%files -n %{libksieveui}
%{_kde5_libdir}/libksieveui.so.%{ksieveui_major}*
%{_kde5_libdir}/libksieveui.so.4*

#-----------------------------------------------------------------------------

%define mailcommon_major 5
%define libmailcommon %mklibname mailcommon %{mailcommon_major}

%package -n %{libmailcommon}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libmailcommon}
KDE library.

%files -n %{libmailcommon}
%{_kde5_libdir}/libmailcommon.so.%{mailcommon_major}*
%{_kde5_libdir}/libmailcommon.so.4*

#-----------------------------------------------------------------------------

%define mailimporter_major 5
%define libmailimporter %mklibname mailimporter %{mailimporter_major}

%package -n %{libmailimporter}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libmailimporter}
KDE library.

%files -n %{libmailimporter}
%{_kde5_libdir}/libmailimporter.so.%{mailimporter_major}*
%{_kde5_libdir}/libmailimporter.so.4*

#-----------------------------------------------------------------------------

%define messagecore_major 5
%define libmessagecore %mklibname messagecore %{messagecore_major}

%package -n %{libmessagecore}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libmessagecore}
KDE library.

%files -n %{libmessagecore}
%{_kde5_libdir}/libmessagecore.so.%{messagecore_major}*
%{_kde5_libdir}/libmessagecore.so.4*

#-----------------------------------------------------------------------------

%define messagelist_major 5
%define libmessagelist %mklibname messagelist %{messagelist_major}

%package -n %{libmessagelist}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libmessagelist}
KDE library.

%files -n %{libmessagelist}
%{_kde5_libdir}/libmessagelist.so.%{messagelist_major}*
%{_kde5_libdir}/libmessagelist.so.4*

#-----------------------------------------------------------------------------

%define messageviewer_major 5
%define libmessageviewer %mklibname messageviewer %{messageviewer_major}

%package -n %{libmessageviewer}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libmessageviewer}
KDE library.

%files -n %{libmessageviewer}
%{_kde5_libdir}/libmessageviewer.so.%{messageviewer_major}*
%{_kde5_libdir}/libmessageviewer.so.4*

#-----------------------------------------------------------------------------

%define kdepimdbusinterfaces_major 4.81.0
%define libkdepimdbusinterfaces %mklibname kdepimdbusinterfaces %{kdepimdbusinterfaces_major}

%package -n %{libkdepimdbusinterfaces}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libkdepimdbusinterfaces}
KDE library.

%files -n %{libkdepimdbusinterfaces}
%{_kde5_libdir}/libkdepimdbusinterfaces.so.%{kdepimdbusinterfaces_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientcore_major 1
%define libkleopatraclientcore %mklibname kleopatraclientcore %{kleopatraclientcore_major}

%package -n %{libkleopatraclientcore}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientcore4 <= 2:4.5

%description -n %{libkleopatraclientcore}
KDE library.

%files -n %{libkleopatraclientcore}
%{_kde5_libdir}/libkleopatraclientcore.so.%{kleopatraclientcore_major}*

#-----------------------------------------------------------------------------

%define kleopatraclientgui_major 1
%define libkleopatraclientgui %mklibname kleopatraclientgui %{kleopatraclientgui_major}

%package -n %{libkleopatraclientgui}
Summary:	KDE library
Group:		System/Libraries
Obsoletes:	%{_lib}kleopatraclientgui4 <= 2:4.5

%description -n %{libkleopatraclientgui}
KDE library.

%files -n %{libkleopatraclientgui}
%{_kde5_libdir}/libkleopatraclientgui.so.%{kleopatraclientgui_major}*

#-----------------------------------------------------------------------------

%define messagecomposer_major 5
%define libmessagecomposer %mklibname messagecomposer %{messagecomposer_major}

%package -n %{libmessagecomposer}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libmessagecomposer}
KDE library.

%files -n %{libmessagecomposer}
%{_kde5_libdir}/libmessagecomposer.so.%{messagecomposer_major}*
%{_kde5_libdir}/libmessagecomposer.so.4*

#-----------------------------------------------------------------------------

%define noteshared_major 5
%define libnoteshared %mklibname noteshared %{noteshared_major}

%package -n %{libnoteshared}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libnoteshared}
KDE library.

%files -n %{libnoteshared}
%{_kde5_libdir}/libnoteshared.so.%{noteshared_major}*
%{_kde5_libdir}/libnoteshared.so.4*

#-----------------------------------------------------------------------------

%define pimcommon_major 5
%define libpimcommon %mklibname pimcommon %{pimcommon_major}

%package -n %{libpimcommon}
Summary:	Library to import/export PIM configuration
Group:		System/Libraries

%description -n %{libpimcommon}
This library provides the tool to import/export PIM configuration.

%files -n %{libpimcommon}
%{_kde5_libdir}/libpimcommon.so.%{pimcommon_major}*
%{_kde5_libdir}/libpimcommon.so.4*

#-----------------------------------------------------------------------------

%define sendlater_major 5
%define libsendlater %mklibname sendlater %{sendlater_major}

%package -n %{libsendlater}
Summary:	KDE PIM library
Group:		System/Libraries

%description -n %{libsendlater}
KDE PIM library.

%files -n %{libsendlater}
%{_kde5_libdir}/libsendlater.so.%{sendlater_major}*
%{_kde5_libdir}/libsendlater.so.4*

#-----------------------------------------------------------------------------

%define templateparser_major 5
%define libtemplateparser %mklibname templateparser %{templateparser_major}

%package -n %{libtemplateparser}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libtemplateparser}
KDE library.

%files -n %{libtemplateparser}
%{_kde5_libdir}/libtemplateparser.so.%{templateparser_major}*
%{_kde5_libdir}/libtemplateparser.so.4*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs-devel
Requires:	kdepimlibs-devel
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
Requires:	%{libkdepim} = %{EVRD}
Requires:	%{libkdepimdbusinterfaces} = %{EVRD}
Requires:	%{libkdgantt2} = %{EVRD}
Requires:	%{libkleo} = %{EVRD}
Requires:	%{libkleopatraclientcore} = %{EVRD}
Requires:	%{libkleopatraclientgui} = %{EVRD}
Requires:	%{libkmailprivate} = %{EVRD}
Requires:	%{libkmanagesieve} = %{EVRD}
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
Requires:	%{libpimsettingexporterprivate}  = %{EVRD}
Requires:	%{libsendlater} = %{EVRD}
Requires:	%{libtemplateparser} = %{EVRD}
%rename		kdepim4-devel

%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%{_kde5_libdir}/*.so

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}
%apply_patches
%cmake_kde5 -DKDEPIM_BUILD_MOBILE:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build

# akonadi_folderarchive_agent was removed, no need to keep desktop file
rm -f %{buildroot}%{_kde5_datadir}/akonadi/agents/folderarchiveagent.desktop

%find_lang %{name} --all-name --with-html

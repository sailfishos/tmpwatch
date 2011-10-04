Summary: A utility for removing files based on when they were last accessed
Name: tmpwatch
Version: 2.9.13
Release: 2
URL: https://fedorahosted.org/tmpwatch/
# https://fedorahosted.org/tmpwatch/attachment/wiki/TmpwatchDownloads/tmpwatch-%{version}?format=raw
Source0: %{name}-%{version}.tar.bz2
Source1: tmpwatch.daily
License: GPLv2
Group: System/Base
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: psmisc

%description
The tmpwatch utility recursively searches through specified
directories and removes files which have not been accessed in a
specified period of time.  Tmpwatch is normally used to clean up
directories which are used for temporarily holding files (for example,
/tmp).  Tmpwatch ignores symlinks, won't switch filesystems and only
removes empty directories and regular files.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make ROOT=%{buildroot} SBINDIR=%{_sbindir} MANDIR=%{_mandir} install

mkdir -p %{buildroot}/etc/cron.daily
cp %{SOURCE1} %{buildroot}/etc/cron.daily/tmpwatch
chmod +x %{buildroot}/etc/cron.daily/tmpwatch

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_sbindir}/tmpwatch
%doc %{_mandir}/man8/tmpwatch.8*
%config(noreplace) /etc/cron.daily/tmpwatch



Name: test1
Version: 9
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: test1
Source0: webapp.tar.gz
Source1: httpd.conf
Source2: bake-scripts.tar.gz
Requires: php-pecl-apc, httpd, php, cosmos-ca-chains
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)




%description
test1 built by the Magic Build Tool

%prep
%setup -q -T -D -n webapp -b 0

%build


%install

            mkdir -p %{buildroot}/usr/share/%{name}/public
            cp -r * %{buildroot}/usr/share/%{name}/
        
mkdir -p %{buildroot}/etc/httpd/conf.d
cp %{SOURCE1} %{buildroot}/etc/httpd/conf.d/%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/bake-scripts/test1
tar -C %{buildroot}%{_sysconfdir}/bake-scripts/test1 -xzf %{SOURCE2}

%pre


%preun


%post


%postun


%clean
rm -rf %{buildroot}

%files
%defattr(644, root, root, 755)
/usr/share/%{name}
%defattr(644, root, root, 755)
/etc/httpd/conf.d/%{name}.conf
%defattr(-, root, root, 755)
/etc/bake-scripts/test1



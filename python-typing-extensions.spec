%global srcname typing_extensions

Name:           python-typing-extensions
Version:        3.7.4
Release:        4%{?dist}
Summary:        Python Typing Extensions

License:        Python
URL:            https://pypi.org/project/typing-extensions/
Source0:        %{pypi_source}

BuildArch:      noarch


%description
Typing Extensions - Backported and Experimental Type Hints for Python

The typing module was added to the standard library in Python 3.5 on a
provisional basis and will no longer be provisional in Python 3.7.
However, this means users of Python 3.5 - 3.6 who are unable to upgrade will not
be able to take advantage of new types added to the typing module, such as
typing.Text or typing.Coroutine.

The typing_extensions module contains both backports of these changes as well as
experimental types that will eventually be added to the typing module, such as
Protocol.

Users of other Python versions should continue to install and use the typing
module from PyPi instead of using this one unless specifically writing code that
must be compatible with multiple Python versions or requires experimental types.

%package -n python3-typing-extensions
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-test
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-typing-extensions
Typing Extensions - Backported and Experimental Type Hints for Python

The typing module was added to the standard library in Python 3.5 on a
provisional basis and will no longer be provisional in Python 3.7.
However, this means users of Python 3.5 - 3.6 who are unable to upgrade will not
be able to take advantage of new types added to the typing module, such as
typing.Text or typing.Coroutine.

The typing_extensions module contains both backports of these changes as well as
experimental types that will eventually be added to the typing module, such as
Protocol.

Users of other Python versions should continue to install and use the typing
module from PyPi instead of using this one unless specifically writing code that
must be compatible with multiple Python versions or requires experimental types.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} src_py3/test_typing_extensions.py

%files -n python3-typing-extensions
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jonny Heggheim <hegjon@gmail.com> - 3.7.4-1
- Updated to 3.7.4

* Sun Mar 31 2019 Jonny Heggheim <hegjon@gmail.com> - 3.7.2-1
- Inital packaging

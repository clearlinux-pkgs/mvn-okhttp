#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-okhttp
Version  : 2.4.0
Release  : 2
URL      : https://github.com/square/okhttp/archive/parent-2.4.0.tar.gz
Source0  : https://github.com/square/okhttp/archive/parent-2.4.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/squareup/okhttp/parent/2.7.5/parent-2.7.5.pom
Source2  : https://repo.maven.apache.org/maven2/com/squareup/okhttp3/logging-interceptor/3.8.1/logging-interceptor-3.8.1.jar
Source3  : https://repo.maven.apache.org/maven2/com/squareup/okhttp3/logging-interceptor/3.8.1/logging-interceptor-3.8.1.pom
Source4  : https://repo.maven.apache.org/maven2/com/squareup/okhttp3/parent/3.8.1/parent-3.8.1.pom
Source5  : https://repo1.maven.org/maven2/com/squareup/okhttp/okhttp/2.4.0/okhttp-2.4.0.jar
Source6  : https://repo1.maven.org/maven2/com/squareup/okhttp/okhttp/2.4.0/okhttp-2.4.0.pom
Source7  : https://repo1.maven.org/maven2/com/squareup/okhttp/okhttp/2.7.5/okhttp-2.7.5.jar
Source8  : https://repo1.maven.org/maven2/com/squareup/okhttp/okhttp/2.7.5/okhttp-2.7.5.pom
Source9  : https://repo1.maven.org/maven2/com/squareup/okhttp3/okhttp/3.8.1/okhttp-3.8.1.jar
Source10  : https://repo1.maven.org/maven2/com/squareup/okhttp3/okhttp/3.8.1/okhttp-3.8.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-okhttp-data = %{version}-%{release}

%description
OkHttp
======
An HTTP & SPDY client for Android and Java applications. For more information see [the website][1] and [the wiki][2].

%package data
Summary: data components for the mvn-okhttp package.
Group: Data

%description data
data components for the mvn-okhttp package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/parent/2.7.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/parent/2.7.5/parent-2.7.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/logging-interceptor/3.8.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/logging-interceptor/3.8.1/logging-interceptor-3.8.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/logging-interceptor/3.8.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/logging-interceptor/3.8.1/logging-interceptor-3.8.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/parent/3.8.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/parent/3.8.1/parent-3.8.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.4.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.4.0/okhttp-2.4.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.4.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.4.0/okhttp-2.4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.7.5
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.7.5/okhttp-2.7.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.7.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.7.5/okhttp-2.7.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/okhttp/3.8.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/okhttp/3.8.1/okhttp-3.8.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/okhttp/3.8.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/squareup/okhttp3/okhttp/3.8.1/okhttp-3.8.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.4.0/okhttp-2.4.0.jar
/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.4.0/okhttp-2.4.0.pom
/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.7.5/okhttp-2.7.5.jar
/usr/share/java/.m2/repository/com/squareup/okhttp/okhttp/2.7.5/okhttp-2.7.5.pom
/usr/share/java/.m2/repository/com/squareup/okhttp/parent/2.7.5/parent-2.7.5.pom
/usr/share/java/.m2/repository/com/squareup/okhttp3/logging-interceptor/3.8.1/logging-interceptor-3.8.1.jar
/usr/share/java/.m2/repository/com/squareup/okhttp3/logging-interceptor/3.8.1/logging-interceptor-3.8.1.pom
/usr/share/java/.m2/repository/com/squareup/okhttp3/okhttp/3.8.1/okhttp-3.8.1.jar
/usr/share/java/.m2/repository/com/squareup/okhttp3/okhttp/3.8.1/okhttp-3.8.1.pom
/usr/share/java/.m2/repository/com/squareup/okhttp3/parent/3.8.1/parent-3.8.1.pom

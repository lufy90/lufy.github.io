---
layout: post
title: Notes of Running Ltp
---

### Installation
1. Install needed packages:
`
yum install -y \
  numactl numactl-devel numactl-libs numad \
  gcc kernel-devel \
  libaio libaio-devel libcap-devel libattr-devel keyutils-libs-devel \
  expect rsh rsh-server telnet telnet-server mkisofs nfs-utils
`

Tip: on aarch64 OS currently:
`
yum install -y libtirpc-devel
`

2. Configure, make and make install
`
./configure --prefix=/opt/ltp20xxxxxx
make && make install
`

Tip: on aarch64 OS currently(isoft 5.0 and 5.1), only **ltp-full-20180118** could run smothly, and the configure options are needed.
`
./configure CPPFLAGS=-I/usr/include/tirpc LDFLAGS=-ltirpc --prefix=/opt/ltp20180118
`

### Run test:
1. Evironment settings:
`
\#disable firewalld
systemctl disable firewalld

\#enable services
systemctl enable rsh.socket
systemctl enable rlogin.socket
systemctl enable telnet.socket
systemctl enable nfs

\#disable selinux
sed -i  "s/SELINUX=enforcing/SELINUX=disabled/" /etc/selinux/config

echo localhost >> /root/.rhosts
echo <eth0_ip> >> /root/.rhosts
echo rlogin >> /etc/securetty
echo rsh >> /etc/securetty
echo rexec >> /etc/securetty

\#then rebooting to make the settings available
reboot
`

2. Run test command
...

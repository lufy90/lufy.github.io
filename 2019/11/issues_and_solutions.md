
Issue:
auto configure with auto conf, encounter with: 
`configure.ac:65: error: possibly undefined macro: AC_ENABLE_SHARED`

Solution:
`dnf install libtool -y`


Issue:
In linux-pam-1.3.1, `make` after `configure`, encounter with:
`No rule to make target 'access.conf.5', needed by 'all-am'`

Solution:


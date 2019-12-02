## ltp research

# Why do this
SW64 OS outline test need to test kernel interfaces about modules, etc.

# 
After search key words, LTP contains all APIs that GJB7723-2012 A.1.2 demands 
in dir `testcases/kernel/device-drivers/`.


# Issues and solutions
In `testcases/kernel/device-drivers/nls`, execute `make`, get `fatal error: 
linux/autoconf.h: No such file or directory`


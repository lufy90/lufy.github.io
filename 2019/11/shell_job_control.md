## job control in bash

```
jobs		# lists the active jobs
bg [*jobsepc*]	# Resume each suspended job *jobspec* in the background
fg [*jobspec*]	# Resume the job *jobspec* in the foreground and make it the current job
kill		# Send a signal to process
wait		# Wait until the child process specified by each PID
disown		# 
suspend
```

E.g.
Could stop a process by `^Z`, after stoped, `ps T` would give the `T` status of the job:
```
lufei@lufei-pc:~$ sleep 60
^Z
[1]+  Stopped                 sleep 60
lufei@lufei-pc:~$ ps T
  PID TTY      STAT   TIME COMMAND
 2853 pts/1    Ss     0:00 bash
 4024 pts/1    T      0:00 sleep 60
 4025 pts/1    R+     0:00 ps T
lufei@lufei-pc:~$ jobs
[1]+  Stopped                 sleep 60
lufei@lufei-pc:~$ bg 1
[1]+ sleep 60 &
lufei@lufei-pc:~$ fg 1
sleep 60
```


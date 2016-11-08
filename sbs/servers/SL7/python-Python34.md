- ``sudo yum search python3 | grep language | less``  # **search** for ``python3`` and ``language``

```
python3.x86_64 : Version 3 of the Python programming language aka Python 3000
python3-Cython.x86_64 : A language for writing Python extension modules
python34.x86_64 : Version 3 of the Python programming language aka Python 3000
python34-Cython.x86_64 : A language for writing Python 3.4 extension modules
```


- ``sudo yum info python3.x86_64``  # **info** about ``python3.x86_64``

```
Loaded plugins: priorities
Available Packages
Name        : python3
Arch        : x86_64
Version     : 3.4.2
Release     : 3.1.geos
Size        : 47 k
Repo        : devolved-uoe
Summary     : Version 3 of the Python programming language aka Python 3000
URL         : http://www.python.org/
Licence     : Python
Description : Python 3 is a new version of the language that is incompatible with the 2.x
            : line of releases. The language is mostly the same, but many details,
            : especially how built-in objects like dictionaries and strings work, have
            : changed considerably, and a lot of deprecated features have finally been
            : removed.
```


- ``sudo yum info python34.x86_64``  # **info** about ``python34.x86_64``

```
Loaded plugins: priorities
Available Packages
Name        : python34
Arch        : x86_64
Version     : 3.4.5
Release     : 2.el7
Size        : 50 k
Repo        : local-epel/x86_64
Summary     : Version 3 of the Python programming language aka Python 3000
URL         : http://www.python.org/
Licence     : Python
Description : Python 3 is a new version of the language that is incompatible with the 2.x
            : line of releases. The language is mostly the same, but many details,
            : especially how built-in objects like dictionaries and strings work, have
            : changed considerably, and a lot of deprecated features have finally been
            : removed.
```


- ``sudo yum install python34.x86_64``  # **install** **``python34.x86_64``**

```
Loaded plugins: priorities
devolved-uoe                                                         | 2.9 kB  00:00:00     
devolved-world                                                       | 2.9 kB  00:00:00     
inf-lcfg                                                             | 2.6 kB  00:00:00     
inf-uoe                                                              | 2.5 kB  00:00:00     
inf-world                                                            | 2.6 kB  00:00:00     
local-epel                                                           | 3.0 kB  00:00:00     
local-epel-src                                                       | 3.5 kB  00:00:00     
local-sl                                                             | 3.7 kB  00:00:00     
local-sl-security                                                    | 2.9 kB  00:00:00     
local-sl-source                                                      | 2.7 kB  00:00:00     
(1/4): inf-lcfg/primary_db                                           | 620 kB  00:00:00     
(2/4): devolved-uoe/primary_db                                       | 990 kB  00:00:00     
(3/4): inf-world/primary_db                                          | 3.8 MB  00:00:01     
(4/4): local-epel/x86_64/primary_db                                  |  15 MB  00:00:02     
Resolving Dependencies
--> Running transaction check
---> Package python34.x86_64 0:3.4.5-2.el7 will be installed
--> Processing Dependency: python34-libs(x86-64) = 3.4.5-2.el7 for package: python34-3.4.5-2.el7.x86_64
--> Processing Dependency: libpython3.4m.so.1.0()(64bit) for package: python34-3.4.5-2.el7.x86_64
--> Running transaction check
---> Package python34-libs.x86_64 0:3.4.5-2.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

============================================================================================
 Package                 Arch             Version                Repository            Size
============================================================================================
Installing:
 python34                x86_64           3.4.5-2.el7            local-epel            50 k
Installing for dependencies:
 python34-libs           x86_64           3.4.5-2.el7            local-epel           6.7 M

Transaction Summary
============================================================================================
Install  1 Package (+1 Dependent package)

Total download size: 6.8 M
Installed size: 27 M
Is this ok [y/d/N]: y
Downloading packages:
(1/2): python34-3.4.5-2.el7.x86_64.rpm                               |  50 kB  00:00:00     
(2/2): python34-libs-3.4.5-2.el7.x86_64.rpm                          | 6.7 MB  00:00:00     
--------------------------------------------------------------------------------------------
Total                                                       8.8 MB/s | 6.8 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
  Installing : python34-libs-3.4.5-2.el7.x86_64                                         1/2 
  Installing : python34-3.4.5-2.el7.x86_64                                              2/2 
  Verifying  : python34-libs-3.4.5-2.el7.x86_64                                         1/2 
  Verifying  : python34-3.4.5-2.el7.x86_64                                              2/2 

Installed:
  python34.x86_64 0:3.4.5-2.el7                                                             

Dependency Installed:
  python34-libs.x86_64 0:3.4.5-2.el7                                                        

Complete!
```


- ``python3``  # **run** Python 3.4 in REPL mode

```
Python 3.4.5 (default, Oct 20 2016, 22:54:51) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

# apt-who-needs

Determines which installed packages require the given package. Save the script somewhere in your path, e.g. in /usr/local/bin and give it executable rights. The script requires root rights.

get it :
```
apt install python3 apt-rdepends
wget  https://github.com/ecxod/apt-who-needs/releases/download/1.0.0/apt-who-needs.deb
sudo dpkg -i apt-who-needs.deb
or
sudo apt install ./apt-who-needs.deb
```

and run it like this: 

```
sudo apt-who-needs packagename
```

>root@host:~# apt-who-needs apt  
>Reading package lists... Done  
>Building dependency tree... Done  
>Reading state information... Done  
>apt-file is installed and requires apt  
>apt-listbugs is installed and requires apt  
>apt-listchanges is installed and requires apt  
>apt-transport-https is installed and requires apt  
>apt-utils is installed and requires apt  
>python3-reportbug is installed and requires apt  
>reportbug is installed and requires apt  


have fun.

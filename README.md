![1733279476617](images/readme/1733279476617.png)

**PeInfo is Information gathering for port scanner and Flood requst or DDoS Attack with TCP and UDP created by Putra Budianto**

*I recommended to use Unix Like Operating System like Linux or macOS because this using bash, you can use Windows operating system, but you must have git application and running this code with git bash*

**How to install?**

```
cd peinfo
python3 -m venv ./
cd bin && source ./activate
cd ..
pip install -r requirements.txt
chmod +x peinfo.py
```

**Example for execution DDoS attack for TCP Method**

`./pinfo.py -tC [target host] -p [optional] -t [optional]`

1. `-tC` TCP Method
3. `-p` Port of target, default (80)
4. `-t` Thread Count, default (10)
5. `[target host]` Target you want to attack

**Example for execution DDoS attack for UDP Method**

`./pinfo.py -uD [target host] -p [optional] -t [optional]`

1. `-uD` UDP Method
2. `-p` Port of target, default (80)
3. `-t` Thread Count, default (10)
4. `target.com` Target you want to attack

We hope you can contribute to this project to make it even better. Thanks

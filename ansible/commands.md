
###
```shell
ansible all -m setup
```

###
```shell
ansible mysql -a "/bin/echo hello"
```

###
```shell
ansible mysql -m copy -a "src=/etc/hosts dest=/tmp/hosts"
```

### 
```shell
ansible mysql -m yum -a "name=acme state=present"
```

### 
```shell
ansible web -m service -a "name=httpd state=started"
```

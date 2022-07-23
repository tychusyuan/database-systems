
###
```shell
ansible all -m setup
```

###
```shell
ansible mysql -a "/bin/echo hello"
```

```shell
ansible -i hosts all -m shell -u root -a "init 0"
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
### 
```shell
ansible -i iplist all -m shell -u root -a "cat /home/work/opbin/falcon_redis/conf/redisConf.yaml | grep ${product_name}"
```

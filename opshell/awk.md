```shell
awk '{k=0; for (i=1;i<=NF;i++){
            if ($i=="ABC"){print $(i-2); k++}
           } 
           if(k==0){print "No ABC in line",NR}
     }'
```

ip_port='10.0.2.100:3306'

part_1=$(echo $ip_port | awk -F'[.:]' '{print $1}')
t_1=$(echo "obase=2;${part_1}"|bc |awk '{printf("%04d\n",$0)}')

part_2=$(echo $ip_port | awk -F'[.:]' '{print $2}')
t_2=$(echo "obase=2;${part_2}"|bc |awk '{printf("%08d\n",$0)}')

part_3=$(echo $ip_port | awk -F'[.:]' '{print $3}')
t_3=$(echo "obase=2;${part_3}"|bc |awk '{printf("%08d\n",$0)}')

part_4=$(echo $ip_port | awk -F'[.:]' '{print $4}')
t_4=$(echo "obase=2;${part_4}"|bc |awk '{printf("%08d\n",$0)}')

part_5=$(echo $ip_port | awk -F'[.:]' '{print $5}')
t_5=$(echo "obase=2;${part_5}"|bc |awk '{printf("%012d\n",$0)}')

echo "obase=10;ibase=2;$t_2$t_3$t_4$t_5"|bc

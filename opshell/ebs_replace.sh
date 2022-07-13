gp2_dir='/home/work'
blk_name='/dev/nvme3n1'
old_dir='/root/work_old'
new_dir='/root/work'
mysql_user=''
mysql_pwd=''
str_port='--port='
str_base='--basedir='
mysql_port=0
mysql_base=''

function getMysqlInstance(){
	arr=($1)
	for s in "${arr[@]}";
	do
	        if [[ $s =~ $str_port ]]
	        then
	                mysql_port=$(echo $s | awk -F'=' '{print $2}')
	        fi
	        if [[ $s =~ $str_base ]]
	        then
	                mysql_base=$(echo $s | awk -F'=' '{print $2}')
	        fi
	done
}

function getMysqlProcesslist(){
	sql_processlist="select count(1) from information_schema.processlist where USER not in ('autopilot','orche_cli','dm_source','system user','mymon');"
	echo "$1/bin/mysql -u$3 -p$4 -h 127.0.0.1 -P $2 -N"
	num_processlist=$(echo $sql_processlist | $1/bin/mysql -u$3 -p$4 -h 127.0.0.1 -P $2 -N)
	if [ $num_processlist -gt 0 ]
	then
		echo $num_processlist
	        echo $1 $2 "mysql processlist count is " $num_processlist
	        return 1
	else
		return 0
	fi
}

function stopMysqlInstance(){
	echo "$1/bin/mysqladmin shutdown -u$3 -p$4 -h 127.0.0.1 -P $2"
	$1/bin/mysqladmin shutdown -u$3 -p$4 -h 127.0.0.1 -P $2
}

function stopService(){
	god stop containerpilot
	killall filebeat
	swapoff -a
}

function startService(){
        god start containerpilot
        swapon -a
}

function startPartition(){
echo "g
w
" | fdisk $1
}

arr_ps=$(ps aux|grep 'mysqld ' |grep -v grep)
for str_ps in "${arr_ps[@]}";
do
	getMysqlInstance "${str_ps[*]}"
	if [ $mysql_port -gt 0 ]
	then
		getMysqlProcesslist $mysql_base $mysql_port $mysql_user $mysql_pwd
		if [ $? -gt 0 ]
		then
			echo "mysql processlist exit"
			exit
		fi
		stopMysqlInstance $mysql_base $mysql_port $mysql_user $mysql_pwd	
	fi
done
stopService

startPartition $blk_name

mkfs.ext4 $blk_name

blk_id=$(blkid $blk_name | awk '{print $2}' | awk -F '=' '{print $2}' | tr -d '"')

no_fstab=$(cat -n /etc/fstab | grep "$gp2_dir " | awk '{print $1}')

sed -i "12c UUID=${blk_id} /home/work ext4 defaults,noatime,nofail 0 0" /etc/fstab

mkdir $new_dir

mount $blk_name $new_dir

blk_old=$(df -lh| grep '/home/work' | awk '{print $1}')

umount $blk_old

mkdir $old_dir

mount $blk_old $old_dir

cp -avx "$old_dir/." "$new_dir/"

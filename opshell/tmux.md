# tmux

## 新建会话
```shell
tmux
```
### 命名会话
```shell
tmux new -s <session-name>
```
### 分离会话
```shell
tmux detach
```
### 查看当前所有的 Tmux 会话
```shell
tmux ls
```
## 接入会话
### 使用会话编号
```shell
tmux attach -t 0
```
### 使用会话名称
```shell
tmux attach -t <session-name>
```
## 切换会话
### 使用会话编号
```shell
tmux switch -t 0
```
### 使用会话名称
```shell
tmux switch -t <session-name>
```
## 杀死会话
### 使用会话编号
```shell
tmux kill-session -t 0
```
### 使用会话名称
```shell
tmux kill-session -t <session-name>
```
### 重命名会话
```shell
tmux rename-session -t 0 <new-name>
```

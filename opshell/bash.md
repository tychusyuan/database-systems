# Bash

### ping with date
```shell
ping host | while read pong; do echo "$(date): $pong"; done
```

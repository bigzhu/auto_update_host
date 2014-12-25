auto_update_host
================

自动更新 host

由于公司使用的是拨号的 pppoe, 外网 ip 随时在变, git 服务器又放在公司的 server 上

一旦改变了, 我们不知道外网 ip, 就没法使用了

开发一个程序取外网 ip, 发送到阿里云上, 修改其 hosts

## 文件说明

* receive_ip.py 服务器端,部署在外网服务器上, 用于接收内网发来的 ip, 写入 highwe.net 的 hosts; 并需要时候返回 ip 给无知的客户端
* send_ip.py 部署在192.168.1.8, 重新拨号导致 ip 变动时候,实时将 ip 告诉 highwe.net
* save_local.py 个人使用的, 从 highwe.net 取到 ip, 并写入 hosts.需要 sudo 运行

## 如何使用
个人使用只需要以 sudo 方式来执行 auto_update_host.sh 就可以了, 因为需要写入 /etc/hosts 所以需要 root 权限

    sudo auto_update_host.sh

每 5s 会自动同步一次

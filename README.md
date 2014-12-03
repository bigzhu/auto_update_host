auto_update_host
================

自动更新 host

由于公司使用的是拨号的 pppoe, 外网 ip 随时在变, git 服务器又放在公司的 server 上

一旦改变了, 我们不知道外网 ip, 就没法使用了

开发一个程序取外网 ip, 发送到阿里云上, 修改其 hosts

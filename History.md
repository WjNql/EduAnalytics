# 此处存储大致过程
## 25.2.4
### linux命令
创建 nql -> EduAnalytics (adduser, mkdir, touch, ls -a, sudo su, exit, mv, sudo chown -R nieqianlong:nieqianlong /EduAnalytics, nvidia-smi, nvcc-v)
linux命令问题不大
主要是创建了一个用户
创建用户命令：adduser
其次是为该用户添加到sudoers
- 首先要切换到root权限 su sudo
- 查看/etc/sudoers文件权限 ls -l /etc/sudoers
- 修改可写权限 chmod u+w /etc/sudoers
- 编辑用户权限 vim/etc/sudoers
- 还原只读权限 chmod 440 /etc/sudoers
- 切换回普通用户 su [用户名]
将原本其他的文件放到新用户文件夹下，发生不可读写问题
现在文件夹下使用ll命令查看文件所属用户
更改为自己 sudo chown -R [用户名]:[用户名] 文件夹/文件
### git命令
连接github仓库 EduAnalytics (git init, git add *, git commit -m "first commit", )
创建仓库 git init 
添加文件 git add *
确认文件 git commit -m "注释"
添加远程 git remote add origin (ssh链接)
推送文件 git push origin master (就是这里有坑，因为github已经改master为main了，所以会多一个分支出来，想改掉可不简单)
(如果创建origin时有冲突可以删除原先的origin git remote rm origin)
到这里成果完成
但是为了改成main要做以下事情
- 先把git默认的分支从master改为 main git branch -m master main
- 查看分支情况 git branch -a
- 删除master分支 git push origin --delete master
- 进入main分支 git checkout main
- 强行合并远程main和本地main git pull origin main --allow-unrelated-histories
以后为了少点麻烦还是从一开始创建仓库时就改成main吧
- 初始化时修改 git init -b main
- 初始化后修改 git branch -m master main
- 全局修改 git config --global init.defaultBranch main
### conda命令
开放conda权限
# 假设 Conda 安装在 /home/ubuntu/anaconda3
sudo chmod -R 755 /home/ubuntu/anaconda3  # 开放读和执行权限
创建共享组
sudo groupadd shared_group  # 创建共享组
sudo usermod -aG shared_group ubuntu
sudo usermod -aG shared_group nieqianlong
sudo chgrp -R shared_group /home/ubuntu/anaconda3  # 修改目录所属组
sudo chmod -R 775 /home/ubuntu/anaconda3  # 组用户可读写执行
在 nieqianlong 用户的 ~/.bashrc 中添加：
export PATH="/home/ubuntu/anaconda3/bin:$PATH"
刷新环境 source ~/.bashrc
# 在 ~/.bashrc 或 /etc/profile 中添加
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
conda env list

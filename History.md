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
- 在 ~/.bashrc 或 /etc/profile 中添加
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
开放conda权限
- 假设 Conda 安装在 /home/ubuntu/anaconda3
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
conda env list
- 初始化 Conda 到当前 Shell
conda init bash
source ~/.bashrc
conda create -n edu_analytics python=3.9
conda activate edu_analytics

## 25.2.5
### 使用命令
pip install pandas numpy matplotlib jupyterlab jupyter
<!-- jupyter lab --generate-config (jupyter生成配置文件) -->
jupyter notebook --generate-config
jupyter notebook password
conda install ipykernel
python -m ipykernel install --user --name edu_analytics --display-name "Edu_Analytics"
touch data_cleaner.py
pip install pyarrow
touch run_pipeline.sh
touch basic_analysis.py
mkdir -p data/{raw,processed} src reports/figures
touch data_generation.py
touch .gitignore
git add .gitignore
python data_generation.py
git commit -m "Add .gitignore to ignore hidden files"
chmod +x run_pipeline.sh
./run_pipeline.sh
python basic_analysis.py
---
./run_pipeline.sh
---
touch knowledge_model.py
使用 Git reset 命令来取消上一次提交：
git reset HEAD~1

---

## 25.2.7
### 安装docker
#### 1.1 卸载旧版本（如存在）
sudo apt-get remove docker docker-engine docker.io containerd runc
#### 1.2 安装依赖工具
sudo apt-get update
- 小插曲
>检查和清理 /etc/apt/sources.list 文件
>打开 /etc/apt/sources.list 文件：
>sudo nano /etc/apt/sources.list
>检查文件内容，删除重复的条目。确保每个软件源只出现一次。

sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
作用：
ca-certificates：SSL证书支持
curl：网络传输工具
gnupg：加密密钥管理
lsb-release：系统版本信息工具
#### 1.3 添加Docker官方GPG密钥
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
解释：
创建密钥存储目录
下载Docker官方加密密钥并转换为apt可识别的格式
#### 1.4 设置软件仓库源
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

参数解析：
arch=$(dpkg --print-architecture)：自动获取系统架构（x86_64/arm等）
signed-by：指定密钥验证路径
stable：使用稳定版仓库

#### 1.5 安装Docker引擎

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

组件说明：
docker-ce：社区版核心
docker-ce-cli：命令行工具
containerd.io：容器运行时
docker-compose-plugin：编排工具
（小插曲）
1. 清理现有配置
sudo rm -f /etc/apt/sources.list.d/docker.list
sudo rm -f /etc/apt/keyrings/docker.gpg
2. 重建Docker源配置（国内优化版）
使用中科大镜像源替代官方源
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

添加镜像源
sudo add-apt-repository \
   "deb [arch=$(dpkg --print-architecture)] \
   https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

添加GPG密钥
curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker.gpg

3. 验证发行版代号
确保返回结果与仓库支持版本一致
lsb_release -cs  # 应该返回"focal"

4. 手动检查仓库结构
验证仓库路径是否存在
curl -I https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/dists/focal/stable/
应返回HTTP 200状态码

5. 重新安装Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

6. 验证成功安装
sudo docker run --rm hello-world
应看到Docker成功运行测试容器
- 小插曲
创建/修改Docker配置
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://ung2thfc.mirror.aliyuncs.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ],
  "dns": ["8.8.8.8", "114.114.114.114"]
}
EOF

重启服务生效
sudo systemctl daemon-reload
sudo systemctl restart docker
验证加速器配置
查看生效配置
sudo docker info | grep -A 1 Mirrors
 应看到类似输出：
  Registry Mirrors:
   https://ung2thfc.mirror.aliyuncs.com/
再次尝试运行测试
sudo docker run --rm hello-world

 sudo chmod a+w /etc/resolv.conf
 sudo chmod 444 /etc/resolv.conf

dig @114.114.114.114 registry-1.docker.io

199.193.116.105    registry-1.docker.io

sudo vim /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://ueo0uggy.mirror.aliyuncs.com",
    "https://docker.m.daocloud.io",
    "https://cf-workers-docker-io-apl.pages.dev",

  ]
}

{
  "registry-mirrors":[
    "https://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://ueo0uggy.mirror.aliyuncs.com",
    "https://docker.m.daocloud.io",
    "https://cf-workers-docker-io-apl.pages.dev"
  ],
  "dns": ["8.8.8.8", "114.114.114.114"]
}

## 25.2.9
conda config --set auto_activate_base False
sudo docker run --rm hello-world(莫名其妙docker就好了)
### Neo4j容器部署
1. 创建专用目录
mkdir -p ~/neo4j/{data,import,logs}
2. 运行Neo4j容器（5.12版本）
sudo docker run -d \
    --name edu_kg \
    -p 7474:7474 \
    -p 7687:7687 \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/import:/import \
    -v $HOME/neo4j/logs:/logs \
    -e NEO4J_AUTH=neo4j/YourSecurePassword \
    -e NEO4JLABS_PLUGINS='["apoc"]' \
    neo4j:5.12

3. 查看运行状态
sudo docker ps | grep edu_kg
sudo docker exec -it edu_kg cypher-shell -u neo4j -p YourSecurePassword
> MATCH (n) RETURN n LIMIT 1;
:quit
端口连通性检查：
curl -v telnet://localhost:7474  # 应返回Connected
netstat -tuln | grep '7474\|7687'
手动修改：
访问地址：http://<您的服务器IP>:7474
在Cypher输入框执行
:server change-password
pip install py2neo==2021.2.4

## 25.2.10
touch model.py
创建知识点数据文件
touch data/raw/math_concepts.csv
创建题目关联文件 
touch data/raw/question_relations.csv

touch import_kg.py
// 创建全文索引加速搜索
CREATE FULLTEXT INDEX conceptSearch FOR (n:Concept) ON EACH [n.name, n.subject]
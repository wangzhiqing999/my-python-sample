## 发布 python 项目到 Docker 上.



### 生成Docker镜像

```
sudo docker build -t demo:v1 .

```


注意：
如果生成镜像的时候，运行到 pip install 的时候，过于耗时的话。

可尝试修改，在后面追加
-i https://pypi.tuna.tsinghua.edu.cn/simple
或者
-i https://mirrors.aliyun.com/pypi/simple/
来提升下载速度.



### 运行Docker容器

```
sudo docker run --rm demo:v1

```


### 加载数据卷

```
sudo docker run --rm -v $(pwd)/logs:/logs demo:v1

```



# 导入numpy验证docker是否根据requirements文件安装好了依赖
import numpy as np
import os



def save_log_file():
    if not os.path.exists('../logs'):
        os.makedirs('../logs', exist_ok=True)

    with open('../logs/docker.log', 'w', encoding='utf-8') as f:
        # 将文本信息， 写入到文件当中去.
        f.write('测试写入日志内容\n')
    # 关闭文件.
    f.close()


if __name__ == '__main__':
    # 在logs目录下创建个名为docker.log的文件，验证容器和宿主机是否能进行数据同步
    save_log_file()

    print("hello docker")

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("加法:", a + b)
    print("减法:", a - b)
    print("乘法:", a * b)
    print("除法:", a / b)
    print()



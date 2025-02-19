# os 模块是 Python 提供的一个标准库模块，它提供了与操作系统进行交互的功能，
# 包括文件和目录操作、进程管理、环境变量访问等。借助 os，
# 可以轻松实现文件路径的操作、创建目录、删除文件等操作，甚至可以通过它执行 shell 命令。

# 要使用 os 模块，首先需要将其导入



import os


# 获取当前工作目录
current_directory = os.getcwd()
print("当前工作目录是:", current_directory)



# 创建一个名为 'new_folder' 的目录
if not os.path.exists('new_folder'):
    os.mkdir('new_folder')
    print("目录 'new_folder' 已创建")
else:
    print("目录 'new_folder' 已存在")



# 删除目录 'new_folder'
if os.path.exists('new_folder'):
    os.rmdir('new_folder')
    print("目录 'new_folder' 已删除")
else:
    print("目录 'new_folder' 不存在")


# 列出当前工作目录下的所有文件和目录
files = os.listdir('.')
print("当前目录中的文件和目录有:", files)




# 判断路径类型
path = 'test_os.py'

if os.path.exists(path):
    if os.path.isdir(path):
        print(f"{path} 是一个目录")
    elif os.path.isfile(path):
        print(f"{path} 是一个文件")
else:
    print(f"{path} 路径不存在")



# 获取文件 'example.txt' 的大小
file_path = 'test_os.py'

if os.path.exists(file_path) and os.path.isfile(file_path):
    file_size = os.path.getsize(file_path)
    print(f"{file_path} 的文件大小是 {file_size} 字节")
else:
    print(f"{file_path} 文件不存在")



# 执行一个简单的系统命令
os.system('echo Hello, world!')



# 切换到上一级目录
os.chdir('..')
print("当前工作目录是:", os.getcwd())



# 获取一个环境变量
path_env = os.environ.get('PATH')
print("系统的 PATH 环境变量是:", path_env)



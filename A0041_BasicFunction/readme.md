## 2023-06-05 追加


没有修改的具体的内容. 主要是用这个目录，来测试 使用 VS Code  配置 flake8 和 yapf


先安装
pip install flake8
pip install yapf


VS Code 中， 先安装 Python 的插件.
然后，Windows文件资源管理器中， 选择 A0041_BasicFunction 目录，“通过 Code 打开”


配置flake8和yapf并关闭pylint工具。
在 Settings.json 中输入以下内容：

{
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "yapf",
    "python.linting.flake8Args": ["--max-line-length=248"],
    "python.linting.pylintEnabled": false
}


在VS Code中，按下快捷键 Alt+Shift+F 即可自动格式化代码。

import os
import shutil


def delete_file(file_path):
    if os.path.exists(file_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(file_path)
    else:
        print('删除文件不存在:%s' % file_path)  # 则返回文件不存在


def deletes_file(file_path):
    """删除一个非空目录"""
    if os.path.exists(file_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        shutil.rmtree(file_path)
        print(file_path, '文件删除成功')
    else:
        print('文件不存在请忽略信息:%s' % file_path)  # 则返回文件不存在

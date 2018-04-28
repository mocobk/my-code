import paramiko
import sys
import subprocess
import os
import threading
import time
from flask import Response, Flask
from globalhotkeys import GlobalHotKeys


def progressbar(cur, total):
    sys.stdout.write(' ' * 80 + '\r')
    sys.stdout.flush()
    sys.stdout.write('正在下载...\t%sM/%sM\r' % (round(cur / 1048576, 1), round(total / 1048576, 1)))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')


def screenshot(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password, timeout=10)

    stdin, stdout, stderr = ssh.exec_command('pwd')
    remote_dir = stdout.read().strip().decode('utf-8')
    screenshot_time = time.strftime('%Y-%m-%d_%H_%M_%S')
    command = 'cat /dev/fb0 > ~/fb_data.raw'
    ssh.exec_command(command)

    trans = ssh.get_transport()  # 从ssh连接中获取transport对象
    sftp = paramiko.SFTPClient.from_transport(trans)
    # sftp.get('%s/Documents/ios_packages.zip' % remote_dir, 'fb_data.raw', callback=progressbar)
    sftp.get('%s/fb_data.raw' % remote_dir, 'fb_data.raw', callback=progressbar)
    command = 'rm -rf %s/fb_data.raw' % remote_dir
    ssh.exec_command(command)
    ssh.close()

    # windows下转码，并打开截图
    screenshot_name = screenshot_time + '.png'
    cmd = 'ffmpeg -loglevel quiet -vcodec rawvideo -f rawvideo -pix_fmt rgb565 -s 800X600 -i fb_data.raw -f image2 ' \
          '-vcodec png %s' % screenshot_name
    subprocess.Popen(cmd, shell=True).wait()
    cur_path = os.getcwd()
    print(os.path.join(cur_path, screenshot_name))
    subprocess.Popen('start %s' % screenshot_name, shell=True)
    return screenshot_name


def run_screenshot():
    return screenshot('172.16.7.83', 22, 'tests', 'mpr123')


@GlobalHotKeys.register(GlobalHotKeys.VK_F1, GlobalHotKeys.MOD_SHIFT)
def hot_key_screenshot():
    run_screenshot()


app = Flask(__name__)


@app.route('/screenshot')
def web_screenshot():
    screenshot_name = run_screenshot()
    image = open(screenshot_name, mode='rb')
    return Response(image, mimetype='image/jpeg')


def main():
    print('请按Shift + F1 开始截图')
    thread = threading.Thread(target=app.run, args=('0.0.0.0', '5000'))
    thread.start()
    GlobalHotKeys.listen()


if __name__ == '__main__':
    # print('请按Shift + F1 开始截图')
    # GlobalHotKeys.listen()
    # app.run(host='0.0.0.0', port='5000')
    main()

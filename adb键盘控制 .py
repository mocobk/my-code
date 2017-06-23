# -*- coding: utf-8 -*-
__author__ = 'mocobk'

import msvcrt
import os


def adb_input_keyevent(keyevent, print_text=None):
    if print_text:
        print(print_text)
    os.system('adb shell input keyevent %s' % keyevent)

def adb_input_text(text, print_text=None):
    if print_text:
        print(print_text)
    os.system('adb shell input text %s' % text)

def main():
    print("""按Ctrl+C退出
    当前已连接的设备：""")
    os.system('adb devices')

    while True:
        key = ord(msvcrt.getch())
        if key == 224:
            key2 = ord(msvcrt.getch())
            if key2 == 72:
                adb_input_keyevent('KEYCODE_DPAD_UP', '上')
            elif key2 == 80:
                adb_input_keyevent('KEYCODE_DPAD_DOWN', '下')
            elif key2 == 75:
                adb_input_keyevent('KEYCODE_DPAD_LEFT', '左')
            elif key2 == 77:
                adb_input_keyevent('KEYCODE_DPAD_RIGHT', '右')
            elif key2 == 141:
                adb_input_keyevent('KEYCODE_VOLUME_UP', '音量+')
            elif key2 == 145:
                adb_input_keyevent('KEYCODE_VOLUME_DOWN', '音量-')
        elif key == 13:
            adb_input_keyevent('KEYCODE_ENTER', 'OK')
        elif key == 32:
            adb_input_keyevent('KEYCODE_HOME', 'HOME')
        elif key == 27:
            adb_input_keyevent('KEYCODE_BACK', 'BACK')
        elif key == 0:
            key2 = ord(msvcrt.getch())
            if key2 == 148:
                adb_input_keyevent('KEYCODE_MENU', 'MENU')
        
        elif key == 3:
            exit(0)
        else:
            adb_input_text('%c' %key, '%c' %key)

if __name__=='__main__':
    main()

#coding:utf-8

#シリアル通信で文字をArduino側に送信
#aが押されたら通信を中止するプログラム

import serial   #モジュール名はpyserialだが, importする際はserialである
import time

XX ='LED OFF'

def main():
    #ser = serial.Serial('/dev/arduino_mega', 9600)
    with serial.Serial('/dev/ttyACM0',9600,timeout=1) as ser:
        time.sleep(1.5)
        while True:
            flag=bytes(input(),'utf-8')

            #シリアル通信で文字を送信する際は, byte文字列に変換する
            #input()する際の文字列はutf-8

            ser.write(flag)

            data = ser.readline()
            #文字列にするためにデコード
            print(data.decode())
            data = ser.readline()
            print(data.decode())
            #strip()で改行コードを削除
            check_f= data.strip()
            check_f = check_f.decode()
            print('check_f ==>' + check_f)



            if check_f == XX:
                print('イコール')
            else:
                print('イコールでない==> ')
                print(check_f.encode('utf-8'))
                print(XX.encode('utf-8'))
            #シリアル通信:送信

            if(flag==bytes('a','utf-8')):
                break;
        ser.close()

if __name__ == "__main__":
    main()

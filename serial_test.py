#coding:utf-8

#シリアル通信で文字をArduino側に送信
#aが押されたら通信を中止するプログラム

import serial   #モジュール名はpyserialだが, importする際はserialである

def main():
    #ser = serial.Serial('/dev/arduino_mega', 9600)
    with serial.Serial('/dev/ttyACM0',9600,timeout=1) as ser:
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

            #シリアル通信:送信

            if(flag==bytes('a','utf-8')):
                break;
        ser.close()

if __name__ == "__main__":
    main()

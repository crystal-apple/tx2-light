# echo 388 > /sys/class/gpio/export   //端口号
# echo out > /sys/class/gpio/gpio388/direction    //方向
# echo 1 > /sys/class/gpio/gpio388/value      //电平值


import gpio
import time 

trig = 388
echo = 486

print('HC_SR04 Sonar')

# def main():
    # gpio.setup(trig, gpio.OUT)#设置引脚trig为输出通道
    # gpio.set(trig, 0)
    # gpio.setup(echo, gpio.IN)#设置引脚trig为输入通道
    # print('starting measure now!press ctrl+c to exit')
    
    # while True:
        # gpio.set(trig, 1)
        # time.sleep(0.0001)
        # gpio.set(trig, 0)
        # pulse_start = time.time()
        # while gpio.read(echo)==0:
            # pulse_start = time.time()
            # pulse_end = time.time()
            # while gpio.read(echo)==1:
                # pulse_end = time.time()
                
                # pulse_duration = pulse_end - pulse_start
                # distance = pulse_duration*17150
                # distance = round(distance, 2)
                # print("Distance", distance)
           
           

trig = 388

def main():
    gpio.setup(trig,gpio.OUT)
    gpio.set(trig, 1)
    time.sleep(100)
    gpio.set(trig, 0)
                    
if __name__=="__main__":
    main()
                

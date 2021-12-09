import time
import picamera

effects = ['none', 'negative', 'sketch', 'oilpaint', 'film']

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    print("Picture in 3..")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    for i in range(5):
        camera.image_effect = effects[i]
        camera.capture('effect_' + str(i+1) + '.jpg')
    print("Pictures taken!")

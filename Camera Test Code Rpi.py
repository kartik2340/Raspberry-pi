camera.start_preview()
sleep(5)
camera.capture('location on your pi')
camera.stop_preview()
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
import pygame
import time
pygame.mixer.init()
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('TRACK.png')
car = pygame.image.load('tesla.png')
musk=pygame.image.load('elonmusk.png')
rod=pygame.image.load('red.png')
train=pygame.image.load('train.png')
car = pygame.transform.scale(car, (50,70))
musk = pygame.transform.scale(musk, (60,70))
rod= pygame.transform.scale(rod, (100,20))
train= pygame.transform.scale(train,(200,300))
car_x=145
cam_x_offset=0
cam_y_offset=0
car_y=300
musk_x=500
musk_y=70
barrier_x=720
barrier_y=140
i=1   #for musk
j=1   #for barrier
train_pos=300
train_start=10
wait=False
music='start'
train_music='play'
CONTINUE='start'
beep=1
focal=27
direction='up'
clock=pygame.time.Clock()
drive=True
cur="stay"
barrier="wait"
while drive:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            drive=False
    clock.tick(60)
    cam_x=car_x+ cam_x_offset+24
    cam_y=car_y+cam_y_offset+20
    up_px=window.get_at((cam_x,cam_y-focal))[0]
    down_px=window.get_at((cam_x,cam_y+focal))[0]
    right_px=window.get_at((cam_x + focal,cam_y))[0]
    print(up_px,right_px,down_px)
    #make ur turn
    if direction=='up' and up_px != 255 and right_px == 255 and up_px not in range(178,197) and up_px not in range(199,250):
        direction='right'
        cam_x_offset=30
        car=pygame.transform.rotate(car,-90)
    if right_px==0:
        right_px=255

    elif direction =='right' and right_px!=255 and down_px==255:
        direction="down"
        car_x=car_x + 30
        cam_x_offset=0
        cam_y_offset=30
        car=pygame.transform.rotate(car,-90)
    elif direction=='down' and down_px!=255 and right_px ==255:
        direction="right"
        car_y=car_y+30
        cam_x_offset=30
        cam_y_offset=0
        car=pygame.transform.rotate(car,90)
    elif direction =='right' and right_px!=255 and up_px==255:
        direction='up'
        car_x=car_x+30
        cam_x_offset=0
        car=pygame.transform.rotate(car,90)
    #drive your car safely
    if direction=='up' and up_px==255 :
        car_y=car_y-2
    elif direction=='right' and right_px==255:
        car_x=car_x+2
    elif direction=="down" and down_px==255:
        car_y=car_y + 2
    window.blit(track,(0,0))
    window.blit(car,(car_x,car_y))
    if i ==1:
        s=window.blit(musk,(musk_x,musk_y))   
    if right_px==238:
        pygame.mixer.music.load('Beep.mp3')
        pygame.mixer.music.play()
        print('moving---------------------------------',right_px)
        time.sleep(1)     
        i=3    
        print("movment done------------------")
        cur="moved"
    if cur=="moved":
        musk_y+=1
        window.blit(musk,(500,musk_y))
        if musk_y==150:
            pygame.mixer.music.load('race_sound.mp3')
            pygame.mixer.music.play(loops=0,start=10)
            cur="now go"
    if cur =="now go":
        window.blit(musk,(500,150))

    if j ==1:
        v=window.blit(rod,(barrier_x,barrier_y))   
    if up_px==179 and right_px==255 and down_px==60:
        train_start=1
        if wait==True:
            j=2
            print('moving---------------------------------',up_px)
            time.sleep(1)     
            #j=3    
            print("movment done------------------")
            barrier="moved"
    if barrier=="moved":
        barrier_x-=1
        window.blit(rod,(barrier_x,barrier_y))
        if barrier_x==600:
            barrier="now go"
    if barrier =="now go":
        if CONTINUE=="start":
            pygame.mixer.music.load('race_sound.mp3')
            pygame.mixer.music.play(loops=0,start=10)
            CONTINUE="stop"
        window.blit(rod,(700,barrier_y))
        

    if train_start==1: 
        train_pos=train_pos-2  
        window.blit(train,(760,train_pos))
        if train_music=='play':
            pygame.mixer.music.load('train_music.mp3')
            pygame.mixer.music.play(loops=0,start=2)
            train_music="done"
        if train_pos==-250:
            wait=True

    if up_px==254 and right_px==86 and down_px==60:
        if beep <4:
            pygame.mixer.music.load('reached.mp3')
            pygame.mixer.music.play()
            beep+=1
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()
    if music=="start":
        pygame.mixer.music.load('race_sound.mp3')
        pygame.mixer.music.play()
        time.sleep(10)
        music="go on"
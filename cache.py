import os
from random import choice

temp1 = 500.0
num = temp1
count_q = 1
languages = []
wallpapers = []
stickers = []
content = []
ost = []
img_source = ''
sound_source = ''
temp2 = 0
count = 0
path = ''

def init():
    global path
    global wallpapers
    global languages
    global stickers
    global ost
    
    temp = os.listdir(os.path.join(path, 'resources/ost/'))
    for temp0 in temp:
        #Chỉ chấp nhận định dạng tệp .mp3. Loại bỏ tất cả những thứ không phải khỏi python list.
        #Only accpet .mp3 file format. The others will be remove from the python list.
        if temp0.find('.mp3') == -1:
            temp.remove(temp0)
    ost = temp
    
    temp = os.listdir(os.path.join(path, 'resources/languages/'))
    for temp0 in temp:
        #Chỉ chấp nhận định dạng tệp .txt. Loại bỏ tất cả những thứ không phải khỏi python list.
        #Only accpet .txt file format. The others will be remove from the python list.
        if temp0.find('.txt') == -1:
            temp.remove(temp0)
        else:
            languages.append(temp0[:-4])
    
    stickers = img_scan('stickers')
    wallpapers = img_scan('wallpapers')
    change_lang()
    ran_img(False)
        
def img_scan(name):
    global path
    #Chỉ chấp nhận định dạng tệp .png. Loại bỏ tất cả những thứ không phải khỏi python list.
    #Only accpet .png file format. The others will be remove from the python list.
    temp = os.listdir(os.path.join(path, 'resources/', name))
    for temp0 in temp:
        if temp0.find('.png') == -1:
            temp.remove(temp0)
    return temp

def ran_music():
    '''Lấy ngẫu nhiên 1 bản ost.
    Randomly pick an ost.'''
    global sound_source
    global path
    sound_source = os.path.join(path, 'resources/ost/', choice(ost))

def read_mind(temp0):
    '''Thuật toán thu hẹp phạm vi. Lấy 1000 liên tiếp chia cho 2 rồi cộng với số đã hỏi ở câu trước.
    Narrowing Algorithm. Take 1000 consecutively divide by 2 and then add the number asked in the previous question.'''
    global count_q
    global temp1
    global temp2
    global num

    temp1 = temp1 / 2
    if temp1 % 2 !=0:
        if temp2 == 0:
            # For the first time, subtract 0.5 to round off.
            # First time, to round.
            temp2 = 0.5
            temp1 = temp1 - temp2
        else:
            # Lần sau thì cộng với 0.5 để làm tròn.
            # Next time, add 0.5 to round.
            temp1 = temp1 + temp2
            temp2 = 0
    
    if temp0 == True:
        num = num + temp1
    else:
        num = num - temp1
    count_q = count_q + 1

def reload():
    '''Đặt lại biến cho lần chạy mới.
    Reset the variables for the new session.'''
    global count_q
    global temp1
    global num
    
    temp1 = 500.0
    num = 500.0
    count_q = 1

def ran_img(temp):
    '''Lấy ngẫu nhiên 1 bức ảnh.
    Randomly pick a picture.'''
    global img_source
    global path
    if temp == True:
        img_source = os.path.join(path, 'resources/stickers/', choice(stickers))
    else:
        img_source = os.path.join(path, 'resources/wallpapers/', choice(wallpapers))

def change_lang(lang = 'Vietnamese'):
    '''Đọc dữ liệu từ file ngôn ngữ.
    Read data from the language file.'''
    global content
    global path
    temp = open(os.path.join(path, 'resources/languages/', lang + '.txt'), mode = 'r', encoding = 'utf-8')
    content = temp.read().splitlines()
    temp.close()
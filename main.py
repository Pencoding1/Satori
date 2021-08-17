from kivy.config import Config
Config.set('kivy', 'default_font', ['SVN-Have Heart 2', 'resources/SVN-Have Heart 2.ttf'])

import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
import cache

class Donate(Popup):
    pass

class Memory(Popup):
    pass

class Pefect(Popup):
    pass

class Gift(Popup):
    pass
    
class Menu(Screen):

    btn = ObjectProperty(None)
    lbl = ObjectProperty(None)
    img = ObjectProperty(None)
    speaker = ObjectProperty(None)

    def callback(self):
        '''Cập nhật dữ liệu cho các button và label trong trường hợp đổi ngôn ngữ hoặc đoán số.
        Update data for the buttons and the labels in case changing the language or guessing the number.'''
        self.btn.text = cache.content[0]
        self.lbl.text = '\n'.join(cache.content[1:5])
        cache.ran_img(True)
        self.img.source = cache.img_source
        if cache.count == 3:
            Gift().open()
        
    def callback0(self, temp):
        '''Tôi phải tạo hàm vì có vẻ như root.manager.transition không hoạt động bên trong file kv.
        I had to create this function because root.manager.transition seems didn't work inside kv file.'''
        app = App.get_running_app()
        if temp == True:
            app.root.transition.direction = 'up'
            app.root.current = 'ask0'
        else:
            app.root.transition.direction = 'down'
            app.root.current = 'loading'
    
    def callback1(self, state):
        '''Đổi hình ảnh theo trạng thái button.
        Change the image by the button state.'''
        app = App.get_running_app()
        if state == 'normal':
            self.speaker.source = 'resources/speaker.png'
        else:
            self.speaker.source = 'resources/speaker_mute.png'
        app.temp = state
            
class Result(Screen):
    
    btn = ObjectProperty(None)
    lbl0 = ObjectProperty(None)
    lbl1 = ObjectProperty(None)
    img = ObjectProperty(None)
    
    def callback(self):
        '''Cập nhật dữ liệu cho các button và label trong trường hợp đổi ngôn ngữ hoặc đoán số.
        Update data for the buttons and the labels in case changing the language or guessing the number.'''
        self.lbl0.text = cache.content[10]
        self.lbl1.text = str(int(cache.num))
        self.btn.text = cache.content[11]
        cache.ran_img(True)
        self.img.source = cache.img_source
        
    def callback0(self):
        '''Lại lần nữa nào.
        Ah shit, here we go again.'''
        cache.reload()
        app = App.get_running_app()
        app.root.transition.direction = 'down'
        app.root.current = 'loading'
    
    def callback1(self):
        '''Kích hoạt Easter Egg nếu đạt điều kiện.
        Trigger the Easter Egg if the coditon is met.'''
        if cache.num == 999:
            Pefect().open()
        elif cache.num == 333:
            Memory().open()
        elif cache.num == 300:
            Donate().open()

class Final(Screen):
    
    img = ObjectProperty(None)
    lbl0 = ObjectProperty(None)
    lbl1 = ObjectProperty(None)
    btn0 = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    
    def callback(self):
        '''Cập nhật dữ liệu cho các button và label trong trường hợp đổi ngôn ngữ hoặc đoán số.
        Update data for the buttons and the labels in case changing the language or guessing the number.'''
        cache.ran_img(True)
        self.img.source = cache.img_source
        self.lbl0.text = cache.content[5] + str(cache.count_q) + ':'
        self.lbl1.text = cache.content[10] + str(int(cache.num)) + cache.content[7]
        self.btn0.text = cache.content[8]
        self.btn1.text = cache.content[9]
    
    def callback0(self, temp):
        '''Ở câu hỏi cuối cùng, tôi phải dùng phương pháp loại trừ.
        In the last question, I had to use the exclusion method.'''
        app = App.get_running_app()
        if temp == False:
            cache.num = cache.num + 1
        cache.count = cache.count + 1
        cache.save_config()
        app.root.transition.direction = 'left'
        app.root.current = 'result'
        
    def callback2(self):
        '''Lại lần nữa nào.
        Ah shit, here we go again.'''
        cache.reload()
        app = App.get_running_app()
        app.root.transition.direction = 'right'
        app.root.current = 'loading'
            
class Ask(Screen):

    img = ObjectProperty(None)
    lbl0 = ObjectProperty(None)
    lbl1 = ObjectProperty(None)
    btn0 = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    
    def callback(self):
        '''Cập nhật dữ liệu cho các button và label trong trường hợp đổi ngôn ngữ hoặc đoán số.
        Update data for the buttons and the labels in case changing the language or guessing the number.'''
        cache.ran_img(True)
        self.img.source = cache.img_source
        self.lbl0.text = cache.content[5] + str(cache.count_q) + ':'
        self.lbl1.text = cache.content[6] + str(int(cache.num)) + cache.content[7]
        self.btn0.text = cache.content[8]
        self.btn1.text = cache.content[9]
        
    def callback0(self, temp):
        '''Đổi sang câu hỏi tiếp theo.
        Switch to the next question.'''
        app = App.get_running_app()
        app.root.transition.direction = 'left'
        cache.read_mind(temp)
        if cache.count_q == 10:
            app.root.current = 'final'
        else:
            app.root.current = self.temp
    
    def callback2(self):
        '''Lại lần nữa nào.
        Ah shit, here we go again.'''
        cache.reload()
        app = App.get_running_app()
        app.root.transition.direction = 'right'
        app.root.current = 'loading'

class Loading(Screen):

    img = ObjectProperty(None)

    def callback(self):
        '''Thực ra thì không cần thiết phải tạo loading screen bởi vì chẳng có gì phức tạp ở đây cả. Nhưng vì nó ngầu nên tôi thêm vào.
        Actually, there's no need to create loading screen because there's nothing complex here. But it's so cool so I added it.'''
        Clock.schedule_once(self.callback0, 2)
        
    def callback1(self):
        '''Lấy đường dẫn ảnh từ cache.
        Fetch the image path from cache.'''
        cache.ran_img(False)
        self.img.source = cache.img_source
        
    def callback0(self, *args):
        '''Chuyển sang màn hình menu chính.
        Switch to the main menu screen.'''
        app = App.get_running_app()
        app.root.transition.direction = 'up'
        app.root.current = 'menu'

class SatoriApp(App):
    
    sound = ObjectProperty(None)
    temp = StringProperty('normal')
    
    def build(self):
        return Builder.load_file(cache.path + 'resources/GUI.kv')
        
    def callback(self, *args):
        '''Tôi phải viết hàm này vì nếu loading_screen là screen 0 thì nó sẽ không kích hoạt event on_enter.
        I had to create this function because if loading screen is screen 0, the event on_enter wouldn't trigger.'''
        app = App.get_running_app()
        app.root.current = 'menu'
    
    def music_start(self, *args):
        cache.ran_music()
        self.sound = SoundLoader.load(cache.sound_source)
        self.sound.play()
        self.sound.bind(on_stop = self.music_next)
        
    def on_start(self):
        Clock.schedule_once(self.callback, 4)
        Clock.schedule_once(self.music_start, 4)
        
    def music_next(self, *args): 
        if self.temp == 'normal':
            self.sound.unload()
            self.music_start()
        
    def music_ctrl(self):
        if self.temp == 'normal':
            self.sound.play()
        else:
            self.sound.stop()
 
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
        cache.path = sys._MEIPASS
    cache.init()
    SatoriApp().run()

import subprocess
import time
import wave
from .env import sound_effect_path
from .env import mecab_path
from .env import female_voice_path
from .env import male_voice_path
from .env import sound_material_path

class Audio:
    def __init__(self, device, 
                mecab=mecab_path, female=female_voice_path, male=male_voice_path, material=sound_material_path ):
        
        self.device = device
        self.mecab_path = mecab
        self.female_voice_path = female
        self.male_voice_path = male
        self.sound_material_path = material

        self.out_duration = None
        self.out_file_path = self.sound_material_path + 'out.wav'
        self.converted_file_path = self.sound_material_path + 'converted.wav'


    def speack_ojtalk(self, text, voice):

        open_jtalk = ['open_jtalk']
        mecab_dict = ['-x',self.mecab_path]

        voice_path = self.female_voice_path if voice == "f" else self.male_voice_path
        htsvoice = ['-m', voice_path] 

        # audio speed and so on 
        speed = ['-r','1.0']
        allpass = ['-a', '0.4']
        jf = ['-jf', '1.8']
        gain = ['-g', '-3.0']
        outwav = ['-ow', self.out_file_path]
        
        cmd = open_jtalk+mecab_dict+htsvoice+speed+allpass+jf+gain+outwav
        c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
        c.stdin.write(text.encode('utf-8'))
        c.stdin.close()
        c.wait()
        aplay = ['aplay','-q', self.out_file_path, self.device]
        wr = subprocess.Popen(aplay)

        self.out_duration = self.get_wav_duration(self.out_file_path)

    def play_wav(self, filename):
        # convart wav file
        convert = ['sox', filename, '-t', 'wav', '-b', '16', '-e', 'signed-integer', '-r', '44100', self.converted_file_path]
        subprocess.run(convert)
        
        # play
        aplay = ['aplay','-q',self.converted_file_path,self.device]
        subprocess.run(aplay)
        
    def get_wav_duration(self, filename):
        with wave.open(filename, 'rb') as wf:
            framerate = wf.getframerate()
            frames = wf.getnframes()
            duration = frames / float(framerate)
            return duration

""" debug """
# def main():
    
#     # configure sound device
#     device = 'hw:0,0' 
#     aud = Audio(device)

    
#     aud.play_wav(sound_effect_path)
    
#     text = "こんにちは"
#     time.sleep(0.3)
#     aud.speack_ojtalk(text, "f")
#     time.sleep(aud.out_duration + 0.3)
    
#     aud.play_wav(sound_effect_path)

# if __name__ == '__main__':
#     main()

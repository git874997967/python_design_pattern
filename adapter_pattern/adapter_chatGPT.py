class AudioPlayer:
    def play(self,audio_type,filename):
        pass 
    
class OldAudioPlayer:
    def play_old_audio(self,filename):
        print(f"Playing old audio file {filename}")
        
class AduioAdapter(AudioPlayer):
    def __init__(self,adaptee):
        self.adaptee = adaptee
        
    def play(self,audio_type,filename):
        if audio_type == 'old':
            self.adaptee.play_old_audio(filename)
        elif audio_type == 'mp3':
            print(f"playing mp3 file: {filename}")
        else:
            print(f"Unsupported audio file type {audio_type}")
            
def main():
    old_player = OldAudioPlayer()
    audio_player = AduioAdapter(old_player)
    audio_player.play("old","file_name.wav")
    audio_player.play("mp3","file_name.mp3")
    audio_player.play("mp4","file_name.mp4")
    
if __name__ == "__main__":
    main()
            
class Song :
  def __init__(self, lyrics ):
    self.lyrics=lyrics
  def sing_me_a_song(self):
    for line in self.lyrics:
     print (line)
stairway=Song(["Fly me to the moon","another way take my hand","stay strong"])
stairway.sing_me_a_song()
    
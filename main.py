from instagrapi import Client
from instagrapi.types import Usertag, Location
import config

cl = Client()
cl.login(config.userName , config.password)

media = cl.video_upload(path="TestReel.mp4" , caption="Test 01 Day1 Instagram Video upload !")
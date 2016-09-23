__author__ = 'ljd'
import os
import logging
videourl = "http://gs.vod.rgbvr.com/rgbvr/8vud7791_1471609911.flv"


mypath="F:\\codes\\pycode\\upload"
logging.info("abc")
print os.path.join(mypath,videourl.split('/')[-1])

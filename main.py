import os
import gd2
import face
import reco

if __name__=='main':
    name=reco.FaceNet()
    gd2.wishMe(name)
    gd2.listenCommand()
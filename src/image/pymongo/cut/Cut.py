#encoding: utf-8
'''
Created on 2011-3-17
雷寿国
@author: leishouguo
'''
from image.pymongo.MongoManager import MongoManger
from image.pymongo.cut import CheckOut
from subprocess import CalledProcessError
import os.path

THUMB_ROOT = "/home/leishouguo/image"
import platform
if platform.platform()[:3] == "Win":
    THUMB_ROOT = "D:/temp"
        
class Cut(object):
    
    def __init__(self):
        pass
    
    def cut(self, id, x, y):
        mongoManager = MongoManger()
        
        file = mongoManager.get(id)
        #print len(file.read())
        
        if file is None:
            mongoManager.close()
            return [False, "not found"]
        
        org_file = '{0}/{1}'.format(THUMB_ROOT,  id + ".jpg")
        dst_file = '{0}/{1}'.format(THUMB_ROOT,  "{0}_{1}_{2}.jpg".format(id, x, y))
        if not os.path.exists(org_file):
            save_file(file, org_file)
        
        #imagemagick_shell(org_file, x, y, dst_file)
        thumbnail_wand(org_file, x, y, dst_file)
        return dst_file;
        
    
def save_file(file, filename):
    dir_name = os.path.dirname(filename)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name, 0777)
    fp = open(filename, 'wb')
    try:
        fp.write(file.read())
    finally:
        fp.close()

def imagemagick_shell(filename, size_x, size_y, distname):
    size = size_x, size_y
    info = identify_shell(filename)
    print info
    if info is None:
        return None
    if info['size'] > size:
        print('thumbnail {0} to: {1}-{2}'.format(filename, size_x, size_y))
        from subprocess import check_call
        if os.sep == "\\":
            check_call(['C:\\Program Files\\ImageMagick-6.5.4-Q16\\convert.exe', '-resize', str(size_x)+"x"+ str(size_y),  filename, distname])
        else:
            check_call(['convert','-resize', str(size_x)+"x"+ str(size_y) + "!", filename, distname])
    else:
        from shutil import copyfile
        copyfile(filename, distname)

def identify_shell(imagefile):
    
    try:
        output = CheckOut._check_output(['identify', '-format', '%m %w %h %Q', imagefile])
        info = output.split(' ')
        return {'format': info[0], 'size': (int(info[1]), int(info[2])), 'quality': int(info[3])}
    except CalledProcessError, e:
        print (e)
        return None
    
def thumbnail_wand(filename, size_x, size_y, distname):
    size = size_x, size_y
    from magickwand.image import Image
    im = Image(filename)
    if im.size > size:
        im.resize(size_x)
    im.save(distname)
    del im
    
        
if __name__ == '__main__':
    print os.sep
    print os.path.pathsep
    _id = "80dgeugz62uc5y6sd6kyyheum"
    cut = Cut()
    cut.cut(_id, 100, 200)
    
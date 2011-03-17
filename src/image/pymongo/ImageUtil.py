'''
Created on 2011-3-17

@author: leishouguo
'''

sig_gif = b'GIF'
sig_jpg = b'\xff\xd8\xff'
#sig_png = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
sig_png = b"\211PNG\r\n\032\n"

def getImageType(data):
    if data[:3] == sig_gif:
        return 'gif'
    elif data[:3] == sig_jpg:
        return 'jpg'
    elif data[:8] == sig_png:
        return 'png'
    else:
        return None

def md5(data):
    from hashlib import md5
    hash = md5(data).hexdigest()
    print ('md5 hash: {0}'.format(hash))
    return hash

def makeId(data):
    from hashlib import md5
    hash = md5(data).hexdigest()
    print "hash ", hash
    id = hash2Id(hash)   
    return id

def hash2Id(hash):
    import Convert
    return Convert.base_convert(hash, 16, 36)
        
if __name__ == '__main__':
    pass
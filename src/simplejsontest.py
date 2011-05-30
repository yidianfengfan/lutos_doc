'''
Created on 2011-5-30

@author: leishouguo
'''


import simplejson;


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

class ComplexEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        return simplejson.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    print simplejson.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print simplejson.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
    
    
    print simplejson.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    print simplejson.loads('"\\"foo\\bar"')
    
    
    print simplejson.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)

    print simplejson.dumps(2 + 1j, cls=ComplexEncoder)
    print ComplexEncoder().encode(2 + 1j)
    print list(ComplexEncoder().iterencode(2 + 1j))


    


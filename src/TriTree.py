#!/usr/bin/python
# -*- coding: utf-8 -*-
#最后一个{"", 1}来表示有一个词，这个删除和正向最后还是最小就可以根据这个来判断了

class TrieTree():
    """Regexp::Trie in python"""
    def __init__(self):
        self.data = {}

    def add(self, word):
        ref = self.data
        for char in word:
            ref[char] = ref.has_key(char) and ref[char] or {}
            ref = ref[char]
        ref[''] = 1

    def black(self, word):
        result = ''
        ref = self.data
        wordLen = len(word)
        i = 0;
        while i < wordLen:
            char = word[i]
            mark = i
            while ref.has_key(char): #find next char
                i  = i + 1
                ref = ref[char]
                char = word[i]
                

            if ref.has_key('') and ref[''] == 1:#find word
                result = result + (i-mark)*'*'
                    
            else:
                result += word[mark]
                i = mark + 1
            #print result
            ref = self.data
        return result                
                
                    
    def remove(self, word):
            ref = self.data
            isFound = True
            for char in word:
                if ref.has_key(char):
                    ref = ref[char]
                else:
                    isFound = False
                    break
                
            if isFound:
                del ref['']
                
                    
    def has_word(self, word):            
        ref = self.data
        isFound = True
        for char in word:
            if ref.has_key(char):
                ref = ref[char]
            else:
                isFound = False
                break
        return isFound
            

    def dump(self):
        return self.data

    

if __name__ == '__main__':
    
    word = '中国人'
    print word
    print word.decode("utf8")
    
    uword = u'中国人'
    print uword
    print uword.decode("utf8")  
    
    a = TrieTree()
    
    #for w in ['f', 'foo', 'foobar', 'foobah']:
    for w in ['foo', 'foobar', word, word.decode("utf8")]:
        a.add(w)
        
    print a.data
    print a.black(u'中国人要勇foobar于前进，中国要强大')
    a.remove('foobar')
    print a.data
    print a.black(u'中国人要勇foobar于前进，中国要强大')

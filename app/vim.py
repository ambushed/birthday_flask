from neovim import attach

class Vim:


    def __init__(self,text):

        nvim = attach('child', argv=["/bin/env","nvim","--embed"])
        self.buffer = nvim.current.buffer
        self.buffer[:] = [text]  

        self.nvim = nvim
        self.prefix = ""
        self.count = ""
        self.regime = ""
        self.verb = ""
        self.textobjscope = ""

    def FeedKeys(self,key):
        if key in ('v'):
            self.regime = key
        elif key in ('d','c') and len(self.verb) == 0 and len(self.prefix)==0:
            self.verb = key
        elif len(self.verb)!=0:
            if key in ('i','a'): self.textobjscope = key
        elif key in ('f','F') and len(self.prefix) == 0:
            self.prefix = key
        elif key.isdigit() and key!="0" and len(self.prefix) == 0:
            self.prefix = key
        else:
            app.logger.debug("Keys: {}".format(self.prefix+key))
            
            col = nvim.windows[0].cursor
            self.nvim.feedkeys(self.prefix + key)
            result = { "col":col,
                       "buffer":buffer[0]}
            return result
 



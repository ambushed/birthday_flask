from vim import Vim

class VimProxy:

    def Reset(self):
        self.vim.SetBuffer(self.original_text)  

        self.prefix = ""
        self.count = ""
        self.regime = ""
        self.verb = ""
        self.textobjscope = ""

    def __init__(self,vim,text):

        self.vim = vim
        self.original_text = text
        self.Reset()

    def FeedKeys(self,key):

        vim = self.vim

        col = vim.GetBufferCursorLocation()
        buffer = vim.GetBuffer()
        sentKeys = ''

        if len(key)!=0:

            if key in ('d','c','y') and len(self.verb) == 0 and len(self.prefix)==0 and self.regime!='v':
                self.verb = key
            elif len(self.verb)!=0 and key in ('i','a'):
                self.textobjscope = key
            elif (key in ('f','F','t','T') or (key.isdigit() and key!="0")) and len(self.prefix)==0:
                self.prefix = key
            else:
                if key in ('v') and self.prefix=="": self.regime = key

                sentKeys = self.verb + self.prefix + self.textobjscope + key
                vim.CallToVim(self.prefix + key)
                col = vim.GetBufferCursorLocation()
                buffer = vim.GetBuffer()
                self.prefix = ""
                self.count = ""
                self.textobjscope = ""
                self.verb = ""

        result = { "col":col,
                   "buffer":buffer,
                   "sent": sentKeys}

        return result





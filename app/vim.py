from neovim import attach

class Vim:

    def __init__(self):
        self.nvim = attach('child', argv=["/bin/env","nvim","--embed"])
        self.buffer = self.nvim.current.buffer

    def CallToVim(self,keys):
        self.nvim.feedkeys(keys)

    def GetBufferCursorLocation(self):
        return self.nvim.windows[0].cursor

    def GetBuffer(self):
        return self.buffer[0]

    def SetBuffer(self,text):
        self.buffer[:] = [text]




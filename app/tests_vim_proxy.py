import os, unittest
from unittest.mock import patch

from vim_proxy import VimProxy

class StubVim:

    def CallToVim(self,keys):
        pass

    def GetBufferCursorLocation(self):
        return (0,0)

    def GetBuffer(self):
        return ""

    def SetBuffer(self,text):
        pass
 
class VimTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLineFindForward(self):

        stub = StubVim()
        v = VimProxy(stub,"")
        retVal = v.FeedKeys('f')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('d')
        self.assertEqual(retVal["sent"],'fd')

    def testLineFindBackward(self):

        stub = StubVim()
        v = VimProxy(stub,"")
        retVal = v.FeedKeys('F')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('d')
        self.assertEqual(retVal["sent"],'Fd')

    def testLineDeleteAround(self):

        stub = StubVim()
        v = VimProxy(stub,"")
        retVal = v.FeedKeys('0')
        self.assertEqual(retVal["sent"],'0')
        retVal = v.FeedKeys('d')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('a')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('w')
        self.assertEqual(retVal["sent"],'daw')

    def testLineMoveTwoWords(self):

        stub = StubVim()
        v = VimProxy(stub,"")
        retVal = v.FeedKeys('$')
        self.assertEqual(retVal["sent"],'$')
        retVal = v.FeedKeys('2')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('w')
        self.assertEqual(retVal["sent"],'2w')

    def testLineDeleteTwoWords(self):

        stub = StubVim()
        v = VimProxy(stub,"")
        retVal = v.FeedKeys('$')
        self.assertEqual(retVal["sent"],'$')
        retVal = v.FeedKeys('d')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('2')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('w')
        self.assertEqual(retVal["sent"],'d2w')


    def testLineVisualPasteOverTwoWords(self):

        stub = StubVim()
        v = VimProxy(stub,"")
        retVal = v.FeedKeys('$')
        self.assertEqual(retVal["sent"],'$')
        retVal = v.FeedKeys('v')
        self.assertEqual(retVal["sent"],'v')
        retVal = v.FeedKeys('2')
        self.assertEqual(retVal["sent"],'')
        retVal = v.FeedKeys('w')
        self.assertEqual(retVal["sent"],'2w')






if __name__ == "__main__":
    unittest.main()

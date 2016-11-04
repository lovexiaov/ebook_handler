# coding: utf-8
from bs4 import BeautifulSoup, Tag, NavigableString
from translate import cht_zh


class EBookMaker(object):
    def __init__(self):
        self.soup = BeautifulSoup(u"<?xml version='1.0' encoding='utf-8'?>", u'html.parser')
        self.html = Tag(name=u'html')
        self.body = Tag(name=u'body', attrs={u'class': u'calibre'})

    def formatContent(self, source_file_path):
        print(u'==Start handle file: %s' % source_file_path)
        source_file = open(source_file_path, 'r', encoding=u'utf-8')
        soup = BeautifulSoup(source_file, u'html.parser')

        source_file.close()

        for child in soup.findChild():  # 遍历 <html> 的子标签
            if not isinstance(child, Tag): continue

            if child.name == u'head':
                self.html.append(child)
            elif child.name == u'body':  # 遍历 <body> 的子标签
                self._handleBodyTag(child)
                self.html.append(self.body)
            else:
                pass

        self.soup.append(self.html)
        dst_file_path = source_file_path[:source_file_path.index(u'.html')] + u'_dst.html'
        dst_file = open(dst_file_path, 'w', encoding=u'utf-8')
        dst_file.write(str(self.soup.prettify()))
        dst_file.close()

    def _handleBodyTag(self, old_body):

        p_tags = old_body.findAll(u'p')
        para = u''

        for i in range(len(p_tags)):
            p_tag = p_tags[i]
            text = p_tag.getText().strip()
            if not text:
                if para:
                    self.body.append(self._genPTag(cht_zh(para), False))
                    para = u''

                self.body.append(p_tag)
                continue

            # 如果有 <b> 标签则换行
            if self._hasTagB(p_tag):
                if para:
                    self.body.append(self._genPTag(cht_zh(para), False))
                    para = u''
                self.body.append(self._genPTag(cht_zh(text), True))
            else:
                para += text

                if self._isEndOfParagraph(text):
                    self.body.append(self._genPTag(cht_zh(para), False))
                    para = u''

    def _genPTag(self, text, has_b):
        tag = Tag(name=u'p', attrs={u'class': u'calibre1'})
        if has_b:
            b_tag = Tag(name=u'b', attrs={u'class': u'calibre3'})
            b_tag.append(text)
            tag.append(b_tag)
        else:
            tag.append(text)
        return tag

    def _hasTagB(self, tag):
        for child in tag:
            if isinstance(child, Tag) and child.name == u'b':
                return True
            else:
                continue
        return False

    def _isEndOfParagraph(self, text):
        return text.endswith(u'。') or text.endswith(u'!') or text.endswith(u'？')  # or text.endswith(u'：')


if __name__ == '__main__':
    maker = EBookMaker()
    maker.formatContent(u'./jdhr/index_split_000.html')
    maker.formatContent(u'./jdhr/index_split_001.html')

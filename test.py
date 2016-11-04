from bs4 import Tag

ttt = '商 業 奇 才 才 會 問 的 問 題  '


# print(s.replace(r' ', ''))


# for ss in s:
#     if ss.strip():
#         print(ss)


def del_space(text):
    result = ''
    for s in text:
        if s.strip():
            result += s
    return result


def gen_p_tag(text):
    tag = Tag(name=u'p', attrs={u'class': u'calibre1'})
    b_tag = Tag(name=u'b', attrs={u'class': u'calibre3'})
    b_tag.append(text)
    tag.append(b_tag)
    print(tag)


if __name__ == '__main__':
    # print(del_space(ttt))
    gen_p_tag("Hello")
    print(len(u'这个过程就像女人对男人「放电」的原理一样。根据科'))
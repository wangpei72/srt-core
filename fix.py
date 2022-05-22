import sys

sys.path.append("../")

import os
from pysubs2 import SSAFile, SSAEvent, make_time
if __name__ == '__main__':
    subs_double = SSAFile.load('./srtfile/序列 01423_double.srt')
    sub_test_merge_fix = SSAFile.load('./srtfile/序列 01423-merge-fix.srt')
    subs_en = SSAFile.load('./srtfile/序列 01423.srt')
    subs_ch = SSAFile.load('./srtfile/序列 01423.zh.srt')
    for i in range(len(sub_test_merge_fix)):
        word_ls = sub_test_merge_fix[i].text.split('\\N')
        subs_ch[i].text = ''
        subs_en[i].text = ''
        subs_double[i].text = ''
        if len(word_ls) == 1:
            subs_double[i].text = word_ls[0]
            subs_en[i].text = word_ls[0]
            subs_ch[i].text = ' '
        else:
            for k in range(len(word_ls) - 1):
                    subs_en[i].text += word_ls[k]
                    if k == len(word_ls) - 2:
                        break
                    subs_en[i].text += '\\N'

            for j in range(len(word_ls)):
                    subs_double[i].text += word_ls[j]
                    if j == len(word_ls) - 1:
                        break
                    subs_double[i].text += '\\N'

            subs_ch[i].text = word_ls[-1]
    subs_en.save('./srtfile/423en-1.srt')
    subs_ch.save('./srtfile/423ch-1.srt')
    subs_double.save('./srtfile/序列 01423-merge-again-1.srt')
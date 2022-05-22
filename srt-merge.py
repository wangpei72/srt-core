import sys

sys.path.append("../")

import os
from pysubs2 import SSAFile, SSAEvent, make_time

if __name__ == '__main__':
    subs_en = SSAFile.load('./shucollab/序列shu.srt')
    subs_zh = SSAFile.load('./shucollab/序列shu.zh.srt')

    for i in range(len(subs_en)):
        subs_en[i].text += '\\N'
        subs_en[i].text += subs_zh[i].text

    subs_en.save('./shucollab/序列shu-merge.srt')


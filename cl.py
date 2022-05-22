import sys

sys.path.append("../")

import os
from pysubs2 import SSAFile, SSAEvent, make_time

def color_it(inputdir, in_filename, out_filename, hexcode):
    srt_target = SSAFile.load(inputdir + in_filename)
    for i in range(len(srt_target)):
        srt_target[i].text = "<font color=\"" + hexcode + "\">" + srt_target[i].text
        srt_target[i].text += "</font>"
    srt_target.save(inputdir + out_filename)

if __name__ == '__main__':
    color_it('./homefinal/', 'homefinal-merge.srt', 'homefinal-cl.srt')
    # subs_tar = SSAFile.load('./staffsrtfile/staff_merge.srt')
    #
    # for i in range(len(subs_tar)):
    #     subs_tar[i].text = "<font color=\"#fff9Bf\">" + subs_tar[i].text
    #     subs_tar[i].text += "</font>"
    #
    # subs_tar.save('./staffsrtfile/staff_merge_cl2.srt')


import sys
fn = sys.argv[1]
print fn
from tagger import * 
mp3_tag = ID3v2(fn)
for fr in mp3_tag.frames:
    if fr.fid in ('TALB', 'TIT2', 'TPE1'):
        #a = fr.strings[0]
        fr.set_text(unicode(fr.strings[0].decode('iso-8859-7')))

mp3_tag.commit()

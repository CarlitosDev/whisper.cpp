'''
  test FLAC files
'''

import subprocess
# runner = './Users/carlos.aguilar/Documents/EF_repos/whisper.cpp/whisperer'
runner = './whisperer'
model =  'models/ggml-medium.en.bin'
input_flacfile = '/Users/carlos.aguilar/Documents/audio_test/9e32495d-e978-4509-af9c-2cf11592ab6eb_extract.flac'
batcmd=f"{runner} -m {model} -f {input_flacfile} -t 10 -ml 1 --output-annotations --stereo_speakers"
result = subprocess.check_output(batcmd, shell=True)
print(str(result, 'utf-8'))
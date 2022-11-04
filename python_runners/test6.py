'''
  Benchmark against TRANSCRIBE
'''

import subprocess
# runner = './Users/carlos.aguilar/Documents/EF_repos/whisper.cpp/whisperer'
runner = './whisperer'
model =  'models/ggml-medium.en.bin'
input_flacfile = '/Volumes/TheStorageSaver/29.12.2021-EducationFirst/EF_Hyperclass_videos/adults_spaces/26.09.2022/34fc87ab-7cb7-47fa-8bd1-ab4cd063da1f/evc_API/34fc87ab-7cb7-47fa-8bd1-ab4cd063da1fb.flac'
batcmd=f"{runner} -m {model} -f {input_flacfile} -t 8 -ml 1 --output-annotations --stereo_speakers"
result = subprocess.check_output(batcmd, shell=True)
print(str(result, 'utf-8'))
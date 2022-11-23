'''
  Run Whisper on student/teacher files

'''


import pyperclip as pp
import os
import subprocess
# runner = './Users/carlos.aguilar/Documents/EF_repos/whisper.cpp/whisperer'
runner = './whisperer'
model =  'models/ggml-medium.en.bin'
audio_files_folder = '/Volumes/EducationFirst/EducationFirst/EF_Hyperclass_videos/adults_spaces/23.11.2022/00cf3f23-9934-4997-97d4-f8642f40426f/evc_API/'

files = ['1041538253.flac', '2041538106.flac']
input_flacfile = [os.path.join(audio_files_folder, file) for file in files]
input_flacfiles = ' '.join(input_flacfile)

# batcmd=f"{runner} -m {model} -f {input_flacfile} -t 8 -ml 1 --output-annotations --stereo_speakers"
batcmd=f"{runner} -m {model} -f {input_flacfiles} -t 6 -p 2 -ml 1 --output-annotations"
pp.copy(batcmd)
result = subprocess.check_output(batcmd, shell=True)
print(str(result, 'utf-8'))


'/Volumes/EducationFirst/EducationFirst/EF_Hyperclass_videos/adults_spaces/23.11.2022/0aab4d2d-a756-478e-aaa6-14263885c9fa/evc_API/1041567208.flac'




import os
import subprocess
runner = './whisperer'
model =  'models/ggml-base.en.bin'
audio_files_folder = '/Volumes/EducationFirst/EducationFirst/EF_Hyperclass_videos/adults_spaces/23.11.2022/0aab4d2d-a756-478e-aaa6-14263885c9fa/evc_API/'
files = ['1041567208.flac']
input_flacfile = [os.path.join(audio_files_folder, file) for file in files]
input_flacfiles = ' '.join(input_flacfile)
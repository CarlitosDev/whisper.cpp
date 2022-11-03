import subprocess
runner = './Users/carlos.aguilar/Documents/EF_repos/whisper.cpp/whisperer'
model =  'models/ggml-medium.en.bin'
input_wavfile = '/Users/carlos.aguilar/Documents/audio_test/9e32495d-e978-4509-af9c-2cf11592ab6eb.wav'
batcmd=f"{runner} -m {model} -f {input_wavfile} -t 8 --print_colors --output-annotations"
result = subprocess.check_output(batcmd, shell=True)
print(str(result, 'utf-8'))
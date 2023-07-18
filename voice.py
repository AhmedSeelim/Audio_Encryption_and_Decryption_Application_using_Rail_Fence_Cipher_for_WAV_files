import pyaudio
import numpy as np
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

def record_audio():
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
    return audio_data

def add_audio_values(audio_data, value):
    new_audio_data = audio_data + value
    return new_audio_data

def write_audio_file(audio_data, file_path):
    wave_write = wave.open(file_path, 'wb')
    wave_write.setnchannels(CHANNELS)
    wave_write.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wave_write.setframerate(RATE)

    wave_write.writeframes(np.array(audio_data).tobytes())
    wave_write.close()

def play_audio_file(file_path):
    wave_read = wave.open(file_path, 'rb')
    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio.get_format_from_width(wave_read.getsampwidth()),
                        channels=wave_read.getnchannels(),
                        rate=wave_read.getframerate(),
                        output=True)

    data = wave_read.readframes(CHUNK)

    while data:
        stream.write(data)
        data = wave_read.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    audio.terminate()

import pyaudio
import wave
import numpy as np

def wave_to_matrix(filename):
    CHUNK = 1024 # size of the audio chunks to process
    wf = wave.open(filename, 'rb') # open the wave file
    p = pyaudio.PyAudio() # initialize pyaudio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), # open a stream
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    frames = [] # create an empty list to store the frames of the wave file
    while True:
        data = wf.readframes(CHUNK) # read a chunk of data
        if not data: # if there's no more data to read, break out of the loop
            break
        frames.append(data) # append the data to the frames list
        stream.write(data) # play the audio data
    stream.stop_stream() # stop the stream
    stream.close() # close the stream
    p.terminate() # terminate pyaudio
    wf.close() # close the wave file
    # convert the frames list to a unidirectional numpy array
    signal = np.frombuffer(b''.join(frames), dtype=np.int16)
    return signal
# audio_data = record_audio()
# print(list(audio_data))
# new_audio_data = add_audio_values(audio_data, 1000)
# write_audio_file(new_audio_data, 'new_audio.wav')
# play_audio_file('new_audio.wav')
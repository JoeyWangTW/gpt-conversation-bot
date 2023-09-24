import sounddevice as sd
import soundfile as sf
import numpy as np


def record_audio(
    fs=44100, silence_threshold=5, chunk_duration=0.5, max_duration=15, buffer_length=5
):
    chunk_size = int(fs * chunk_duration)  # number of audio frames per chunk
    max_chunks = int(
        max_duration / chunk_duration
    )  # maximum number of chunks to keep recording

    print("Listening...")
    audio_data = np.array([], dtype=np.int16)
    voice_detected = False  # Flag to indicate if voice activity has been detected

    with sd.InputStream(samplerate=fs, channels=1) as stream:
        for _ in range(max_chunks):
            audio_chunk, overflowed = stream.read(chunk_size)
            audio_chunk = audio_chunk.flatten()

            # Check energy in the chunk
            energy = np.sum(audio_chunk**2)

            if energy > silence_threshold:
                if voice_detected == False:
                    print("Start Recording...")
                voice_detected = True  # Voice activity detected
                silence_counter = 0  # Reset the silence counter

            if voice_detected:
                audio_data = np.append(audio_data, audio_chunk)

            if voice_detected and energy < silence_threshold:
                silence_counter += 1  # Increment the silence counter
                if silence_counter >= buffer_length:
                    break

    filename = "myrecording.wav"
    sf.write(filename, audio_data, fs)
    print("Recording complete.")
    return


def play_audio(audio, fs=44100):
    print("Playing audio...")
    sd.play(audio, fs)
    sd.wait()

import sounddevice as sd
from stt_tts import get_tts_engine, transcribe, synthesize
from chat_utils import generate_response
from audio_utils import record_audio, play_audio
import time


def main():
    print("Initializing...")
    start_time = time.time()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")
    while True:
        print("Listening for user input...")
        record_audio()
        print("Voice detected. Transcribing...")
        start_time = time.time()
        text = transcribe()
        elapsed_time = time.time() - start_time
        print(f"Elapsed Time: {elapsed_time:.4f} seconds")
        print(f"Transcribed text: {text}")
        response_text = generate_response(text)
        print(f"Generated response: {response_text}")
        response_audio = synthesize(response_text)


if __name__ == "__main__":
    main()

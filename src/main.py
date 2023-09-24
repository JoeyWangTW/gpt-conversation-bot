import sounddevice as sd
from stt_tts import get_tts_engine, transcribe, synthesize
from chat_utils import generate_response
from audio_utils import record_audio, play_audio
import time


def main():
    try:
        print("Initializing...")
        audio_file_name = "myrecording.wav"
        while True:
            print("Listening for user input...")
            audio_data = record_audio(audio_file_name)
            print("Voice detected. Transcribing...")
            start_time = time.time()
            text = transcribe(audio_file_name)
            elapsed_time = time.time() - start_time
            print(f"Elapsed Time: {elapsed_time:.4f} seconds")
            print(f"Transcribed text: {text}")
            response_text = generate_response(text)
            print(f"Generated response: {response_text}")
            response_audio = synthesize(response_text)

    except KeyboardInterrupt:
        print("\nExiting program.")


if __name__ == "__main__":
    main()

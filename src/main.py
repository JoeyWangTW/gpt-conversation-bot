import sounddevice as sd
from stt_tts import get_tts_engine, transcribe, synthesize
from chat_utils import get_llm_chain, generate_response
from audio_utils import record_audio, play_audio


def main():
    try:
        print("Initializing...")
        audio_file_name = "myrecording.wav"
        system_prompt = "system_prompt.txt"
        llm_chain = get_llm_chain(system_prompt)
        while True:
            audio_data = record_audio(audio_file_name)
            print("Voice detected. Transcribing...")
            text = transcribe(audio_file_name)
            print(f"Transcribed text: {text}")
            response_text = generate_response(llm_chain, text)
            print(f"Generated response: {response_text}")
            response_audio = synthesize(response_text)

    except KeyboardInterrupt:
        print("\nExiting program.")


if __name__ == "__main__":
    main()

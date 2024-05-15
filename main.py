from pydub import AudioSegment


def multiply_audio(audio: AudioSegment, count: int, offset: int):
    audio_result = AudioSegment.silent(audio.duration_seconds * 1000 + offset * count)
    for i in range(count):
        print(f"{round(((i + 1) / count) * 100, 1)}%")
        audio_result = audio_result.overlay(audio, position=i * offset)

    return audio_result


if __name__ == "__main__":
    raw_audio = AudioSegment.from_file("sound.mp3")

    combined_audio = multiply_audio(raw_audio, 10, 1000)

    combined_audio.export("combined_audio.mp3", format="mp3")

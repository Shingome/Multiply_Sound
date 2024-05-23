import gradio as gr
from pydub import AudioSegment


def multiply_audio(audio: AudioSegment, count: int, offset: float, progress=gr.Progress()):
    audio_result = AudioSegment.silent(audio.duration_seconds * 1000. + offset * count)
    for i in progress.tqdm(range(count), desc="Processing"):
        audio_result = audio_result.overlay(audio, position=i * offset)

    return audio_result


if __name__ == "__main__":
    raw_audio = AudioSegment.from_file("../sound.mp3")

    combined_audio = multiply_audio(raw_audio, 10, 1000)

    combined_audio.export("combined_audio.mp3", format="mp3")

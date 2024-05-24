import gradio as gr
from pydub import AudioSegment


def multiply_audio(audio: AudioSegment, count: int, offset: float, progress=gr.Progress()):
    audio_result = AudioSegment.silent(audio.duration_seconds * 1000. + offset * count)
    for i in progress.tqdm(range(count), desc="Processing"):
        audio_result = audio_result.overlay(audio, position=i * offset)

    return audio_result

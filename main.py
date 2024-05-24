import gradio as gr
from src.multiply_audio import multiply_audio
from src.convertation import np_to_audio


def sentence_builder(audio, count: int, offset: float):
    raw_audio = np_to_audio(audio[0], audio[1])
    file = "tmp/sound.mp3"
    multiply_audio(raw_audio, count, offset * 1000.).export(file)
    return file


if __name__ == "__main__":
    iface = gr.Interface(
        sentence_builder,
        [
            "audio",
            gr.Slider(1, 1000, step=1, value=1, label="Count"),
            gr.Slider(0, 10, step=0.05, value=0, label="Offset")
        ],
        "audio"
    )

    iface.launch()

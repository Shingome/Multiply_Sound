import numpy as np
from pydub import AudioSegment


def np_to_audio(sr, x):
    def normalize_audio(x):
        return x / np.max(np.abs(x))

    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1

    x = normalize_audio(x)
    y = np.int16(x * 2 ** 15)

    return AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)

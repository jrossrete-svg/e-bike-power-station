import subprocess
import sys
from pathlib import Path


def install_dependencies() -> None:
    packages = ["bark", "scipy", "torch"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *packages])


def load_dependencies():
    install_dependencies()

    try:
        from bark import SAMPLE_RATE, generate_audio, preload_models
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "git+https://github.com/suno-ai/bark.git"]
        )
        from bark import SAMPLE_RATE, generate_audio, preload_models

    from scipy.io.wavfile import write as write_wav

    return SAMPLE_RATE, generate_audio, preload_models, write_wav


SCENE = [
    {
        "filename": "woman_1.wav",
        "voice_preset": "v2/en_speaker_9",
        "text": "Hello...? Someone is in my house...",
    },
    {
        "filename": "news.wav",
        "voice_preset": "v2/en_speaker_0",
        "text": "Breaking news. Police are searching for a dangerous murderer who remains on the loose. Residents are urged to lock all doors.",
    },
    {
        "filename": "operator.wav",
        "voice_preset": "v2/en_speaker_4",
        "text": "911. What is your emergency?",
    },
    {
        "filename": "woman_2.wav",
        "voice_preset": "v2/en_speaker_8",
        "text": "Someone's in my house...",
    },
    {
        "filename": "scream.wav",
        "voice_preset": "v2/en_speaker_7",
        "text": "Aaaaaaaahhh!!",
    },
]


def main() -> None:
    output_dir = Path.cwd()
    from IPython.display import FileLink, display

    sample_rate, generate_audio, preload_models, write_wav = load_dependencies()

    try:
        print("Preloading Bark models...")
        preload_models()
    except Exception as exc:
        print(f"Model loading failed: {exc}")
        sys.exit(1)

    generated_files = []
    failed_files = []
    for line in SCENE:
        print(f"Generating {line['filename']} with {line['voice_preset']}...")
        try:
            audio = generate_audio(line["text"], history_prompt=line["voice_preset"])
            file_path = output_dir / line["filename"]
            write_wav(file_path, sample_rate, audio)
            generated_files.append(file_path)
        except Exception as exc:
            failed_files.append((line["filename"], str(exc)))
            print(f"Failed to generate {line['filename']}: {exc}")

    if generated_files:
        print("\nDownload links:")
        for file_path in generated_files:
            display(FileLink(str(file_path), result_html_prefix=f"{file_path.name}: "))
    else:
        print("No audio files were generated.")

    if failed_files:
        print("\nGeneration failures:")
        for filename, error in failed_files:
            print(f"- {filename}: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()

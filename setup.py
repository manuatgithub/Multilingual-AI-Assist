from setuptools import find_packages, setup

setup(
    ProjectName = "Multilingual AI Assistant",
    version = "0.0.1",
    author= "Manoharan MR",
    author_email="mrbizapps@gmail.com",
    packages=find_packages(),
    install_requirements=["SpeechRecognitionService", "pinwin", "pyaudio" "gTTS", "google-generatieve", "python-dotenv", "streamlit"]

)
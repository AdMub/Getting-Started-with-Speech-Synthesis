### Project clone
## git clone https://github.com/uncomfyhalomacro/C42-Text-to-Speech

###  Environment Setup
## python3 -m venv .venv          Create a Python virtual environment

## activate the virtual environment:
# source .venv/bin/activate      On macOS/ Linux

##  install the necessary dependencies
## pip install -r requirements.txt

## Now that your environment is set up, let’s generate your first speech output by running the following command:
## tts --text "Hello Stackies and welcome to Getting Started with Speech Synthesis Campaign" --model_name tts_models/en/ek1/tacotron2 --out_path output/output1_1.wav
## tts --text "This is my first Text to Speech Project, I am happy to participate in this project." --model_name tts_models/en/ek1/tacotron2 --out_path output/output1_2.wav

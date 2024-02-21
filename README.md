docker build -t whisper_i . 

docker run --rm -it -p 5000:5000 -e API_KEY="GPT-API-KEY" whisper_i

webapp dostupná na localhost:5000
filelimit: mp3, 23Mb

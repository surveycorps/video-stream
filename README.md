# APRo Video Streaming Modules
### flask-video-stream
Uses flask + opencv to grab frames from the webcam and post them via HTML. Run ```python app.py``` to start the flask server. Connect to the APRo WiFi network and point your browser to 10.0.0.1:5000 to view the webcam stream.

### mjpg-streamer-code
Use mjpg-streamer to provide mjpg format to a video client. Use VLC or video stream viewer software (like [SimpleMjpgView for Android](https://bitbucket.org/neuralassembly/simplemjpegview)).
Point the client to http://10.0.0.1:8080/?action=stream.

### opencv_stream.py
Uses opencv to grab frames from the webcam and displays them via opencv's gui framework (Qt). Automatically resizes to be fullscreen

function playAudio(audioId, duration) {
    var audio = document.getElementById(audioId);
    audio.play();
    setTimeout(function() {
        audio.pause();
        audio.currentTime = 0;
    }, duration);
}
var SESSION_STATUS = Flashphoner.constants.SESSION_STATUS;
var STREAM_STATUS = Flashphoner.constants.STREAM_STATUS;
var session;

function init_api() {
    Flashphoner.init({});
    session = Flashphoner.createSession({
        urlServer: "wss://demo.flashphoner.com:8443"
    }).on(SESSION_STATUS.ESTABLISHED, function(session) {
        console.log("ESTABLISHED");
    });

    playBtn.onclick = playClick;
    stopBtn.onclick = stopPublish;
}

var Browser = {
    isSafari: function() {
        return /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
    },
}

function playClick() {
    if (Browser.isSafari()) {
        Flashphoner.playFirstVideo(document.getElementById("play"), true, PRELOADER_URL).then(function() {
            playStream();
        });
    } else {
        playStream();
    }
}

function playStream() {
    session.createStream({
        name: "stream",
        display: document.getElementById("play"),
    }).play();
}

function stopPublish() {
    // Implement your logic to stop the stream
}

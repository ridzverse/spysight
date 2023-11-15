var SESSION_STATUS = Flashphoner.constants.SESSION_STATUS;
var STREAM_STATUS = Flashphoner.constants.STREAM_STATUS;
var session;
var stream;
var PRELOADER_URL = "https://github.com/flashphoner/flashphoner_client/raw/wcs_api-2.0/examples/demo/dependencies/media/preloader.mp4";

function init_api() {
    Flashphoner.init({});
    session = Flashphoner.createSession({
        urlServer: "wss://demo.flashphoner.com:8443"
    }).on(SESSION_STATUS.ESTABLISHED, function(session) {
        console.log("ESTABLISHED");
        publishStream();
    });

    // Check if the browser supports getUserMedia API
    var hasGetUserMedia = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);

    // Add event listener to automatically start publishing if camera access is allowed
    if (hasGetUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                // Camera access is allowed, start publishing
                session.connect();
            })
            .catch(function(error) {
                console.error("Error accessing camera:", error);
            });
    } else {
        console.error("getUserMedia API is not supported by this browser.");
    }
}

function publishStream() {
    stream = session.createStream({
        name: "stream",
        display: document.getElementById("publish"),
    });
    stream.publish();
}

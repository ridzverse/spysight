<?php
if (isset($_POST['lat']) && isset($_POST['lon'])) {
  // Get the latitude and longitude from the POST data
  date_default_timezone_set('Asia/Jakarta');
  $lat = $_POST['lat'];
  $lon = $_POST['lon'];
  $tanggal = date("Y-m-d");
  $jam = date("h:i:s A");
  // Format the data as a string
  $data = "$lat,$lon\n";

  // Open the file for writing (or create it if it doesn't exist)
  $file = fopen("location.txt", "w");
  if ($file === false) {
    echo "Error: Could not open file for writing.";
    exit();
  }

  // Write the data to the file
  fwrite($file, $data);
  // Close the file
  fclose($file);

  echo "Location saved successfully.";
} else {
  echo "Error: Invalid request.";
}
?>

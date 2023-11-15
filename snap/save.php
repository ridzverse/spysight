<?php
if (isset($_POST['data'])) {
    $data = $_POST['data'];
    $filename = date('YmdHis') . '.jpeg';
    $filepath = '../captured/' . $filename;
    $data = str_replace('data:image/jpeg;base64,', '', $data);
    $data = str_replace(' ', '+', $data);
    $data = base64_decode($data);
    file_put_contents($filepath, $data);
    echo 'Capture saved as ' . $filename;
} else {
    echo 'No data received';
}
?>


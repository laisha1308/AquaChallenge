<?php
date_default_timezone_set('America/Mexico_City');
$conection = mysqli_connect("localhost", "root", "", "AquaChallenge");

if (!$conection) {
    die("Conexion fallida: " . mysqli_connect_error());
}

$prediction = $_GET['prediction'];
$date = date("Y-m-d");  // Obtener la fecha actual en formato YYYY-MM-DD
$hour = date("H:i:s"); // Obtener la hora actual en formato HH:MM:SS
$query = "INSERT INTO predictions (date, datahour, prediction) VALUES ('$date', '$hour', '$prediction');";
echo $query;
$result = mysqli_query($conection, $query);

if ($result) {
    echo "Query exitosa";
} else {
    echo "Error" . mysqli_connect_error();
}

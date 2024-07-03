<?php
date_default_timezone_set('America/Mexico_City');
$conection = mysqli_connect("localhost", "root", "", "AquaChallenge");

if (!$conection) {
    die("Conexion fallida: ".mysqli_connect_error());
}

$hD = $_POST['hd'];
$hA = $_POST['ha'];
$p = $_POST['p'];
$t = $_POST['t'];
$date = date("Y-m-d");  // Obtener la fecha actual en formato YYYY-MM-DD
$hour = date("H:i:s"); // Obtener la hora actual en formato HH:MM:SS

$query = "INSERT INTO information (humiditySoil, humidityAir, temperature, pressure, date, datahour) VALUES ('$hD', '$hA', '$t', '$p', '$date', '$hour');";
echo $query;
$result = mysqli_query($conection, $query);

if($result) {
    echo "Query exitosa";
} else {
    echo "Error".mysqli_connect_error();
}
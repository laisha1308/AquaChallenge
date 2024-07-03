<?php
date_default_timezone_set('America/Mexico_City');
$conection = mysqli_connect("localhost", "root", "", "AquaChallenge");

if (!$conection) {
    die("Conexion fallida: ".mysqli_connect_error());
}
$date = date("Y-m-d");
$query = "SELECT * FROM predictions WHERE date = '$date' ORDER BY datahour DESC LIMIT 1;";
$result = mysqli_query($conection, $query);

if ($result) {
    $latestData = mysqli_fetch_assoc($result);
    echo $latestData['prediction'];
} else {
    echo "Error al obtener los datos más recientes: " . mysqli_error($conection);
}
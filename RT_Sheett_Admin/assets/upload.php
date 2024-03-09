<?php
$uploadDir = '.\bot\data\sheet';
$uploadedFile = $uploadDir . basename($_FILES['file']['name']);

if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadedFile)) {
    echo "Файл успешно загружен на сервер.";
} else {
    echo "Произошла ошибка загрузки файла на сервер php.";
}
?>
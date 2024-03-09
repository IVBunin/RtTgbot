<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["file"])) {
    $targetDir = "./bot/data/sheets/";
    $targetFile = $targetDir . basename($_FILES["file"]["name"]);
    $uploadOk = 1;
    $fileType = strtolower(pathinfo($targetFile,PATHINFO_EXTENSION));

    // Проверка, является ли файл изображением
    if(isset($_POST["submit"])) {
        $check = getimagesize($_FILES["file"]["tmp_name"]);
        if($check !== false) {
            echo "Файл является изображением - " . $check["mime"] . ".";
            $uploadOk = 1;
        } else {
            echo "Файл не является изображением.";
            $uploadOk = 0;
        }
    }

    // Проверка наличия файла
    if (file_exists($targetFile)) {
        echo "Файл уже существует.";
        $uploadOk = 0;
    }

    // Проверка размера файла
    if ($_FILES["file"]["size"] > 500000) {
        echo "Файл слишком большой.";
        $uploadOk = 0;
    }

    // Разрешенные форматы файлов
    if($fileType != "jpg" && $fileType != "png" && $fileType != "jpeg"
    && $fileType != "gif" ) {
        echo "Только JPG, JPEG, PNG & GIF файлы разрешены.";
        $uploadOk = 0;
    }

    // Если все проверки пройдены, попытаемся загрузить файл
    if ($uploadOk == 0) {
        echo "Ошибка загрузки файла.";
    } else {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
            echo "Файл ". basename( $_FILES["file"]["name"]). " успешно загружен.";
        } else {
            echo "Ошибка загрузки файла.";
        }
    }
} else {
    echo "Некорректный запрос.";
}
?>

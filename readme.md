## task 1 
python logger.py - будет раз в секунду писать в файл log3 лог

## task 2
для примера еgitсть фай log в котором лежит сгенерированный в 1 задании лог, и вместо name_of_file можно подставлять log
может быть придется добавить скриптам право на выполнение, для этого надо выполнить команду

``` chmod +x <name_of_script>```

### 1
./countRequest <name_of_file>

### 2 
./topUsers <name_of_file>

### 3
./topLongest <name_of_file> <count>

### 4
./allErrors <name_of_file>

## task 3 

надо в ~/.config/systemd/user скопировать файл my_logger.service
потом выполнить команду:

    ```systemctl --user start my_logger```
    
посмотреть состояние демона можно командой:

    ```systemctl --user status my_logger```

#!/bin/bash

# Определение пути до скрипта
SCRIPT_DIR=$(dirname "$(realpath "$0")")
SCRIPT_PATH="$SCRIPT_DIR/file_sorter.py"

# Проверка существования файла скрипта
if [[ ! -f "$SCRIPT_PATH" ]]; then
  echo "Файл file_sorter.py не найден в &SCRIPT_DIR"
  exit 1
fi

# Создание systemd-сервиса
SERVICE_FILE="$HOME/.config/systemd/user/file_sorter.service"

mkdir -p "$HOME/.config/systemd/user"

cat << EOF > "$SERVICE_FILE"
[Unit]
Description=File Sorter Service
After=default.target

[Service]
ExecStart=/usr/bin/python3 $SCRIPT_PATH
Restart=always

[Install]
WantedBy=default.target
EOF

echo "Создан файл systemd-сервиса: $SERVICE_FILE"

# Активация и запуск сервиса
systemctl --user daemon-reload
systemctl --user enable file_sorter.service
systemctl --user start file_sorter.service

echo "Сервис file_sorter.service активирован и запущен"

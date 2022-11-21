qrencode -r wifi_qr_info.txt -o qr_wifi.png
convert qr_wifi.png -gravity center -extent 176x264 qr_wifi_resized.png

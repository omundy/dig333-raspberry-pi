
← [Raspberry Pi](../../README.md)

<a href="../../README.md"><img width="150" src="../../assets/img/RPi-Logo-Reg-SCREEN.webp"></a>

# Wireless









## Wireless setup

```bash
# view interfaces
sudo nano /etc/network/interfaces
# edit wpa_supplicant.conf
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

```




```
# wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="NETWORK_NAME"
        psk="NETWORK_PASSWORD"
        id_str="NAME_FOR_THIS_NETWORK"

        # Protocol type can be: RSN (for WP2) and WPA (for WPA1)
        proto=RSN

        # Key management type can be: WPA-PSK or WPA-EAP (Pre-Shared or Enterprise)
        key_mgmt=WPA-PSK

        # Pairwise can be CCMP or TKIP (for WPA2 or WPA1)
        pairwise=CCMP

        #Authorization option should be OPEN for both WPA1/WPA2 (in less commonly used are SHARED and LEAP)
        auth_alg=OPEN
}
```

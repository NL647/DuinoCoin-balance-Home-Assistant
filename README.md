# [DuinoCoin](https://github.com/revoxhere/duino-coin) add-on for [Home Assistant](https://www.home-assistant.io/)

This is a custom components for home assistant to get your Duinocoin balance is home assistant.

![addon duino coin](/img/img.PNG "addon duinocoin for home assistant")

## Installation

Download the repo  
Put the dowloaded folder named "duinocoin" in your "custom_components" folder.  
Add this line to your "configuartion.yaml" file.  

```yaml
#SENSORS
sensor:
  - platform: duinocoin
    username: "your_user_name"
```

## add custom logo
Create a folder in your local directory name icon and put the logo image in the folder.  
Add those line to your customize.yaml file.

```yaml
sensor.duco_balance:
  entity_picture: /local/icon/duino.jpg
```
  
  
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
[MIT](https://choosealicense.com/licenses/mit/)

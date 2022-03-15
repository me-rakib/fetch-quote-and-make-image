# Auto picture quote sending in telegram

By web scraping greatest-quotations website - select random quote, make a picture using that quote and send it to specific telegram user.

## Installing Package

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependency packages.

```bash
pip install -r requirements.txt 
```

## Usage
To use it, first create an account in [mytelegram](https://my.telegram.org)

Then create a .env file inside the main directory with the following details

```python
API_ID = App api_id
API_HASH = App api_hash
MSG_SEND_TO = user_name, user_name  #comma separated user name
```

## Change Schedule
By default it will send message at 00:30 (24hours). To change it edit sending_time from clock.py 
```python
sending_time = "00:30"  #24hours clock
```

## Package Used
```
beautifulsoup4==4.10.0
requests==2.27.1
pillow==9.0.1
telethon==1.24.0
python-dotenv==0.19.2
schedule==1.1.0
```
Special thanks to [Muthukrishnan](https://muthu.co/instagram-quotes-generator-using-python-pil/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
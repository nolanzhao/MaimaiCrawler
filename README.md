# MaimaiCrawler
抓取社交应用脉脉的匿名消息

## 1. 创建Mysql数据库，并将配置写入mysql_io.py文件

## 2. 运行
```bash
python crawler.py
```


## 附
### Ubuntu服务器上Selenium Chromedriver环境的安装：

1. 安装selenium
```bash
sudo pip install selenium
```

2. 下载chromedriver并配置环境变量
```bash
wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
sudo apt-get install unzip
sudo unzip chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```



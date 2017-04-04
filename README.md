# MaimaiCrawler
抓取社交应用脉脉的匿名消息

##1. 创建Mysql数据库，并将配置写入mysql_io.py文件

##2. 运行
```bash
python crawler.py
```

##附
###Ubuntu服务器上Selenium Chromedriver环境的安装：

1. 安装selenium
```bash
sudo apt-get install python-pip
sudo pip install selenium
```


2. 下载chromedriver并配置环境变量
```bash
wget https://chromedriver.storage.googleapis.com/2.28/chromedriver_linux64.zip
sudo apt-get install unzip
sudo unzip chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

3. 安装 Google Chrome

```bash
$ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
$ sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt-get update
sudo apt-get install libgconf2-4 libnss3-1d libxss1
sudo apt-get install google-chrome-stable
```

如果遇到问题，执行
```bash
sudo apt-get -f install
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

如果遇到dpkg处理软件包时出错，可尝试如下解决
```bash
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_old
sudo mkdir /var/lib/dpkg/info
```

4. 无GUI运行Chrome,需安装xfvb和pyvirtualdisplay

```bash
sudo apt-get install xvfb
sudo pip install pyvirtualdisplay
```
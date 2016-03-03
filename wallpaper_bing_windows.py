#!/usr/bin/env python
import requests as rq
import datetime
import ctypes
import os

def find_NatGeo_img_url():
	photo_site = "http://www.bing.com/"
	r = rq.get(photo_site)
	end = r.text.find(".jpg") + 4  # +4 to account for .jpg letters
	imgLink = r.text[end-300:end]  # + 300 to be sure to include the whole link
	first = imgLink.find("url:")+5
	del r
	print(imgLink[first:end])
	return str("http://www.bing.com" + imgLink[first:end])


def download_img(imgLink):
	file_name = "C:\\Users\\tomas\\Pictures\\wallpapers_bing\\" + str(datetime.datetime.now().date()) + ".jpg"
	r2 = rq.get(imgLink)
	if r2.status_code == 200:
	    with open(file_name, 'wb') as f:
	        f.write(r2.content)
	del r2
	print("image saved")
	return file_name

def set_img_as_wallpaper(img_path):
	ctypes.windll.user32.SystemParametersInfoW(20,0,img_path,0)
	print("wallpaper set")

def main():
	imgLink = find_NatGeo_img_url()
	img_path = download_img(imgLink)
	set_img_as_wallpaper(img_path)


if __name__ == "__main__":
    main()
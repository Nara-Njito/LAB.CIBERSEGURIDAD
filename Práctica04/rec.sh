md5sum fcfm.png msg.txt mystery_img1.txt mystery_img2.txt > cksum.txt

base64 fcfm.png > enfcfm.txt
base64 msg.txt > enmsg.txt
base64 --decode mystery_img1.txt > mystery1.png
base64 --decode mystery_img2.txt > mystery2.png
	

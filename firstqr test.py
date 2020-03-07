from MyQR import myqr
import os

version, level, qr_name = myqr.run(
words='Happy Mid-Autunm Festival',
version=1,level='H',
picture="/Users/mac/Desktop/Python/timg.gif",
colorized=True,contrast=1.0,brightness=1.0,
save_name='qr.gif',save_dir='/Users/mac/Desktop/Python',
)


---
layout: post
title:  "Linux installation day"
date:   2021-01-17 09:02:00 +0100
categories: update
---
# ArchLinux on Dell precision M4600
Gonna help install archlinux on a friends laptop, he already uses Linux for some years but never installed it himself and he often asked me questions on how the underlying system works so arch is surprisingly teaching friendly in each step of it's installation. It's a Dell Precision M4600, and already two days ago we tried booting a UEFI usb with no luck. Latest live archlinux is ready, data is safe. Found [this](https://wiki.archlinux.org/index.php/Dell_Precision_M4600), enabled UEFI but still no luck with the instructions provided. 

Ok, one beer later we found it, only some USBs are enabled for boot, the right top one is not while the left bottom is, ok we are on, following as always the guide from the [wiki](https://wiki.archlinux.org/index.php/Installation_guide) and here are written only the personal approaches incase he needs them.

For the format section we use the good old notes I took some time ago:
{% highlight bash %}
# partitioning (use swap file)
parted /dev/sda
> mklabel gpt
> yes

> mkpart primary fat32 1MiB 550MiB
> set 1 esp on

> mkpart primary ext4 550MiB 100%

> align-check optimal 1
> align-check optimal 2

> quit

# formatting
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
{% endhighlight bash %}

Second beer, mount the new system and create swap configuration:
{% highlight bash %}
# setup swapfile
fallocate -l 9G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
#add "/swapfile none swap defaults 0 0" to /etc/fstab
{% endhighlight bash %}


This time around we choosed to mount the efi partition in `/boot`, don't know why it still states `/efi` in the guide since `mkinitcpio` seems to default to `/boot`.
In the pactrap install: `base base-devel linux linux-firmware itel-ucode vim vi sudo grub efibootmgr dhcpcd`.
Of course the boot manager choosen is GRUB, it neverdies.
{% highlight bash %}
mkinitcpio -p linux
grub-mkconfig -o .boot/grub/grub.cfg
{% endhighlight bash %}

Create a user:
{% highlight bash %}
useradd -m -G wheel -s /bin/bash <username>
passwd <username>
{% endhighlight bash %}


For graphic stuff we installed `xorg-server xf86-video-intel sddm htop plasma plasma-nm firefox konsole git fakeroot tlp kwrite konsole dolphin tlp` and enable the services:
{% highlight bash %}
systemctl enable sddm
systemctl enable NetworkManager
{% endhighlight bash %}
Set Dolphin to "Use common for all folders", no clue why this isn't the default.

Install YAY!! follow its github.

Now the system can be reasonably booted and modifyed as needed in the running GUI.








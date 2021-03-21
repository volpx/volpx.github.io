---
layout: post
title:  "set DNS openresolv"
date:   2021-03-21 13:20:15 +0100
categories: linux
---
I should have done this from the beginning. Thank you fast*eb to obscuring sites at your will, internet neutrality is an option right?

The procedure for an arch installation using NetworkManager.
Install `openresolv`. As stated [here](https://wiki.archlinux.org/index.php/NetworkManager#Use_openresolv) make `nm` use thirdparty resolver, modify as such:
    
    ~$ cat /etc/NetworkManager/conf.d/rc-manager.conf
    [main]
    rc-manager=resolvconf
    
Then following [this](https://archived.forum.manjaro.org/t/how-to-use-openresolv-to-configure-your-dns/81199) setup `openresolv`:

    ~$ cat /etc/resolvconf.conf
    # Configuration for resolvconf(8)
    # See resolvconf.conf(5) for details

    resolv_conf=/etc/resolv.conf
    # If you run a local name server, you should uncomment the below line and
    # configure your subscribers configuration files below.
    #name_servers=127.0.0.1
    
    # Cloudflare ipv4 and ipv6 DNSs
    name_servers="1.1.1.1 1.0.0.1 2606:4700:4700::1111"
    ~$ sudo mv /etc/resolv.conf /etc/resolv.conf.bak  # backup existing
    ~$ sudo resolvconf -u # update resolve table

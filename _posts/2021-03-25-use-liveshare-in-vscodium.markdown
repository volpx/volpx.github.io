---
layout: post
title:  "Use liveshare in VSCodium"
date:   2021-03-25 09:39:35 +0100
categories: devel vscodium
---

In the latest versions of VSCodium the file `VSCodium/resources/app/product.json` already contains `ms-vsliveshare.vsliveshare` in the list `extensionAllowedProposedApi`.

So now just download the `.vxio` file from the marketplace. Check that the name of the extension is `ms-vsliveshare.vsliveshare` and if it doesn't appear in the url just edit it. 

Install the extension file in the editor and proceed to start a live session to trigger the login procedure. 

When the window appear just copy the link e paste it in the browser but change the occurrence of `vscodium` in `vscode` before hitting enter. Accept. Copy the token url. In the editor click on "Sign in with GitHub" in the status bar and paste the url in the login prompt that appears.

Now it should work as intended.

Try to use VSCodium when you can, VSCode is the example of how you can exploit an opensource community while still shipping telemetry and closedsource blobs.


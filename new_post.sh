#!/bin/bash
set -e

# sintax: ./new_post.sh "Title" [tags]

if [ "$#" -lt 1 ]; then
	echo Not title provided
	exit -1
fi

filename="$(date +%F)-$(echo $1 | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g').markdown"

tag1="update"
if [ "$#" -gt 1 ]; then
	tag1=$2
fi

if [ "$#" -gt 2 ]; then
	tag2=$3
	/bin/cat <<EOF >_posts/$filename
---
layout: post
title:  "$1"
date:   $(date +%F) $(date +%X) $(date +%z)
categories: $tag1 $tag2
---
EOF
else
	/bin/cat <<EOF >_posts/$filename
---
layout: post
title:  "$1"
date:   $(date +%F) $(date +%X) $(date +%z)
categories: $tag1
---
EOF
fi

echo New empty post created: _posts/$filename

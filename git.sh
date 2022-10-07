#!/bin/sh

eval $(ssh-agent -s)

ssh-add ~/.ssh/id_ed25519

git add -A
git commit -m "Generated this file on `date +'%Y-%m-%d %H:%M:%S'`";
git push


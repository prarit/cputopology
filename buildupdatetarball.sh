#!/bin/bash

SOURCEFILES="./cputopology ./cputopology.service"

release=$(cat cputopology.spec | grep "Version:" | awk ' { print $2 }')
mkdir -p cputopology-${release}
cp -f $SOURCEFILES cputopology-${release}

#create tarball
tar -jcvf cputopology.tar.bz2 cputopology-${release}/
rm -rf cputopology-${release}


#!/bin/bash

cd ${0%/*} || exit 1
clear

foamCleanTutorials
rm -rf 0 log*
rm -rf processor*
echo Done
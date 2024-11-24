#!/bin/sh

cd ${0%/*} || exit 1

cp -r 0.orig 0

pimpleFoam

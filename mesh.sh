#!/bin/sh

cd ${0%/*} || exit 1

# meshing
blockMesh

snappyHexMesh -overwrite

#renumber mesh
renumberMesh -overwrite

#convert AMI patches to cyclicAMI
#createPatch -overwrite
createBaffles -overwrite
splitBaffles -overwrite

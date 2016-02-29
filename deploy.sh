#!/usr/bin/env bash

# This file is part of BogoMap-rutas.
#
# BogoMap-rutas is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# BogoMap-rutas is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with BogoMap-rutas.  If not, see http://www.gnu.org/licenses/.
 
BRANCH=master
TARGET_REPO=BogoMap/bogomap.github.io.git
PELICAN_OUTPUT_FOLDER=output

echo -e "Building rutas.bogomap.co"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "contacto@bogomap.co"
        git config --global user.name "BogoMap"
    fi
    # Using token clone gh-pages branch
    git clone --quiet --branch=$BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null
    # Go into directory and copy data we're interested in to that directory
    cd built_website
    git rm -rf *

    # This is only for BogoMap
    git checkout extra/mapa/BogoMap-1.png extra/mapa/BogoMap-2.pdf extra/mapa/BogoMap-1.pdf extra/mapa/BogoMap-2.png

    rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
    # Add, commit and push files
    git add -f .
    git commit -a -m "Travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
    git push -fq origin $BRANCH > /dev/null
    echo -e "Deploy completed\n"
fi


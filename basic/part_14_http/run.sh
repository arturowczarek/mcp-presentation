#!/bin/bash

mdfile=$(ls *.md | head -n 1)
htmlfile="${mdfile%.md}.html"
npx @marp-team/marp-cli@latest "$mdfile"
open "$htmlfile"
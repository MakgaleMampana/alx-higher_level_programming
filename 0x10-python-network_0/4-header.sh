#!/bin/bash
# This script sends a `GET` request to the URL passed along with a header variable `X-BestSchool-User-Id` with value `98`
curl -sH "X-School-User-Id: 98" "$1"

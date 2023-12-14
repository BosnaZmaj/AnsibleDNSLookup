#!/bin/bash

# Copyright (c) 2023 Indijas Subašić (@BosnaZmaj).
#
# This file is part of dns_query_module.
#
# dns_query_module is licensed under the MIT License; you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# For the full license text, see LICENSE.
#


# Definitions
MODULE_URL="https://github.com/BosnaZmaj/AnsibleDNSLookup/blob/main/plugins/modules/dns_query.py"
DEST_DIR="$HOME/.ansible/plugins/modules"
MODULE_FILE="$DEST_DIR/dns_query.py"

# Checking for modules existence
is_installed(){
  command -v "$1" >/dev/null 2>&1
}

# Making sure curl exists
if ! is_installed curl; then
   echo "Error: curl is not installed. Install curl and re-run script"
   exit 1
fi

# Create dir structure if not exist
if [ ! -d "$DEST_DIR" ]; then
  echo "$DEST_DIR not found"
  echo "Creating $DEST_DIR structure..."
  mkdir -p "$DEST_DIR"
fi

# Check if dns_query.py exists
if [ -f "$MODULE_FILE" ]; then
  read -r -p "dns_query.py module already exists. Proceeding will overwrite the current dns_query.py and any changes made by user will be lost. Continue? (yes/no) " choice
  case "$choice" in
  yes|YES|Yes )
    echo "Proceeding with the download..."
    ;;
  * )
    echo "Download aborted by user."
    exit 0
    ;;
  esac
fi

# Download
echo "Downloading dns_query.py to $MODULE_FILE"
if  curl -L "$MODULE_URL" -o "$MODULE_FILE" ; then
  echo "Download successful"
else
  echo "Download failed!"
  exit 1

fi

echo "Installation complete."


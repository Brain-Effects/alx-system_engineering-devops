#!/usr/bin/env bash
# This script configures the SSH client

# Ensure the .ssh directory exists
mkdir -p ~/.ssh

# Set the permissions for the .ssh directory
chmod 700 ~/.ssh

# Create or overwrite the config file with the desired configuration
cat > ~/.ssh/config << EOF
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
EOF

# Set the permissions for the config file
chmod 600 ~/.ssh/config

#!/bin/sh

# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$ENCRYPT_PASSPHRASE" \
--output oauth2_creds.json oauth2_creds.json.gpg
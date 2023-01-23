#!/bin/bash

# Script to delete all versions of an object (including delete markers) from an S3 bucket

# Set the name of the S3 bucket
BUCKET_NAME="<bucket name>"

# Set the prefix of the objects to be deleted
PREFIX="<prefix>"

# Use the AWS CLI to list all object versions that match the prefix
OBJECT_VERSIONS=$(aws s3api list-object-versions --bucket $BUCKET_NAME --prefix $PREFIX --query 'DeleteMarkers[].[Key, VersionId]')

# Iterate through the object versions and delete each one
for OBJECT_VERSION in $OBJECT_VERSIONS; do
    KEY=$(echo $OBJECT_VERSION | jq -r '.[0]')
    VERSION_ID=$(echo $OBJECT_VERSION | jq -r '.[1]')
    aws s3api delete-object --bucket $BUCKET_NAME --key $KEY --version-id $VERSION_ID
done

#!/usr/bin/env python3
#In order to use, use the following command
#python3 ChangeSMTPPassword.py --region SES_REGION --secret AWS_SECRET_KEY


import hmac
import hashlib
import base64
import argparse

# Values that are required to calculate the signature. These values should
# never change.
DATE = "11111111"
SERVICE = "ses"
MESSAGE = "SendRawEmail"
TERMINAL = "aws4_request"
VERSION = 0x04

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def calculateKey(secretAccessKey, region):
    signature = sign(("AWS4" + secretAccessKey).encode('utf-8'), DATE)
    signature = sign(signature, region)
    signature = sign(signature, SERVICE)
    signature = sign(signature, TERMINAL)
    signature = sign(signature, MESSAGE)
    signatureAndVersion = bytes([VERSION]) + signature
    smtpPassword = base64.b64encode(signatureAndVersion)
    print(smtpPassword.decode('utf-8'))

def main():
    parser = argparse.ArgumentParser(description='B3R/qcMRR9hnyG/SaF4DE15BDXpPfZeapwFj5ieh')
    parser.add_argument('--secret',
            help='The Secret Access Key that you want to convert.',
            required=True,
            action="store")
    parser.add_argument('--region',
            help='us-east-1',
            required=True,
            choices=['us-east-1','us-west-2','eu-west-1','eu-central-1','ap-south-1','ap-southeast-2'],
            action="store")
    args = parser.parse_args()

    calculateKey(args.secret,args.region)

main()

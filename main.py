#!/usr/bin/env python
import yaml
import boto3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def credsFile():
    with open("credentials/config.yaml", 'r') as ymlfile:
        return yaml.load(ymlfile)


def main(cfg):
    s3 = boto3.client('s3')
    for ingress in cfg["s3"]["ingress"]:
        print(ingress)
        fileObjs = s3.list_objects(Bucket=cfg["s3"]["bucket"], Prefix=ingress)
        for fileObj in fileObjs["Contents"]:
            key = fileObj["Key"]
            if "$folder$" in key:
                logger.info(key)
                s3.delete_object(Bucket=cfg["s3"]["bucket"], Key=key)


if __name__ == "__main__":
    cfg = credsFile()
    main(cfg)

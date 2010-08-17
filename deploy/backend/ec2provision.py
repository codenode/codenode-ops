#!/usr/bin/env python
import os
import sys
import time

import boto


def run_instance(conn, id, key_name=None, security_groups=None, user_data=None, timeout=200, cntstep=5):
    print "Running instance with id '%s' using key_name '%s'" % (id, key_name)
    instances = conn.run_instances(id, key_name=key_name, security_groups=security_groups, user_data=user_data)
    instance = instances.instances[0]
    print "===Waiting %d seconds for instance to be running...===" % timeout
    cnt = 0
    while instance.update() != "running":
        cnt += cntstep
        time.sleep(cntstep)
        print "Waiting for instance to be running now for %d seconds..." % cnt
        if cnt == timeout:
            print "FAILED: Timeout reached! Stopping Instance and aborting"
            instance.stop()
            return None 
    return instance


def main():
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    KEYPAIR_NAME = os.getenv('KEYPAIR_NAME')
    AMI_ID = os.getenv('AMI_ID')
    SECURITY_GROUPS = os.getenv('SECURITY_GROUPS')
    USER_DATA = os.getenv('USER_DATA')
    PUBLIC_IP = os.getenv('PUBLIC_IP')

    if not (AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY and KEYPAIR_NAME and AMI_ID):
        print "export AWS_ACCESS_KEY & AWS_SECRET_ACCESS_KEY & KEYPAIR_NAME & AMI_ID"
        sys.exit(1)

    conn = boto.connect_ec2(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)
    instance = run_instance(conn, AMI_ID, key_name=KEYPAIR_NAME, security_groups=SECURITY_GROUPS, user_data=USER_DATA)
    instance.associate_address(instance.id, PUBLIC_IP)
    if instance is None:
        sys.exit(1)

    print "SUCCESS.  hostname is '%s'" % (instance.dns_name,) 


if __name__ == "__main__":
    main()


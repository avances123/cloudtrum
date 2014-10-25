grunt --force
s3cmd -r del  s3://www.cloudtrum.xyz/ --force
s3cmd -r put dist/* s3://www.cloudtrum.xyz/

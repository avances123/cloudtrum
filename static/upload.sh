s3cmd -r del  s3://cloudtrum.fabio.rueda.guru/ --force
s3cmd -r put dist/* s3://cloudtrum.fabio.rueda.guru/

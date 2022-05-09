#!/bin/sh

docker exec -i electrify_mariadb mysql -uroot -proot < electrify.sql

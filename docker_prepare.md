# Connecting to a database

## Oracle

Get the oracle docker image

docker pull container-registry.oracle.com/database/free:latest

```bash
docker run --name oracle-container -p 1521:1521 -e ORACLE_PWD=testpassword container-registry.oracle.com/database/free:latest
```


## MongoDB

Get the mongodb image

docker pull mongo

```bash
docker run -d --name mongo-container -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=test -e MONGO_INITDB_ROOT_PASSWORD=testpassword mongo
```
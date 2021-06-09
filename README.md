

# user defined network

docker create network griddb-net

# server with persistent storage 

docker volume create griddb-data

cd server && \
    docker build -t griddb-server . && \
    docker run --network griddb-net --name griddb-server --mount source=griddb-data,target=/var/lib/gridstore/data -d -t griddb-server


# server with temporary storage

cd server && \
    docker build -t griddb-server . && \
    docker run --network griddb-net --name griddb-server -d -t griddb-server

# lookup griddb-server IP

CONT=`docker ps | grep griddb-server | awk '{ print $1 }'`
docker exec $CONT cat /etc/hosts | grep $CONT | awk '{ print $1 }'

# python

cd python && \
    docker build -t griddb-python . && \
    docker run --network griddb-net -t griddb-python

# java 

cd java && \
    docker build -t griddb-java . && \
    docker run --network griddb-net -t griddb-java

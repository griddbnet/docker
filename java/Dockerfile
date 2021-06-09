FROM centos:7

RUN yum install -y java-1.8.0-openjdk-devel
RUN rpm -Uvh https://github.com/griddb/griddb_nosql/releases/download/v4.2.1/griddb_nosql-4.2.1-1.linux.x86_64.rpm

ADD Sample1.java /

ENV CLASSPATH /usr/share/java/gridstore.jar:$CLASSPATH

RUN javac Sample1.java

CMD java Sample1

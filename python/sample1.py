#!/usr/bin/python3

import datetime
import griddb_python as griddb
import sys

factory = griddb.StoreFactory.get_instance()

argv = sys.argv

blob = bytearray([65, 66, 67, 68, 69, 70, 71, 72, 73, 74])
update = True

#Get GridStore object
gridstore = factory.get_store(
        notification_member="griddb-server:10001",
        cluster_name="defaultCluster",
        username="admin",
        password="admin"
        )

#Create Collection
conInfo = griddb.ContainerInfo("testrespycol01",
        [["ts", griddb.Type.TIMESTAMP],
        ["name", griddb.Type.STRING],
        ["status", griddb.Type.BOOL],
        ["count", griddb.Type.LONG],
        ["lob", griddb.Type.BLOB]],
        griddb.ContainerType.COLLECTION, row_key=False)
col = gridstore.put_container(conInfo)

    #Change auto commit mode to false
col.set_auto_commit(False)

ts = datetime.datetime.now()
#Set an index on the Row-key Column
col.create_index("ts", griddb.IndexType.DEFAULT)
#Set an index on the Column
col.create_index("name", griddb.IndexType.DEFAULT)

#Put row: RowKey is "name01"
ret = col.put([ts, "name01", False, 1, blob])

#Put row: RowKey is "name02"
col.put([ts, "name02", False, 1, blob])
col.commit();

#Create normal query
print("ts="+str(int(ts.timestamp()*1000)))
query=col.query("select * where ts < TO_TIMESTAMP_MS("+str(int(ts.timestamp()*1000))+")")

#Execute query
rs = query.fetch(update)
while rs.has_next():
        data = rs.next()
        print(repr(data))

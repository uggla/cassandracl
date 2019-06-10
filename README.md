# Commands

```
root@a7ed23c9cda6:/# export JVM_OPTS="-Xmx64M -Xms64M"; nodetool status system_traces
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address          Load       Tokens       Owns (effective)  Host ID                               Rack
UN  188.166.28.4     317.88 KiB  256          66.8%             468bad1a-45a1-4e55-b085-4b0930d86eb8  rack1
UN  188.166.17.31    308.33 KiB  256          67.3%             8ab2281d-5e2b-4596-bbd2-ba4169ba0b10  rack1
UN  178.128.241.124  293.15 KiB  256          65.8%             a1427441-a7ce-417c-bf0e-503ec9714998  rack1

root@a7ed23c9cda6:/# cqlsh
Connected to Test Cluster at 127.0.0.1:9042.
[cqlsh 5.0.1 | Cassandra 3.11.4 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh> SELECT * from system
system.              system_auth.         system_distributed.  system_schema.       system_traces.       
cqlsh> SELECT * from system_schema.keyspaces 
   ... ;

 keyspace_name      | durable_writes | replication
--------------------+----------------+-------------------------------------------------------------------------------------
            cycling |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
        system_auth |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
      system_schema |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
 system_distributed |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
             system |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
      system_traces |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '2'}
```

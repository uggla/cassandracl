#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cassandra.cluster import Cluster

cluster = Cluster(["node-1.uggla.fr", "node-2.uggla.fr", "node-3.uggla.fr"])
session = cluster.connect("system_schema")
query = session.execute("SELECT * from system_schema.keyspaces")
keyspaces = [keyspace.keyspace_name for keyspace in query]
keyspaces.remove("system")
keyspaces.remove("system_schema")

for keyspace in keyspaces:
    print(keyspace)
    print("Changing replication")
    cmd = (
        "ALTER KEYSPACE "
        + keyspace
        + " WITH REPLICATION = "
        + " { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }"
    )
    print(cmd)
    replication = session.execute(cmd)

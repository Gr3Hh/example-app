## Installation
`helm install --name postgresql -f values.default.yaml oci://registry-1.docker.io/bitnamicharts/postgresql`


A database has been made here just to have it.  
The database must be a separate service. Or if you really need to keep it in a cluster, then you need to create a separate node group.  
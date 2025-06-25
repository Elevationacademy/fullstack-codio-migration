In the previous page, we've seen many kinds of DNS servers. All of them together implement the DNS distributed service. The servers store information in the form of **resource records** (RRs). Each DNS reply message carries one or more resource records. We provide a brief overview of selected DNS record types.

A resource record is a four-tuple that contains the following fields:

**(Name, Value, Type, TTL)**

TTL is the time to live of the resource record, it determines when a resource should be removed from a cache. The meaning of Name and Value depend on record Type, as we will see now.

### "A" record

If Type is A, then Name is a domain name and Value is the **IP address** for the domain. Thus, a Type A record provides the standard hostname-to-IP address mapping. As an example, `(docs.google.com, 145.37.93.126, A, 60)` is a Type A record. A records are stored in an authoritative DNS servers.

### "NS" record
If Type is NS, then Name is a domain and Value is the hostname of an **authoritative DNS server** that knows how to obtain the IP addresses for hosts in the domain. This record is used to route DNS queries further along in the query chain. As an example, `(google.com, ns1.google.com, NS, 300)` is a Type NS record. NS records are stored in top-level domain DNS servers. 

### "CNAME" record

If Type is CNAME, then Value is a canonical hostname for the alias hostname Name. This record can provide querying hosts the canonical name for a hostname. As an example, `(my-branch.com, my-new-branch-name.com, CNAME, 3600)` is a CNAME record.


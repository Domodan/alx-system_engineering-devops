# Design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored

## Must have
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients(data collector for Sumologic or other monitoring services)

## Questions

* Why did we add each additional element?
    firewall protects us hacks?infiltration/penetration, ssl protects others from collecting user data, monitors servers
* What are firewalls for?
    protect from infiltration/penetrations/virus
* Why is the traffic served over HTTPS?
    To protect user data
* What is monitoring used for?
    monitoring is used to check on server that it is working
* How does the monitoring tool collect data?

* Explain what to do if you want to monitor your web server QPS?
    

## What are the issues with this infrastructure?

* Why terminating SSL at the load balancer level is an issue?

* Why having only one MySQL server capable of accepting writes is an issue?

* Why having servers with all the same components (database, webserver and application server) might be a problem?


* [URL to design of a three server web infrastructure](https://drive.google.com/file/d/1NJr8HIbK8uC6w87_3_fbGiFhrNuuLWCs/view?usp=drive_link)

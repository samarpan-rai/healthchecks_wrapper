=====
Usage
=====

To use HealthChecks Context Manager in a project with sample health check
::
  
  from healthchecks_wrapper import HealthCheck
  
  with HealthCheck("https://hc-ping.com/b2b308a5-765c-4136-8d0a-2ff0b906e3ee"):
    # Your job
      ...


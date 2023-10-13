on 15th october 2023, we experienced server outage on all our server infrastructure which resulted in our clients inability to use our services and we sincerely apologize for the financial loss and frustration our clients have incurred during this period.


Timeline:

2:30 PM: The issue was first detected through automated monitoring alerts, indicating a sudden spike in server response times.

2:35 PM: Engineers were notified of the issue and began investigating the problem. Initial assumption was high traffic due to a marketing campaign.

2:50 PM: After investigating server metrics and logs, it was noticed that only a few servers were receiving traffic, while others remained idle.

3:15 PM: The team initially suspected a network issue but couldn't find any abnormalities. The issue was escalated to the infrastructure team.

4:00 PM: Further analysis of load balancer configurations revealed the misconfiguration. The misconfigured rule was promptly corrected.

5:45 PM: After the correction, the service was gradually restored to normal operations, and users could access the platform without errors


Root Cause:
The root cause of the outage was identified as a misconfigured load balancer. Due to an erroneous update in the load balancer configuration, incoming traffic was not being properly distributed among the application servers. As a result, the servers became overloaded, causing a cascade failure and ultimately leading to the service downtime.


Ways to prevent it from happening again:
Task 1: Develop and implement an automated load balancer configuration validation tool by the end of the month.

Task 2: Conduct a comprehensive review of all load balancer rules bi-weekly to identify and rectify potential misconfigurations.

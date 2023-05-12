As professional programmers, we know that despite our best efforts, things can go wrong in our projects. Bugs, crashes, and failures are an inevitable part of the development process. But what sets successful teams apart is their ability to learn from these mistakes and use that knowledge to improve future projects. That's where the post-mortem comes in.

A post-mortem is a formal process of analyzing what went wrong in a project, how it happened, and what can be done to prevent similar issues in the future. It's not about pointing fingers or assigning blame, but rather about taking an objective and honest look at what happened and what can be learned from it.

The first step in a post-mortem is to gather as much information as possible. This includes reviewing code, logs, and documentation, as well as interviewing team members involved in the project. The goal is to create a detailed timeline of events leading up to the issue and identify any contributing factors.

Next, the team should identify the root cause of the issue. This is often more complex than it may seem, as there may be multiple factors that contributed to the problem. It's important to dig deep and not settle for surface-level explanations.

Once the root cause has been identified, the team can move on to identifying solutions. This could involve changes to processes, tools, or even team composition. It's important to prioritize these solutions and create a plan for implementing them.

Finally, the team should document the entire post-mortem process and share it with relevant stakeholders. This helps ensure that everyone is aware of what went wrong and what steps are being taken to prevent similar issues in the future.

While post-mortems may seem like a lot of work, they are an essential part of any successful development process. By taking the time to learn from mistakes and make changes based on that knowledge, we can improve not only our current projects but also our future ones. So don't be afraid to embrace the post-mortem – it may just be the key to your team's success.

# BooktifuL requests failure report
Last week, it was reported that the BooktifuL platform was returning 500 Error on all requests made on the platform routes, all the services were down.  90% of the users were affected. The root cause was the failure of our master server web-01.

## Timeline
The error was realized on Saturday 26th February 1200 hours (East Africa Time) when our Site Reliability Engineer, Mr Elie saw the master server lagging in speed. Our engineers on call disconnected the master server web-01 for further system analysis and channelled all requests to client server web-02. They soled problem by Sunday 27th Febraury 2200 hours (East Africa Time).

## Root cause and resolution
The BooktifuL platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a results of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards. 


The issue was fixed when the master server was temporarily disconnected for memory clean-up then connected back to the loadbalancer and round-robin algorithm was configured so that both the master and client servers can handle equal amount of requests.

## Measures against such problem in future
- Choose the best loadbalancing algorithm for your programs
- Always keep an eye on your servers to ensure they are running properly
- Have extra back-up servers to prevent your program fro completely going offline during an issue

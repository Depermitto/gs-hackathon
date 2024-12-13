# Problem statement

Create an application, website, algorithm, or any other tool, that can be used to automatically
evaluate web application security.

# Brief context

Web application security is paramount in today's digital landscape as it protects sensitive data
from unauthorized access and cyber threats. With the increasing reliance on web applications
for personal, financial, and business transactions, robust security measures are essential to
prevent data breaches, financial loss, and reputational damage. Effective security practices help
safeguard user information, maintain trust, and comply with regulatory requirements, making it
a fundamental aspect of modern web development.

# Example of vulnerabilities

Consider that you are given a web application to test its security. Your task is to develop an
automated solution that will help you identify potential vulnerabilities in the service. It is up to
you to determine which risks you want to target. A few possibilities are described below

- Assume you are given an Open API specification of an API application that is open to the
public. The API has an authorization mechanism, and all endpoints specify which
users/roles can access them. Your solution should ensure that these declarations are
fulfilled and that no unauthorized users can access restricted endpoints. For example, if
the endpoint /employees/all is defned to be accessible only by HR members, no other
user should be able to query this data.
- Assume you are given the same Open API defnition as in the previous point. This time,
the specifcation states how invalid input is handled, so you can test the API against its
declarations and report how bad actors might exploit the service using the API. For
instance, if the endpoint *\/alerts\/subscribe?email=<email\>* accepts an email as input
and is supposed to respond with a 403 Invalid Input status for non-email inputs, you
should verify this behavior.
- Assume you are given an application that has implemented an authentication
mechanism. Your task is to monitor the user session and identify whether the
authentication flow follows best practices, such as using the HTTPS protocol, having
the Secure fag enabled on authentication cookies, implementing session timeouts, and
using Multi-Factor Authentication (MFA).
The task is open to interpretation, so feel free to come up with other security testing
methodologies of your choice.

# Summary

The task is to develop an application, service, or website that will provide an interface to
automatically test the web application and its API. Remember, part of the task is to create a
presentation of the idea, which will be as important as the code. Make sure to talk to the mentors!

## Scoring criteria

- 10 points for innovation
- 10 points for level of impact
- 20 points for level of implementation
- 10 points for user experience

Every team needs to prepare a max 5-minutes video explaining and showcasing their solution.
The video should be uploaded to Lockbox under a directory named with the team's name.
Additionally, there can be other resources submitted - e.g. text file with link to Git repository or a
to a demo application. After the first round, judges will pick the three best teams to present live
during the finals, followed by the Q&A. Good luck!

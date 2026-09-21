---
title: 'OOPs Demo using SOC APP'
author: Vishwas K Singh
mainfont: 'Noto Sans'
fontsize: 12pt
...

# OOPs Demo using SOC APP
Let's build a small **Security Incident Management System** using Python OOP.

## 1. Real-world scenario

Imagine a SOC (Security Operations Center) receives alerts:

```text
Alert #1001
Source IP: 192.168.1.50
Type: Brute Force
Severity: HIGH
Status: OPEN
```

The security team needs to:

* Create an incident
* Store incident information
* Change its status
* Assign it to an analyst
* Escalate critical incidents
* Display incident details
* Keep track of multiple incidents

OOP is a natural fit because each **security incident can be represented as an object**.

---

# 2. Create a `SecurityIncident` class

```python
class SecurityIncident:

    def __init__(self, incident_id, attack_type, source_ip, severity):
        self.incident_id = incident_id
        self.attack_type = attack_type
        self.source_ip = source_ip
        self.severity = severity
        self.status = "OPEN"
        self.assigned_to = None

    def assign(self, analyst):
        self.assigned_to = analyst

    def close(self):
        self.status = "CLOSED"

    def display(self):
        print(f"Incident ID : {self.incident_id}")
        print(f"Attack Type : {self.attack_type}")
        print(f"Source IP   : {self.source_ip}")
        print(f"Severity    : {self.severity}")
        print(f"Status      : {self.status}")
        print(f"Analyst     : {self.assigned_to}")
```

---

# 3. Create an incident object

```python
incident1 = SecurityIncident(
    1001,
    "Brute Force",
    "192.168.1.50",
    "HIGH"
)
```

Think of it like this:

```text
SecurityIncident
       │
       │ creates
       ↓
   incident1
       │
       ├── incident_id = 1001
       ├── attack_type = "Brute Force"
       ├── source_ip = "192.168.1.50"
       ├── severity = "HIGH"
       ├── status = "OPEN"
       └── assigned_to = None
```

---

# 4. Use the object's methods

Assign the incident:

```python
incident1.assign("Vishwas")
```

Close it:

```python
incident1.close()
```

Display it:

```python
incident1.display()
```

Output:

```text
Incident ID : 1001
Attack Type : Brute Force
Source IP   : 192.168.1.50
Severity    : HIGH
Status      : CLOSED
Analyst     : Vishwas
```

This is the basic idea of OOP:

> **Data + operations on that data are grouped together inside an object.**

---

# 5. Now create multiple security incidents

```python
incident1 = SecurityIncident(
    1001,
    "Brute Force",
    "192.168.1.50",
    "HIGH"
)

incident2 = SecurityIncident(
    1002,
    "Port Scanning",
    "10.10.20.15",
    "MEDIUM"
)

incident3 = SecurityIncident(
    1003,
    "Malware",
    "172.16.5.25",
    "CRITICAL"
)
```

Now you have:

```text
incident1 → Brute Force
incident2 → Port Scanning
incident3 → Malware
```

Each object has its own data but uses the same class definition.

---

# 6. Put incidents into a list

A SOC application could maintain:

```python
incidents = [
    incident1,
    incident2,
    incident3
]
```

Then:

```python
for incident in incidents:
    incident.display()
    print("----------------")
```

This is much cleaner than creating separate variables for every piece of information.

---

# 7. Encapsulation

One important OOP concept is **encapsulation**.

Suppose you don't want every part of your application directly modifying an incident's status.

Instead of:

```python
incident1.status = "CLOSED"
```

you provide:

```python
incident1.close()
```

The class controls how its data is changed.

For example:

```python
def close(self):

    if self.status == "OPEN":
        self.status = "CLOSED"
        print("Incident closed")
    else:
        print("Incident is already closed")
```

Now the class can enforce rules.

This is particularly useful in security applications because you often have rules around:

* incident status
* severity
* authorization
* escalation
* analyst assignment
* audit logging

---

# 8. Add security rules

Let's improve our class.

```python
class SecurityIncident:

    def __init__(self, incident_id, attack_type, source_ip, severity):
        self.incident_id = incident_id
        self.attack_type = attack_type
        self.source_ip = source_ip
        self.severity = severity
        self.status = "OPEN"
        self.assigned_to = None

    def assign(self, analyst):
        self.assigned_to = analyst

    def close(self):

        if self.severity == "CRITICAL":
            print("Critical incidents require manager approval")

        else:
            self.status = "CLOSED"
            print("Incident closed")

    def escalate(self):

        if self.severity in ["HIGH", "CRITICAL"]:
            print(f"Incident {self.incident_id} escalated")
        else:
            print("Escalation not required")
```

Now:

```python
incident3 = SecurityIncident(
    1003,
    "Ransomware",
    "172.16.5.25",
    "CRITICAL"
)

incident3.close()
```

Output:

```text
Critical incidents require manager approval
```

The **business/security rule lives inside the object**.

---

# 9. Inheritance — different types of security incidents

Now suppose your security team has different incident types:

```text
SecurityIncident
       │
       ├── NetworkIncident
       │
       ├── MalwareIncident
       │
       └── AuthenticationIncident
```

This is where **inheritance** becomes useful.

Base class:

```python
class SecurityIncident:

    def __init__(self, incident_id, source_ip, severity):
        self.incident_id = incident_id
        self.source_ip = source_ip
        self.severity = severity

    def investigate(self):
        print("Generic security investigation")
```

Now create a network incident:

```python
class NetworkIncident(SecurityIncident):

    def investigate(self):
        print(f"Checking network traffic from {self.source_ip}")
```

And a malware incident:

```python
class MalwareIncident(SecurityIncident):

    def investigate(self):
        print(f"Scanning host {self.source_ip} for malware")
```

Create objects:

```python
network_alert = NetworkIncident(
    1001,
    "192.168.1.50",
    "HIGH"
)

malware_alert = MalwareIncident(
    1002,
    "10.10.10.20",
    "CRITICAL"
)
```

Now:

```python
network_alert.investigate()
```

Output:

```text
Checking network traffic from 192.168.1.50
```

And:

```python
malware_alert.investigate()
```

Output:

```text
Scanning host 10.10.10.20 for malware
```

Same method:

```python
investigate()
```

but different behavior.

That's **polymorphism**.

---

# 10. Polymorphism in a SOC application

You could have:

```python
incidents = [
    NetworkIncident(1001, "192.168.1.50", "HIGH"),
    MalwareIncident(1002, "10.10.10.20", "CRITICAL")
]
```

Then simply:

```python
for incident in incidents:
    incident.investigate()
```

Python automatically calls the appropriate implementation.

```text
NetworkIncident
       ↓
investigate()
       ↓
Network investigation


MalwareIncident
       ↓
investigate()
       ↓
Malware investigation
```

The SOC code doesn't need:

```python
if incident_type == "network":
    ...

elif incident_type == "malware":
    ...
```

That is one of the major benefits of OOP.

---

# 11. `__str__` in our cyber example

This connects directly to your previous question.

Instead of:

```python
incident.display()
```

we can implement `__str__`.

```python
class SecurityIncident:

    def __init__(self, incident_id, attack_type, source_ip, severity):
        self.incident_id = incident_id
        self.attack_type = attack_type
        self.source_ip = source_ip
        self.severity = severity

    def __str__(self):
        return (
            f"Incident {self.incident_id}: "
            f"{self.attack_type} from {self.source_ip} "
            f"[{self.severity}]"
        )
```

Now:

```python
incident = SecurityIncident(
    1001,
    "Brute Force",
    "192.168.1.50",
    "HIGH"
)

print(incident)
```

Output:

```text
Incident 1001: Brute Force from 192.168.1.50 [HIGH]
```

That's a **human-friendly representation**.

---

# 12. `__repr__` for debugging

We can also add:

```python
def __repr__(self):
    return (
        f"SecurityIncident("
        f"incident_id={self.incident_id}, "
        f"attack_type='{self.attack_type}', "
        f"source_ip='{self.source_ip}', "
        f"severity='{self.severity}')"
    )
```

Then:

```python
print(incident)
```

uses:

```text
Incident 1001: Brute Force from 192.168.1.50 [HIGH]
```

while:

```python
print(repr(incident))
```

uses:

```text
SecurityIncident(incident_id=1001, attack_type='Brute Force', source_ip='192.168.1.50', severity='HIGH')
```

So in a SOC project:

```text
__str__
   ↓
Analyst-friendly display

__repr__
   ↓
Developer/debugging information
```

---

# 13. The four major OOP concepts using cybersecurity

| OOP concept       | Cybersecurity example                                                        |
| ----------------- | ---------------------------------------------------------------------------- |
| **Encapsulation** | Incident controls its own status/escalation                                  |
| **Inheritance**   | NetworkIncident inherits SecurityIncident                                    |
| **Polymorphism**  | Different incident types implement `investigate()` differently               |
| **Abstraction**   | Analyst calls `investigate()` without needing internal investigation details |

---

## 14. Putting everything together

A simplified SOC design could look like:

```text
                 SecurityIncident
                        │
             ┌──────────┼──────────┐
             ↓          ↓          ↓
        Network       Malware    Auth
        Incident      Incident   Incident
             │          │          │
             ↓          ↓          ↓
        investigate  investigate investigate
             │          │          │
             └──────────┼──────────┘
                        ↓
                 SOC Application
                        │
              ┌─────────┴─────────┐
              ↓                   ↓
         Incident DB          SIEM/Logs
```

And this is the key mindset shift:

**Without OOP:**

```text
incident_id
source_ip
severity
status
assign_incident()
close_incident()
escalate_incident()
```

All potentially scattered throughout the application.

**With OOP:**

```text
SecurityIncident
     │
     ├── data
     │    ├── incident_id
     │    ├── source_ip
     │    ├── severity
     │    └── status
     │
     └── behavior
          ├── assign()
          ├── close()
          ├── escalate()
          └── investigate()
```

That's the fundamental reason OOP is useful for a **cybersecurity/SOC application**: you model real security entities—**incidents, alerts, users, IP addresses, devices, vulnerabilities, threats, and analysts**—as objects that contain both their data and the operations that make sense for them.

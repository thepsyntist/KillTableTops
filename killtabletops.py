
def mainMenuFn():
    print ("\nMenu: \n 1. Malware \n 2. Creds Compromise \n 3. Insider Threat ")
    mainMenu = input("\nEnter your choice: ")
    decide(mainMenu)


def decide(mainMenu):


    if mainMenu == "1":
        print ("Is it on an endpoint/employee system? (y/n)")
        malwareMenu = input("\nEnter your choice: ")
        if malwareMenu == "y":
            print ("\nLog sources to check:\n 1. Local system: WinEvent, Linux syslog, OSQuery logs. \n 2. Network: Web proxy, VPN, CASB Agent logs. \n 3. EDR events.\n")
            exit()
        else: 
            print("Is it on an EC2/Cloud VM instance? (y/n)")
            ec2Menu = input("\nEnter your choice: ")
            if ec2Menu == "y":
                print ("\nLog sources to check:\n 1. Local system: hosted application logs (if configured), EDR logs.\n 2. Cloud logs: VPC flow, CloudTrail, GuardDuty, CloudWatch\n")
                exit()
            else:
                print("Is it on Docker/ECS/EKS environment?(y/n)")
                ecsMenu = input("\nEnter your choice: ")
                if ecsMenu == "y":
                    print("\nLog sources to check:\n 1. Local system: EDR logs, app specific logs (if configured)\n 2.Cloud logs: VPC flow, CloudTrail, CloudWatch\n")
                    exit()
                else:
                    mainMenuFn()

    if mainMenu == "2":
        print ("\nCredential Compromise - log sources:\n 1. SSO Auth (expected vs suspicious activity)\n 2. Email activity \n 3. Cloud Activity from account. \n 4. <user_id> | stats count by index, sourcetype\n")
        exit()
    if mainMenu == "3":
        print ("\nInsider Threat - log sources:\n 1.<user_id> | stats count by index, sourcetype\n 2. Check all accessed\n 3. Downloaded files & sizes\n 4. Confluence, Code repos, Jira activity.\n 5. Proxy/CASB logs for cloud uploads\n") 
        exit()
    else:
        mainMenuFn()

mainMenuFn()
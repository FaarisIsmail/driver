import webbrowser
import os
from kubernetes import client, config



def main():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    print("Welcome to Big Data Processing Application\nPlease type the number that corresponds to which application you would like to run:\n1. Apache Hadoop\n2. Apache Spark\n3. Jupyter Notebook\n4. SonarQube and SonarScanner")
    val = int(input("Type the number here > "))
    if(val == 1):
        print("Apache Hadoop")
    elif(val == 2):
        print("Apache Spark")
    elif(val == 3):
        print("Jupyter Notebook")
        webbrowser.open('http://localhost:8888/?token=7284adc13ac9eca5c7f8fa6ac3f09cf7a2be7d7484613609')
        os.system("docker run -p 8888:8888 jupyter/base-notebook")
    elif(val == 4):
        print("Sonar Scanner")
    else:
        print("Invalid input")

main()

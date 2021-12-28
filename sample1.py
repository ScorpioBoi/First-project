number = int(input("Enter number: "))
n1 = 0
n2 = 1
count = 0
if number <= 0:
    print("Please enter a positive number.")
elif number == 1:
    print("Fibonacci sequence upto", number)
    print(n1)
else:
    print("Fibonacci sequence")
    while count <= number:
        print(n1)
        nextnum = n1 + n2
        n1 = n2
        n2 = nextnum
        count = count + 1
        
        Microsoft Windows [Version 10.0.19043.1415]
(c) Microsoft Corporation. All rights reserved.

C:\Users\DELL>git config --global user.name "ScorpioBoi"

C:\Users\DELL>git config --global user.email "scorpioboi7308@gmail.com"

C:\Users\DELL>git init Sample
Initialized empty Git repository in C:/Users/DELL/Sample/.git/

C:\Users\DELL>cd sample

C:\Users\DELL\Sample>git add sample1.c
fatal: pathspec 'sample1.c' did not match any files

C:\Users\DELL\Sample>git add sample1.py

C:\Users\DELL\Sample>git commit m
error: pathspec 'm' did not match any file(s) known to git

C:\Users\DELL\Sample>git commit -m "this is my first commit"
[master (root-commit) 2758cd1] this is my first commit
 1 file changed, 17 insertions(+)
 create mode 100644 sample1.py

C:\Users\DELL\Sample>git remote add origin https://github.com/ScorpioBoi/First-project.git

C:\Users\DELL\Sample>git push origin master
info: please complete authentication in your browser...
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 403 bytes | 403.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ScorpioBoi/First-project.git
 * [new branch]      master -> master

C:\Users\DELL\Sample>cd git@github.com:ScorpioBoi/First-project.git
The filename, directory name, or volume label syntax is incorrect.

C:\Users\DELL\Sample>cd ..

C:\Users\DELL>cd Sample

C:\Users\DELL\Sample>git clone git@github.com:ScorpioBoi/First-project.git
Cloning into 'First-project'...
The authenticity of host 'github.com (13.234.210.38)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

C:\Users\DELL\Sample>git clone git@github.com:ScorpioBoi/First-project.git
Cloning into 'First-project'...
The authenticity of host 'github.com (13.234.210.38)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? ☺☺☺☺☺The authenticity of host 'github.com (13.234.210.38)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

C:\Users\DELL\Sample>git clone git@github.com
fatal: repository 'git@github.com' does not exist

C:\Users\DELL\Sample>cd ..

C:\Users\DELL>git init project_todo
Initialized empty Git repository in C:/Users/DELL/project_todo/.git/

C:\Users\DELL>cd project_todo

C:\Users\DELL\project_todo>git add project_todo

C:\Users\DELL\project_todo>

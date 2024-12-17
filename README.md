Download the Code from github: https://github.com/iFernandez96/CDN

git clone https://github.com/iFernandez96/CDN

run all steps in their own wsl terminal

NOTE: All steps require you to navigate to the CDN folder you just cloned:
        cd CDN

Step 1. Start Client server.
python3 Client/Client_client.py

Step 2. Start the edge servers.
chmod +x start_edge_server
./start_edge_server

Step 3. Start the Load Balancer
python3 LoadBalancer/LB_server.py

Step 4. Start the Database Server
python3 DataBase/DB_server.py
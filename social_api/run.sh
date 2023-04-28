echo "Containers are going down..."
sudo docker compose down
echo "Deploying locally..."
sudo docker compose up --build

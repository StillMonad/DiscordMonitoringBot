
cd DiscordMonitoringBot
git pull origin main
docker build . -t monitoring
docker stop $(docker ps -a -q)
docker run -d -v SharedVolume:/sharedvolume monitoring

# db path: sqlite3 /var/lib/docker/volumes/SharedVolume/_data/activity_log.db table ActivityLog
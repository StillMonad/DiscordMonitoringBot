
cd DiscordMonitoringBot
git pull origin main
docker build . -t DiscordMonitor
docker stop discord_monitor
docker run --name discord_monitor -d -v SharedVolume:/sharedvolume DiscordMonitor

# db path: sqlite3 /var/lib/docker/volumes/SharedVolume/_data/activity_log.db table ActivityLog

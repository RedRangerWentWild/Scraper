# HP-Pulse Scraper - Production Deployment Guide

## Overview

This guide covers deploying the HP-Pulse scraper to a production Linux server for continuous operation.

## Prerequisites

- Linux server (Ubuntu 20.04+ or similar)
- Python 3.8 or higher
- systemd (for service management)
- Network access to target websites

## Installation Steps

### 1. Setup Server

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Create application user (optional but recommended)
sudo useradd -m -s /bin/bash hppulse
sudo su - hppulse
```

### 2. Deploy Application

```bash
# Create directory
mkdir -p ~/hp-pulse-scraper
cd ~/hp-pulse-scraper

# Copy/clone your code here
# Or use git clone if in a repository

# Install dependencies
pip3 install -r requirements.txt --user
```

### 3. Configure Environment

```bash
# Create .env file from template
cp .env.example .env

# Edit configuration
nano .env
```

**Production .env Example:**
```env
DATABASE_PATH=/home/hppulse/hp-pulse-scraper/hp_pulse.db
TENDER_INTERVAL=1
NEWS_INTERVAL=6
DIRECTORY_INTERVAL=24
REQUESTS_PER_SECOND=1
REQUEST_TIMEOUT=15
USER_AGENT=HP-Pulse-Research-Bot/1.0 (HPCL Direct Sales; contact@yourdomain.com)
LOG_TO_FILE=true
LOG_FILE_PATH=/home/hppulse/hp-pulse-scraper/scraper.log
```

### 4. Test Run

```bash
# Test the scraper
python3 scraper.py

# Should see initialization and scraping activity
# Press Ctrl+C to stop after verifying it works

# Check data
python3 monitor.py
```

## Service Setup (systemd)

### Create Service File

```bash
sudo nano /etc/systemd/system/hp-pulse-scraper.service
```

**Service Configuration:**
```ini
[Unit]
Description=HP-Pulse B2B Lead Intelligence Scraper
After=network.target

[Service]
Type=simple
User=hppulse
WorkingDirectory=/home/hppulse/hp-pulse-scraper
ExecStart=/usr/bin/python3 /home/hppulse/hp-pulse-scraper/scraper.py
Restart=always
RestartSec=10
StandardOutput=append:/home/hppulse/hp-pulse-scraper/scraper.log
StandardError=append:/home/hppulse/hp-pulse-scraper/scraper_error.log

[Install]
WantedBy=multi-user.target
```

### Enable and Start Service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (start on boot)
sudo systemctl enable hp-pulse-scraper

# Start service
sudo systemctl start hp-pulse-scraper

# Check status
sudo systemctl status hp-pulse-scraper

# View logs
sudo journalctl -u hp-pulse-scraper -f
```

## Monitoring

### Check Service Status

```bash
# Service status
sudo systemctl status hp-pulse-scraper

# View recent logs
sudo journalctl -u hp-pulse-scraper -n 50

# Follow logs in real-time
sudo journalctl -u hp-pulse-scraper -f
```

### Monitor Data

```bash
cd /home/hppulse/hp-pulse-scraper

# Quick stats
python3 monitor.py --quick

# Full dashboard
python3 monitor.py

# Export data
python3 monitor.py --export leads_$(date +%Y%m%d).csv
```

### Database Queries

```bash
sqlite3 hp_pulse.db

-- Recent leads
SELECT * FROM leads ORDER BY scraped_at DESC LIMIT 10;

-- Today's stats
SELECT COUNT(*) FROM leads WHERE DATE(scraped_at) = DATE('now');

-- Success rate
SELECT 
    status, 
    COUNT(*) as count 
FROM scrape_log 
GROUP BY status;
```

## Backup & Maintenance

### Database Backup

```bash
# Create backup script
cat > ~/backup_hp_pulse.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/home/hppulse/backups"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
cp /home/hppulse/hp-pulse-scraper/hp_pulse.db $BACKUP_DIR/hp_pulse_$DATE.db
# Keep only last 30 days
find $BACKUP_DIR -name "hp_pulse_*.db" -mtime +30 -delete
EOF

chmod +x ~/backup_hp_pulse.sh

# Add to crontab (daily at 2 AM)
(crontab -l 2>/dev/null; echo "0 2 * * * /home/hppulse/backup_hp_pulse.sh") | crontab -
```

### Log Rotation

```bash
# Create logrotate config
sudo nano /etc/logrotate.d/hp-pulse-scraper
```

```
/home/hppulse/hp-pulse-scraper/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    missingok
}
```

## Troubleshooting

### Service Won't Start

```bash
# Check service status
sudo systemctl status hp-pulse-scraper

# Check logs
sudo journalctl -u hp-pulse-scraper -n 100

# Common issues:
# 1. Python not found - check ExecStart path
# 2. Permissions - check file ownership
# 3. Dependencies - ensure all packages installed
```

### No Data Being Collected

```bash
# Check if service is running
sudo systemctl status hp-pulse-scraper

# View real-time logs
sudo journalctl -u hp-pulse-scraper -f

# Check database
sqlite3 hp_pulse.db "SELECT COUNT(*) FROM scrape_log;"

# Common issues:
# 1. Network connectivity
# 2. robots.txt blocking
# 3. Website structure changes
```

### High Resource Usage

```bash
# Check memory/CPU
top -u hppulse

# Adjust intervals in .env
# Increase TENDER_INTERVAL, NEWS_INTERVAL, DIRECTORY_INTERVAL
# Decrease scraping frequency
```

## Service Management Commands

```bash
# Start service
sudo systemctl start hp-pulse-scraper

# Stop service
sudo systemctl stop hp-pulse-scraper

# Restart service
sudo systemctl restart hp-pulse-scraper

# Disable service (prevent auto-start)
sudo systemctl disable hp-pulse-scraper

# View logs
sudo journalctl -u hp-pulse-scraper -f
```

## Security Considerations

1. **User Permissions**: Run as dedicated user, not root
2. **Database**: Ensure database file has appropriate permissions (600)
3. **Environment File**: Protect .env file (chmod 600 .env)
4. **Network**: Consider firewall rules if scraper needs to be restricted
5. **User Agent**: Always use descriptive user agent with contact info

## Performance Tuning

### Adjust Scraping Intervals

Edit `.env`:
```env
# More frequent (for demo/testing)
TENDER_INTERVAL=0.5
NEWS_INTERVAL=2
DIRECTORY_INTERVAL=12

# Less frequent (production)
TENDER_INTERVAL=2
NEWS_INTERVAL=12
DIRECTORY_INTERVAL=48
```

### Database Optimization

```bash
sqlite3 hp_pulse.db

-- Vacuum database (reclaim space)
VACUUM;

-- Analyze for query optimization
ANALYZE;
```

## Updating the Application

```bash
# Stop service
sudo systemctl stop hp-pulse-scraper

# Backup database
cp hp_pulse.db hp_pulse_backup_$(date +%Y%m%d).db

# Update code
# (git pull or copy new files)

# Install any new dependencies
pip3 install -r requirements.txt --user

# Restart service
sudo systemctl start hp-pulse-scraper

# Verify
sudo systemctl status hp-pulse-scraper
```

## Support Checklist

Before seeking help, gather:
- [ ] Service status: `sudo systemctl status hp-pulse-scraper`
- [ ] Recent logs: `sudo journalctl -u hp-pulse-scraper -n 100`
- [ ] Database stats: `python3 monitor.py --quick`
- [ ] Configuration: Check .env file
- [ ] System resources: `top`, `df -h`

---

**Deployment Ready!** 🚀

For questions or issues, check the main README.md and code comments.

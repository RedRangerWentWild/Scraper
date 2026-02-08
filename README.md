# HP-Pulse Scraper

**B2B Lead Intelligence System for HPCL Direct Sales**

Automated, policy-compliant web scraper that monitors government tenders, news sources, and business directories to identify potential HPCL customers.

---

## 🎯 Features

### ✅ Multi-Source Scraping
- **Government Tenders** (every 1 hour): CPP Portal, GEM
- **News Sources** (every 6 hours): Economic Times, Business Standard, Hindu Business Line
- **Business Directories** (every 24 hours): IndiaMART, TradeIndia

### ✅ Policy-Compliant
- Respects `robots.txt`
- Rate limiting (1 request/second per domain)
- Provenance logging (every fact traceable)
- Source registry with trust scores

### ✅ Intelligent Detection
- Keyword matching for fuel products (HSD, FO, Bitumen, Hexane, etc.)
- Operational cue detection (boilers, furnaces, expansions)
- Company name extraction
- Confidence scoring

### ✅ Production-Ready
- SQLite database with full audit trail
- Error handling and retry logic
- Comprehensive logging
- Monitoring dashboard

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt --break-system-packages
```

### 2. Start Scraper

```bash
python scraper.py
```

The scraper will:
1. Initialize the database
2. Run initial scrape of all sources
3. Continue running on schedule (tenders hourly, news 6h, directories daily)

### 3. Monitor Progress

In another terminal:

```bash
# Full dashboard
python monitor.py

# Quick stats
python monitor.py --quick

# Or watch continuously
watch -n 30 python monitor.py
```

### 4. Query Database

```bash
sqlite3 hp_pulse.db

# View recent leads
SELECT * FROM leads ORDER BY scraped_at DESC LIMIT 10;

# View scrape log
SELECT * FROM scrape_log ORDER BY scraped_at DESC;

# Exit
.quit
```

---

## 📁 Project Structure

```
hp-pulse-scraper/
├── scraper.py              # Main scheduler (START HERE)
├── monitor.py              # Monitoring dashboard
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── README.md              # This file
│
├── scrapers/              # Scraper modules
│   ├── tender_scraper.py  # Government tenders
│   ├── news_scraper.py    # News sources
│   └── directory_scraper.py # Business directories
│
├── utils/                 # Utilities
│   ├── database.py        # SQLite operations
│   └── compliance.py      # Policy-safe scraping
│
└── hp_pulse.db           # SQLite database (created on first run)
```

---

## ⚙️ Configuration

Edit `config.py` to customize:

### Scraping Intervals
```python
TENDER_INTERVAL = 1      # Hours
NEWS_INTERVAL = 6        # Hours
DIRECTORY_INTERVAL = 24  # Hours
```

### Keywords
```python
FUEL_KEYWORDS = [
    'fuel', 'diesel', 'HSD', 'furnace oil', 'FO',
    'bitumen', 'hexane', 'lubricant', ...
]
```

### Sources
```python
SOURCES = {
    'tenders': {
        'sources': [
            {
                'name': 'CPP Portal',
                'url': '...',
                'enabled': True,
                'trust_score': 10
            }
        ]
    }
}
```

---

## 📊 Database Schema

### `companies`
- Company profile (name, industry, location)
- Automatic deduplication

### `leads`
- Signal text (news/tender content)
- Signal type (tender/news/directory)
- Products mentioned
- Confidence score
- Source provenance

### `scrape_log`
- Every scrape attempt logged
- Status (success/error)
- Items found
- Timestamp

### `source_registry`
- Domain tracking
- robots.txt compliance
- Trust scores

---

## 🎬 For Demo/Video

### Show Scraper Running
```bash
# Start scraper (shows activity in real-time)
python scraper.py

# In another window, monitor
watch -n 10 python monitor.py
```

### Query Results
```bash
# Open database
sqlite3 hp_pulse.db

# Show stats
SELECT 
    signal_type, 
    COUNT(*) as count 
FROM leads 
GROUP BY signal_type;

# Show recent high-value leads
SELECT 
    c.name as company,
    l.signal_text,
    l.confidence
FROM leads l
JOIN companies c ON l.company_id = c.id
WHERE l.confidence > 0.8
ORDER BY l.scraped_at DESC
LIMIT 5;
```

### Stop Scraper
```bash
# Press Ctrl+C in scraper window
# Shows final statistics automatically
```

---

## 🛡️ Compliance Features

### robots.txt Checking
- Automatically fetches and parses robots.txt
- Caches results to avoid repeated requests
- Blocks scraping if disallowed

### Rate Limiting
- Maximum 1 request per second per domain
- Prevents server overload
- Logged in console output

### Provenance Logging
- Every lead links to source URL
- Timestamp recorded
- Source name and trust score tracked

### Audit Trail
- All scrape attempts logged
- Success/failure tracking
- Error messages preserved

---

## 🔧 Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt --break-system-packages
```

### "Database is locked"
```bash
# Only one scraper.py instance can run at a time
pkill -f scraper.py
python scraper.py
```

### "No items found"
- Check internet connection
- Some sites may require authentication (CPP Portal, GEM)
- Verify source URLs in config.py

### "robots.txt blocking"
- Normal for some sites
- Adjust USER_AGENT in config.py
- Add your contact email

---

## 📈 Scaling

### Add More Sources
Edit `config.py` and add to SOURCES dict:

```python
SOURCES['news']['sources'].append({
    'name': 'Your News Source',
    'url': 'https://example.com',
    'rss': 'https://example.com/feed',  # Optional
    'enabled': True,
    'trust_score': 8
})
```

### Adjust Intervals
```python
# Check tenders more frequently
TENDER_INTERVAL = 0.5  # Every 30 minutes

# Check news less frequently  
NEWS_INTERVAL = 12     # Twice per day
```

### Run in Background
```bash
# Linux/Mac
nohup python scraper.py > scraper.log 2>&1 &

# View logs
tail -f scraper.log

# Stop
pkill -f scraper.py
```

---

## 💾 Backup Data

```bash
# Backup database
cp hp_pulse.db hp_pulse_backup_$(date +%Y%m%d).db

# Export to CSV
sqlite3 hp_pulse.db << EOF
.headers on
.mode csv
.output leads_export.csv
SELECT * FROM leads;
.quit
EOF
```

---

## 🎯 HPCL-Specific Features

### Product Keywords
Searches for HPCL products:
- **Fuels**: MS, HSD, LDO, FO, LSHS, SKO
- **Specialty**: Hexane, Solvent 1425, JBO, MTO, Propylene
- **Lubricants**: HP Milcy, HP Racer4, HP Enklo, HP Lithon
- **Other**: Bitumen, Marine Bunker Fuel, Sulphur

### Industry Focus
Monitors key industries:
- Power generation (boilers, gensets, captive power)
- Infrastructure (highways, road construction)
- Manufacturing (textiles, chemicals, pharmaceuticals)
- Marine (shipping, ports)

### Confidence Scoring
- **High (0.8-1.0)**: Explicit tenders with fuel mentions
- **Medium (0.5-0.8)**: News about expansions in relevant industries
- **Low (0.3-0.5)**: Directory listings in target sectors

---

## 📝 License

Proprietary - HPCL Productathon 2026

---

## 🤝 Support

For issues or questions:
1. Check this README
2. Review `config.py` for settings
3. Check `scraper.log` for errors
4. Query database directly with SQLite

---

## 🎓 Technical Details

**Built with:**
- Python 3.8+
- BeautifulSoup4 (HTML parsing)
- Requests (HTTP client)
- Schedule (job scheduling)
- Feedparser (RSS feeds)
- SQLite (database)

**Architecture:**
- Modular design (scrapers, utils, config separated)
- Event-driven (scheduled jobs)
- Database-backed (persistent storage)
- Compliance-first (robots.txt, rate limiting, logging)

---

**🚀 Ready to start? Run `python scraper.py`**

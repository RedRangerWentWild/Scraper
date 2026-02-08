# HP-Pulse Demo Dataset Summary

## Overview
Generated **30 high-quality demo leads** across 3 categories (10 each):
- ✅ 10 Tenders (88-98% confidence)
- ✅ 10 News items (55-75% confidence)  
- ✅ 10 Directory listings (28-42% confidence)

---

## ⏰ Automated Scheduling

### How the Scraper Works

When you run `python3 scraper.py`, it:
1. **Runs initial scrape** of all sources immediately
2. **Sets up scheduled jobs** that run continuously
3. **Keeps running** until you press Ctrl+C

### Scraping Intervals

| Category | Frequency | Why? |
|----------|-----------|------|
| **Tenders** | Every **1 hour** | Time-sensitive, deadlines are critical |
| **News** | Every **6 hours** | Daily monitoring, 4x per day |
| **Directories** | Every **24 hours** | Static data, changes infrequently |

**Example Timeline:**
```
10:00 AM - Initial scrape (all sources)
11:00 AM - Tenders only
12:00 PM - Tenders only
01:00 PM - Tenders only
04:00 PM - Tenders + News
05:00 PM - Tenders only
10:00 AM (next day) - Tenders + News + Directories
```

> **Note**: `generate_demo_data.py` is a **one-time** script. It doesn't run automatically - you run it manually when you want fresh demo data.

### Source Trust Scores & Domains

**Trust Score Scale**: 1-10 (10 = highest reliability)

#### Tender Sources
| Source | Domain | Trust Score | Alert Frequency |
|--------|--------|-------------|----------------|
| CPP Portal | eprocure.gov.in | **10/10** | Every 1 hour |
| GEM Portal | gem.gov.in | **10/10** | Every 1 hour |

#### News Sources
| Source | Domain | Trust Score | Alert Frequency |
|--------|--------|-------------|----------------|
| Economic Times | economictimes.indiatimes.com | **9/10** | Every 6 hours |
| Business Standard | business-standard.com | **9/10** | Every 6 hours |
| Hindu Business Line | thehindubusinessline.com | **8/10** | Every 6 hours |
| PTI News | ptinews.com | **9/10** | Every 6 hours |

#### Directory Sources
| Source | Domain | Trust Score | Alert Frequency |
|--------|--------|-------------|----------------|
| IndiaMART | indiamart.com | **7/10** | Every 24 hours |
| TradeIndia | tradeindia.com | **7/10** | Every 24 hours |

---

## 📋 TENDER SAMPLES (10 items)

### High-Value Government & Corporate Tenders

| # | Company | Tender Title | Value | Location |
|---|---------|-------------|-------|----------|
| 1 | **Indian Oil Corporation** | HSD Supply - 5000 KL | ₹15 Cr | All India |
| 2 | **NTPC** | Furnace Oil for Thermal Plant | ₹8.5 Cr | Uttar Pradesh |
| 3 | **Tata Steel** | Industrial Lubricants | ₹3.2 Cr | Jamshedpur |
| 4 | **L&T Construction** | Bitumen for Highway | ₹12 Cr | Maharashtra, Gujarat |
| 5 | **Indian Railways** | LDO Annual Contract | ₹6.75 Cr | Kolkata |
| 6 | **Shipping Corp** | Marine Bunker Fuel IFO 380 | ₹18 Cr | Mumbai, Vizag, Chennai |
| 7 | **Reliance Industries** | Hexane for Solvent Unit | ₹4.5 Cr | Jamnagar |
| 8 | **JSW Steel** | HP Racer4 Lubricant | ₹2.8 Cr | Karnataka |
| 9 | **Adani Power** | LSHS for Power Plant | ₹9.25 Cr | Mundra |
| 10 | **HPCL** | Jute Batch Oil | ₹1.95 Cr | Kolkata |

**Total Tender Value**: ~₹82 Crore

---

## 📰 NEWS SAMPLES (10 items)

### Expansion & Growth Signals

| # | Company | Signal | Industry |
|---|---------|--------|----------|
| 1 | **UltraTech Cement** | Capacity expansion with new kilns | Cement Manufacturing |
| 2 | **Vedanta Resources** | New aluminum smelter in Odisha | Mining & Metals |
| 3 | **GMR Infrastructure** | Captive power plant for airport | Infrastructure |
| 4 | **Asian Paints** | New manufacturing facility in Rajasthan | Paint & Coatings |
| 5 | **Essar Steel** | Modernization with new boilers | Steel Manufacturing |
| 6 | **Grasim Industries** | Viscose fiber capacity expansion | Textiles & Chemicals |
| 7 | **Jindal Steel & Power** | Coal gasification project | Steel & Power |
| 8 | **Century Textiles** | Jute processing units upgrade | Textiles |
| 9 | **Ambuja Cements** | Greenfield project in Himachal | Cement Manufacturing |
| 10 | **Hindalco Industries** | Aluminum & power expansion | Metals & Power |

**Key Products Mentioned**: Fuel oil, diesel, hexane, lubricants, JBO, solvents

---

## 📂 DIRECTORY SAMPLES (10 items)

### Fuel & Chemical Industry Companies

| # | Company | Industry | Location |
|---|---------|----------|----------|
| 1 | **Bharat Petroleum Distributors** | Petroleum Distribution | Mumbai |
| 2 | **Supreme Petrochemicals** | Petrochemicals | Vadodara |
| 3 | **Navbharat Furnace Oil** | Fuel Supply & Trading | Delhi NCR |
| 4 | **Eastern Lubricants Mfg** | Lubricants Manufacturing | Kolkata |
| 5 | **Gujarat Chemical Solvents** | Chemical Solvents | Ahmedabad |
| 6 | **Southern Bitumen Products** | Road Construction | Chennai |
| 7 | **Rajasthan Industrial Fuels** | Industrial Fuel Supply | Jaipur |
| 8 | **Maharashtra Hexane Industries** | Specialty Chemicals | Pune |
| 9 | **Punjab Jute Processing** | Textile Processing | Ludhiana |
| 10 | **Karnataka Marine Fuel** | Marine Fuel Supply | Mangalore |

**Geographic Coverage**: 9 states across India

---

## 📊 Statistics

- **Total Companies**: 30
- **Total Leads**: 30
- **Geographic Coverage**: Pan-India
- **Industries Covered**: 15+ sectors
- **Combined Tender Value**: ₹82+ Crore

### Confidence Distribution
- **High (>70%)**: 10 leads (Tenders)
- **Medium (50-70%)**: 10 leads (News)
- **Low (<50%)**: 10 leads (Directories)

---

## 🎯 HPCL Product Coverage

The demo data includes mentions of:
- ✅ HSD (High Speed Diesel)
- ✅ Furnace Oil (FO)
- ✅ LSHS (Low Sulphur Heavy Stock)
- ✅ Marine Bunker Fuel (IFO 380)
- ✅ Light Diesel Oil (LDO)
- ✅ Hexane (Technical Grade)
- ✅ Bitumen (Grade 60/70, 80/100)
- ✅ Jute Batch Oil (JBO)
- ✅ Industrial Lubricants (HP Racer4, etc.)
- ✅ Mineral Turpentine Oil

---

## 📁 Files Generated

1. **`generate_demo_data.py`** - Demo data generator script
2. **`demo_leads.csv`** - Exported CSV with all 30 leads
3. **`hp_pulse.db`** - SQLite database (updated)

---

## 🚀 Usage

### Start Automated Scraping (Runs Continuously)
```bash
python3 scraper.py
# Scrapes immediately, then runs on schedule
# Press Ctrl+C to stop
```

### View Dashboard
```bash
python3 monitor.py              # Full dashboard
python3 monitor.py --quick      # Quick stats
```

### Export Data
```bash
python3 monitor.py --export my_leads.csv
```

### Query Database
```bash
sqlite3 hp_pulse.db
SELECT * FROM leads WHERE signal_type = 'tender';
SELECT * FROM companies WHERE industry LIKE '%Steel%';
SELECT * FROM leads WHERE confidence > 0.8;
```

### Regenerate Demo Data
```bash
python3 generate_demo_data.py
```
*Note: This will clear existing data and create fresh demo dataset*

---

## 🔧 Configuration

You can customize intervals by editing `.env`:

```env
TENDER_INTERVAL=1      # Hours (default: 1)
NEWS_INTERVAL=6        # Hours (default: 6)
DIRECTORY_INTERVAL=24  # Hours (default: 24)
```

**Examples:**
- More frequent monitoring: `TENDER_INTERVAL=0.5` (every 30 min)
- Less frequent: `NEWS_INTERVAL=12` (twice per day)

---

**Generated**: 2026-02-08  
**Dataset Quality**: Production-ready realistic data  
**Use Case**: Demo, testing, proof of concept

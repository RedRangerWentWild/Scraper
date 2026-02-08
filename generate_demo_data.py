#!/usr/bin/env python3
"""
Demo Data Generator for HP-Pulse Scraper
Generates 10 sample items each from tenders, news, and directories
"""

from utils.database import Database
from datetime import datetime, timedelta
import random

def generate_demo_data():
    """Generate comprehensive demo dataset"""
    
    print("\n" + "=" * 70)
    print("🎯 HP-PULSE DEMO DATA GENERATOR")
    print("=" * 70)
    
    db = Database()
    
    # Clear existing data (optional - comment out to keep existing data)
    print("\n⚠️  Clearing existing data...")
    conn = db.get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM leads")
    c.execute("DELETE FROM companies")
    c.execute("DELETE FROM scrape_log")
    conn.commit()
    conn.close()
    
    # ============================================
    # TENDER DATA (10 samples)
    # ============================================
    print("\n📋 Generating 10 TENDER samples...")
    
    tender_data = [
        {
            'company': 'Indian Oil Corporation Limited',
            'title': 'Supply of High Speed Diesel (HSD) - 5000 KL',
            'value': '₹15,00,00,000',
            'location': 'All India',
            'deadline': 25,
            'industry': 'Oil & Gas PSU'
        },
        {
            'company': 'National Thermal Power Corporation',
            'title': 'Furnace Oil Supply for Thermal Power Plant',
            'value': '₹8,50,00,000',
            'location': 'Uttar Pradesh',
            'deadline': 18,
            'industry': 'Power Generation'
        },
        {
            'company': 'Tata Steel Limited',
            'title': 'Procurement of Industrial Lubricants - Various Grades',
            'value': '₹3,20,00,000',
            'location': 'Jamshedpur, Jharkhand',
            'deadline': 30,
            'industry': 'Steel Manufacturing'
        },
        {
            'company': 'Larsen & Toubro Construction',
            'title': 'Bitumen Grade 60/70 for Highway Construction Project',
            'value': '₹12,00,00,000',
            'location': 'Maharashtra, Gujarat',
            'deadline': 22,
            'industry': 'Construction & Infrastructure'
        },
        {
            'company': 'Indian Railways - Eastern Railway',
            'title': 'Light Diesel Oil (LDO) Annual Supply Contract',
            'value': '₹6,75,00,000',
            'location': 'Kolkata, West Bengal',
            'deadline': 15,
            'industry': 'Railways'
        },
        {
            'company': 'Shipping Corporation of India',
            'title': 'Marine Bunker Fuel - IFO 380 for Merchant Fleet',
            'value': '₹18,00,00,000',
            'location': 'Mumbai, Visakhapatnam, Chennai',
            'deadline': 28,
            'industry': 'Shipping & Logistics'
        },
        {
            'company': 'Reliance Industries Limited',
            'title': 'Hexane (Technical Grade) for Solvent Extraction Unit',
            'value': '₹4,50,00,000',
            'location': 'Jamnagar, Gujarat',
            'deadline': 20,
            'industry': 'Petrochemicals'
        },
        {
            'company': 'JSW Steel Limited',
            'title': 'Supply of HP Racer4 Lubricant Oil for Rolling Mills',
            'value': '₹2,80,00,000',
            'location': 'Vijayanagar, Karnataka',
            'deadline': 35,
            'industry': 'Steel Manufacturing'
        },
        {
            'company': 'Adani Power Limited',
            'title': 'Low Sulphur Heavy Stock (LSHS) for Power Plant',
            'value': '₹9,25,00,000',
            'location': 'Mundra, Gujarat',
            'deadline': 12,
            'industry': 'Power Generation'
        },
        {
            'company': 'Hindustan Petroleum Corporation',
            'title': 'Jute Batch Oil (JBO) for Textile Processing',
            'value': '₹1,95,00,000',
            'location': 'Kolkata, West Bengal',
            'deadline': 40,
            'industry': 'Textiles & Processing'
        }
    ]
    
    for i, tender in enumerate(tender_data, 1):
        company_id = db.insert_company(
            name=tender['company'],
            industry=tender['industry'],
            location=tender['location']
        )
        
        deadline = (datetime.now() + timedelta(days=tender['deadline'])).strftime('%Y-%m-%d')
        signal_text = f"""{tender['title']}

Organization: {tender['company']}
Tender Value: {tender['value']}
Submission Deadline: {deadline}
Location: {tender['location']}
Industry: {tender['industry']}
"""
        
        db.insert_lead(
            company_id=company_id,
            signal_text=signal_text,
            signal_type='tender',
            source_name='CPP Portal / GEM',
            source_url='https://eprocure.gov.in',
            confidence=random.uniform(0.88, 0.98)
        )
        
        print(f"   {i:2}. {tender['company'][:50]:50} | {tender['value']:15}")
    
    db.log_scrape('Demo Tender Generator', 'tender', 'success', 10)
    
    # ============================================
    # NEWS DATA (10 samples)
    # ============================================
    print("\n📰 Generating 10 NEWS samples...")
    
    news_data = [
        {
            'company': 'UltraTech Cement Limited',
            'headline': 'UltraTech Cement announces expansion of production capacity with new kilns',
            'summary': 'Major cement manufacturer to invest ₹2,500 crore in expanding operations across three states. New facilities expected to increase fuel oil and diesel consumption by 40%.',
            'source': 'Economic Times - Industry'
        },
        {
            'company': 'Vedanta Resources Limited',
            'headline': 'Vedanta plans new aluminum smelter in Odisha, fuel requirements to surge',
            'summary': 'The mining giant announced plans for a 1.5 million tonne aluminum smelter. Project will require significant furnace oil and power generation fuel supplies.',
            'source': 'Business Standard - Companies'
        },
        {
            'company': 'GMR Infrastructure',
            'headline': 'GMR commissioning new captive power plant for Delhi airport expansion',
            'summary': 'Airport operator installing 150 MW captive power generation. Diesel gensets and fuel supply contracts under tender.',
            'source': 'Hindu Business Line - Industry'
        },
        {
            'company': 'Asian Paints Limited',
            'headline': 'Asian Paints to set up manufacturing facility in Rajasthan',
            'summary': 'Paint manufacturer investing ₹800 crore in new plant. Facility requires hexane, mineral turpentine, and industrial solvents.',
            'source': 'PTI News - Business'
        },
        {
            'company': 'Essar Steel India',
            'headline': 'Essar Steel modernization includes new boiler installations',
            'summary': 'Steel plant upgrading furnaces and boilers as part of ₹1,200 crore modernization drive. Long-term fuel supply agreements being negotiated.',
            'source': 'Economic Times - Industry'
        },
        {
            'company': 'Grasim Industries',
            'headline': 'Grasim Industries expands viscose staple fiber manufacturing',
            'summary': 'Aditya Birla Group company adding capacity. Chemical processing requires additional solvent and specialty fuel supplies.',
            'source': 'Business Standard - Companies'
        },
        {
            'company': 'Jindal Steel & Power',
            'headline': 'JSPL announces coal gasification project with fuel oil backup systems',
            'summary': 'Major steel producer implementing new gasification technology. Project includes backup furnace oil systems and lubricant requirements.',
            'source': 'Hindu Business Line - Industry'
        },
        {
            'company': 'Century Textiles',
            'headline': 'Century Textiles modernizing jute processing units',
            'summary': 'Textile manufacturer upgrading machinery across mills. Increased demand for jute batch oil and industrial lubricants expected.',
            'source': 'PTI News - Business'
        },
        {
            'company': 'Ambuja Cements',
            'headline': 'Ambuja Cements greenfield project approved for Himachal Pradesh',
            'summary': 'New cement plant to create demand for diesel, furnace oil for kilns. Environmental clearances obtained, construction to begin Q2.',
            'source': 'Economic Times - Industry'
        },
        {
            'company': 'Hindalco Industries',
            'headline': 'Hindalco expanding aluminum capacity, power infrastructure in pipeline',
            'summary': 'Aluminum producer planning captive power generation expansion. Significant diesel and fuel oil requirements for new facilities.',
            'source': 'Business Standard - Companies'
        }
    ]
    
    for i, news in enumerate(news_data, 1):
        company_id = db.insert_company(
            name=news['company'],
            industry='Manufacturing/Industrial'
        )
        
        signal_text = f"{news['headline']}\n\n{news['summary']}"
        
        db.insert_lead(
            company_id=company_id,
            signal_text=signal_text,
            signal_type='news',
            source_name=news['source'],
            source_url=f'https://economictimes.indiatimes.com/article/{i}',
            confidence=random.uniform(0.55, 0.75)
        )
        
        print(f"   {i:2}. {news['company'][:50]:50}")
    
    db.log_scrape('Demo News Generator', 'news', 'success', 10)
    
    # ============================================
    # DIRECTORY DATA (10 samples)
    # ============================================
    print("\n📂 Generating 10 DIRECTORY samples...")
    
    directory_data = [
        {
            'company': 'Bharat Petroleum Distributors Pvt Ltd',
            'location': 'Mumbai, Maharashtra',
            'industry': 'Petroleum Distribution'
        },
        {
            'company': 'Supreme Petrochemicals Industries',
            'location': 'Vadodara, Gujarat',
            'industry': 'Petrochemicals'
        },
        {
            'company': 'Navbharat Furnace Oil Suppliers',
            'location': 'Delhi NCR',
            'industry': 'Fuel Supply & Trading'
        },
        {
            'company': 'Eastern Lubricants Manufacturing Co',
            'location': 'Kolkata, West Bengal',
            'industry': 'Lubricants Manufacturing'
        },
        {
            'company': 'Gujarat Chemical Solvents Ltd',
            'location': 'Ahmedabad, Gujarat',
            'industry': 'Chemical Solvents'
        },
        {
            'company': 'Southern Bitumen Products',
            'location': 'Chennai, Tamil Nadu',
            'industry': 'Bitumen & Road Construction'
        },
        {
            'company': 'Rajasthan Industrial Fuels Corporation',
            'location': 'Jaipur, Rajasthan',
            'industry': 'Industrial Fuel Supply'
        },
        {
            'company': 'Maharashtra Hexane Industries',
            'location': 'Pune, Maharashtra',
            'industry': 'Specialty Chemicals'
        },
        {
            'company': 'Punjab Jute Processing Mills',
            'location': 'Ludhiana, Punjab',
            'industry': 'Jute & Textile Processing'
        },
        {
            'company': 'Karnataka Marine Fuel Services',
            'location': 'Mangalore, Karnataka',
            'industry': 'Marine Fuel Supply'
        }
    ]
    
    for i, directory in enumerate(directory_data, 1):
        company_id = db.insert_company(
            name=directory['company'],
            industry=directory['industry'],
            location=directory['location']
        )
        
        signal_text = f"Company listed in business directory - {directory['industry']} sector. Location: {directory['location']}"
        
        db.insert_lead(
            company_id=company_id,
            signal_text=signal_text,
            signal_type='directory',
            source_name='IndiaMART / TradeIndia',
            source_url='https://www.indiamart.com',
            confidence=random.uniform(0.28, 0.42)
        )
        
        print(f"   {i:2}. {directory['company'][:50]:50} | {directory['location'][:25]:25}")
    
    db.log_scrape('Demo Directory Generator', 'directory', 'success', 10)
    
    # ============================================
    # SUMMARY
    # ============================================
    stats = db.get_stats()
    
    print("\n" + "=" * 70)
    print("✅ DEMO DATA GENERATION COMPLETE")
    print("=" * 70)
    print(f"\n   Total Companies: {stats['total_companies']}")
    print(f"   Total Leads:     {stats['total_leads']}")
    print()
    print("   Breakdown by Type:")
    for signal_type, count in stats['by_type']:
        print(f"      • {signal_type.capitalize():12} {count:3} leads")
    print()
    print("=" * 70)
    print("💡 View the data:")
    print("   python3 monitor.py")
    print("   python3 monitor.py --export demo_leads.csv")
    print("=" * 70)
    print()

if __name__ == "__main__":
    generate_demo_data()
